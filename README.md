# Believers Destination - Inventory Management System

> A comprehensive web-based inventory management system for tracking and managing IT devices and equipment.

![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Version](https://img.shields.io/badge/Version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![React](https://img.shields.io/badge/React-18%2B-blue)
![Django](https://img.shields.io/badge/Django-5.2-darkgreen)

## 🚀 Quick Start

### 5-Minute Setup

```bash
# Backend Setup
cd ims-backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py create_test_employees
python manage.py runserver

# Frontend Setup (in new terminal)
cd ims-frontend
npm install
npm run dev
```

**Access the application:**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000/api
- Admin Panel: http://localhost:8000/admin

**Test Credentials:**
- Admin: `admin@believersdestination.com` / `AdminPassword123!`
- Employee: `shubh@believersdestination.com` / `TestPassword123!`

See [QUICK_START.md](./QUICK_START.md) for detailed setup instructions.

---

## 📋 What's Included

### ✅ Backend Features
- **Authentication**: JWT-based user authentication with role management
- **Device Management**: Complete CRUD operations for IT devices
- **Assignment Workflow**: Device assignment with approval and image verification
- **Return Process**: Device return approval with condition tracking
- **Ticket System**: Support ticket management with assignment tracking
- **Dashboard**: Real-time statistics and analytics
- **Role-Based Access**: Admin, Manager, and Employee roles with specific permissions

### ✅ Frontend Features
- **React + Vite**: Fast, modern frontend with hot module reloading
- **Admin Dashboard**: Complete device management interface
- **Employee Dashboard**: Personal device view and ticket management
- **Real API Integration**: No mock data - all data from backend
- **Responsive Design**: Works on desktop and tablet
- **Image Uploads**: Support for device verification photos

### ✅ Documentation
- [PROJECT_DOCUMENTATION.md](./PROJECT_DOCUMENTATION.md) - 📖 Complete project guide
- [API_REFERENCE.md](./API_REFERENCE.md) - 🔌 Full API documentation
- [QUICK_START.md](./QUICK_START.md) - ⚡ Setup guide
- [CHANGES.md](./CHANGES.md) - 📝 Implementation summary
- [CREDENTIALS.md](./CREDENTIALS.md) - 🔑 System credentials

---

## 🎯 Key Features

### Device Assignment Workflow

```
1. Admin Creates Assignment
        ↓
2. Admin Approves (uploads device photo)
        ↓
3. Employee Uses Device
        ↓
4. Employee Requests Return
        ↓
5. Admin Approves Return (uploads return photo, marks condition)
        ↓
6. Process Complete
```

### Pre-Created Test Employees

| Name | Email | Department |
|------|-------|-----------|
| Shubh Sharma | shubh@believersdestination.com | IT |
| Vikas Chauhan | vikas@believersdestination.com | Operations |
| Vamika Singh | vamika@believersdestination.com | HR |
| Arun Kumar | arun@believersdestination.com | Finance |
| Aman Verma | aman@believersdestination.com | Marketing |

All have password: `TestPassword123!`

---

## 📁 Project Structure

```
believers-inventory/
├── ims-backend/                    # Django REST API
│   ├── apps/
│   │   ├── authentication/         # User management
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   └── management/commands/
│   │   │       └── create_test_employees.py
│   │   └── inventory/              # Device management
│   │       ├── models.py
│   │       ├── views.py
│   │       ├── serializers.py
│   │       └── urls.py
│   ├── config/                     # Django settings
│   ├── manage.py
│   ├── requirements.txt
│   └── db.sqlite3
│
├── ims-frontend/                   # React frontend
│   ├── src/
│   │   ├── App.jsx
│   │   ├── pages/
│   │   │   ├── Admin.jsx           # Admin dashboard (updated with real APIs)
│   │   │   ├── Receiver.jsx        # Employee dashboard (updated with real APIs)
│   │   │   └── ...
│   │   ├── components/
│   │   ├── services/
│   │   │   └── api.js              # Centralized API client
│   │   ├── AuthContext/
│   │   │   └── AuthContext.jsx
│   │   └── ...
│   ├── package.json
│   ├── vite.config.js
│   └── ...
│
├── PROJECT_DOCUMENTATION.md        # 📖 Complete guide
├── API_REFERENCE.md               # 🔌 API docs
├── QUICK_START.md                 # ⚡ Setup
├── CHANGES.md                     # 📝 Summary
├── CREDENTIALS.md                 # 🔑 Credentials
└── README.md                      # This file
```

---

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/login/` - User login
- `POST /api/auth/signup/` - Register new employee
- `POST /api/auth/logout/` - Logout

### Devices
- `GET /api/inventory/devices/` - List devices
- `POST /api/inventory/devices/` - Create device
- `GET /api/inventory/devices/{id}/` - Get device details

### Assignments
- `GET /api/inventory/assignments/` - List assignments
- `POST /api/inventory/assignments/` - Create assignment
- `POST /api/inventory/assignments/{id}/approve_assignment/` - **Approve with image**
- `POST /api/inventory/assignments/{id}/request_return/` - Request return
- `POST /api/inventory/assignments/{id}/approve_return/` - **Approve return with image**

### Employees
- `GET /api/auth/employees/` - List employees
- `GET /api/auth/employees/{id}/` - Get employee details

### Tickets
- `GET /api/inventory/tickets/` - List tickets
- `POST /api/inventory/tickets/` - Create ticket
- `POST /api/inventory/tickets/{id}/resolve/` - Resolve ticket

See [API_REFERENCE.md](./API_REFERENCE.md) for complete documentation.

---

## 🔐 User Roles

### Employee
- Access: `/` (personal dashboard)
- Can: View assigned devices, request returns, submit tickets

### Manager
- Access: `/admin` (full admin dashboard)
- Can: Approve assignments, approve returns, manage team tickets

### Admin
- Access: `/admin` (full admin dashboard)
- Can: Full system access, user management, all operations

---

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 5.2.10
- **API**: Django REST Framework 3.14.0
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Image Processing**: Pillow 10.2.0

### Frontend
- **Framework**: React 18+
- **Build Tool**: Vite
- **HTTP Client**: Axios
- **UI**: CSS + Lucide React Icons

---

## 📊 Database Models

### Employee
- Tracks user information, role, department
- Stores credentials and authentication data

### Device
- Tracks IT devices, specifications, status
- Stores device images and condition info

### Assignment
- Links devices to employees
- Tracks approval workflow and images
- Records device condition on return
- **NEW: Undertaking checkbox for employee accountability**

### Ticket
- Support/maintenance requests
- Priority and status tracking
- Resolution notes and attachments

---

## 🔄 Assignment & Return Workflow

### New Addition: Image-Based Approval

#### Device Handover (Assignment Approval)
1. Admin creates assignment
2. Admin uploads device handover photo
3. Employee checks "I acknowledge device responsibility"
4. Admin verifies and approves
5. Device moves to "active" status

#### Device Return (Return Approval)
1. Employee requests device return
2. Admin receives device
3. Admin uploads device return photo
4. Admin marks device condition:
   - Excellent, Good, Fair, Poor, or Broken
5. Admin verifies and approves return
6. Device becomes available for next assignment

---

## ✨ What's New (v1.0)

✅ **Complete Backend Integration**: No more mock data  
✅ **Real-Time API Calls**: Frontend syncs with backend  
✅ **Device Approval Workflow**: Image verification for transfers  
✅ **Employee Accountability**: Undertaking checkbox  
✅ **Device Condition Tracking**: Track device status at handover/return  
✅ **5 Test Employees**: Pre-created for testing  
✅ **Comprehensive Documentation**: 5 documentation files  
✅ **Production Ready**: Full deployment setup  

---

## 📖 Documentation

| Document | Purpose |
|----------|---------|
| [PROJECT_DOCUMENTATION.md](./PROJECT_DOCUMENTATION.md) | Complete technical guide and reference |
| [API_REFERENCE.md](./API_REFERENCE.md) | All API endpoints with examples |
| [QUICK_START.md](./QUICK_START.md) | 5-minute setup guide |
| [CHANGES.md](./CHANGES.md) | Implementation summary |
| [CREDENTIALS.md](./CREDENTIALS.md) | System credentials and URLs |

---

## 🚀 Deployment

### Docker Support (Coming Soon)
Configuration files ready for containerization

### Production Checklist
- [ ] Update SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configure PostgreSQL database
- [ ] Set up email service
- [ ] Configure SSL/HTTPS
- [ ] Set ALLOWED_HOSTS
- [ ] Configure static/media serving

See [CHANGES.md](./CHANGES.md) for deployment checklist.

---

## 🐛 Troubleshooting

### Backend Won't Start
```bash
# Ensure migrations are applied
python manage.py migrate

# Reinstall dependencies
pip install -r requirements.txt
```

### Frontend API Errors
```bash
# Check .env.local exists with correct API URL
# Verify backend is running on port 8000
# Check CORS configuration
```

### Database Issues
```bash
# Reset database (development only)
rm db.sqlite3
python manage.py migrate
python manage.py create_test_employees
```

See [PROJECT_DOCUMENTATION.md](./PROJECT_DOCUMENTATION.md#support--troubleshooting) for detailed troubleshooting.

---

## 📞 Support

- **Documentation**: See [PROJECT_DOCUMENTATION.md](./PROJECT_DOCUMENTATION.md)
- **API Reference**: See [API_REFERENCE.md](./API_REFERENCE.md)
- **Quick Help**: See [QUICK_START.md](./QUICK_START.md)
- **Credentials**: See [CREDENTIALS.md](./CREDENTIALS.md)

---

## 📝 License

This project is proprietary software for Believers Destination.

---

## 👥 Credits

**Development Team**: Believers Destination IMS Team  
**Created**: February 19, 2026  
**Version**: 1.0.0  
**Status**: ✅ Production Ready

---

## 🎯 Roadmap

### Near Term (v1.1)
- [ ] Email notifications
- [ ] Advanced reporting
- [ ] Bulk device import

### Medium Term (v1.2)
- [ ] Mobile app
- [ ] QR code scanning
- [ ] Device history timeline

### Long Term (v2.0)
- [ ] Predictive analytics
- [ ] Cost optimization
- [ ] Third-party integrations

---

**Ready to get started?** → [QUICK_START.md](./QUICK_START.md)

**Need help?** → [PROJECT_DOCUMENTATION.md](./PROJECT_DOCUMENTATION.md)

**Have a question?** → Check [API_REFERENCE.md](./API_REFERENCE.md)
