# kpa-backend
KPA Assignment: Wheel & Bogie Form Backend (Django)
Project Description
This repository provides the backend API for KPA'sWheel Specification and Bogie Checksheet formsThe API is implemented in Django, allows storing form submissions in PostgreSQL, and is designed to integrate seamlessly with the provided frontend and adhere strictly to the assignment's structure.

Tech Stack
Python 3.x

Django 4.x

Django REST Framework

PostgreSQL 12+

Docker (optional, for containerized development)

Postman (for API testing)

dotenv (for environment variable management)

Setup Instructions
Clone the repository:

text
git clone https://github.com/praveenkumar122002/kpa-backend
cd kpa-backend
Create and activate a Python virtual environment:


Install dependencies:

text
pip install -r requirements.txt
Set up PostgreSQL:

Create a database named kpa_db, and a user kpa_user with password kpa_password.

Edit kpa_backend/settings.py or create a .env file with:

text
DB_NAME=kpa_db
DB_USER=kpa_user
DB_PASSWORD=kpa_password
DB_HOST=localhost
DB_PORT=5432
Apply migrations:

text
python manage.py makemigrations
python manage.py migrate
Start the server:

text
python manage.py runserver
(Optional) Run with Docker:

text
docker-compose up --build
Environment Variables
If using a .env file, include these keys:

text
DB_NAME=kpa_db
DB_USER=kpa_user
DB_PASSWORD=kpa_password
DB_HOST=localhost
DB_PORT=5432
API Endpoints Implemented

1. POST /api/forms/wheel-specifications
Description: Submit a new wheel specification.

Sample Request:

json
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    ...
  }
}
Sample Response:

json
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "status": "Saved",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03"
  }
}
2. GET /api/forms/wheel-specifications
Description: Retrieve all or filtered wheel specifications.

Query Params Supported: formNumber, submittedBy, submittedDate

3. POST /api/forms/bogie-checksheet
Description: Submit a new bogie checksheet.

Sample Request/Response: Matches the assignment’s provided structure.

How to Test
Import the included Postman collection (KPA_form data.postman_collection.json) into Postman.

Use the sample data above to make POST and GET requests.

(Optional) Run the provided frontend and verify it communicates with your backend.

Assumptions & Limitations
No authentication is implemented for simplicity.

Fields with dynamic or variable content are stored as JSON in the database.

API responses strictly follow the structures given in the assignment and sample Postman docs.

Additional Info / Bonus Features
Docker support included for quick local setup (see Dockerfile and docker-compose.yml).

Basic input validation is handled by DRF serializers.

Uses environment-based configuration for sensitive settings via .env.

 Author
Praveen Kumar  
This README will fulfill the requirements for clarity, reproducibility, and professional documentation for your assignment.
