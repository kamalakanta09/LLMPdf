import requests

# Post prompt message to slack
def post_to_slack(channel, text, token):
    url = 'https://slack.com/api/chat.postMessage'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'channel': channel, 'text': text}
    response = requests.post(url, headers=headers, json=data)
    print(response.json()) 
    
    return response.status_code == 200
