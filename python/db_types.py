import dataclasses
import datetime


@dataclasses.dataclass
class News:
    news_id: int
    publication_time: datetime.datetime
    name: str
    preview_description: str
    description: str
    preview_photo_id: int


@dataclasses.dataclass
class Quantum:
    quantum_id: int
    name: str
    description: str


@dataclasses.dataclass
class Tutor:
    tutor_id: int
    name: str
    description: str
    photo_id: int


@dataclasses.dataclass
class Event:
    event_id: int
    name: str
    quantum_id: int
    tutor_id: int
    time_start: datetime.datetime
    time_end: datetime.datetime
