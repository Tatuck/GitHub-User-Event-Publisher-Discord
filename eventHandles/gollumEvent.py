EVENT = "GollumEvent"
COLOR = 0x14b5ff


actions = {
    "created":"creada",
    "edited":"editada"
}
def run(data):
    payload = data['payload']
    return [
        {
            "name": f"Página wiki \"{page['title']}\" {actions[page['action']]}",
            "value": f"[Ver página ({page['title']})]({page['html_url']})"
        } for page in payload['pages']
    ]