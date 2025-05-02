from pydantic import BaseModel

class RailwayCrossing(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float

class CrossingStatus(BaseModel):
    crossing_id: int
    status: str
    reason: str
