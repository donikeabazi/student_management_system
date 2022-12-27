from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from student_management_app import views

from student_management_system import settings

urlpatterns = [
    path('', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('chat/', include('chat_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

