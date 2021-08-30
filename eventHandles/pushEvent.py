EVENT = "PushEvent"
COLOR = 0xffbb00

def run(data):
    payload = data['payload']
    return [
        {
            "name":f"Nuevo commit:",
            "value":f"[{commit['message']}]({commit['url'].replace('https://api.github.com/repos/', 'https://github.com/')})"
        } for commit in payload['commits']
    ]