from flask import (
    Blueprint,
    jsonify,
    request
)

from app.services.emp_service import (
    get_all_employee,
    create_employee,
    update_employee,
    delete_employee
)

emp_bp = Blueprint(
    "employee",
    __name__,
    url_prefix="/employees"
)
print("Employee route loaded")


@emp_bp.route("/", methods=["GET"])
def get_emp():

    employees = get_all_employee()

    return jsonify(
        [emp.to_dict() for emp in employees]
    )


@emp_bp.route("/", methods=["POST"])
def add_emp():

    data = request.json

    emp = create_employee(
    data["name"],
    data["email"],
    data["department"],
    data["salary"]
    )

    return jsonify(
        emp.to_dict()
    ), 201


@emp_bp.route("/<int:id>", methods=["PUT"])
def update_emp(id):

    data = request.json

    emp = update_employee(
    id,
    data["name"],
    data["email"],
    data["department"],
    data["salary"]
  )

    if not emp:
        return jsonify({
            "message": "Employee Not Found"
        }), 404

    return jsonify(emp.to_dict())


@emp_bp.route("/<int:id>", methods=["DELETE"])
def delete_emp(id):

    emp = delete_employee(id)

    if not emp:
        return jsonify({
            "message": "Employee Not Found"
        }), 404

    return jsonify({
        "message": "Deleted Successfully"
    })