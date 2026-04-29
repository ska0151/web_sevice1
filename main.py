import os
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

app = FastAPI()

# 環境変数からAPIキーを取得
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@app.get("/news-summary")
def get_summary():
    if not GEMINI_API_KEY:
        return {"error": "GEMINI_API_KEY is not set in environment variables."}

    # --- ここにニュース収集、フィルタリング、要約のロジックを詰め込む ---
    # ① RSSからタイトルとURLを取得 (Feedparser)
    # ② AI(Gemini Flash)に「選別」させる
    # ③ 選ばれたURLの本文をスクレイピング (BeautifulSoup4, requests)
    # ④ AI(Gemini)に「要約」させる
    # ----------------------------------------------------
    
    # 仮のレスポンス
    return {
        "status": "success",
        "date": "2026-04-29",
        "articles": [
            {"title": "Sample Article 1", "url": "https://example.com/article1", "summary": "This is a summary of sample article 1."},
            {"title": "Sample Article 2", "url": "https://example.com/article2", "summary": "This is a summary of sample article 2."},
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
