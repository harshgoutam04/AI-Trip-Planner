from pydantic import BaseModel


class Attraction(BaseModel):
    name: str
    category: str
    latitude: float
    longitude: float
    distance: float | None = None
    wikipedia: str | None = None
    osm: str | None = None