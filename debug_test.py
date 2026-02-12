import requests
import json

# Test adding an employee
url = "http://127.0.0.1:8000/api/employees/"
data = {
    "name": "Debug Test User",
    "email": "debugtest@example.com",
    "department": "Testing",
    "salary": 55000
}

print("Testing Add Employee API...")
print(f"URL: {url}")
print(f"Data: {json.dumps(data, indent=2)}")

try:
    response = requests.post(url, json=data)
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 201:
        print("\n✅ SUCCESS! Employee added successfully!")
    else:
        print(f"\n❌ FAILED! Status: {response.status_code}")
except Exception as e:
    print(f"\n❌ ERROR: {e}")
