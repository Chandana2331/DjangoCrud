# API Testing Guide

## Quick Start

1. **Import Postman Collection**:
   - Open Postman
   - Click "Import"
   - Select `Employee_Management_API.postman_collection.json`

2. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

3. **Test Endpoints** in this order:

## Testing Sequence

### 1. Create Employees (POST)
**Endpoint**: `POST /api/employees/`

**Request Body**:
```json
{
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "department": "IT",
  "salary": 75000,
  "phone": "+1234567890",
  "position": "Software Engineer",
  "hire_date": "2024-01-15"
}
```

**Expected Response** (201 Created):
```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "department": "IT",
  "salary": "75000.00",
  "phone": "+1234567890",
  "position": "Software Engineer",
  "hire_date": "2024-01-15",
  "created_at": "2024-02-12T06:30:00Z",
  "updated_at": "2024-02-12T06:30:00Z"
}
```

### 2. Get All Employees (GET)
**Endpoint**: `GET /api/employees/`

**Expected Response** (200 OK):
```json
[
  {
    "id": 1,
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "department": "IT",
    "salary": "75000.00",
    ...
  }
]
```

### 3. Get Statistics (GET)
**Endpoint**: `GET /api/employees/stats/`

**Expected Response** (200 OK):
```json
{
  "total_employees": 3,
  "average_salary": 68333.33,
  "department_breakdown": [
    {"department": "IT", "count": 2},
    {"department": "HR", "count": 1}
  ],
  "recent_employees": [...]
}
```

### 4. Update Employee (PUT)
**Endpoint**: `PUT /api/employees/1/`

**Request Body**:
```json
{
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "department": "IT",
  "salary": 80000,
  "position": "Senior Software Engineer"
}
```

### 5. Bulk Delete (POST)
**Endpoint**: `POST /api/employees/bulk-delete/`

**Request Body**:
```json
{
  "ids": [1, 2]
}
```

**Expected Response** (200 OK):
```json
{
  "deleted": 2
}
```

### 6. Export CSV (GET)
**Endpoint**: `GET /api/employees/export/`

**Expected Response**: CSV file download

## Error Responses

### Validation Error (400)
```json
{
  "name": ["This field is required."],
  "salary": ["Salary cannot be negative"]
}
```

### Not Found (404)
```json
{
  "detail": "Not found."
}
```

## Testing Tips

1. **Create multiple employees** with different departments to see charts
2. **Test validation** by sending invalid data (negative salary, duplicate email)
3. **Test bulk delete** with multiple IDs
4. **Export CSV** after adding several employees
5. **Check statistics** to verify calculations

## Web Interface Testing

### Home Page (`/`)
- Fill form with valid data
- Try submitting with missing fields
- Check toast notifications
- Verify loading states

### Admin Dashboard (`/admin-dashboard/`)
- View statistics cards
- Check department chart
- Use multi-field search
- Test bulk selection
- Edit employee via modal
- Export to CSV
- Delete employees

## Automated Testing

Run the test script:
```bash
python test_api.py
```

This will test all CRUD operations automatically.
