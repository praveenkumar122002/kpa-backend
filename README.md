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


## API Endpoints Implemented

### 1.1. POST `/api/forms/wheel-specifications`

- **URL:** `http://127.0.0.1:8000/api/forms/wheel-specifications`
- **Method:** `POST`
- **Headers:** `Content-Type: application/json`
- **Body:**
    ```
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "treadDiameterNew": "915 (900-1000)",
        "lastShopIssueSize": "837 (800-900)",
        "condemningDia": "825 (800-900)",
        "wheelGauge": "1600 (+2,-1)",
        "variationSameAxle": "0.5",
        "variationSameBogie": "5",
        "variationSameCoach": "13",
        "wheelProfile": "29.4 Flange Thickness",
        "intermediateWWP": "20 TO 28",
        "bearingSeatDiameter": "130.043 TO 130.068",
        "rollerBearingOuterDia": "280 (+0.0/-0.035)",
        "rollerBearingBoreDia": "130 (+0.0/-0.025)",
        "rollerBearingWidth": "93 (+0/-0.250)",
        "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
        "wheelDiscWidth": "127 (+4/-0)"
      }
    }
    ```

#### Example Success Response
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

text
---

### 1.2. GET `/api/forms/wheel-specifications`
- **Method:** `GET`
- **URL Example (all):**
    ```
    http://127.0.0.1:8000/api/forms/wheel-specifications
    ```
- **URL Example (with filters):**
    ```
    http://127.0.0.1:8000/api/forms/wheel-specifications?formNumber=WHEEL-2025-001&submittedBy=user_id_123&submittedDate=2025-07-03
    ```

#### Example Success Response
{
"success": true,
"message": "Filtered wheel specification forms fetched successfully.",
"data": [
{
"formNumber": "WHEEL-2025-001",
"submittedBy": "user_id_123",
"submittedDate": "2025-07-03",
"fields": {
"treadDiameterNew": "915 (900-1000)",
"lastShopIssueSize": "837 (800-900)",
"condemningDia": "825 (800-900)",
"wheelGauge": "1600 (+2,-1)"
}
}
]
}

text
---

### 1.3. POST `/api/forms/bogie-checksheet`
- **Method:** `POST`
- **URL:** `http://127.0.0.1:8000/api/forms/bogie-checksheet`
- **Headers:** `Content-Type: application/json`
- **Body:**
    ```
    {
      "formNumber": "BOGIE-2025-001",
      "inspectionBy": "user_id_456",
      "inspectionDate": "2025-07-03",
      "bogieDetails": {
        "bogieNo": "BG1234",
        "makerYearBuilt": "RDSO/2018",
        "incomingDivAndDate": "NR / 2025-06-25",
        "deficitComponents": "None",
        "dateOfIOH": "2025-07-01"
      },
      "bogieChecksheet": {
        "bogieFrameCondition": "Good",
        "bolster": "Good",
        "bolsterSuspensionBracket": "Cracked",
        "lowerSpringSeat": "Good",
        "axleGuide": "Worn"
      },
      "bmbcChecksheet": {
        "cylinderBody": "WORN OUT",
        "pistonTrunnion": "GOOD",
        "adjustingTube": "DAMAGED",
        "plungerSpring": "GOOD"
      }
    }
    ```

#### Example Success Response
{
"success": true,
"message": "Bogie checksheet submitted successfully.",
"data": {
"formNumber": "BOGIE-2025-001",
"inspectionBy": "user_id_456",
"inspectionDate": "2025-07-03",
"status": "Saved"
}
}
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
