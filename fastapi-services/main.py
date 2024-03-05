from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from dao.dept_dao import DeptDAO
from dao.emp_dao import EmpDAO
from dao.user_dao import UserDAO
from model.dept_model import Department
from model.user_model import User
from model.emp_model import Employee

app = FastAPI()

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user_dao = UserDAO()
emp_dao = EmpDAO()
dept_dao = DeptDAO()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get_users")
async def getAllUsers():
    return user_dao.get_all_users()


@app.post("/create_users")
async def create(user: User):
    user = user_dao.create_user(user)
    return user


@app.post("/delete_user_by_name")
async def remove_user_by_name(user_name: str):
    try:
        user_dao.delete_user_by_name(user_name)
        return True
    except Exception as e:
        print("Encountered an exception", e)
        return False


@app.post("/delete_user_by_id")
async def remove_user_by_id(user_id: int):
    try:
        user_dao.delete_user_by_id(user_id)
        return True
    except Exception as e:
        print("Encountered an exception", e)
        return False


@app.get("/get_emp/{emp_id}")
async def get_emp_by_id(emp_id: int):
    return emp_dao.get_emp(emp_id)


@app.post("/create_emp", response_model=Employee)
async def create_emp(emp: Employee) -> Employee:
    employee = emp_dao.create_emp(emp)
    return employee


@app.get("/get_dept/{dept_code}")
async def get_dept_by_code(dept_code: str):
    return dept_dao.get_dept(dept_code)


@app.get("/get_all_depts")
async def get_all_depts():
    return dept_dao.get_all_depts()


@app.post("/create_dept", response_model=Department)
async def create_dept(dept: Department) -> Department:
    return dept_dao.create_dept(dept)


@app.post("/delete_dept_by_code")
async def remove_dept_by_code(dept_code: str):
    return dept_dao.delete_dept_by_code(dept_code)


@app.get("/get_all_emp")
async def get_all_emp():
    employees = emp_dao.get_all_emp()
    return employees


@app.get("/delete_emp_by_id/{emp_id}")
async def delete_emp_by_id(emp_id):
    success = emp_dao.delete_emp_by_id(emp_id)
    return success
