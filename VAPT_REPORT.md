# SecureBank API - VAPT Report

## 1. Project Overview

SecureBank is a Flask-based banking REST API developed for security assessment and penetration-testing practice.

## 2. Security Testing Performed

- JWT authentication testing
- Authentication failure testing
- Authorization testing
- Broken Object Level Authorization (BOLA/IDOR) testing
- Role-Based Access Control testing
- Duplicate account testing
- Security-header testing
- Debug configuration testing
- Error handling and endpoint enumeration testing

## 3. Findings

### VAPT-01 - Debug Mode Enabled

OWASP: API8 - Security Misconfiguration

Initial configuration used Flask debug mode.

Remediation:
- Disabled debug mode using `debug=False`.

Status: Remediated

### VAPT-02 - Security Headers

OWASP: API8 - Security Misconfiguration

Implemented:

- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- Content-Security-Policy: default-src 'self'

Status: Remediated

### VAPT-03 - Object-Level Authorization

OWASP: API1 - Broken Object Level Authorization

Bob attempted to access Alice's account.

Result:

HTTP 404 - account not found

Status: Security control validated

### VAPT-04 - Function-Level Authorization

OWASP: API5 - Broken Function Level Authorization

A normal user attempted to access the administrative endpoint.

Result:

HTTP 403 - admin access required

Status: Security control validated

### VAPT-05 - JWT Authentication

OWASP: API2 - Broken Authentication

Tested:

- Missing JWT
- Malformed JWT
- Invalid JWT
- Expired JWT
- Valid JWT

Unauthorized requests were rejected.

Status: Security control validated

## 4. Retesting

All implemented security fixes were retested after remediation.

Results:

- Debug mode disabled
- Security headers present
- Account ownership enforced
- Admin authorization enforced
- JWT authentication enforced

## 5. Conclusion

The SecureBank API was assessed for common API security weaknesses. Identified configuration weaknesses were remediated and authorization/authentication controls were retested successfully.
