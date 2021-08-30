EVENT = "ReleaseEvent"
COLOR = 0xa914ff

actions = {
    "published" : "publicada",
    "edited" : "editada"
}
def run(data):
    payload = data['payload']
    return [
        {
            "name" : f"Release {actions[payload['action']]}: {payload['release']['name']} {payload['release']['tag_name']}",
            "value" : f"[Ver release ({payload['release']['name']})]({payload['release']['html_url']})"
        }
    ]