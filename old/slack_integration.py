import json
import slack # type: ignore
from config import SLACK_BOT_TOKEN, SLACK_CHANNEL

def post_to_slack(results):
    client = slack.WebClient(token=SLACK_BOT_TOKEN)
    client.chat_postMessage(channel=SLACK_CHANNEL, text=json.dumps(results))
