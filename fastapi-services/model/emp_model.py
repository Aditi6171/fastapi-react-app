from datetime import date

from pydantic import BaseModel


class Employee(BaseModel):
    id: int | None = None
    fullname: str
    email: str
    mobile: str
    city: str | None = None
    gender: str | None = None
    dept_code: str | None = None
    dept_name: str | None = None
    hire_date: date | None = None
    permanent_employee: str = "no"