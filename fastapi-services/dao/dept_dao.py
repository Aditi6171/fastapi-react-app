from dao.base_dao import BaseDAO
from model.dept_model import Department


class DeptDAO(BaseDAO):
    def __init__(self):
        super().__init__()

    def get_dept(self, dept_code):
        cursor = self.query("SELECT * FROM dept WHERE code = %s", (dept_code,))
        rs = cursor.fetchone()
        if rs is not None:
            dept = Department(code=rs[0], name=rs[1], description=rs[2])
        else:
            dept = None
        return dept

    def get_all_depts(self):
        depts = []
        cursor = self.query("SELECT * FROM dept", None)
        results = cursor.fetchall()
        for rs in results:
            dept = Department(code=rs[0], name=rs[1], description=rs[2])
            depts.append(dept)
        return depts

    def create_dept(self, dept):
        sql = "INSERT INTO dept (code, name, description) VALUES (%s, %s, %s)"
        val = (dept.code, dept.name, dept.description)
        cursor = self.query(sql, val)
        self.commit()
        return dept

    def delete_dept_by_code(self, dept_code: str):
        sql = "DELETE FROM dept WHERE code = %s"
        val = (dept_code,)
        cursor = self.query(sql, val)
        self.commit()
