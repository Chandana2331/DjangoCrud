# Employee Management System

A modern, feature-rich Employee Management System built with Django REST Framework, featuring a beautiful gradient UI, data visualization, and advanced management capabilities.

## 🌟 Features

### Frontend
- **Modern UI**: Gradient backgrounds with glassmorphism effects
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Real-time Validation**: Instant feedback on form inputs
- **Toast Notifications**: Non-intrusive success/error messages
- **Smooth Animations**: Professional transitions and hover effects

### Admin Dashboard
- **Statistics Cards**: Total employees, average salary, department count
- **Data Visualization**: Interactive Chart.js doughnut chart for department distribution
- **Advanced Search**: Multi-field search (name, email, department)
- **Bulk Actions**: Select and delete multiple employees
- **CSV Export**: Download all employee data
- **Modal Editing**: Beautiful popup form for editing employees
- **Recent Activity**: View last 5 added employees

### API Features
- Full CRUD operations (Create, Read, Update, Delete)
- Employee statistics endpoint
- CSV export endpoint
- Bulk delete endpoint
- Field validation and error handling

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Installation & Setup

### 1. Clone or Download the Project
```bash
cd DjangoCrud
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Admin User (Optional)
```bash
python create_superuser.py
```
This creates an admin user with:
- **Username**: `admin`
- **Password**: `admin`

### 5. Run the Development Server
```bash
python manage.py runserver 0.0.0.0:8080
```

The server will start at `http://127.0.0.1:8080/`

## 🎯 Usage

### Home Page
Visit `http://127.0.0.1:8080/` to:
- Add new employees with the beautiful form
- Fill in required fields: Name, Email, Department, Salary
- Optionally add: Phone, Position, Hire Date

### Admin Dashboard
Visit `http://127.0.0.1:8080/admin-dashboard/` to:
- View employee statistics and charts
- Search and filter employees
- Edit employee details in modal
- Delete single or multiple employees
- Export data to CSV

### Django Admin Panel
Visit `http://127.0.0.1:8080/admin/` to:
- Access Django's built-in admin interface
- Login with admin/admin credentials

## 📡 API Endpoints

### Employee Operations
- **GET** `/api/employees/` - List all employees
- **POST** `/api/employees/` - Create new employee
- **GET** `/api/employees/{id}/` - Get employee by ID
- **PUT** `/api/employees/{id}/` - Update employee
- **DELETE** `/api/employees/{id}/` - Delete employee

### Statistics & Export
- **GET** `/api/employees/stats/` - Get statistics (total, average salary, departments, recent)
- **GET** `/api/employees/export/` - Export all employees to CSV
- **POST** `/api/employees/bulk-delete/` - Bulk delete employees

## 📊 Employee Model

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | Integer | Auto | Primary key |
| name | String | Yes | Employee name (min 2 chars) |
| email | Email | Yes | Unique email address |
| department | String | Yes | Department name |
| salary | Decimal | Yes | Salary (0-10,000,000) |
| phone | String | No | Phone number |
| position | String | No | Job title/position |
| hire_date | Date | No | Date of hire |
| created_at | DateTime | Auto | Record creation timestamp |
| updated_at | DateTime | Auto | Last update timestamp |

## 🧪 Testing

### Test API Endpoints
```bash
python test_api.py
```

### Manual Testing
Use the included Postman collection (`Employee_Management_API.postman_collection.json`) to test all endpoints.

## 📦 Project Structure

```
DjangoCrud/
├── employee_project/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── employees/                 # Main app
│   ├── models.py             # Employee model
│   ├── serializers.py        # DRF serializers
│   ├── views.py              # API views
│   ├── urls.py               # App URLs
│   ├── admin.py              # Admin configuration
│   └── templates/
│       └── employees/
│           ├── index.html           # Home page
│           └── admin_dashboard.html # Admin dashboard
├── manage.py
├── requirements.txt
├── README.md
└── Employee_Management_API.postman_collection.json
```

## 🎨 Technologies Used

- **Backend**: Django 5.x, Django REST Framework
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Charts**: Chart.js 4.x
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Inter)
- **Database**: SQLite (development)

## 🔒 Security Notes

- CSRF protection enabled for all POST/PUT/DELETE requests
- Email uniqueness enforced
- Input validation on both frontend and backend
- REST Framework authentication configured

## 📝 API Request Examples

### Create Employee
```bash
POST /api/employees/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "department": "IT",
  "salary": 75000,
  "phone": "+1234567890",
  "position": "Software Engineer",
  "hire_date": "2024-01-15"
}
```

### Get Statistics
```bash
GET /api/employees/stats/

Response:
{
  "total_employees": 10,
  "average_salary": 65000.50,
  "department_breakdown": [
    {"department": "IT", "count": 5},
    {"department": "HR", "count": 3}
  ],
  "recent_employees": [...]
}
```

### Bulk Delete
```bash
POST /api/employees/bulk-delete/
Content-Type: application/json

{
  "ids": [1, 2, 3]
}
```

## 🤝 Contributing

This is a demonstration project. Feel free to fork and modify as needed.

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created as a comprehensive Django REST Framework demonstration project.

## 🆘 Support

For issues or questions:
1. Check the API documentation above
2. Review the Postman collection for request examples
3. Verify all migrations are applied
4. Ensure the development server is running

## 🎯 Future Enhancements

- User authentication and authorization
- Role-based access control
- Advanced filtering and sorting
- Pagination for large datasets
- Email notifications
- File upload for employee photos
- Performance analytics
- Dark mode toggle
