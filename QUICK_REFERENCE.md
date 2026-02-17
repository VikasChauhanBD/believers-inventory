# Quick Reference - Login System Commands

## Starting the Development Environment

### Terminal 1 - Backend (Django)
```bash
cd /home/admin2/believers-inventory/ims-backend
source .venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

### Terminal 2 - Frontend (React + Vite)
```bash
cd /home/admin2/believers-inventory/ims-frontend
npm run dev
```

## Test Credentials

### Regular Employee
```
Email: test@example.com
Password: Test@123456
```

### Admin User
```
Email: admin@example.com
Password: Admin@123456
```

### Other Existing Users
```
- admin@gmail.com (Admin)
- shubham@gmail.com (Admin)
```

## Common Commands

### Backend Management

#### Create a new superuser
```bash
cd ims-backend
python manage.py createsuperuser
```

#### List all employees
```bash
python manage.py shell
>>> from apps.authentication.models import Employee
>>> for emp in Employee.objects.all():
...     print(f"{emp.email} - {emp.role}")
>>> exit()
```

#### Reset user password manually
```bash
python manage.py shell
>>> from apps.authentication.models import Employee
>>> user = Employee.objects.get(email='test@example.com')
>>> user.set_password('NewPassword123')
>>> user.save()
>>> exit()
```

#### Access Django admin
- URL: http://localhost:8000/admin
- Use superuser credentials created above

### Frontend Commands

#### Install dependencies
```bash
npm install
```

#### Build for production
```bash
npm run build
```

#### Preview production build
```bash
npm run preview
```

#### Run linter
```bash
npm run lint
```

## API Testing with curl

### Login
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"Test@123456"}'
```

### Get Current User (requires token)
```bash
curl -X GET http://localhost:8000/api/auth/me/ \
  -H "Authorization: Bearer <your_access_token>"
```

### Signup
```bash
curl -X POST http://localhost:8000/api/auth/signup/ \
  -H "Content-Type: application/json" \
  -d '{
    "email":"newuser@example.com",
    "password":"SecurePass123",
    "password_confirm":"SecurePass123",
    "first_name":"John",
    "last_name":"Doe",
    "department":"IT",
    "phone_number":"+1234567890"
  }'
```

### Refresh Token
```bash
curl -X POST http://localhost:8000/api/auth/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh":"<your_refresh_token>"}'
```

### Request Password Reset
```bash
curl -X POST http://localhost:8000/api/auth/password/reset/ \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com"}'
```

## File Locations

### Backend
- Main settings: `/home/admin2/believers-inventory/ims-backend/config/settings.py`
- Auth models: `/home/admin2/believers-inventory/ims-backend/apps/authentication/models.py`
- Auth views: `/home/admin2/believers-inventory/ims-backend/apps/authentication/views.py`
- Database: `/home/admin2/believers-inventory/ims-backend/db.sqlite3`
- Environment: `/home/admin2/believers-inventory/ims-backend/.env`

### Frontend
- Main app: `/home/admin2/believers-inventory/ims-frontend/src/App.jsx`
- Auth context: `/home/admin2/believers-inventory/ims-frontend/src/AuthContext/AuthContext.jsx`
- API service: `/home/admin2/believers-inventory/ims-frontend/src/services/api.js`
- Login page: `/home/admin2/believers-inventory/ims-frontend/src/pages/loginPage/Login.jsx`
- Environment: `/home/admin2/believers-inventory/ims-frontend/.env.local`

## Troubleshooting Checklist

- [ ] Backend running on http://localhost:8000
- [ ] Frontend running on http://localhost:5173
- [ ] .env file in backend folder configured
- [ ] .env.local file in frontend folder configured
- [ ] Test user exists (test@example.com)
- [ ] Database migrations applied
- [ ] CORS_ALLOWED_ORIGINS includes frontend URL
- [ ] No port conflicts (8000 and 5173)

## Important Endpoints Status

| Endpoint | Port | Status |
|----------|------|--------|
| Backend API | 8000 | Running |
| Frontend App | 5173 | Running |
| Django Admin | 8000/admin | Available |

---

**Last Updated**: February 17, 2026
**Verified**: ✓ Login working, ✓ JWT tokens functional, ✓ Frontend-Backend connected
