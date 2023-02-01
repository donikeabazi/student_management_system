from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

class LoginCheckMiddleWare(MiddlewareMixin):
    
    def process_view( self, request, view_func, view_args, view_kwargs):
        modulename=view_func.__module__
        print(modulename)
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "student_management_app.HodViews":
                    pass
                elif modulename == "student_management_app.views" or modulename == "django.views.static":
                    pass
                else:
                    HttpResponseRedirect(reverse('admin_home'))
            elif user.user_type == "2":
                if modulename == "student_management_app.StaffViews":
                    pass
                elif modulename == "student_management_app.views" or modulename == "django.views.static":
                    pass
                else:
                    HttpResponseRedirect(reverse('staff_home'))
            elif user.user_type == "3":
                if modulename == "student_management_app.StudentViews" or modulename == "django.views.static":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home"))
            else:
                return HttpResponseRedirect(reverse("login"))

        else:
            if request.path == reverse("login") or request.path == reverse("do_login") or modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites" or modulename=="student_management_app.views":
                pass
            else:
                return HttpResponseRedirect(reverse("login"))
