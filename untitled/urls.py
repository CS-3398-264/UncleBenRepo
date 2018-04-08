
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from nuber import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('driver/', views.DriverList.as_view()),
    path('user/', views.UserList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
