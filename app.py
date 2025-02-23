# from flask import Flask, request, jsonify, render_template
# import asyncio
# import aiohttp
# from newspaper import Article
# import google.generativeai as genai
# import logging

# # Set up Google Gemini API
# def configure_gemini_api(api_key):
#     genai.configure(api_key=api_key)

# def summarize_with_gemini(text: str) -> str:
#     """Use Gemini AI to summarize the text."""
#     model = genai.GenerativeModel("gemini-pro")
#     response = model.generate_content(f"Summarize the following article:\n{text}")
#     return response.text if response else "No summary available."

# class NewsSearchSummarizer:
#     def __init__(self, news_api_key, gemini_api_key):
#         self.news_api_key = news_api_key
#         self.gemini_api_key = gemini_api_key
#         configure_gemini_api(gemini_api_key)

#     async def fetch_news(self, query: str, max_articles: int) -> list[dict]:
#         """Fetch news articles from NewsAPI."""
#         url = f"https://newsapi.org/v2/everything?q={query}&language=en&apiKey={self.news_api_key}"
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as response:
#                 if response.status == 200:
#                     data = await response.json()
#                     return data.get("articles", [])[:max_articles]
#                 else:
#                     return []

#     async def search_and_summarize(self, query: str, max_articles: int) -> list[dict]:
#         """Search for news articles and summarize them using Gemini AI."""
#         articles = await self.fetch_news(query, max_articles)
#         results = []

#         for article in articles:
#             url = article.get("url", "")
#             title = article.get("title", "No Title")
#             source = article.get("source", {}).get("name", "Unknown Source")
#             summary = ""
            
#             try:
#                 news_article = Article(url)
#                 news_article.download()
#                 news_article.parse()
#                 summary = summarize_with_gemini(news_article.text)
#             except Exception as e:
#                 logging.error(f"Error summarizing article: {e}")
#                 summary = "Summary not available."

#             results.append({
#                 "title": title,
#                 "source": source,
#                 "ai_summary": summary,
#                 "url": url
#             })
#         return results

# # Initialize Flask app
# app = Flask(__name__)

# # Initialize NewsSearchSummarizer
# news_api_key = "3fcd57ae77be4306a2fd6fadc4917c5c"  # Replace with your NewsAPI key
# gemini_api_key = "AIzaSyDHNPArRKEMeeBHUYJ5x5R01HzByccleVo"  # Replace with your Gemini API key
# agent = NewsSearchSummarizer(news_api_key, gemini_api_key)

# # Serve the HTML file
# @app.route("/")
# def index():
#     return render_template("index.html")

# # API endpoint for searching news
# @app.route("/api/search", methods=["POST"])
# async def search_news():
#     data = request.json
#     query = data.get("query", "")
#     max_articles = data.get("max_articles", 3)
    
#     try:
#         max_articles = min(max(int(max_articles), 1), 10)
#     except ValueError:
#         max_articles = 3

#     results = await agent.search_and_summarize(query, max_articles)
#     return jsonify(results)

# # Run the Flask app
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify, render_template
import asyncio
import aiohttp
from newspaper import Article
import google.generativeai as genai
import logging

# Set up Google Gemini API
def configure_gemini_api(api_key):
    genai.configure(api_key=api_key)

def summarize_with_gemini(text: str) -> str:
    """Use Gemini AI to summarize the text."""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Summarize the following article:\n{text}")
    return response.text if response else "No summary available."

class NewsSearchSummarizer:
    def __init__(self, news_api_key, gemini_api_key):
        self.news_api_key = news_api_key
        self.gemini_api_key = gemini_api_key
        configure_gemini_api(gemini_api_key)

    async def fetch_news(self, query: str, max_articles: int) -> list[dict]:
        """Fetch news articles from NewsAPI."""
        url = f"https://newsapi.org/v2/everything?q={query}&language=en&apiKey={self.news_api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("articles", [])[:max_articles]
                else:
                    return []

    async def search_and_summarize(self, query: str, max_articles: int) -> list[dict]:
        """Search for news articles and summarize them using Gemini AI."""
        articles = await self.fetch_news(query, max_articles)
        results = []

        for article in articles:
            url = article.get("url", "")
            title = article.get("title", "No Title")
            source = article.get("source", {}).get("name", "Unknown Source")
            summary = ""
            
            try:
                news_article = Article(url)
                news_article.download()
                news_article.parse()
                summary = summarize_with_gemini(news_article.text)
            except Exception as e:
                logging.error(f"Error summarizing article: {e}")
                summary = "Summary not available."

            results.append({
                "title": title,
                "source": source,
                "ai_summary": summary,
                "url": url
            })
        return results

# Initialize Flask app
app = Flask(__name__)

# Initialize NewsSearchSummarizer
news_api_key = "3fcd57ae77be4306a2fd6fadc4917c5c"  # Replace with your NewsAPI key
gemini_api_key = "AIzaSyDHNPArRKEMeeBHUYJ5x5R01HzByccleVo"  # Replace with your Gemini API key
agent = NewsSearchSummarizer(news_api_key, gemini_api_key)

# Serve the HTML file
@app.route("/")
def index():
    return render_template("index.html")

# API endpoint for fetching default news
@app.route("/api/default-news", methods=["GET"])
async def get_default_news():
    """Fetch default news articles (e.g., top headlines)."""
    query = "latest news"  # Default query
    max_articles = 5  # Default number of articles
    results = await agent.search_and_summarize(query, max_articles)
    return jsonify(results)

# API endpoint for searching news
@app.route("/api/search", methods=["POST"])
async def search_news():
    data = request.json
    query = data.get("query", "")
    max_articles = data.get("max_articles", 3)
    
    try:
        max_articles = min(max(int(max_articles), 1), 10)
    except ValueError:
        max_articles = 3

    results = await agent.search_and_summarize(query, max_articles)
    return jsonify(results)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)