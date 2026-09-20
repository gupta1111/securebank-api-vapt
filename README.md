# SecureBank API - VAPT Project

A Flask REST API built for hands-on Web API security testing and VAPT practice.

## Features

- User registration and login
- JWT authentication
- Role-based authorization
- Banking account management
- Account ownership enforcement
- Admin-only endpoint
- Security headers
- Error handling

## Security Testing

The project was tested for:

- JWT authentication
- Broken Object Level Authorization
- Broken Function Level Authorization
- Authentication failures
- Authorization failures
- Security misconfiguration
- Debug mode exposure
- Security headers

## Tools

- Python
- Flask
- Flask-JWT-Extended
- SQLAlchemy
- SQLite
- cURL
- Git

## VAPT Methodology

1. Reconnaissance
2. Authentication testing
3. Authorization testing
4. IDOR/BOLA testing
5. RBAC testing
6. Configuration testing
7. Remediation
8. Retesting
9. OWASP API Security mapping

## Project Structure

```text
securebank-vapt/
├── app/
│   ├── models/
│   ├── routes/
│   └── __init__.py
├── evidence/
├── instance/
├── run.py
├── VAPT_REPORT.md
└── README.md
