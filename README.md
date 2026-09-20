# 🔐 SecureBank API — VAPT & Web API Security Assessment

A deliberately security-focused **Flask REST API** designed as a cybersecurity portfolio project to demonstrate **Web/API VAPT, authentication, authorization, OWASP API Security testing, security hardening, evidence collection, and remediation**.

The project follows a practical security assessment workflow:

> **Build → Deploy → Test → Identify → Document → Remediate → Retest**

---

## 🎯 Project Objectives

* Build a realistic REST API with authentication and authorization controls.
* Implement JWT-based authentication and role-based access control.
* Implement object-level authorization to prevent BOLA/IDOR.
* Perform security testing against common API attack surfaces.
* Map findings and test cases to the **OWASP API Security Top 10 (2023)**.
* Maintain reproducible security-testing evidence.
* Apply security hardening and perform retesting.
* Deploy the application using **Render + PostgreSQL + Gunicorn**.
* Produce a professional security-assessment workflow suitable for a VAPT portfolio.

---

## 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │       Client        │
                         │ Browser / cURL      │
                         └──────────┬──────────┘
                                    │ HTTPS
                                    ▼
                         ┌─────────────────────┐
                         │       Render        │
                         │    Web Service      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Flask REST API      │
                         │      + Gunicorn     │
                         └──────────┬──────────┘
                                    │
                     ┌──────────────┴──────────────┐
                     │                             │
                     ▼                             ▼
             ┌───────────────┐             ┌───────────────┐
             │ JWT / Auth    │             │ Authorization │
             │ Authentication│             │ RBAC + BOLA   │
             └───────────────┘             └───────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     PostgreSQL      │
                         │      Database       │
                         └─────────────────────┘
```

---

## 🛠️ Technology Stack

| Category             | Technology                       |
| -------------------- | -------------------------------- |
| Language             | Python                           |
| Framework            | Flask                            |
| Authentication       | JWT                              |
| Password Security    | Werkzeug password hashing        |
| ORM                  | Flask-SQLAlchemy                 |
| Database             | PostgreSQL                       |
| Local Database       | SQLite                           |
| Web Server           | Gunicorn                         |
| API Documentation    | Swagger / OpenAPI                |
| Deployment           | Render                           |
| Testing              | cURL / Manual VAPT               |
| Security Methodology | OWASP API Security Top 10 (2023) |
| Version Control      | Git / GitHub                     |

---

## 🔑 API Features

### Authentication

* User registration
* User login
* JWT access tokens
* Password hashing
* Invalid credential handling
* JWT validation
* Protected API endpoints

### Authorization

* User/Admin role separation
* Role-based authorization
* Object-level authorization
* User account isolation
* BOLA/IDOR protection

### Account Management

* Account creation
* Account retrieval
* User-specific account access
* Account ownership enforcement

### Security Controls

* Security HTTP headers
* CSP
* `X-Content-Type-Options`
* `X-Frame-Options`
* Debug mode disabled
* Authentication enforcement
* Authorization enforcement

---

# 🧪 VAPT Methodology

The security assessment was performed using a structured workflow:

```text
1. Reconnaissance
       ↓
2. API Enumeration
       ↓
3. Authentication Testing
       ↓
4. Authorization Testing
       ↓
5. BOLA / IDOR Testing
       ↓
6. Injection Testing
       ↓
7. Security Header Testing
       ↓
8. API Documentation / Exposure Review
       ↓
9. Evidence Collection
       ↓
10. Remediation
       ↓
11. Retesting
```

---

# 🔍 Security Testing Performed

## 1. Authentication Testing

Tested:

* Successful registration
* Successful login
* Invalid credentials
* Missing JWT
* Invalid JWT
* Malformed Authorization header

Example:

```bash
POST /api/auth/login
```

Expected secure behavior:

```text
Valid credentials      → 200 OK
Invalid credentials    → 401 Unauthorized
Missing JWT            → 401 Unauthorized
Invalid JWT            → 401 Unauthorized
```

---

## 2. Authorization Testing

Tested whether a normal user could access administrative functionality.

```text
GET /api/accounts/admin-test
```

Expected:

```text
Normal User → 403 Forbidden
```

Result:

```text
403 Forbidden
```

Role-based authorization was enforced successfully.

---

## 3. BOLA / IDOR Testing

A second user was created and authenticated.

The second user attempted to access the first user's account:

```text
GET /api/accounts/1
```

Expected secure behavior:

```text
User B → User A Account
        ↓
   Access Denied
