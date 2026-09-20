#!/bin/bash

BASE="http://127.0.0.1:5000"

echo "======================================"
echo "   SECUREBANK VAPT LIVE DEMO"
echo "======================================"

echo
echo "[1] LOGIN - JWT AUTHENTICATION"
curl -s -X POST "$BASE/api/auth/login" \
-H "Content-Type: application/json" \
-d '{"username":"bob","password":"Bob@12345"}'

echo
echo
echo "[2] NO TOKEN - EXPECTED 401"
curl -s -o /dev/null -w "HTTP STATUS: %{http_code}\n" \
"$BASE/api/accounts/my-account"

echo
echo "[3] LOGIN AGAIN TO GET TOKEN"
BOB_TOKEN=$(curl -s -X POST "$BASE/api/auth/login" \
-H "Content-Type: application/json" \
-d '{"username":"bob","password":"Bob@12345"}' \
| python -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

echo "JWT TOKEN RECEIVED"

echo
echo "[4] VALID JWT - EXPECTED 200"
curl -s -o /dev/null -w "HTTP STATUS: %{http_code}\n" \
"$BASE/api/accounts/my-account" \
-H "Authorization: Bearer $BOB_TOKEN"

echo
echo "[5] NORMAL USER -> ADMIN ENDPOINT - EXPECTED 403"
curl -s -o /dev/null -w "HTTP STATUS: %{http_code}\n" \
"$BASE/api/accounts/admin-test" \
-H "Authorization: Bearer $BOB_TOKEN"

echo
echo "[6] BOLA/IDOR TEST - BOB ACCESSING ALICE ACCOUNT"
curl -s -w "\nHTTP STATUS: %{http_code}\n" \
"$BASE/api/accounts/1" \
-H "Authorization: Bearer $BOB_TOKEN"

echo
echo "[7] SECURITY HEADERS"
curl -s -I "$BASE/api/accounts/my-account" \
-H "Authorization: Bearer $BOB_TOKEN" \
| grep -E "X-Content-Type-Options|X-Frame-Options|Content-Security-Policy"

echo
echo "======================================"
echo "          DEMO COMPLETED"
echo "======================================"
