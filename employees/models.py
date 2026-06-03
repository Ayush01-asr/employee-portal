from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Employee', 'Employee'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='Employee'
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    department = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    designation = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    employee_salary = models.IntegerField(
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    profile_pic = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username


class Attendance(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    date = models.DateField(
        auto_now_add=True
    )

    check_in = models.TimeField(
        blank=True,
        null=True
    )

    check_out = models.TimeField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        default='Present'
    )

    def __str__(self):
        return f"{self.employee.user.username} - {self.date}"


class Salary(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    month = models.CharField(
        max_length=20
    )

    basic_salary = models.IntegerField()

    hra = models.IntegerField()

    bonus = models.IntegerField()

    tax = models.IntegerField()

    pf = models.IntegerField()

    net_salary = models.IntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        self.net_salary = (
            self.basic_salary
            + self.hra
            + self.bonus
            - self.tax
            - self.pf
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.user.username} - {self.month}"


class Leave(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    leave_type = models.CharField(
        max_length=50
    )

    start_date = models.DateField()

    end_date = models.DateField()

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.employee.user.username} - {self.leave_type}"


class Announcement(models.Model):

    title = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Document(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    document_name = models.CharField(
        max_length=100
    )

    document_file = models.FileField(
        upload_to='documents/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.employee.user.username} - {self.document_name}"