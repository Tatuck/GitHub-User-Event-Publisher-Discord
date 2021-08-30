import requests
from time import sleep
import config
import os
import importlib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

print("""
GitHub user event publisher

Made by Tatuck :D
""")

logger.debug("Adding handlers")
# Get event handlers
eventHandles = {}
for x in os.listdir("eventHandles"):
    if not x.endswith(".py") or not os.path.isfile(f"eventHandles/{x}"):
        continue
    logger.info(f"Adding handler {x}")
    lib = importlib.import_module(f"eventHandles.{x.split('.')[0]}")
    eventHandles[lib.EVENT] = {"run":lib.run, "color":lib.COLOR}

def sendEvents(events):
    for x in events:
        if data:=eventHandles.get(x["type"], False):
            run = data["run"]
            color = data["color"]
            embed = {
                "embeds":[
                    {
                        "author":{
                            "name":f"{x['repo']['name']}",
                            "url":f"{x['repo']['url'].replace('https://api.github.com/repos', 'https://github.com')}",
                            "icon_url":"https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
                        },
                        "fields":run(x),
                        "footer":{
                            "text":f"{config.GITHUB_USERNAME} updates",
                            "icon_url":f"{x['actor']['avatar_url']}"
                        },
                        "color":color,
                        "timestamp":x["created_at"]
                    }
                ]
            }
            logger.info(f"Sending message")
            try:
                requests.post(f"{config.DISCORD_URL}", json=embed)
            except Exception as e:
                logger.error("Error sending the message:")
                logger.error(e)
        else:
            continue

def getDiferentLists(listA, listB):
    differentList = []
    for x in listA:
        if x not in listB:
            differentList.append(x)
    for x in listB:
        if x not in listA:
            differentList.append(x)
    return differentList

headers = {"Accept" : "application/vnd.github.v3+json"}
events = requests.get(f"{config.GITHUB_URL}/users/{config.GITHUB_USERNAME}/events/public", headers=headers).json()
sleep(config.TIME_PER_REQUEST)

while True:
    try:
        newEvents = requests.get(f"{config.GITHUB_URL}/users/{config.GITHUB_USERNAME}/events/public", headers=headers).json()
    except Exception as e:
        logger.error("Error getting the events")
        logger.error(e)
        sleep(config.TIME_PER_REQUEST)

    onlyNewEvents = getDiferentLists(newEvents, events)
    if onlyNewEvents != []:
        sendEvents(onlyNewEvents)
    events = newEvents
    sleep(config.TIME_PER_REQUEST)