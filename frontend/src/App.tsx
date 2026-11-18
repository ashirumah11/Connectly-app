import { useEffect, useState } from 'react'
import { api } from './services/api'

interface HealthResponse {
  status: string
  service: string
}

function App() {
  const [health, setHealth] = useState<HealthResponse | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    api.get<HealthResponse>('/health/')
      .then((response) => setHealth(response.data))
      .catch(() => setError('The Connectly API is unavailable'))
  }, [])

  return (
    <main className="app-shell">
      <h1>Connectly</h1>
      <p>A modern social network, built with Django and React.</p>
      {health && <p className="status success">API: {health.service} — {health.status}</p>}
      {error && <p className="status error">{error}</p>}
    </main>
  )
}

export default App
