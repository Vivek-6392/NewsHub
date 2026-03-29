# 📰 NewsHub — Intelligent News Digest

A modern, AI-powered news web app that fetches real-time headlines and generates concise summaries using LLMs.

---

## 🚀 Live Demo

👉 https://vivek-6392.github.io/NewsHub/

---

## ✨ Features

* 🔎 **Search News by Topic**
* 🧠 **AI Summarization (Groq - Llama 3)**
* 🌍 **Real-time Headlines (Currents API)**
* ⚡ **Fast & Responsive UI**
* 🌙 **Dark Mode Support**
* 🔄 **Manual Refresh Button**
* 📊 **Quota Tracking (API usage)**

---

## 🏗️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **News API:** Currents API
* **AI Model:** Groq (Llama 3)
* **Deployment:** GitHub Pages
* **CI/CD:** GitHub Actions

---

## 📂 Project Structure

```
NewsHub/
│── index.html
│── .github/
│   └── workflows/
│       └── deploy.yml
│── README.md
```

---

## ⚙️ Setup & Deployment

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Vivek-6392/NewsHub.git
cd NewsHub
```

---

### 2️⃣ Add API Keys (IMPORTANT)

Go to:

**GitHub → Settings → Secrets → Actions**

Add:

```
CURRENTS_API_KEY = your_currents_api_key
GROQ_API_KEY     = your_groq_api_key
```

---

### 3️⃣ Deploy using GitHub Actions

* Push code to `main` branch
* Go to **Actions tab**
* Click **Run workflow**

Your app will be live on GitHub Pages 🚀

---

## 🔐 Environment Variables

| Variable           | Description            |
| ------------------ | ---------------------- |
| `CURRENTS_API_KEY` | Fetches news articles  |
| `GROQ_API_KEY`     | Generates AI summaries |

---

## ⚠️ Important Note

This project injects API keys into frontend at build time.

👉 This means:

* API keys are **visible in browser**
* Not suitable for production use

---

## 🚀 Future Improvements

* 🔐 Move to backend (Vercel / Node.js)
* 🧠 AI-based news ranking (semantic search)
* ⚡ Caching for faster responses
* 📱 Mobile-first UI improvements
* 🗂️ Category-based filtering
* 🌐 Multi-language support

---

## 🧠 How It Works

1. User enters a query or selects a category
2. App fetches news from **Currents API**
3. Each article is sent to **Groq AI**
4. AI generates a short summary
5. Results are displayed in a clean UI

---

## 🐞 Known Issues

* API keys exposed in frontend (temporary approach)
* Free API limits (600 requests/day)
* Search results may include loosely related articles

---

## 🤝 Contributing

Contributions are welcome!

```bash
fork → clone → create branch → commit → push → PR
```

## 👨‍💻 Author

**Vivek Yadav**

* GitHub: https://github.com/Vivek-6392

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
