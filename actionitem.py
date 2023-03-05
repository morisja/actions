#!/usr/bin/python3
from dataclasses import dataclass, asdict, field, InitVar
import uuid

URLBASE = "http://192.168.0.223:5000/"


def make_default_headers():
    return {"": ""}


def make_uuid() -> str:
    return str(uuid.uuid4())


@dataclass
class ActionItem:
    title: str
    section: str
    path: InitVar[str]
    headers: dict = field(default_factory=make_default_headers)
    id: str = field(default_factory=make_uuid)
    httpBody: str = ""
    showResponse: bool = False
    url: str = ""
    httpMethod: int = 0
    contentTypeHeader: int = 1
    acceptHeader: int = 1

    def __post_init__(self, path):
        self.url = f"{URLBASE}/{path}"

    def as_dict(self):
        return asdict(self)
