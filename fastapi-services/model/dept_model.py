from pydantic import BaseModel

class Department(BaseModel):
    code: str
    name: str
    description: str | None = None
