# Django REST API for user and organisation management, utilizing a Postgres SQL database. The application is deployed on Clever Cloud.

## Models and Business Logic:

1. **User**
2. **Organisation**

## [Live_url] https://ancestor-org.cleverapps.io/

### A) Authentication

#### 1) Register API
- **Endpoint:** `POST https://ancestor-org.cleverapps.io/auth/register`
- **Request Payload:**
```{
    "firstName": "String",
    "lastName": "String",
    "email": "String",
    "password": "String",
    "phone": "String"
}
```
- **Successful Response (HTTP Status Code: 201 Created):**

```
{
    "status": "success",
    "message": "Registration successful",
    "data": {
        "accessToken": "String-access-token",
        "user": {
            "userId": "String",
            "email": "String",
            "firstName": "String",
            "lastName": "String",
            "phone": "String"
        }
    }
}
```
#### 2) Login
- **Endpoint:** `POST https://ancestor-org.cleverapps.io/auth/login`
- **Request Payload:**

```
{
"email": "String",
"password": "String"
}
```

- **Successful Response (HTTP Status Code: 200 OK):**

  
```
{
    "status": "success",
    "message": "Login successful",
    "data": {
        "accessToken": "",
        "user": {
            "userId": "String-access-token",
            "email": "String",
            "firstName": "String",
            "lastName": "String",
            "phone": "String"
        }
    }
}
```

### B) User

#### 1) Get User By User Id API
- **Endpoint:** `GET https://ancestor-org.cleverapps.io/api/users/<userId>`
- **Request Payload:**


- **Successful Response (HTTP Status Code: 200 OK):**

```
{
    "status": "success",
    "message": "User details retrieved successfully",
    "data": {
        "userId": "String",
        "email": "String",
        "firstName": "String",
        "lastName": "String",
        "phone": "String"
    }
}
```

#### 2) Add User to an Organisation API
- **Endpoint:** `POST https://ancestor-org.cleverapps.io/api/organisations/<orgId>/users`
- **Request Payload:**
```
{
    "userId": "String"
}
```

- **Successful Response (HTTP Status Code: 200 OK):**

```
{
    "status": "success",
    "message": "User added to organisation successfully"
}
```

### C) Organisation

#### 1) Create Organisation API
- **Endpoint:** `POST https://ancestor-org.cleverapps.io/api/organisations`
- **Request Payload:**
```
{
    "name": "String",
    "description": "String"
}
```
- **Successful Response (HTTP Status Code: 201 CREATED):**

```
{
    "status": "success",
    "message": "Organisation created successfully",
    "data": {
        "orgId": "Strig",
        "name": "String",
        "description": "String"
    }
}
```

#### 2) Get All Organisation API
- **Endpoint:** `GET https://ancestor-org.cleverapps.io/api/organisations`
- **Request Payload:**


- **Successful Response (HTTP Status Code: 200 OK):**

```
{
    "status": "success",
    "message": "Organisations retrieved successfully",
    "data": {
        "organisations": [
            {
                "orgId": "String",
                "name": "String's Organisation",
                "description": "String"
            }
        ]
    }
}
```

#### 3) Get Organisation By Organisation Id API
- **Endpoint:** `GET https://ancestor-org.cleverapps.io/api/organisations/<orgId>`
- **Request Payload:**


- **Successful Response (HTTP Status Code: 200 OK):**

```
{
    "status": "success",
    "message": "Organisation retrieved successfully",
    "data": {
        "orgId": "String",
        "name": "String",
        "description": "String"
    }
}
```
# Running the application locally

### Installation

- **Clone the repository:**
```commandline
git clone https://github.com/WaveGuide1/organisation-api
cd your-repo
```
- **Create and activate a virtual environment on linux os (This might not work on Window OS):**
```commandline
python3 -m venv venv
source venv/bin/activate
```
- **Install dependencies:**
```commandline
pip install -r requirements.txt
```

- **Create a Postgres SQL database.**
- **Update database credentials in setting.py.**
- **Apply migrations**
```commandline
python manage.py makemigrations
python manage.py migrate
```

- **Start the development server:**
```commandline
python3 manage.py runserver
```
### Replace the live_url with local url (E.g. http://localhost:8000/) other parts of the endpoints remains the same as stated above.
