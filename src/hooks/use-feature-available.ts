import { useQuery } from '@tanstack/react-query'
import type { EnhancedFeature } from '@/lib/feature-gates'

interface GatewayStatus {
  capabilities: Record<string, boolean>
  hermesUrl: string
}

const LOCALLY_BROWSABLE_FEATURES = new Set<EnhancedFeature>([
  'memory',
  'skills',
])

export function useFeatureAvailable(feature: EnhancedFeature): boolean {
  const { data } = useQuery({
    queryKey: ['gateway-status'],
    queryFn: async () => {
      const res = await fetch('/api/gateway-status')
      if (!res.ok) return null
      return (await res.json()) as GatewayStatus
    },
    staleTime: 30_000,
    refetchInterval: 60_000,
  })

  if (LOCALLY_BROWSABLE_FEATURES.has(feature)) {
    return true
  }

  return data?.capabilities[feature] === true
}