```

Observed:

```text
404 Not Found
```

This demonstrated object-level access isolation for the tested scenario.

---

## 4. SQL Injection Testing

A login authentication-bypass payload was tested:

```text
' OR 1=1 --
```

Observed:

```text
401 Unauthorized
```

No authentication bypass was observed for the tested payload.

> Note: A negative result for one payload does not prove complete immunity to SQL injection. Broader automated/manual testing can provide additional coverage.

---

## 5. XSS Testing

Input-handling behavior was tested using controlled XSS-oriented input.

The application accepted the registration request, but successful acceptance alone does **not** demonstrate XSS execution.

XSS confirmation requires a reflection or rendering sink where attacker-controlled input reaches an executable browser context.

Therefore, XSS was treated as a test case rather than claiming a confirmed vulnerability without evidence of execution.

---

## 6. JWT Security Testing

Tested:

* Missing JWT
* Invalid JWT
* Malformed Authorization header
* Valid JWT
* Protected endpoint access
* User identity enforcement

Example:

```http
Authorization: Bearer <JWT>
```

Protected endpoints reject requests when authentication is missing or invalid.

---

## 7. Security Headers

The deployed API was tested for security headers.

Observed:

```http
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Security-Policy: default-src 'self'
```

These controls provide additional browser-side security hardening.

---

# 🗺️ OWASP API Security Top 10 Mapping

| OWASP API Risk                                         | Test / Control                                                     |
| ------------------------------------------------------ | ------------------------------------------------------------------ |
| API1 — Broken Object Level Authorization               | BOLA/IDOR testing + object ownership checks                        |
| API2 — Broken Authentication                           | Registration, login, JWT validation testing                        |
| API3 — Broken Object Property Level Authorization      | Object access and response behavior review                         |
| API4 — Unrestricted Resource Consumption               | API surface reviewed; rate limiting identified as future hardening |
| API5 — Broken Function Level Authorization             | Admin endpoint authorization testing                               |
| API6 — Unrestricted Access to Sensitive Business Flows | Authentication and account-flow review                             |
| API7 — Server Side Request Forgery                     | No SSRF-prone functionality identified in current API scope        |
| API8 — Security Misconfiguration                       | Debug mode disabled + security headers                             |
| API9 — Improper Inventory Management                   | Swagger/OpenAPI endpoint inventory                                 |
| API10 — Unsafe Consumption of APIs                     | External API consumption not present in current scope              |

> Mapping reflects the project's implemented functionality and tested attack surface. Absence of a vulnerability test should not be interpreted as proof that the risk is impossible.

---

# 📁 Evidence Structure

Security-testing evidence is maintained in a structured directory:

```text
evidence/
├── authentication/
│   ├── 01-registration-success.txt
│   ├── 02-login-success.txt
│   ├── 03-invalid-login.txt
│   ├── 03-missing-jwt.txt
│   ├── 04-invalid-jwt.txt
│   └── 05-malformed-auth-header.txt
│
├── authorization/
│   ├── 01-my-account-isolation.txt
│   ├── 02-admin-authorization-enforced.txt
│   └── 03-bola-negative.txt
│
├── accounts/
│   ├── 01-account-creation-success.txt
│   └── 02-my-account-success.txt
│
├── security-headers/
│   └── 01-security-headers.txt
│
├── swagger/
│   ├── 01-swagger-ui.png
│   └── 02-swagger-json-exposure.txt
│
└── injection/
    ├── 01-sqli-login-negative.txt
    └── 02-xss-negative.txt
```

---

# 🚀 Live Deployment

The application is deployed using:

```text
GitHub
   ↓
Render Web Service
   ↓
Gunicorn
   ↓
Flask API
   ↓
PostgreSQL
   ↓
