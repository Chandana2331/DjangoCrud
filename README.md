# Employee Management System API

This is a Django REST Framework project for managing employees.

## Prerequisites

- Python 3.8+
- Django 5.0+
- Django REST Framework

## Setup Instructions

1.  **Clone the repository/Extract the zip**
2.  **Navigate to the project directory**
    ```bash
    cd employee_project
    ```
    *(Adjust path if necessary depending on where you extracted it)*

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Run Server**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

The API is available at `/api/employees/`.

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/employees/` | Get all employees |
| `POST` | `/api/employees/` | Create a new employee |
| `GET` | `/api/employees/<id>/` | Get employee by ID |
| `PUT` | `/api/employees/<id>/` | Update employee (full) |
| `PATCH` | `/api/employees/<id>/` | Update employee (partial) |
| `DELETE` | `/api/employees/<id>/` | Delete employee |

## Sample Requests

### Create Employee (POST)

**URL:** `http://127.0.0.1:8000/api/employees/`

**Headers:**
`Content-Type: application/json`

**Body:**
```json
{
    "name": "Chandu",
    "email": "john.doe@example.com",
    "department": "IT",
    "salary": 75000.0
}
```

### Get All Employees (GET)

**URL:** `http://127.0.0.1:8000/api/employees/`

### Get Employee by ID (GET)

**URL:** `http://127.0.0.1:8000/api/employees/1/`

### Update Employee (PUT)

**URL:** `http://127.0.0.1:8000/api/employees/1/`

**Body:**
```json
{
    "name": "John Doe Updated",
    "email": "john.doe@example.com",
    "department": "Engineering",
    "salary": 80000.0
}
```

### Delete Employee (DELETE)

**URL:** `http://127.0.0.1:8000/api/employees/1/`
