from time import time
from datetime import datetime
from zoneinfo import ZoneInfo
import requests

class GameAnalytics:
    @staticmethod
    def update(start_time):
        start_play = datetime.fromtimestamp(start_time, tz=ZoneInfo("Europe/Paris"))
        end_play = datetime.fromtimestamp(time(), tz=ZoneInfo("Europe/Paris"))

        info = {
            'start_play': start_play.strftime("%Y-%m-%d %H:%M:%S"),
            'end_play': end_play.strftime("%Y-%m-%d %H:%M:%S"),
            'play_duration': int(time() - start_time)
        }

        return info

BASE_URL = "https://soma-game-analytics-default-rtdb.firebaseio.com"
SECRET = "mOuuzIFmpsHo9nRUHmo0ygl0G9AnTRL9al9H7ODK"
ENDPOINT = f"/players.json?auth={SECRET}"

def send_to_firebase(data):
    response = requests.post(BASE_URL + ENDPOINT, json=data)
    print("Status:", response.status_code)
    print("Response:", response.text)


