from fastapi import APIRouter
from app.schemas import CrossingStatus
from app.utils import check_google_traffic, get_nearest_train_distance

router = APIRouter(prefix="/status", tags=["Status"])

@router.get("/{crossing_id}", response_model=CrossingStatus)
def get_crossing_status(crossing_id: int):
    crossing_location = {
        1: (28.6139, 77.2090),
        2: (28.7041, 77.1025)
    }.get(crossing_id)

    if not crossing_location:
        return {"crossing_id": crossing_id, "status": "unknown", "reason": "Invalid crossing ID."}

    traffic_status = check_google_traffic(*crossing_location)
    train_distance_km = get_nearest_train_distance(*crossing_location)

    if train_distance_km is not None and train_distance_km <= 5:
        return {"crossing_id": crossing_id, "status": "closed", "reason": f"Train is {train_distance_km:.1f} km away."}
    elif traffic_status == "heavy":
        return {"crossing_id": crossing_id, "status": "likely closed", "reason": "Heavy congestion detected on both sides."}
    else:
        return {"crossing_id": crossing_id, "status": "open", "reason": "No train nearby and traffic is light."}
