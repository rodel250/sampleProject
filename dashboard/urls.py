from django.urls import path
from . import views

#path arranged alphabetically by name
app_name= 'dashboard'
urlpatterns=[
    #path('api/data', views.get_data, name='api-data'),

    #TEST URL
    path('dashboard', views.DashboardIndexView.as_view(), name="dashboard_view"),
    path('registration', views.RegistrationView.as_view(), name="registration_view"),

]