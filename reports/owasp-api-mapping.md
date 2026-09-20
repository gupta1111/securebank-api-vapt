# SecureBank API - OWASP API Security Mapping

Reference: OWASP API Security Top 10 - 2023

| OWASP Category | Test Performed | Result |
|---|---|---|
| API1: Broken Object Level Authorization | Cross-user account access | Negative - authorization enforced |
| API2: Broken Authentication | Missing/invalid JWT, invalid login | Negative - authentication enforced |
| API3: Broken Object Property Level Authorization | Account object/property review | No confirmed vulnerability |
| API4: Unrestricted Resource Consumption | Basic request behavior reviewed | No confirmed vulnerability |
| API5: Broken Function Level Authorization | Normal user -> admin endpoint | Negative - 403 enforced |
| API6: Unrestricted Access to Sensitive Business Flows | Basic business-flow review | No confirmed vulnerability |
| API7: Server Side Request Forgery | No user-controlled server-side URL fetch identified | Not applicable / no confirmed vulnerability |
| API8: Security Misconfiguration | Debug mode, headers, Swagger exposure | Hardening observations identified |
| API9: Improper Inventory Management | Route and Swagger inventory review | API inventory documented |
| API10: Unsafe Consumption of APIs | No third-party API consumption identified | Not applicable |

## Overall Assessment

Testing performed against the local SecureBank API did not demonstrate
a confirmed critical authentication or authorization bypass.

Security testing produced several negative-test results and hardening
observations. Findings should be distinguished from tests where no
vulnerability was demonstrated.
