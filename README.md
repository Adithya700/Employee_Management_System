#  Flask Employee Management API

A RESTful Employee Management System built using **Flask** and **Blueprints**. This API allows users to perform CRUD (Create, Read, Update, Delete) operations on employee records.

---

##  Features

*  Retrieve all employees
*  Add a new employee
*  Update employee details
*  Delete an employee
*  Modular project structure using Flask Blueprints
*  JSON-based REST API

---

##  Tech Stack

* Python 
* Flask
* Flask Blueprints
* JSON
* Service Layer Architecture

---

## Project Structure

```text
employee-management-api/
│
├── app/
│   ├── routes/
│   │   └── emp_routes.py
│   ├── services/
│   │   └── emp_service.py
│   └── models/
│       └── employee.py
│
├── run.py
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Get All Employees

**Endpoint**

```http
GET /employees/
```

**Response**

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "department": "IT",
    "salary": 50000
  }
]
```

---

### Add Employee

**Endpoint**

```http
POST /employees/
```

**Request Body**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "department": "IT",
  "salary": 50000
}
```

**Response**

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "department": "IT",
  "salary": 50000
}
```

Status Code: `201 Created`

---

### Update Employee

**Endpoint**

```http
PUT /employees/<id>
```

**Request Body**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "department": "HR",
  "salary": 60000
}
```

**Response**

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "department": "HR",
  "salary": 60000
}
```

If the employee does not exist:

```json
{
  "message": "Employee Not Found"
}
```

Status Code: `404 Not Found`

---

### Delete Employee

**Endpoint**

```http
DELETE /employees/<id>
```

**Response**

```json
{
  "message": "Deleted Successfully"
}
```

If the employee does not exist:

```json
{
  "message": "Employee Not Found"
}
```

Status Code: `404 Not Found`

---

##  Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/employee-management-api.git
cd employee-management-api
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python run.py
```

The server will start at:

```text
http://127.0.0.1:5000/
```

---

## Testing the API

You can test the endpoints using:

* Postman
* Thunder Client
* curl commands

Example:

```bash
curl http://127.0.0.1:5000/employees/
```

-

## Author
ADITHYA K S

Built using Flask to practice REST API development, Flask Blueprints, and layered application architecture.
