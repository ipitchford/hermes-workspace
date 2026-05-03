import { readFile, readdir, stat } from 'node:fs/promises'
import { homedir } from 'node:os'
import { join } from 'node:path'
import { createFileRoute } from '@tanstack/react-router'
import { json } from '@tanstack/react-start'
import { isAuthenticated } from '../../server/auth-middleware'

const JOB_ID_RE = /^[a-f0-9]{12}$/

function hermesHome(): string {
  return process.env.HERMES_HOME || join(homedir(), '.hermes')
}

function extractFinalResponse(markdown: string): string {
  const marker = '\n## Response\n'
  const index = markdown.lastIndexOf(marker)
  if (index < 0) return markdown.trim()
  return markdown.slice(index + marker.length).trim()
}

export const Route = createFileRoute('/api/conductor-output')({
  server: {
    handlers: {
      GET: async ({ request }) => {
        if (!isAuthenticated(request)) {
          return json({ ok: false, error: 'Unauthorized' }, { status: 401 })
        }

        const url = new URL(request.url)
        const jobId = url.searchParams.get('jobId')?.trim() ?? ''
        if (!JOB_ID_RE.test(jobId)) {
          return json({ ok: false, error: 'Invalid jobId' }, { status: 400 })
        }

        const outputDir = join(hermesHome(), 'cron', 'output', jobId)
        try {
          const entries = await readdir(outputDir)
          const candidates = await Promise.all(
            entries
              .filter((entry) => entry.endsWith('.md'))
              .map(async (entry) => {
                const path = join(outputDir, entry)
                const info = await stat(path)
                return { path, mtimeMs: info.mtimeMs }
              }),
          )
          if (candidates.length === 0) {
            return json({ ok: true, found: false, completed: false })
          }
          const latest = candidates.sort((a, b) => b.mtimeMs - a.mtimeMs)[0]

          const outputText = await readFile(latest.path, 'utf-8')
          return json({
            ok: true,
            found: true,
            completed: true,
            outputPath: latest.path,
            modifiedAt: new Date(latest.mtimeMs).toISOString(),
            finalResponse: extractFinalResponse(outputText),
            outputText,
          })
        } catch (error) {
          const code =
            error && typeof error === 'object' && 'code' in error
              ? String((error as { code?: unknown }).code)
              : ''
          if (code === 'ENOENT') {
            return json({ ok: true, found: false, completed: false })
          }
          return json(
            {
              ok: false,
              error: error instanceof Error ? error.message : String(error),
            },
            { status: 500 },
          )
        }
      },
    },
  },
})
