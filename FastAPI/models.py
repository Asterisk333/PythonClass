from datetime import datetime

from pydantic import BaseModel

class Pet(BaseModel):
    rfid: str
    name: str
    silo: int
    profile_picture: str = None

class FeedingSchedule(BaseModel):
    rfid: str
    timeWindow: str
    amount: float

class Silo(BaseModel):
    id: int
    stockWeight: float

class FeedingEvent(BaseModel):
    rfid: str
    timestamp : datetime
    amountDispensed: float

class SensorData(BaseModel):
    timestamp: datetime
    scaleEntry: float
    scaleLeft: float
    scaleRight: float
    rfidTag: str