# Login System Setup Guide - Believers Inventory Management System

## Overview
Your login system is now fully configured and tested. Both the Django DRF backend and React Vite frontend are working correctly with proper JWT authentication.

## ✅ Verification Summary

### Backend (Django DRF)
- **Status**: ✓ Running on http://localhost:8000
- **Database**: SQLite (db.sqlite3) configured with migrations applied
- **Authentication**: JWT tokens implemented with SimpleJWT
- **CORS**: Configured to allow frontend requests from http://localhost:5173
- **API Endpoints**: All authentication endpoints verified and working

### Frontend (React + Vite)
- **Status**: ✓ Running on http://localhost:5173
- **Environment**: Configured to connect to http://localhost:8000/api
- **Components**: Login, Signup, Password Reset, and Auth Context all set up
- **Routing**: Protected routes configured with role-based access

### Test Credentials
- **Regular User**: 
  - Email: `test@example.com`
  - Password: `Test@123456`
  - Role: Employee

- **Admin User**:
  - Email: `admin@example.com`
  - Password: `Admin@123456`
  - Role: Admin

## API Endpoints Reference

### Authentication Endpoints
All endpoints are prefixed with `/api/auth/`

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | `/signup/` | No | Create new employee account |
| POST | `/login/` | No | Login and get JWT tokens |
| POST | `/logout/` | Yes | Logout and invalidate refresh token |
| GET | `/me/` | Yes | Get current user profile |
| PATCH | `/me/` | Yes | Update current user profile |
| POST | `/password/change/` | Yes | Change user password |
| POST | `/password/reset/` | No | Request password reset |
| POST | `/password/reset/confirm/` | No | Confirm password reset with token |
| GET | `/password/reset/verify/` | No | Verify if reset token is valid |
| POST | `/token/refresh/` | No | Refresh access token |

## Backend Structure

```
ims-backend/
├── apps/
│   ├── authentication/
│   │   ├── models.py              # Employee and PasswordResetToken models
│   │   ├── views.py               # All auth views (Login, Signup, etc.)
│   │   ├── serializers.py         # Request/response serializers
│   │   ├── urls.py                # Auth endpoint routes
│   │   ├── permissions.py         # Custom permission classes
│   │   └── utils.py               # Email sending utilities
│   └── inventory/
├── config/
│   ├── settings.py                # Django settings with JWT config
│   ├── urls.py                    # Main URL routing
│   └── wsgi.py
├── manage.py
├── db.sqlite3
└── requirements.txt
```

## Frontend Structure

```
ims-frontend/
├── src/
│   ├── App.jsx                    # Main app with routing
│   ├── AuthContext/
│   │   └── AuthContext.jsx        # Authentication state management
│   ├── pages/
│   │   ├── loginPage/
│   │   │   └── Login.jsx          # Login form component
│   │   ├── signupPage/
│   │   │   └── Signup.jsx         # Signup form component
│   │   ├── forgetpasswordPage/
│   │   │   └── ForgotPassword.jsx # Password reset request
│   │   └── resetPasswordPage/
│   │       └── ResetPassword.jsx  # Password reset confirmation
│   └── services/
│       └── api.js                 # Axios API client with interceptors
├── package.json
└── .env.local                     # Environment configuration
```

## Key Implementation Details

### JWT Authentication Flow
1. User submits credentials to `/auth/login/`
2. Backend validates credentials and returns:
   - `access` token (expires in 1 hour)
   - `refresh` token (expires in 7 days)
   - User profile data
3. Frontend stores tokens in localStorage
4. All API requests include `Authorization: Bearer <access_token>` header
5. If access token expires, frontend automatically refreshes using refresh token
6. If refresh fails, user is logged out

### Protected Routes
- `/` - User dashboard (all authenticated users)
- `/admin` - Admin dashboard (admin role only)
- `/login` - Login page (public, redirects if logged in)
- `/signup` - Signup page (public, redirects if logged in)
- `/forgot-password` - Password reset request (public with verification link)
- `/reset-password` - Password reset form (public with token verification)

### Error Handling
The frontend API client (`api.js`) includes:
- Request interceptor: Adds auth token to headers
- Response interceptor: Handles 401 errors with token refresh
- Error parsing: Converts backend error messages to user-friendly format

## Environment Configuration Files

### Backend (.env)
```env
SECRET_KEY=django-insecure-change-this-in-production-believers-inventory
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
FRONTEND_URL=http://localhost:5173
```

### Frontend (.env.local)
```env
VITE_API_URL=http://localhost:8000/api
```

## Running the Application

### Backend
```bash
cd ims-backend
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
python manage.py runserver 0.0.0.0:8000
```

### Frontend
```bash
cd ims-frontend
npm run dev
```

Then access the application at: **http://localhost:5173**

## Testing the Login
1. Navigate to http://localhost:5173
2. Click "Sign In"
3. Enter test credentials:
   - Email: `test@example.com`
   - Password: `Test@123456`
4. You should be redirected to the dashboard

## Production Deployment Considerations

### Backend
1. Change `SECRET_KEY` to a strong, secure value
2. Set `DEBUG=False`
3. Update `ALLOWED_HOSTS` with your domain
4. Update `CORS_ALLOWED_ORIGINS` with frontend URL
5. Use PostgreSQL instead of SQLite
6. Set up email backend for password reset emails
7. Use environment-based settings from .env

### Frontend
1. Update `VITE_API_URL` to your production backend domain
2. Build: `npm run build`
3. Deploy built files from `dist/` folder to your hosting

## Troubleshooting

### "Port already in use" error
Kill the existing process:
```bash
lsof -i :8000  # Find process
kill -9 <PID>  # Kill the process
```

### CORS errors
Verify `CORS_ALLOWED_ORIGINS` in backend settings includes your frontend URL.

### Login fails with "Invalid credentials"
1. Check username/password are correct
2. Verify user exists: `python manage.py shell` then query Employee model
3. Check email is lowercase for consistency

### "Token is invalid" error
1. Clear browser localStorage
2. Log in again
3. Check token expiration times in settings.py

### Frontend not connecting to backend
1. Verify backend is running on port 8000
2. Check `.env.local` has correct `VITE_API_URL`
3. Check browser console for CORS errors
4. Verify `CORS_ALLOWED_ORIGINS` in backend includes frontend URL

## Next Steps

1. Customize user roles and permissions as needed
2. Add additional authentication features (2FA, social login)
3. Configure email backend for production password resets
4. Set up database backups
5. Implement audit logging for authentication events
6. Add rate limiting to prevent brute force attacks

## Support
For issues or questions, refer to:
- Django DRF docs: https://www.django-rest-framework.org/
- Django JWT docs: https://django-rest-framework-simplejwt.readthedocs.io/
- React docs: https://react.dev/
- Vite docs: https://vitejs.dev/