HTTPS
```

### API

```text
https://securebank-api-vapt.onrender.com
```

### Swagger Documentation

```text
https://securebank-api-vapt.onrender.com/docs/
```

Swagger provides an interactive interface for exploring the API endpoints.

---

# 📋 API Endpoints

| Method | Endpoint                     | Purpose                    | Authentication  |
| ------ | ---------------------------- | -------------------------- | --------------- |
| POST   | `/api/auth/register`         | Register user              | No              |
| POST   | `/api/auth/login`            | Authenticate user          | No              |
| POST   | `/api/accounts/create`       | Create account             | JWT             |
| GET    | `/api/accounts/my-account`   | Get current user's account | JWT             |
| GET    | `/api/accounts/<account_id>` | Get specific account       | JWT + ownership |
| GET    | `/api/accounts/admin-test`   | Admin-only functionality   | JWT + Admin     |
| GET    | `/docs/`                     | Swagger UI                 | No              |
| GET    | `/docs/swagger.json`         | OpenAPI specification      | No              |

---

# 🔐 Security Hardening Implemented

The project includes several security controls:

### Authentication

* JWT-based authentication
* Password hashing
* Invalid credential handling
* Protected endpoints

### Authorization

* Role-based access control
* User identity validation
* Object ownership checks
* Admin-only endpoint protection

### Application Hardening

* Debug mode disabled
* HTTP security headers
* Content Security Policy
* `X-Frame-Options`
* `X-Content-Type-Options`

### Deployment Security

Sensitive configuration is provided through environment variables:

```text
DATABASE_URL
JWT_SECRET_KEY
```

Secrets are **not stored in source control**.

---

# 📊 VAPT Result Summary

| Test Category               | Result                       |
| --------------------------- | ---------------------------- |
| Registration                | ✅ Passed                     |
| Login / JWT                 | ✅ Passed                     |
| Missing JWT                 | ✅ Blocked                    |
| Invalid JWT                 | ✅ Blocked                    |
| BOLA / IDOR                 | ✅ Blocked in tested scenario |
| Admin Authorization         | ✅ Enforced                   |
| SQLi Authentication Bypass  | ✅ Not observed               |
| Security Headers            | ✅ Present                    |
| Swagger / API Documentation | ✅ Available                  |
| Live Deployment             | ✅ Operational                |

---

# 📸 Evidence & Reporting

The repository contains:

* VAPT test evidence
* Authentication test results
* Authorization test results
* Injection test results
* Security-header evidence
* Swagger screenshots
* OWASP API Security mapping
* Remediation/retest documentation

---

# 🧰 Local Setup

## Clone

```bash
git clone https://github.com/gupta1111/securebank-api-vapt.git
cd securebank-api-vapt
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Linux / Kali

```bash
source venv/bin/activate
```

### Windows

```cmd
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

```bash
export DATABASE_URL="sqlite:///securebank.db"
export JWT_SECRET_KEY="change-this-development-secret"
```

For Windows:

```cmd
set DATABASE_URL=sqlite:///securebank.db
set JWT_SECRET_KEY=change-this-development-secret
```

## Run

```bash
python run.py
```

API:

```text
http://127.0.0.1:5000
```

Swagger:

```text
http://127.0.0.1:5000/docs/
```

---

# 🧪 Example Security Test

Missing JWT:

```bash
curl -i http://127.0.0.1:5000/api/accounts/my-account
```

Expected:

```text
401 Unauthorized
```

BOLA test:

```bash
curl -i http://127.0.0.1:5000/api/accounts/<ACCOUNT_ID> \
-H "Authorization: Bearer <USER_2_JWT>"
```

Expected:

```text
404 Not Found
```

for an account owned by another user.

---

# 📚 Security Concepts Demonstrated

This project demonstrates practical experience with:

* Web API Security
* REST API Security
* VAPT
* OWASP API Security Top 10
* JWT Authentication
* RBAC
* BOLA / IDOR
* Authentication Testing
* Authorization Testing
* Injection Testing
* XSS Testing
* Security Headers
* API Enumeration
* Evidence Collection
* Security Documentation
* Remediation & Retesting
* Secure Deployment
* PostgreSQL
* Git/GitHub

---

# ⚠️ Disclaimer

This project is intended for **educational, defensive security testing, and portfolio purposes**.

All security testing should be performed only against systems for which you have explicit authorization.

Do not use the testing techniques demonstrated in this repository against third-party systems without permission.

---

# 👨‍💻 Author

**Bhola Gupta**

Cybersecurity / VAPT Portfolio Project

GitHub:

https://github.com/gupta1111/securebank-api-vapt

---

## ⭐ Project Highlights

```text
Flask REST API
      +
JWT Authentication
      +
RBAC
      +
BOLA/IDOR Protection
      +
OWASP API Security Testing
      +
VAPT Evidence
      +
Security Hardening
      +
PostgreSQL
      +
Gunicorn
      +
Render Deployment
```

**SecureBank API — Build it. Test it. Secure it. Retest it.**
