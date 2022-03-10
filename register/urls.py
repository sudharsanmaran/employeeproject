from django.urls import path,include
from . import views
app_name="register"
urlpatterns = [
    path('',views.home, name = "home"),
    path('login/',views.login  ,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),
    path('show/',views.show,name="show"),
    path('update/',views.update,name="update"),
    path('delete/',views.delete,name="delete"),
    path('real_delete/',views.real_delete,name="real_delete"),
    path('employee_form/',views.employee_form,name='employee_form')
]
