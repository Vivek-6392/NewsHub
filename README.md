# NewsHub — GitHub Pages Deployment

Live headlines via **GNews API** (browser CORS-friendly) + summaries by **Google Gemini**. Keys are injected at build time by GitHub Actions — never in source code.

---

## Why GNews instead of NewsAPI?

NewsAPI blocks all browser-side requests (even on paid plans) with:
> *"Requests from the browser are not allowed on the Developer plan, except from localhost."*

**GNews explicitly supports CORS** and works from any domain including GitHub Pages. Free plan: **100 requests/day, up to 10 articles/request**.

---

## File structure

```
your-repo/
├── index.html
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## Setup (4 steps)

### 1. Create a public GitHub repository

[github.com/new](https://github.com/new) → public repo.

### 2. Upload files

Upload `index.html` to the root and `deploy.yml` to `.github/workflows/`.

### 3. Add secrets

**Settings → Secrets and variables → Actions → New repository secret**

| Secret name     | Where to get it                         |
|-----------------|-----------------------------------------|
| `GNEWS_API_KEY` | [gnews.io](https://gnews.io) → Dashboard → API Key |
| `GEMINI_API_KEY`| [aistudio.google.com](https://aistudio.google.com) → Get API Key |

### 4. Enable GitHub Pages

**Settings → Pages → Build and deployment → Source: GitHub Actions**

Push a commit or run the workflow manually — your site goes live at:
```
https://<username>.github.io/<repo-name>/
```

---

## How injection works

```
git push
   │
   ▼
GitHub Actions checks out index.html
(contains __GNEWS_API_KEY__ and __GEMINI_API_KEY__ as plain text)
   │
   ▼
sed replaces both placeholders with real secret values
   │
   ▼
Verification step fails the build if any placeholder remains
   │
   ▼
Processed index.html deployed to GitHub Pages CDN
```

Real keys only exist in the deployed CDN file, never in git history.

---

## Troubleshooting

| Error | Fix |
|---|---|
| Placeholders not replaced | Add `GNEWS_API_KEY` and `GEMINI_API_KEY` to repo Secrets |
| GNews 429 error | Hit 100 req/day limit — resets midnight UTC, or upgrade at gnews.io |
| Gemini error | Check key at aistudio.google.com — free quota is generous |
| Site shows 404 | Pages source must be **GitHub Actions**, not "Deploy from branch" |
