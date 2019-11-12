from django.contrib import admin
from django.urls import path
from welcome.views import welcfunc
from complaint.views import compfunc
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcfunc),
    path('complaint/', compfunc),
]
