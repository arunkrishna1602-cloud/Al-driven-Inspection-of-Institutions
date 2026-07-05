# InspectAI 🔍

AI-powered facility inspection and compliance analysis — upload a photo, get an instant compliance report.

Built for restaurants, schools, hospitals, factories, warehouses, offices, and retail stores. Powered by Claude's vision capabilities.

---

## What It Does

Upload a photo of a facility and InspectAI analyzes it for compliance using Claude Vision, returning:

- **Overall compliance score** (0–100)
- **Category breakdown** (cleanliness, safety, organization, maintenance, etc.)
- **Findings** flagged by severity (Critical → Low)
- **Actionable recommendations** for improvement
- **Inspection history** for tracking over time

---

## Two Ways to Run This

### 🌐 Website — Single-file website
No backend, no database. Runs entirely in the browser and calls the Claude API directly.

1. Deploy `index.html` to Vercel, Netlify, or GitHub Pages
2. Get a free API key at console.anthropic.com
3. Open the site → Settings → paste your API key
4. Start analyzing

### 🏢 Full Stack — Node.js + React + SQLite
A complete backend/frontend app with persistent storage, built for teams.

```bash
npm install
cp .env.example .env        # add your ANTHROPIC_API_KEY
npm start                   # backend → localhost:5000
npm run dev                 # frontend → localhost:3000
