import os
from slack_sdk import WebClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

slack_token = os.getenv('SLACK_API_TOKEN')
client = WebClient(token=slack_token)

def post_to_slack(channel, message):
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message
        )
        print(f"Message posted successfully to Slack channel '{channel}'")
    except Exception as e:
        print(f"Error posting message to Slack: {e}")
