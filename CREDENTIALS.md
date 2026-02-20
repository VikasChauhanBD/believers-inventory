# System Credentials & Quick Reference

## Admin Account
| Field | Value |
|-------|-------|
| Email | admin@believersdestination.com |
| Password | AdminPassword123! |
| Role | Admin (Superuser) |
| Access | Can access /admin panel and full dashboard |

---

## Test Employees

### 1. Shubh Sharma
| Field | Value |
|-------|-------|
| Email | shubh@believersdestination.com |
| Password | TestPassword123! |
| Department | IT |
| Employee ID | EMP001 |
| Role | Employee |
| Phone | +91-9876543210 |

### 2. Vikas Chauhan
| Field | Value |
|-------|-------|
| Email | vikas@believersdestination.com |
| Password | TestPassword123! |
| Department | Operations |
| Employee ID | EMP002 |
| Role | Employee |
| Phone | +91-9876543211 |

### 3. Vamika Singh
| Field | Value |
|-------|-------|
| Email | vamika@believersdestination.com |
| Password | TestPassword123! |
| Department | HR |
| Employee ID | EMP003 |
| Role | Employee |
| Phone | +91-9876543212 |

### 4. Arun Kumar
| Field | Value |
|-------|-------|
| Email | arun@believersdestination.com |
| Password | TestPassword123! |
| Department | Finance |
| Employee ID | EMP004 |
| Role | Employee |
| Phone | +91-9876543213 |

### 5. Aman Verma
| Field | Value |
|-------|-------|
| Email | aman@believersdestination.com |
| Password | TestPassword123! |
| Department | Marketing |
| Employee ID | EMP005 |
| Role | Employee |
| Phone | +91-9876543214 |

---

## System URLs

| Service | URL | Purpose |
|---------|-----|---------|
| Backend API | http://localhost:8000 | Django REST API |
| Django Admin | http://localhost:8000/admin | Database management |
| Frontend | http://localhost:5173 | React application |
| API Docs | http://localhost:8000/api | API endpoints |

---

## Database Location

| Type | Location |
|------|----------|
| SQLite (Development) | `/home/admin2/believers-inventory/ims-backend/db.sqlite3` |
| Media Files | `/home/admin2/believers-inventory/ims-backend/media/` |
| Static Files | `/home/admin2/believers-inventory/ims-backend/staticfiles/` |

---

## Key Directories

```
believers-inventory/
├── ims-backend/                   # Django backend
│   ├── apps/
│   │   ├── authentication/        # User management
│   │   └── inventory/             # Device management
│   ├── config/                    # Django settings
│   ├── manage.py
│   ├── db.sqlite3                 # Database
│   └── requirements.txt
│
├── ims-frontend/                  # React frontend
│   ├── src/
│   │   ├── pages/
│   │   └── components/
│   ├── package.json
│   └── vite.config.js
│
├── PROJECT_DOCUMENTATION.md       # Complete guide
├── API_REFERENCE.md              # API documentation
├── QUICK_START.md                # Setup instructions
└── CHANGES.md                    # Implementation summary
```

---

## Quick Commands

### Start Backend
```bash
cd ims-backend
source .venv/bin/activate
python manage.py runserver
```

### Start Frontend
```bash
cd ims-frontend
npm run dev
```

### Create Test Employees
```bash
python manage.py create_test_employees
```

### Run Migrations
```bash
python manage.py migrate
```

### Make New Migrations
```bash
python manage.py makemigrations
```

### Access Django Admin
```
http://localhost:8000/admin/
Email: admin@believersdestination.com
Password: AdminPassword123!
```

---

## Testing Workflow

### 1. **As Admin** (Full Access)
- Login: http://localhost:5173/login
- Email: `admin@believersdestination.com`
- Password: `AdminPassword123!`
- Dashboard: `/admin`

### 2. **As Employee** (Limited Access)
- Login: http://localhost:5173/login
- Email: `shubh@believersdestination.com` (or any test employee)
- Password: `TestPassword123!`
- Dashboard: `/` (personal devices and tickets)

---

## Key Features

### Device Management
- ✅ Add, edit, delete devices
- ✅ Track device status
- ✅ View device condition
- ✅ Search and filter

