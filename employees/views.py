import json
import openpyxl
from .models import Leave
from .models import Announcement
from .models import Document
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Attendance
from .models import Salary
from datetime import datetime
from datetime import date
from django.contrib import messages
from .models import Employee
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg, Max, Min


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.employee.role == "Admin":
                return redirect('dashboard')

            elif user.employee.role == "Employee":
                return redirect('dashboard')

    return render(request, 'login.html')


@login_required
def dashboard(request):

    total_employees = Employee.objects.count()

    present_today = Attendance.objects.filter(
        date=date.today(),
        status='Present'
    ).count()

    total_leaves = Leave.objects.filter(
        status='Approved'
    ).count()

    present_count = Attendance.objects.filter(
        status='Present'
    ).count()

    leave_count = Attendance.objects.filter(
        status='Leave'
    ).count()

    absent_count = Attendance.objects.filter(
        status='Absent'
    ).count()

    total_announcements = Announcement.objects.count()

    total_documents = Document.objects.count()

    # Payroll Analytics

    salary_data = Salary.objects.aggregate(

        total_payroll=Sum('net_salary'),

        average_salary=Avg('net_salary'),

        highest_salary=Max('net_salary'),

        lowest_salary=Min('net_salary')

    )

    total_payroll = salary_data['total_payroll'] or 0

    average_salary = round(
        salary_data['average_salary'] or 0
    )

    highest_salary = salary_data['highest_salary'] or 0

    lowest_salary = salary_data['lowest_salary'] or 0

    salaries = Salary.objects.all()

    payroll_months = []
    payroll_values = []

    for salary in salaries:
        payroll_months.append(salary.month)

        payroll_values.append(salary.net_salary)

    context = {

        'total_employees': total_employees,
        'present_today': present_today,
        'total_leaves': total_leaves,
        'total_announcements': total_announcements,
        'total_documents': total_documents,

        'total_payroll': total_payroll,
        'highest_salary': highest_salary,
        'lowest_salary': lowest_salary,
        'average_salary': average_salary,

        'attendance_present': present_count,
        'attendance_leave': leave_count,
        'attendance_absent': absent_count,

        'payroll_months': json.dumps(payroll_months),
        'payroll_values': json.dumps(payroll_values),

    }

    return render(
        request,
        'dashboard.html',
        context
    )


def logout_view(request):

    logout(request)
    return redirect('login')


@login_required
def profile(request):

    employee = Employee.objects.get(user=request.user)

    return render(
        request,
        'profile.html',
        {'employee': employee}
    )


@login_required
def attendance_view(request):

    employee = request.user.employee

    today = datetime.today().date()

    attendance_record, created = Attendance.objects.get_or_create(
        employee=employee,
        date=today
    )

    if request.method == 'POST':

        if 'check_in' in request.POST:

            attendance_record.check_in = datetime.now().time()

            attendance_record.save()

            messages.success(request, 'Checked In Successfully')

        if 'check_out' in request.POST:

            attendance_record.check_out = datetime.now().time()

            attendance_record.save()

            messages.success(request, 'Checked Out Successfully')

    attendance_records = Attendance.objects.filter(
        employee=employee
    ).order_by('-date')

    return render(
        request,
        'attendance.html',
        {
            'attendance_records': attendance_records
        }
    )

@login_required
def salary_view(request):

    employee = request.user.employee

    salary = Salary.objects.filter(
        employee=employee
    ).last()

    return render(
        request,
        'salary.html',
        {
            'salary': salary
        }
    )


@login_required
def download_salary_pdf(request):

    employee = request.user.employee

    salary = Salary.objects.filter(
        employee=employee
    ).last()

    response = HttpResponse(
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename="salary_slip.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 18)
    p.drawString(180, 800, "Employee Salary Slip")

    p.setFont("Helvetica", 12)

    p.drawString(
        50, 740,
        f"Employee: {employee.user.username}"
    )

    p.drawString(
        50, 710,
        f"Department: {employee.department}"
    )

    p.drawString(
        50, 680,
        f"Designation: {employee.designation}"
    )

    p.drawString(
        50, 650,
        f"Month: {salary.month}"
    )

    p.drawString(
        50, 600,
        f"Basic Salary: Rs {salary.basic_salary}"
    )

    p.drawString(
        50, 570,
        f"HRA: Rs {salary.hra}"
    )

    p.drawString(
        50, 540,
        f"Bonus: Rs {salary.bonus}"
    )

    p.drawString(
        50, 510,
        f"Tax: Rs {salary.tax}"
    )

    p.drawString(
        50, 480,
        f"PF: Rs {salary.pf}"
    )

    p.setFont("Helvetica-Bold", 14)

    p.drawString(
        50, 430,
        f"Net Salary: Rs {salary.net_salary}"
    )

    p.save()

    return response


@login_required
def leave_view(request):

    employee = request.user.employee

    if request.method == 'POST':

        leave_type = request.POST['leave_type']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        reason = request.POST['reason']

        Leave.objects.create(
            employee=employee,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            reason=reason
        )

    leaves = Leave.objects.filter(
        employee=employee
    ).order_by('-created_at')

    return render(
        request,
        'leave.html',
        {
            'leaves': leaves
        }
    )


@login_required
def announcements_view(request):

    announcements = Announcement.objects.all().order_by(
        '-created_at'
    )

    return render(
        request,
        'announcements.html',
        {
            'announcements': announcements
        }
    )


@login_required
def documents_view(request):

    employee = request.user.employee

    if request.method == 'POST':

        document_name = request.POST['document_name']

        document_file = request.FILES['document_file']

        Document.objects.create(
            employee=employee,
            document_name=document_name,
            document_file=document_file
        )

    documents = Document.objects.filter(
        employee=employee
    )

    return render(
        request,
        'documents.html',
        {
            'documents': documents
        }
    )

@login_required
def employee_directory(request):

    employees = Employee.objects.all()

    search = request.GET.get('search')

    if search:

        employees = employees.filter(
            user__username__icontains=search
        )

    return render(
        request,
        'employee_directory.html',
        {
            'employees': employees
        }
    )


@login_required
def admin_dashboard(request):

    employees = Employee.objects.all()

    leaves = Leave.objects.all().order_by('-created_at')

    documents = Document.objects.all()

    salaries = Salary.objects.all()


    for salary in salaries:
        payroll_months.append(salary.month)

        payroll_values.append(salary.net_salary)

    context = {

        'employees': employees,
        'leaves': leaves,
        'documents': documents,
        'salaries': salaries,

    }

    return render(
        request,
        'admin_dashboard.html',
        context
    )


@login_required
def approve_leave(request, leave_id):

    leave = Leave.objects.get(id=leave_id)

    leave.status = "Approved"

    leave.save()

    return redirect('admin_dashboard')


@login_required
def export_employees_excel(request):

    workbook = openpyxl.Workbook()

    worksheet = workbook.active

    worksheet.title = "Employees"

    worksheet.append([
        "Employee ID",
        "Name",
        "Department",
        "Designation",
        "Salary"
    ])

    employees = Employee.objects.all()

    for employee in employees:

        worksheet.append([

            employee.employee_id,

            employee.user.username,

            employee.department,

            employee.designation,

            employee.employee_salary

        ])

    response = HttpResponse(
        content_type=
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename=employees.xlsx'

    workbook.save(response)

    return response