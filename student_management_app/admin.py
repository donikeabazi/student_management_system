from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Students, Courses, Subjects, Attendance, AttendanceReport, \
    LeaveReportStudent, FeedBackStudent, NotificationStudent, SessionYearModel, StudentResult, OnlineClassRoom

class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)
admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(FeedBackStudent)
admin.site.register(NotificationStudent)
admin.site.register(SessionYearModel)
admin.site.register(StudentResult)
admin.site.register(OnlineClassRoom)
