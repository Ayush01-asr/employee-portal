from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_view, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('profile/', views.profile, name='profile'),

    path('attendance/', views.attendance_view, name='attendance'),

    path('salary/', views.salary_view, name='salary'),

    path('logout/', views.logout_view, name='logout'),

    path(
        'download-salary-pdf/',
        views.download_salary_pdf,
        name='download_salary_pdf'
    ),

    path('leave/', views.leave_view, name='leave'),

    path(
        'announcements/',
        views.announcements_view,
        name='announcements'
    ),

    path(
        'documents/',
        views.documents_view,
        name='documents'
    ),

    path(
        'employee-directory/',
        views.employee_directory,
        name='employee_directory'

    ),

    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    path(
        'approve-leave/<int:leave_id>/',
        views.approve_leave,
        name='approve_leave'
    ),

    path(
        'export-employees/',
        views.export_employees_excel,
        name='export_employees'
    ),

]