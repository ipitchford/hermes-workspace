//  @ts-check

import { tanstackConfig } from '@tanstack/eslint-config'
import reactHooks from 'eslint-plugin-react-hooks'

export default [
  ...tanstackConfig,
  {
    ignores: [
      'dist/**',
      '.output/**',
      'node_modules/**',
      'eslint.config.js',
      'prettier.config.js',
      'vite.config.ts',
    ],
  },
  {
    files: ['**/*.js'],
    languageOptions: {
      parserOptions: {
        project: false,
      },
    },
  },
  {
    plugins: {
      'react-hooks': reactHooks,
    },
    rules: {
      'react-hooks/rules-of-hooks': 'error',
      'react-hooks/exhaustive-deps': 'warn',

      '@typescript-eslint/array-type': 'off',
      '@typescript-eslint/consistent-type-imports': 'off',
      '@typescript-eslint/no-unnecessary-condition': 'off',
      '@typescript-eslint/no-unnecessary-type-assertion': 'off',
      '@typescript-eslint/require-await': 'off',
      'import/consistent-type-specifier-style': 'off',
      'import/first': 'off',
      'import/order': 'off',
      'no-shadow': 'off',
      'sort-imports': 'off',
    },
  },
]
