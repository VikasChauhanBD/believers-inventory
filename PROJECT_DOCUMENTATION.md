# Believers Destination Inventory Management System (IMS) Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Technology Stack](#technology-stack)
4. [Features](#features)
5. [User Roles and Access Control](#user-roles-and-access-control)
6. [Database Models](#database-models)
7. [API Endpoints](#api-endpoints)
8. [Frontend Structure](#frontend-structure)
9. [Device Assignment & Return Workflow](#device-assignment--return-workflow)
10. [Setup and Installation](#setup-and-installation)
11. [Running the Application](#running-the-application)
12. [Test Employees](#test-employees)
13. [Key File Locations](#key-file-locations)

---

## Project Overview

The Believers Destination Inventory Management System (IMS) is a comprehensive web application designed to manage, track, and control IT devices and equipment within the organization. The system facilitates:

- **Device Management**: Track all IT devices including laptops, desktops, phones, tablets, and accessories
- **Employee Management**: Manage employee information and device assignments
- **Device Assignment & Return**: Streamlined workflow for assigning devices to employees with approval and image verification
- **Device Condition Tracking**: Track device condition during assignment and return
- **Ticket Management**: Support for device-related requests and issues
- **Dashboard & Analytics**: Real-time statistics and overview of inventory

---

## Architecture

### Three-Tier Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Frontend (React)                          │
│              ims-frontend/ - React + Vite                       │
└─────────────────────────────────────────────────────────────────┘
                              ↓ (HTTP/JSON)
┌─────────────────────────────────────────────────────────────────┐
│                      Backend (Django REST)                       │
│              Django 5.2 + Django REST Framework                 │
│         - Authentication & Authorization                         │
│         - Device Management APIs                                │
│         - Assignment Workflow APIs                              │
│         - Ticket Management APIs                                │
└─────────────────────────────────────────────────────────────────┘
                              ↓ (ORM)
┌─────────────────────────────────────────────────────────────────┐
│                      Database (SQLite/PostgreSQL)               │
│         - Employees (Users)                                      │
│         - Devices                                               │
│         - Assignments                                           │
│         - Tickets                                               │
│         - Approval Records (Images)                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Technology Stack

### Backend
- **Framework**: Django 5.2.10
- **API**: Django REST Framework 3.14.0
- **Authentication**: JWT (djangorestframework-simplejwt 5.3.1)
- **Database**: SQLite (development) / PostgreSQL (production)
- **Image Handling**: Pillow 10.2.0
- **CORS**: django-cors-headers 4.3.1
- **Other**: python-decouple, dj-database-url, gunicorn

### Frontend
- **Framework**: React 18+
- **Build Tool**: Vite
- **HTTP Client**: Axios
- **UI Components**: Lucide React (Icons)
- **Styling**: CSS
- **State Management**: React Hooks (useState, useContext, useEffect)

---

## Features

### 1. **User Authentication & Authorization**
- Employee signup and login with JWT tokens
- Role-based access control (Employee, Manager, Admin)
- Password reset functionality
- Secure token refresh mechanism

### 2. **Device Management**
- Add, edit, delete, and view devices
- Track device specifications (brand, model, serial number, etc.)
- Device status tracking (Available, Assigned, In Maintenance, Retired)
- Condition tracking (New, Excellent, Good, Fair, Poor)
- Device categorization by type (Laptop, Desktop, Phone, Tablet, etc.)
- Purchase and warranty information

### 3. **Employee Management**
- Manage employee profiles
- Assign roles and departments
- Track assigned devices
- Employee status tracking

### 4. **Device Assignment & Return Workflow**

#### Assignment Process:
1. **Admin Creates Assignment**
   - Select device and employee
   - Set expected return date
   - Add assignment notes

2. **Pending Approval**
   - Assignment enters "pending_approval" status
   - Admin reviews and uploads device photo
   - Employee checks "undertaking" checkbox (acknowledging responsibility)
   - Admin clicks "Approve" button

3. **Active Assignment**
   - Status changes to "active"
   - Device is now assigned to employee
   - Device status becomes "assigned"

#### Return Process:
1. **Employee Requests Return**
   - Employee clicks "Request Return"
   - Provides return notes (device condition, damage, etc.)
   - Assignment status becomes "pending_return"

2. **Admin Approves Return**
   - Admin reviews return request
   - Takes photo of device condition
   - Selects device condition on return
   - Marks if device is broken/damaged
   - Clicks approve

3. **Device Returned**
   - Status changes to "returned"
   - Device status becomes "available" again (if not damaged/broken)
   - Return date and approval recorded in system

### 5. **Ticket Management**
- Create support tickets for devices
- Track ticket status (Pending, In Progress, Resolved, Closed)
- Assign tickets to support staff
- Resolve tickets with notes
- Multiple ticket types (Repair, Replacement, Issue Report, Return Request)

### 6. **Dashboard & Analytics**
- Overview of device inventory
- Assignment statistics
- Employee tracking
- Ticket pipeline visualization
- Device type breakdown

---

## User Roles and Access Control

### 1. **Employee** (role: 'employee')
- **Access**: /
- **Permissions**:
  - View assigned devices only
  - View their own tickets
  - Request device return
  - Submit support tickets
  - View own profile

### 2. **Manager** (role: 'manager')
- **Access**: /admin
- **Permissions**:
  - View all devices
  - View all employees
  - Create and manage assignments
  - Approve device assignments
  - Approve device returns
  - View all tickets
  - Manage tickets assigned to team

### 3. **Admin** (role: 'admin')
- **Access**: /admin
- **Permissions**:
  - Full access to all features
  - User management (not through UI yet)
  - System configuration
  - All manager permissions
  - Advanced analytics and reporting

### 4. **Superadmin** (role: 'admin', is_superuser: True)
- **Access**: Django admin panel (/admin)
- **Permissions**:
  - Access Django admin
  - Database management
  - User role assignment
  - System-level configurations

---

## Database Models

### Employee Model
```python
class Employee(AbstractBaseUser, PermissionsMixin):
    id: UUID
    email: String (unique)
    first_name: String
    last_name: String
    employee_id: String (auto-generated: EMP001, EMP002, ...)
    role: Choice (admin, manager, employee)
    department: Choice (IT, HR, Finance, Operations, Sales, Marketing)
    phone_number: String
    is_active: Boolean
    is_staff: Boolean
    date_joined: DateTime
    last_login: DateTime
    profile_picture: Image
```

### Device Model
```python
class Device:
    id: UUID
    device_id: String (unique)
    name: String
    device_type: Choice (laptop, desktop, monitor, phone, tablet, etc.)
    brand: String
    model: String
    serial_number: String (unique)
    status: Choice (available, assigned, maintenance, retired)
    condition: Choice (new, excellent, good, fair, poor)
    specifications: JSON
    purchase_date: Date
    purchase_price: Decimal
    warranty_expiry: Date
    location: String
    notes: Text
    image: Image
    created_at: DateTime
    updated_at: DateTime
    created_by: ForeignKey(Employee)
```

### Assignment Model
```python
class Assignment:
    id: UUID
    device: ForeignKey(Device)
    employee: ForeignKey(Employee)
    assigned_date: DateTime
    return_date: DateTime (nullable)
    expected_return_date: Date (nullable)
    status: Choice (
        pending_approval, 
        active, 
        pending_return, 
        returned, 
        lost, 
        damaged
    )
    
    # Assignment Approval Fields
    assignment_image: Image
    assignment_approved_by: ForeignKey(Employee)
    assignment_approved_date: DateTime
    assignment_undertaking: Boolean (employee responsibility acknowledgment)
    
    # Return Approval Fields
    return_image: Image
    return_approved_by: ForeignKey(Employee)
    return_approved_date: DateTime
    device_condition_on_return: Choice (new, excellent, good, fair, poor)
    device_broken: Boolean
    
    # Notes
    assignment_notes: Text
    return_notes: Text
    
    # Created By
    assigned_by: ForeignKey(Employee)
```

### TicketRequest Model
```python
class TicketRequest:
    id: UUID
    ticket_number: String (unique, auto-generated: TKT001, TKT002, ...)
    requested_by: ForeignKey(Employee)
    ticket_type: Choice (repair, replacement, new_device, issue, return, other)
    priority: Choice (low, medium, high, urgent)
    status: Choice (pending, in_progress, resolved, rejected, closed)
    device: ForeignKey(Device, nullable)
    subject: String
    description: Text
    assigned_to: ForeignKey(Employee, nullable)
    resolution_notes: Text
    resolved_at: DateTime (nullable)
    attachment: File (nullable)
    created_at: DateTime
    updated_at: DateTime
```

---

## API Endpoints

### Authentication Endpoints (`/api/auth/`)

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| POST | `/signup/` | Register new employee | No |
| POST | `/login/` | Login (returns JWT tokens) | No |
| POST | `/logout/` | Logout (blacklist token) | Yes |
| POST | `/token/refresh/` | Refresh access token | No |
| GET | `/me/` | Get current employee profile | Yes |
| PATCH | `/me/` | Update current employee profile | Yes |
| POST | `/password/change/` | Change password | Yes |
| POST | `/password/reset/` | Request password reset | No |
| POST | `/password/reset/confirm/` | Confirm password reset | No |
| GET | `/password/reset/verify/` | Verify reset token | No |
| GET | `/employees/` | List all employees | Yes |
| GET | `/employees/<id>/` | Get employee details | Yes |

### Device Endpoints (`/api/inventory/devices/`)

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| GET | `/` | List all devices (filterable) | Yes |
| POST | `/` | Create new device | Yes (Admin/Manager) |
| GET | `/<id>/` | Get device details | Yes |
| PATCH | `/<id>/` | Update device | Yes (Admin/Manager) |
| DELETE | `/<id>/` | Delete device | Yes (Admin/Manager) |
| GET | `/available/` | Get available devices | Yes |
| POST | `/<id>/mark_maintenance/` | Mark device as under maintenance | Yes (Admin/Manager) |
| POST | `/<id>/mark_available/` | Mark device as available | Yes (Admin/Manager) |

### Assignment Endpoints (`/api/inventory/assignments/`)

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| GET | `/` | List assignments | Yes |
| POST | `/` | Create new assignment | Yes (Admin/Manager) |
| GET | `/<id>/` | Get assignment details | Yes |
| PATCH | `/<id>/` | Update assignment | Yes (Admin/Manager) |
| DELETE | `/<id>/` | Delete assignment | Yes (Admin/Manager) |
| POST | `/<id>/approve_assignment/` | Admin approves assignment with image | Yes (Admin/Manager) |
| POST | `/<id>/request_return/` | Employee requests device return | Yes |
| POST | `/<id>/approve_return/` | Admin approves return with image | Yes (Admin/Manager) |
| POST | `/<id>/return_device/` | Mark device as returned (deprecated) | Yes |
| GET | `/my_assignments/` | Get current user's active assignments | Yes |

**Request/Response Examples:**

**Approve Assignment:**
```
POST /api/inventory/assignments/{id}/approve_assignment/
Content-Type: multipart/form-data

Fields:
- assignment_image (File) - Photo of device handed to employee
- assignment_undertaking (Boolean) - Employee acknowledgment checkbox
```

**Request Return:**
```
POST /api/inventory/assignments/{id}/request_return/
Content-Type: application/json

Body:
{
    "return_notes": "Device in good condition"
}
```

**Approve Return:**
```
POST /api/inventory/assignments/{id}/approve_return/
Content-Type: multipart/form-data

Fields:
- return_image (File) - Photo of device being returned
- device_condition_on_return (String) - new|excellent|good|fair|poor
- device_broken (Boolean) - Whether device is broken
```

### Ticket Endpoints (`/api/inventory/tickets/`)

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| GET | `/` | List tickets (filterable) | Yes |
| POST | `/` | Create new ticket | Yes |
| GET | `/<id>/` | Get ticket details | Yes |
| PATCH | `/<id>/` | Update ticket | Yes |
| DELETE | `/<id>/` | Delete ticket | Yes (Admin/Manager) |
| POST | `/<id>/assign/` | Assign ticket to employee | Yes (Admin/Manager) |
| POST | `/<id>/resolve/` | Resolve ticket | Yes (Admin/Manager) |
| GET | `/my_tickets/` | Get current user's tickets | Yes |

### Dashboard Endpoints (`/api/inventory/dashboard/`)

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| GET | `/stats/` | Get dashboard statistics | Yes |

---

## Frontend Structure

### Directory Structure

```
ims-frontend/
├── src/
│   ├── App.jsx                    # Main app component with routing
│   ├── App.css                    # Global styles
│   ├── main.jsx                   # Vite entry point
│   ├── index.css                  # Global CSS
│   │
│   ├── AuthContext/
│   │   └── AuthContext.jsx        # Authentication context and hooks
│   │
│   ├── components/
│   │   ├── admin/
│   │   │   ├── dashboard/
│   │   │   ├── devices/
│   │   │   ├── employees/
│   │   │   ├── assignments/
│   │   │   └── ticketRequestsView/
│   │   ├── user/
│   │   │   ├── userDevices/
│   │   │   └── userTicket/
│   │   ├── navbar/
│   │   │   └── Navbar.jsx
│   │   └── animatedBackground/
│   │       └── AnimatedBackground.jsx
│   │
│   ├── pages/
│   │   ├── Admin.jsx              # Admin dashboard page (now uses real APIs)
│   │   ├── Receiver.jsx           # Employee dashboard page (now uses real APIs)
│   │   ├── loginPage/
│   │   │   └── Login.jsx
│   │   ├── signupPage/
│   │   │   └── Signup.jsx
│   │   ├── profile/
│   │   │   └── EmployeeProfile.jsx
│   │   ├── forgetpasswordPage/
│   │   │   └── ForgotPassword.jsx
│   │   └── resetPasswordPage/
│   │       └── ResetPassword.jsx
│   │
│   ├── services/
│   │   └── api.js                 # Axios API service with all endpoints
│   │
│   └── assets/
│       ├── data/
│       │   └── mockData.js        # DEPRECATED - No longer used
│       └── images/
│           └── [device images]
│
├── vite.config.js
├── package.json
└── eslint.config.js
```

### Key Components

#### 1. **AuthContext** (`AuthContext.jsx`)
Provides global authentication state:
- `isAuthenticated`: Boolean flag
- `user`: Current user object
- `login()`: Login function
- `logout()`: Logout function
- `loading`: Loading state
- `error`: Error messages

#### 2. **Admin Panel** (`Admin.jsx`)
- Dashboard with statistics
- Device management
- Employee management
- Assignment management
- Ticket management
- **Updated**: Now fetches real data from APIs

#### 3. **Employee Panel** (`Receiver.jsx`)
- View assigned devices
- Request device return
- View personal tickets
- Submit support tickets
- **Updated**: Now fetches real data from APIs

#### 4. **API Service** (`api.js`)
Centralized API client with methods for:
- Authentication
- Device CRUD operations
- Assignment workflow (approve, request return, approve return)
- Ticket management
- Employee listing
- Dashboard statistics

---

## Device Assignment & Return Workflow

### Visual Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│         1. Admin Creates Assignment (pending_approval)          │
│  Device: Laptop A | Employee: John Doe | Expected: 2026-03-01  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│         2. Admin Approves Assignment (active)                   │
│  - Takes photo of device                                        │
│  - John Doe checks: "I acknowledge device responsibility"       │
│  - Admin clicks "Approve Assignment"                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│         3. Device is Given to Employee                          │
│  Status: ACTIVE                                                 │
│  Device status: ASSIGNED                                        │
│  Employee can use device                                        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│         4. Employee Requests Return (pending_return)            │
│  - Employee clicks "Request Return"                             │
│  - Provides return notes: "Device working fine, minor scratch"  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│         5. Admin Approves Return (returned)                     │
│  - Receives device from employee                                │
│  - Takes photo of device condition                              │
│  - Selects condition: "Good"                                    │
│  - Marks: "Device broken? NO"                                   │
│  - Clicks "Approve Return"                                      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│         6. Device Returned                                      │
│  Status: RETURNED                                               │
│  Device status: AVAILABLE (for next assignment)                 │
│  Return documented with images                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Status Flow Diagram

```
    ┌──────────────────┐
    │ pending_approval │ (Admin creates assignment)
    └────────┬─────────┘
             │ (Admin approves with image)
             ↓
    ┌──────────────────┐
    │     active       │ (Device in use by employee)
    └────────┬─────────┘
             │ (Employee requests return)
             ↓
    ┌──────────────────┐
    │  pending_return  │ (Waiting for admin approval)
    └────────┬─────────┘
             │ (Admin approves return with image)
             ↓
    ┌──────────────────┐
    │    returned      │ (Device returned)
    └──────────────────┘
```

---

## Setup and Installation

### Prerequisites
- Python 3.12+
- Node.js 18+ and npm
- Git

### Backend Setup

1. **Clone Repository**
   ```bash
   git clone https://github.com/VikasChauhanBD/believers-inventory.git
   cd believers-inventory/ims-backend
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   - Copy `.env.example` to `.env` (if exists)
   - Edit `.env` with your configuration:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   CORS_ALLOWED_ORIGINS=http://localhost:5173
   FRONTEND_URL=http://localhost:5173
   DATABASE_URL=  # Leave empty for SQLite or add PostgreSQL URL
   ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Create Test Employees**
   ```bash
   python manage.py create_test_employees
   ```

### Frontend Setup

1. **Navigate to Frontend Directory**
   ```bash
   cd ../ims-frontend
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Create Environment File**
   ```bash
   # Create .env.local file
   VITE_API_URL=http://localhost:8000/api
   ```

---

## Running the Application

### Backend

```bash
cd ims-backend
source .venv/bin/activate
python manage.py runserver
```

Backend runs on: `http://localhost:8000`
Admin panel: `http://localhost:8000/admin/`

### Frontend

```bash
cd ims-frontend
npm run dev
```

Frontend runs on: `http://localhost:5173`

### Both Services (in separate terminals)

**Terminal 1:**
```bash
cd ims-backend
source .venv/bin/activate
python manage.py runserver
```

**Terminal 2:**
```bash
cd ims-frontend
npm run dev
```

---

## Test Employees

The following test employees are created by default:

### Regular Employees

| Name | Email | Password | Department | Role |
|------|-------|----------|------------|------|
| Shubh Sharma | shubh@believersdestination.com | TestPassword123! | IT | employee |
| Vikas Chauhan | vikas@believersdestination.com | TestPassword123! | Operations | employee |
| Vamika Singh | vamika@believersdestination.com | TestPassword123! | HR | employee |
| Arun Kumar | arun@believersdestination.com | TestPassword123! | Finance | employee |
| Aman Verma | aman@believersdestination.com | TestPassword123! | Marketing | employee |

### Administrator

| Name | Email | Password | Role |
|------|-------|----------|------|
| Admin User | admin@believersdestination.com | AdminPassword123! | admin |

### Test Workflow

1. **Login as Admin**
   - Go to http://localhost:5173/login
   - Email: `admin@believersdestination.com`
   - Password: `AdminPassword123!`
   - Access: Admin Dashboard at `/admin`

2. **Create Test Device**
   - Click "Devices" tab
   - Click "Add Device"
   - Fill device details (e.g., laptop with model/brand)

3. **Create Assignment**
   - Click "Assignments" tab
   - Click "Create Assignment"
   - Select device and employee
   - Set expected return date

4. **Approve Assignment**
   - Device shows "Pending Approval"
   - Click on assignment
   - Upload device photo
   - Check "I acknowledge..."
   - Click "Approve Assignment"

5. **Request Return (as Employee)**
   - Logout and login as employee (e.g., shubh@believersdestination.com)
   - Go to Employee Dashboard at `/`
   - Click device
   - Click "Request Return"

6. **Approve Return (as Admin)**
   - Login as admin
   - Go to Assignments
   - Find assignment with "Pending Return" status
   - Upload return photo
   - Select device condition
   - Mark if broken
   - Click "Approve Return"

---

## Key File Locations

### Backend
- **Models**: `apps/authentication/models.py`, `apps/inventory/models.py`
- **Views**: `apps/authentication/views.py`, `apps/inventory/views.py`
- **Serializers**: `apps/authentication/serializers.py`, `apps/inventory/serializers.py`
- **URLs**: `apps/authentication/urls.py`, `apps/inventory/urls.py`
- **Settings**: `config/settings.py`

### Frontend
- **Main App**: `src/App.jsx`
- **Auth Context**: `src/AuthContext/AuthContext.jsx`
- **API Service**: `src/services/api.js`
- **Admin Page**: `src/pages/Admin.jsx`
- **Employee Page**: `src/pages/Receiver.jsx`
- **Profile Page**: `src/pages/profile/EmployeeProfile.jsx`

### Configuration
- **Backend Config**: `ims-backend/.env`
- **Frontend Config**: `ims-frontend/.env.local`
- **Backend Requirements**: `ims-backend/requirements.txt`
- **Frontend Dependencies**: `ims-frontend/package.json`

---

## API Authentication

All authenticated endpoints require JWT token in Authorization header:

```
Authorization: Bearer <access_token>
```

### Token Refresh
When access token expires (default 1 hour):

```
POST /api/auth/token/refresh/
Content-Type: application/json

Body:
{
    "refresh": "<refresh_token>"
}

Response:
{
    "access": "<new_access_token>"
}
```

---

## Error Handling

### Common HTTP Status Codes

| Status | Meaning |
|--------|---------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 400 | Bad Request - Invalid data |
| 401 | Unauthorized - Authentication required |
| 403 | Forbidden - Permission denied |
| 404 | Not Found - Resource doesn't exist |
| 500 | Internal Server Error |

### Error Response Format

```json
{
    "error": "Error message",
    "detail": "Detailed error explanation",
    "field_name": ["Field-specific error"]
}
```

---

## Security Considerations

1. **HTTPS**: Use in production
2. **CORS**: Configured to allow frontend origin
3. **JWT**: Tokens have expiration and refresh mechanism
4. **CSRF**: Enabled for POST/PUT/DELETE requests
5. **Role-Based Access**: Enforced at API level
6. **Image Upload**: Validate file types and size

---

## Future Enhancements

- [ ] Email notifications for assignments/returns
- [ ] Barcode scanning for devices
- [ ] Mobile app for easier device management
- [ ] Advanced reporting and analytics
- [ ] Device maintenance scheduling
- [ ] Automated device deprecation
- [ ] Integration with HR systems
- [ ] Bulk device import/export
- [ ] Device history timeline
- [ ] Cost tracking and ROI analysis

---

## Support & Troubleshooting

### Common Issues

**1. Database Connection Error**
- Check `.env` file configuration
- For SQLite: Ensure db.sqlite3 is writable
- For PostgreSQL: Verify connection string and credentials

**2. CORS Errors**
- Verify `CORS_ALLOWED_ORIGINS` in `.env`
- Frontend URL should match exactly

**3. Migration Errors**
- Delete db.sqlite3 and run migrations fresh
- Check for syntax errors in models

**4. API Returns 401 Unauthorized**
- Token may have expired
- Use token refresh endpoint
- Login again if needed

---

## Contact & Support

For issues, questions, or contributions:
- Email: support@believersdestination.com
- Project Repository: https://github.com/VikasChauhanBD/believers-inventory

---

**Last Updated**: February 19, 2026
**Version**: 1.0
**Status**: Production Ready
