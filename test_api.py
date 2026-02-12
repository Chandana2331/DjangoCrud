import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/employees/"

def print_response(response):
    print(f"Status Code: {response.status_code}")
    try:
        print(json.dumps(response.json(), indent=4))
    except:
        print(response.text)
    print("-" * 20)

def test_api():
    # 1. Create Employee
    print("Testing CREATE Employee...")
    data = {
        "name": "Alice Smith",
        "email": "alice@example.com",
        "department": "HR",
        "salary": 60000.0
    }
    response = requests.post(BASE_URL, json=data)
    print_response(response)
    if response.status_code == 201:
        emp_id = response.json()['id']
    else:
        print("Failed to create employee, stopping tests.")
        return

    # 2. Get All Employees
    print("\nTesting GET ALL Employees...")
    response = requests.get(BASE_URL)
    print_response(response)

    # 3. Get Employee by ID
    print(f"\nTesting GET Employee by ID ({emp_id})...")
    response = requests.get(f"{BASE_URL}{emp_id}/")
    print_response(response)

    # 4. Update Employee
    print(f"\nTesting UPDATE Employee ({emp_id})...")
    update_data = {
        "name": "Alice Smith-Jones",
        "email": "alice@example.com",
        "department": "HR Management",
        "salary": 70000.0
    }
    response = requests.put(f"{BASE_URL}{emp_id}/", json=update_data)
    print_response(response)

    # 5. Delete Employee
    print(f"\nTesting DELETE Employee ({emp_id})...")
    response = requests.delete(f"{BASE_URL}{emp_id}/")
    print(f"Status Code: {response.status_code}")
    print("-" * 20)

    # Verify Deletion
    print("\nVerifying Deletion...")
    response = requests.get(f"{BASE_URL}{emp_id}/")
    print_response(response)

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Make sure it is running.")
