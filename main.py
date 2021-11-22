import time
import userRepository
from keys.telegram import TOKEN, CHATID

import requests

BOT_URL = "https://api.telegram.org/bot"+TOKEN+"/sendMessage"


def sendMessage(msg):
    print(msg)
    params = {"chat_id": CHATID, "text": msg}
    message = requests.post(BOT_URL, params=params)


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}

users = userRepository.getUsers()

while len(users) > 0:
    for user in users:
        r = requests.post("https://www.labor-ostsachsen.de/mein-laborbefund",
                          data=user.as_json_query(),
                          headers=headers)
        if r.status_code == 200:
            if "Dieser Auftrag ist noch in Bearbeitung" not in r.text:
                # maybe ready, send a message
                sendMessage("Testergebnis für {} da, ID: {}, Link: https://www.labor-ostsachsen.de/mein-laborbefund".format(user.name, user.id))
                users.remove(user)
            else:
                print("{} checked but still in progress".format(user.name))
    time.sleep(60*10)

