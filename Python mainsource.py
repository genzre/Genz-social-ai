social_media_clients.py

import os import requests import json from googleapiclient.discovery import build from google_auth_oauthlib.flow import InstalledAppFlow from google.auth.transport.requests import Request import tweepy

=== Instagram Graph API ===

class InstagramClient: def init(self): self.access_token = os.getenv("IG_ACCESS_TOKEN") self.page_id = os.getenv("IG_PAGE_ID")

def post(self, content):
    url = f"https://graph.facebook.com/v18.0/{self.page_id}/feed"
    params = {
        "message": content,
        "access_token": self.access_token
    }
    response = requests.post(url, data=params)
    print("[Instagram] Response:", response.json())

=== Twitter/X API ===

class TwitterClient: def init(self): self.client = tweepy.Client( bearer_token=os.getenv("TW_BEARER_TOKEN"), consumer_key=os.getenv("TW_CONSUMER_KEY"), consumer_secret=os.getenv("TW_CONSUMER_SECRET"), access_token=os.getenv("TW_ACCESS_TOKEN"), access_token_secret=os.getenv("TW_ACCESS_SECRET") )

def post(self, content):
    response = self.client.create_tweet(text=content)
    print("[Twitter] Response:", response)

=== TikTok (Requires automation or third-party service) ===

class TikTokClient: def post(self, content): print("[TikTok] No public API for posting. Use a third-party tool or manual upload.") # Future: integrate with third-party like TikTok API Partners or automation bot

=== YouTube (Community Tab / Shorts Upload) ===

class YouTubeClient: def init(self): self.api_service_name = "youtube" self.api_version = "v3" self.client_secret_file = "client_secret.json" self.scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"] self.youtube = self.authenticate()

def authenticate(self):
    creds = None
    if os.path.exists("token.json"):
        with open("token.json", "r") as token:
            creds = json.load(token)

    if not creds or not creds.get("token"):
        flow = InstalledAppFlow.from_client_secrets_file(self.client_secret_file, self.scopes)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            json.dump(creds.to_json(), token)

    return build(self.api_service_name, self.api_version, credentials=creds)

def post(self, content):
    print("[YouTube] Uploading post to community or short placeholder.")
    # Actual upload logic requires video content and metadata
    # Future: Auto-generate a video or thumbnail + caption

OPENAI_API_KEY=your_openai_key

# Instagram
IG_ACCESS_TOKEN=your_ig_access_token
IG_PAGE_ID=your_ig_page_id

# Twitter
TW_BEARER_TOKEN=your_bearer_token
TW_CONSUMER_KEY=your_consumer_key
TW_CONSUMER_SECRET=your_consumer_secret
TW_ACCESS_TOKEN=your_access_token
TW_ACCESS_SECRET=your_access_secret
your_project/
│
├── main.py                      # (From earlier: AI scheduler)
├── social_media_clients.py     # (Updated with real API logic)
├── .env                         # (Your API keys)
├── client_secret.json          # (Google API credentials)
├── token.json                  # (Will be auto-created)
