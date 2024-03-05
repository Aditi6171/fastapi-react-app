import mysql.connector
from dao.base_dao import BaseDAO
from model.emp_model import Employee
class EmpDAO(BaseDAO):
    def __init__(self):
        super().__init__()

    def get_emp(self, emp_id):
        cursor = self.query("SELECT * FROM employee where id = %s", (emp_id,))
        rs = cursor.fetchone()
        if rs is not None:
            emp = Employee(id=rs[0], fullname=rs[1], email=rs[2], mobile=rs[3], city=rs[4], gender=rs[5], dept_code=rs[6], hire_date=rs[7], permanent_employee=rs[8])
        else:
            emp = None
        return emp

    def get_all_emp(self):
        emps = []
        cursor = self.query(" select e.id, e.fullname, e.email, e.mobile, e.city, e.gender, d.code dept_code, d.name dept_name, e.hire_date, e.permanent_employee from employee e, dept d where e.dept_code = d.code", None)
        results = cursor.fetchall()
        for rs in results:
            emp = Employee(id=rs[0], fullname=rs[1], email=rs[2], mobile=rs[3], city=rs[4], gender=rs[5], dept_code=rs[6], dept_name=rs[7], hire_date=rs[8], permanent_employee=rs[9])
            emps.append(emp)
        return emps

    def create_emp(self, emp: Employee):
        sql = "INSERT INTO employee (fullname, email, mobile, city, gender, dept_code, hire_date, permanent_employee) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (emp.fullname, emp.email, emp.mobile, emp.city, emp.gender, emp.dept_code, emp.hire_date, emp.permanent_employee)
        cursor = self.query(sql, val)
        self.commit()
        emp.id = cursor.lastrowid
        return emp

    def delete_emp_by_id(self, emp_id: int):
        sql = "DELETE FROM employee WHERE id = %s"
        val = (emp_id,)
        cursor = self.query(sql, val)
        self.commit()

    def delete_emp_by_name(self, emp_name: str):
        sql = "DELETE FROM employee WHERE name = %s"
        val = (emp_name,)
        cursor = self.query(sql, val)
