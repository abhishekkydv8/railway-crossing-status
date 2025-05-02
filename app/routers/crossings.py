from fastapi import APIRouter, Query
from geopy.distance import geodesic
from app.schemas import RailwayCrossing

router = APIRouter(prefix="/crossings", tags=["Crossings"])

CROSSINGS = [
    RailwayCrossing(id=1, name="Crossing A", latitude=28.6139, longitude=77.2090),
    RailwayCrossing(id=2, name="Crossing B", latitude=28.7041, longitude=77.1025),
]

@router.get("/nearby")
def get_nearby_crossings(lat: float, lon: float, radius_km: float = 2):
    location = (lat, lon)
    nearby = [
        crossing for crossing in CROSSINGS
        if geodesic(location, (crossing.latitude, crossing.longitude)).km <= radius_km
    ]
    return nearby
