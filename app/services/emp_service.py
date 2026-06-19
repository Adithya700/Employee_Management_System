from app import db
from app.models.employee import Employee


def get_all_employee():

    return Employee.query.all()


def create_employee(name, email, department, salary):

    emp = Employee(
        name=name,
        email=email,
        department=department,
        salary=salary
    )

    db.session.add(emp)
    db.session.commit()

    return emp


def update_employee(emp_id, name, email, department, salary):

    emp = Employee.query.get(emp_id)

    if emp:

        emp.name = name
        emp.email = email
        emp.department = department
        emp.salary = salary

        db.session.commit()

    return emp


def delete_employee(emp_id):

    emp = Employee.query.get(emp_id)

    if emp:

        db.session.delete(emp)
        db.session.commit()

    return emp