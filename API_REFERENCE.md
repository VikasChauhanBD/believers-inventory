# API Reference Guide

## Base URL
```
http://localhost:8000/api
```

## Authentication

All authenticated endpoints require JWT token:
```
Authorization: Bearer <access_token>
```

### Get Tokens
**POST** `/auth/login/`
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```
Response:
```json
{
  "message": "Login successful",
  "employee": { /* employee data */ },
  "tokens": {
    "refresh": "refresh_token_here",
    "access": "access_token_here"
  }
}
```

### Refresh Token
**POST** `/auth/token/refresh/`
```json
{
  "refresh": "refresh_token_here"
}
```
Response:
```json
{
  "access": "new_access_token_here"
}
```

---

## Device Management

### List Devices
**GET** `/inventory/devices/`

Query Parameters:
- `status`: Filter by status (available, assigned, maintenance, retired)
- `device_type`: Filter by type (laptop, desktop, phone, etc.)
- `condition`: Filter by condition (new, excellent, good, fair, poor)
- `search`: Search by device_id, name, brand, model, serial_number
- `ordering`: Sort by field (-created_at, name, status)

Response:
```json
{
  "count": 10,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "uuid",
      "device_id": "DEV001",
      "name": "Laptop A",
      "device_type": "laptop",
      "brand": "Apple",
      "model": "MacBook Pro",
      "serial_number": "ABC123",
      "status": "available",
      "condition": "excellent",
      "location": "Office",
      "created_at": "2024-01-15T10:00:00Z",
      "image": "url_to_image"
    }
  ]
}
```

### Create Device
**POST** `/inventory/devices/`

Request (all required fields):
```json
{
  "device_id": "DEV001",
  "name": "MacBook Pro 16",
  "device_type": "laptop",
  "brand": "Apple",
  "model": "MacBook Pro 16\"",
  "serial_number": "MBP123456",
  "purchase_date": "2024-01-15",
  "purchase_price": "2500.00",
  "warranty_expiry": "2026-01-15",
  "location": "Office",
  "condition": "new",
  "notes": "M3 Max chip, 32GB RAM"
}
```

### Get Device Details
**GET** `/inventory/devices/{id}/`

### Update Device
**PATCH** `/inventory/devices/{id}/`
```json
{
  "status": "maintenance",
  "condition": "good"
}
```

### Delete Device
**DELETE** `/inventory/devices/{id}/`

### Get Available Devices
**GET** `/inventory/devices/available/`

### Mark Device for Maintenance
**POST** `/inventory/devices/{id}/mark_maintenance/`

### Mark Device as Available
**POST** `/inventory/devices/{id}/mark_available/`

---

## Assignment Workflow

### List Assignments
**GET** `/inventory/assignments/`

Query Parameters:
- `status`: Filter by status
- `employee`: Filter by employee UUID
- `device`: Filter by device UUID
- `ordering`: Sort by field

### Create Assignment
**POST** `/inventory/assignments/`

Request:
```json
{
  "device": "device-uuid",
  "employee": "employee-uuid",
  "expected_return_date": "2026-03-01",
  "assignment_notes": "Device for development work"
}
```

Response:
```json
{
  "id": "assignment-uuid",
  "device": "device-uuid",
  "device_details": { /* device info */ },
  "employee": "employee-uuid",
  "employee_details": { /* employee info */ },
  "status": "pending_approval",
  "assigned_date": "2024-01-15T10:00:00Z",
  "expected_return_date": "2026-03-01"
}
```

### Approve Assignment
**POST** `/inventory/assignments/{id}/approve_assignment/`

Request (multipart/form-data):
```
Form Fields:
- assignment_image: <image file>
- assignment_undertaking: true/false
```

Response:
```json
{
  "message": "Assignment approved successfully",
  "assignment": { /* updated assignment data */ }
}
```

### Request Device Return
**POST** `/inventory/assignments/{id}/request_return/`

Request:
```json
{
  "return_notes": "Device in good condition, ready to return"
}
```

Response:
```json
{
  "message": "Return request submitted",
  "assignment": { /* updated assignment */ }
}
```

### Approve Device Return
**POST** `/inventory/assignments/{id}/approve_return/`

Request (multipart/form-data):
```
Form Fields:
- return_image: <image file>
- device_condition_on_return: good|excellent|fair|poor
- device_broken: true/false
```

Response:
```json
{
  "message": "Return approved successfully",
  "assignment": { /* updated assignment */ }
}
```

### Get My Assignments
**GET** `/inventory/assignments/my_assignments/`

Returns only current user's active assignments

---

## Employee Management

### List Employees
**GET** `/auth/employees/`

Response:
```json
[
  {
    "id": "uuid",
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "full_name": "John Doe",
    "employee_id": "EMP001",
    "role": "employee",
    "department": "IT",
    "phone_number": "+1-2025551234",
    "is_active": true,
    "date_joined": "2024-01-15T10:00:00Z"
  }
]
```

### Get Employee Details
**GET** `/auth/employees/{id}/`

### Get Current User Profile
**GET** `/auth/me/`

### Update Current User Profile
**PATCH** `/auth/me/`

Request:
```json
{
  "first_name": "Jane",
  "phone_number": "+1-2025559876"
}
```

---

## Ticket Management

### List Tickets
**GET** `/inventory/tickets/`

Query Parameters:
- `status`: pending, in_progress, resolved, rejected, closed
- `ticket_type`: repair, replacement, new_device, issue, return, other
- `priority`: low, medium, high, urgent
- `search`: Search by ticket_number, subject

### Create Ticket
**POST** `/inventory/tickets/`

Request:
```json
{
  "ticket_type": "repair",
  "priority": "high",
  "device": "device-uuid",
  "subject": "Laptop not turning on",
  "description": "MacBook Pro won't power on after update"
}
```

### Assign Ticket
**POST** `/inventory/tickets/{id}/assign/`

Request:
```json
{
  "assigned_to": "employee-uuid"
}
```

### Resolve Ticket
**POST** `/inventory/tickets/{id}/resolve/`

Request:
```json
{
  "resolution_notes": "Replaced hard drive, device working fine now"
}
```

### Get My Tickets
**GET** `/inventory/tickets/my_tickets/`

Returns matching tickets created by or assigned to current user

---

## Dashboard

### Get Dashboard Statistics
**GET** `/inventory/dashboard/stats/`

Response:
```json
{
  "total_devices": 50,
  "available_devices": 20,
  "assigned_devices": 25,
  "maintenance_devices": 5,
  "retired_devices": 0,
  "total_employees": 30,
  "active_employees": 25,
  "total_assignments": 25,
  "active_assignments": 25,
  "total_tickets": 15,
  "pending_tickets": 3,
  "in_progress_tickets": 5,
  "resolved_tickets": 7,
  "device_by_type": {
    "laptop": 20,
    "desktop": 15,
    "phone": 10,
    "tablet": 5
  },
  "recent_assignments": [ /* array of assignments */ ],
  "recent_tickets": [ /* array of tickets */ ]
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid data",
  "field": ["Error message for field"]
}
```

### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden
```json
{
  "error": "You do not have permission to perform this action."
}
```

### 404 Not Found
```json
{
  "detail": "Not found."
}
```

---

## Rate Limiting
None implemented yet (add in production)

## Pagination
Default page size: 10
Query parameter: `?page=2`

---

## File Upload Limits
- Device image: Max 5MB, formats: JPG, PNG, GIF
- Assignment image: Max 5MB, formats: JPG, PNG, GIF
- Return image: Max 5MB, formats: JPG, PNG, GIF
- Ticket attachment: Max 10MB

---

## Status Codes

| Code | Status | Meaning |
|------|--------|---------|
| 200 | OK | Request successful |
| 201 | Created | Resource created |
| 204 | No Content | Delete successful |
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Auth required |
| 403 | Forbidden | Permission denied |
| 404 | Not Found | Resource not found |
| 500 | Server Error | Something went wrong |

---

**Last Updated**: February 19, 2026
