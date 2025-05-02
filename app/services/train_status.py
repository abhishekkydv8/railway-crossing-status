import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("INDIAN_RAIL_API_KEY")

def get_train_status(train_number):
    url = f"https://indianrailapi.com/api/v2/livetrainstatus/apikey/{API_KEY}/trainnumber/{train_number}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
