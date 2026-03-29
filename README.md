# NewsHub — GitHub Pages Deployment Guide

Live headlines fetched via **NewsAPI** and summarised by **Google Gemini**. API keys are injected securely at build time — they never appear in your source code.

---

## 📁 Repository structure

```
your-repo/
├── index.html                        ← the app (has __PLACEHOLDER__ keys)
└── .github/
    └── workflows/
        └── deploy.yml                ← GitHub Actions workflow
```

---

## 🚀 Setup in 4 steps

### Step 1 — Create a GitHub repository

Go to [github.com/new](https://github.com/new) and create a **public** repository (GitHub Pages requires public repos on free plans).

### Step 2 — Add your files

Upload both files maintaining this structure:
```
index.html
.github/workflows/deploy.yml
```

### Step 3 — Add API keys as GitHub Secrets

1. Go to your repo → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret** and add:

| Secret name     | Value                                |
|-----------------|--------------------------------------|
| `NEWS_API_KEY`  | Your key from newsapi.org            |
| `GEMINI_API_KEY`| Your key from Google AI Studio       |

> ⚠️ **Never** put real API keys inside `index.html` or commit them to git.

### Step 4 — Enable GitHub Pages

1. Go to **Settings** → **Pages**
2. Under **Build and deployment**, set Source to **GitHub Actions**
3. Push a commit (or go to **Actions** → run workflow manually)

Your site goes live at:
```
https://<your-username>.github.io/<repo-name>/
```

---

## 🔑 Getting API Keys

### NewsAPI
1. Sign up at [newsapi.org](https://newsapi.org)
2. Copy your API key from the dashboard
3. ⚠️ **Free plan only works on `localhost`**. For a live GitHub Pages site you need the **Developer or Business plan** (paid) because free plan blocks CORS requests from production domains.

### Google Gemini
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click **Get API key** → **Create API key**
3. Copy the key — Gemini supports CORS on both free and paid tiers.

---

## ⚙️ How the workflow works

```
git push to main
      │
      ▼
GitHub Actions runner checks out code
      │
      ▼
sed replaces __NEWS_API_KEY__ and __GEMINI_API_KEY__
in index.html with real values from Secrets
      │
      ▼
BUILD_TIME placeholder replaced with current UTC time
      │
      ▼
Verification step confirms no placeholders remain
      │
      ▼
Site uploaded and deployed to GitHub Pages
```

The real keys are **only** present in the deployed HTML served by GitHub's CDN. They are **never** stored in your git history.

---

## 🕐 Auto-rebuild schedule

The workflow runs on:
- Every `git push` to `main`
- Manual trigger (Actions tab → Run workflow)
- Every 6 hours automatically (cron schedule) — keeps build timestamp fresh

You can remove the `schedule:` block from `deploy.yml` if you don't want scheduled rebuilds.

---

## 🐛 Troubleshooting

| Problem | Solution |
|---|---|
| "API keys not injected" banner | Add `NEWS_API_KEY` and `GEMINI_API_KEY` to repo Secrets and re-run the workflow |
| NewsAPI CORS error on live site | Upgrade to a paid NewsAPI plan |
| Gemini errors | Check your key at aistudio.google.com — free quota is generous |
| Workflow fails on verification step | One of your secrets is empty or missing |
| Site shows 404 | Ensure Pages source is set to "GitHub Actions" not "Deploy from branch" |
