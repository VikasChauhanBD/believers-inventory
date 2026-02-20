# Quick Start Guide - IMS Backend

## Prerequisites
- Python 3.12+
- pip

## 5-Minute Setup

### 1. Install Dependencies
```bash
cd ims-backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run Migrations
```bash
python3 manage.py migrate
```

### 3. Create Test Data
```bash
python3 manage.py create_test_employees
```

### 4. Start Server
```bash
python3 manage.py runserver
```

Server runs at: `http://localhost:8000`

## Accounts Created

### Admin Account
- Email: `admin@believersdestination.com`
- Password: `AdminPassword123!`

### Test Employees (5)
- `shubh@believersdestination.com` - TestPassword123!
- `vikas@believersdestination.com` - TestPassword123!
- `vamika@believersdestination.com` - TestPassword123!
- `arun@believersdestination.com` - TestPassword123!
- `aman@believersdestination.com` - TestPassword123!

## Access Admin Panel
Go to: `http://localhost:8000/admin/`
Login with admin account

## API Documentation
See `PROJECT_DOCUMENTATION.md` for complete API reference
