from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from student_management_app import StaffViews, StudentViews, views, HodViews

from student_management_system import settings

urlpatterns = [
    path('', HodViews.admin_home,name="admin_home"),
    path('admin/', admin.site.urls),
    path('login',views.ShowLoginPage, name="show_login"),
    path('auth/', include('django.contrib.auth.urls')),
    path('signup_student',views.signup_student,name="signup_student"),
    path('signup_staff',views.signup_staff,name="signup_staff"),
    path('do_staff_signup',views.do_staff_signup,name="do_staff_signup"),
    path('do_signup_student',views.do_signup_student,name="do_signup_student"),
    
    path('chat/', include('chat_app.urls')),

    path('get_user_details',views.GetUserDetails),
    path('logout_user',views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),

    path('students', HodViews.view_students ,name="view_students"),
    path('students/<str:id>', HodViews.view_students ,name="edit_student"),
    path('edit_student',HodViews.edit_student,name="edit_student"),

    path('staff', HodViews.view_staff ,name="view_staff"),
    path('staff/<str:id>', HodViews.view_staff ,name="edit_staff"),
    path('edit_staff',HodViews.edit_staff,name="edit_stafsf"),

    path('courses',HodViews.view_courses,name="view_courses"),
    path('courses/<str:id>',HodViews.view_courses,name="edit_course"),
    path('edit_course',HodViews.edit_course,name="edit_course"),
    
    path('subjects',HodViews.view_subjects,name="view_subjects"),
    path('subjects/<str:id>',HodViews.view_subjects,name="edit_subject"),
    path('edit_subject',HodViews.edit_subject,name="edit_subject"),
    
    path('manage_session',HodViews.manage_session,name="manage_session"),
    path('add_session_save',HodViews.add_session_save,name="add_session_save"),
#  Staff URL PATH 
    path('staff_home',StaffViews.staff_home,name="staff_home"),
    path('staff_take_attendance',StaffViews.staff_take_attendance,name="staff_take_attendance"),
    path('staff_update_attendance',StaffViews.staff_update_attendance,name="staff_update_attendance"),
    path('get_students',StaffViews.get_students,name="get_students"),
    path('get_attendance_dates',StaffViews.get_attendance_dates,name="get_attendance_dates"),
    path('get_attendance_student',StaffViews.get_attendance_student,name="get_attendance_student"),
    path('save_attendance_data',StaffViews.save_attendance_data,name="save_attendance_data"),
    path('save_updateattendance_data',StaffViews.save_updateattendance_data,name="save_updateattendance_data"),
    path('staff_apply_leave',StaffViews.staff_apply_leave,name="staff_apply_leave"),
    path('staff_apply_leave_save',StaffViews.staff_apply_leave_save,name="staff_apply_leave_save"),
    path('staff_feedback',StaffViews.staff_feedback,name="staff_feedback"),
    path('staff_feedback_save',StaffViews.staff_feedback_save,name="staff_feedback_save"),
    
    # Student
    path('student_home',StudentViews.student_home,name="student_home"),
    path('student_view_attendance',StudentViews.student_view_attendance,name="student_view_attendance"),
    path('student_view_attendance_post',StudentViews.student_view_attendance_post,name="student_view_attendance_post"),
    path('student_apply_leave', StudentViews.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save', StudentViews.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback', StudentViews.student_feedback, name="student_feedback"),
    path('student_feedback_save', StudentViews.student_feedback_save, name="student_feedback_save"),
    path('student_profile', StudentViews.student_profile, name="student_profile"),
    path('student_profile_save', StudentViews.student_profile_save, name="student_profile_save"),
    # path('student_fcmtoken_save', StudentViews.student_fcmtoken_save, name="student_fcmtoken_save"),
    # path('firebase-messaging-sw.js',views.showFirebaseJS,name="show_firebase_js"),
    # path('student_all_notification',StudentViews.student_all_notification,name="student_all_notification"),
    path('student_view_result',StudentViews.student_view_result,name="student_view_result"),
    path('join_class_room/<int:subject_id>/<int:session_year_id>',StudentViews.join_class_room,name="join_class_room"),
    # path('node_modules/canvas-designer/widget.html',StaffViews.returnHtmlWidget,name="returnHtmlWidget"),
    path('testurl/',views.Testurl)
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

