from re import I
from django.test import TestCase
from .models import Department, Employee

# Create your tests here.


class CreateEmployeeTest(TestCase):
    
    def test_create_employee(self):
        User = Employee
        employee = User.objects.create_user(
            name = 'John',
            surname = 'Smith',
            phone_number = '87058543217',
            position = 'Reception Employee',
            department = Department(name = 'Reception'),
            password = '762423123',
        )
        self.assertEqual(employee.name,'John')
        self.assertEqual(employee.surname,'Smith')
        self.assertEqual(employee.phone_number,'87058543217')
        self.assertEqual(employee.position,'Reception Employee')        