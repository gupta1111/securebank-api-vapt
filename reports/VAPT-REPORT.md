# SecureBank API
# Vulnerability Assessment & Penetration Testing Report

## 1. Executive Summary

SecureBank is a Flask-based REST API developed for security assessment
and VAPT practice.

The application implements:

- User registration
- User authentication
- JWT-based authentication
- Role-based authorization
- Object-level authorization
- Bank account management
- Swagger API documentation
- Security headers

Testing focused on authentication, authorization, object-level access
control, injection, XSS, API exposure, and security hardening.

No confirmed authentication bypass, BOLA/IDOR vulnerability, SQL
injection authentication bypass, or XSS execution was demonstrated
during the performed tests.

## 2. Scope

Target:

http://127.0.0.1:5000

Primary API endpoints tested:

- POST /api/auth/register
- POST /api/auth/login
- POST /api/accounts/create
- GET /api/accounts/my-account
- GET /api/accounts/<account_id>
- GET /api/accounts/admin-test
- GET /docs/swagger.json

## 3. Methodology

Testing included:

1. Authentication testing
2. Authorization testing
3. BOLA/IDOR testing
4. Function-level authorization testing
5. SQL injection testing
6. XSS testing
7. Security-header review
8. Swagger/API exposure review
9. JWT validation testing
10. Retesting after security controls

## 4. Key Test Results

### Authentication

Missing and invalid authentication tokens were tested against protected
endpoints.

Result:
Authentication controls rejected unauthorized requests.

### Authorization

A normal user attempted to access an administrative endpoint.

Result:
HTTP 403 Forbidden.

### BOLA / IDOR

A user attempted to access another user's account.

Result:
HTTP 404 Not Found.

No unauthorized object access was demonstrated.

### SQL Injection

Authentication bypass payload:

' OR 1=1 --

Result:
HTTP 401 Unauthorized.

No SQL injection authentication bypass was demonstrated.

### XSS

Payload:

<script>alert(1)</script>

Result:
The payload was not demonstrated to execute or reflect in an application
response.

### Security Headers

Observed:

X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Security-Policy

### Swagger

Swagger UI and swagger.json were accessible.

This was documented as an API information-disclosure/security-hardening
observation rather than a confirmed exploitable vulnerability.

## 5. Security Improvements Implemented

- JWT authentication
- Password hashing
- Role-based authorization
- Object-level authorization
- Debug mode disabled
- Security headers
- Swagger API documentation
- Duplicate account prevention
- Evidence-based security testing

## 6. Conclusion

The SecureBank API was subjected to a structured VAPT process covering
authentication, authorization, injection, object-level access control,
API documentation exposure, and security hardening.

The performed tests primarily demonstrated correctly enforced security
controls, with selected hardening observations documented separately.

## 7. Evidence

Evidence is stored under:

evidence/

Authentication:
- registration success
- login success
- invalid/missing authentication tests

Authorization:
- account isolation
- admin authorization
- BOLA/IDOR testing

Injection:
- SQL injection negative test
- XSS negative test

Security Headers:
- security header response

Swagger:
- Swagger UI
- Swagger JSON exposure

