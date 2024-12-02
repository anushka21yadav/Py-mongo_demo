from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    title: str
    desc: str
    status: bool = False
    deleted: bool = False
    creation: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))