"""
Management command to create test employees
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.authentication.models import Employee


class Command(BaseCommand):
    help = 'Create 5 test employees with @believersdestination.com emails'

    def handle(self, *args, **options):
        test_employees = [
            {
                'first_name': 'Shubh',
                'last_name': 'Sharma',
                'email': 'shubh@believersdestination.com',
                'department': 'IT',
                'phone_number': '+91-9876543210',
                'role': 'employee'
            },
            {
                'first_name': 'Vikas',
                'last_name': 'Chauhan',
                'email': 'vikas@believersdestination.com',
                'department': 'Operations',
                'phone_number': '+91-9876543211',
                'role': 'employee'
            },
            {
                'first_name': 'Vamika',
                'last_name': 'Singh',
                'email': 'vamika@believersdestination.com',
                'department': 'HR',
                'phone_number': '+91-9876543212',
                'role': 'employee'
            },
            {
                'first_name': 'Arun',
                'last_name': 'Kumar',
                'email': 'arun@believersdestination.com',
                'department': 'Finance',
                'phone_number': '+91-9876543213',
                'role': 'employee'
            },
            {
                'first_name': 'Aman',
                'last_name': 'Verma',
                'email': 'aman@believersdestination.com',
                'department': 'Marketing',
                'phone_number': '+91-9876543214',
                'role': 'employee'
            },
        ]

        created_count = 0
        for emp_data in test_employees:
            email = emp_data['email']
            
            # Check if employee already exists
            if Employee.objects.filter(email=email).exists():
                self.stdout.write(
                    self.style.WARNING(f'Employee {email} already exists, skipping...')
                )
                continue

            # Create employee with default password
            employee = Employee.objects.create_user(
                email=email,
                password='TestPassword123!',  # Default password
                first_name=emp_data['first_name'],
                last_name=emp_data['last_name'],
                department=emp_data['department'],
                phone_number=emp_data['phone_number'],
                role=emp_data['role'],
                is_active=True,
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created employee: {employee.full_name} ({email})'
                )
            )
            created_count += 1

        # Also create an admin user if not exists
        admin_email = 'admin@believersdestination.com'
        if not Employee.objects.filter(email=admin_email).exists():
            admin = Employee.objects.create_superuser(
                email=admin_email,
                password='AdminPassword123!',
                first_name='Admin',
                last_name='User',
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created admin: {admin.full_name} ({admin_email})'
                )
            )
            created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'\nTotal {created_count} users created successfully!'
            )
        )
        self.stdout.write(
            self.style.WARNING(
                '\nDefault password for all test employees: TestPassword123!'
            )
        )
        self.stdout.write(
            self.style.WARNING(
                'Default password for admin: AdminPassword123!'
            )
        )
