import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { initializeAnalyticsTracking } from './analytics.js'

// Google Analytics 4 integration added here so it loads once when the app starts.
initializeAnalyticsTracking();

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
