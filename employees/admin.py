from django.contrib import admin
from .models import Employee, Attendance, Salary, Leave, Announcement, Document

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Salary)
admin.site.register(Leave)
admin.site.register(Announcement)
admin.site.register(Document)