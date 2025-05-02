import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def check_google_traffic(lat: float, lon: float) -> str:
    try:
        url = (
            f"https://maps.googleapis.com/maps/api/directions/json?"
            f"origin={lat},{lon}&destination={lat+0.001},{lon+0.001}&key={GOOGLE_API_KEY}&departure_time=now"
        )
        response = httpx.get(url)
        data = response.json()

        if 'routes' in data and data['routes']:
            duration_in_traffic = data['routes'][0]['legs'][0]['duration_in_traffic']['value']
            normal_duration = data['routes'][0]['legs'][0]['duration']['value']

            delay_ratio = duration_in_traffic / normal_duration
            if delay_ratio > 1.5:
                return "heavy"
            elif delay_ratio > 1.2:
                return "moderate"
            else:
                return "light"
    except:
        return "unknown"

    return "unknown"

def get_nearest_train_distance(lat: float, lon: float) -> float:
    try:
        return 3.0
    except:
        return None