### Assignment Workflow
1. **Create Assignment** (Admin)
2. **Approve with Image** (Admin) - Device handover photo
3. **Active Assignment** (Device in use)
4. **Request Return** (Employee)
5. **Approve Return with Image** (Admin) - Device return photo
6. **Completed**

### Ticket System
- ✅ Create support tickets
- ✅ Track ticket status
- ✅ Assign to staff
- ✅ Add resolution notes

---

## API Authentication

All API calls require JWT token:

```
Header: Authorization: Bearer <access_token>
```

### Getting Tokens

**Login:**
```
POST /api/auth/login/
{
  "email": "admin@believersdestination.com",
  "password": "AdminPassword123!"
}
```

**Response:**
```json
{
  "message": "Login successful",
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLC...",
    "refresh": "eyJ0eXAiOiJKV1QiLC..."
  }
}
```

---

## Common Endpoints

| Endpoint | Method | Auth | Purpose |
|----------|--------|------|---------|
| `/api/auth/login/` | POST | No | Login |
| `/api/auth/me/` | GET | Yes | Get profile |
| `/api/inventory/devices/` | GET | Yes | List devices |
| `/api/inventory/assignments/` | GET | Yes | List assignments |
| `/api/inventory/assignments/{id}/approve_assignment/` | POST | Yes | Approve assignment |
| `/api/inventory/assignments/{id}/request_return/` | POST | Yes | Request return |
| `/api/inventory/assignments/{id}/approve_return/` | POST | Yes | Approve return |
| `/api/inventory/tickets/` | GET | Yes | List tickets |

---

## System Architecture

```
┌─────────────────────┐
│   React Frontend    │ (http://localhost:5173)
└──────────┬──────────┘
           │ HTTP/JSON
           ↓
┌─────────────────────┐
│  Django REST API    │ (http://localhost:8000)
└──────────┬──────────┘
           │ ORM
           ↓
┌─────────────────────┐
│  SQLite Database    │ (db.sqlite3)
└─────────────────────┘
```

---

## Environment Variables

### Backend (.env)
```
SECRET_KEY=django-insecure-change-this-in-production-believers-inventory
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173
FRONTEND_URL=http://localhost:5173
DATABASE_URL=  # Empty for SQLite
```

### Frontend (.env.local)
```
VITE_API_URL=http://localhost:8000/api
```

---

## Troubleshooting

### "Connection to server failed"
- Check if backend is running
- Verify `.env.local` has correct `VITE_API_URL`

### "401 Unauthorized"
- Token may have expired
- Login again to get new tokens

### "Device not found"
- Verify device ID is correct
- Check device is not deleted

### "Permission denied"
- Check user role (admin/manager for approval)
- Verify authentication token

---

## Documentation Files

| File | Purpose |
|------|---------|
| `PROJECT_DOCUMENTATION.md` | Complete project guide |
| `API_REFERENCE.md` | API endpoint documentation |
| `QUICK_START.md` | 5-minute setup guide |
| `CHANGES.md` | Implementation summary |
| `CREDENTIALS.md` | This file |

---

## Support Information

**Backend Server**
- Location: `/home/admin2/believers-inventory/ims-backend`
- Port: 8000
- Database: SQLite

**Frontend Application**
- Location: `/home/admin2/believers-inventory/ims-frontend`
- Port: 5173
- Build Tool: Vite

**Documentation**
- Comprehensive: `PROJECT_DOCUMENTATION.md`
- Quick Setup: `QUICK_START.md`
- API Details: `API_REFERENCE.md`

---

## Version Information

- **Django**: 5.2.10
- **React**: 18+
- **Python**: 3.12+
- **Node.js**: 18+

---

## Deployment Checklist

- [ ] Update `SECRET_KEY` in `.env`
- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Update `CORS_ALLOWED_ORIGINS`
- [ ] Set `DATABASE_URL` for PostgreSQL
- [ ] Configure email service
- [ ] Generate SSL certificates
- [ ] Set up HTTPS
- [ ] Configure static files serving
- [ ] Set up media files storage

---

**Last Updated**: February 19, 2026  
**Ready for Testing**: ✅ YES  
**Ready for Production**: ⚠️ Requires configuration
