EVENT = "CreateEvent"
COLOR = 0x00ff91

types = {
    "branch":("a", "branch"),
    "tag":("a", "tag"),
    "repository":("o", "repositorio"),
}
def run(data):
    payload = data['payload']
    return [
        {
            "name":f"Nuev{' '.join(types[payload['ref_type']])}" + (f": {payload['ref']}" if payload['ref'] != None else ""),
            "value":f"Descripción: {payload['description']}"
        }
    ]