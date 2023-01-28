from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from student_management_app import views, HodViews

from student_management_system import settings

urlpatterns = [
    path('', views.showDemoPage),

    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('login',views.ShowLoginPage),

    path('chat/', include('chat_app.urls')),

    path('get_user_details',views.GetUserDetails),
    path('logout_user',views.logout_user),
    path('doLogin',views.doLogin),
    path('admin_home', HodViews.admin_home),

    path('add_staff',HodViews.add_staff),
    path('add_staff_save',HodViews.add_staff_save),
    path('manage_staff',HodViews.manage_staff),
    path('edit_staff/<str:staff_id>',HodViews.edit_staff),
    path('edit_staff_save',HodViews.edit_staff_save),
    path('staff_feedback',HodViews.edit_student_save),

    path('add_course',HodViews.add_course),
    path('add_course_save',HodViews.add_course_save),
    path('manage_course',HodViews.manage_course),

    path('add_student',HodViews.add_student),
    path('add_student_save',HodViews.add_student_save),
    path('manage_student',HodViews.manage_student),
    path('edit_student/<str:student_id>',HodViews.edit_student),

    path('add_subject',HodViews.add_subject),
    path('add_subject_save',HodViews.add_subject_save),
    path('manage_subject',HodViews.manage_subject),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

