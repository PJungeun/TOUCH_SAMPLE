from django.contrib import admin
from django.urls import path
import count.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', count.views.main, name="main"),
    path('count/',count.views.count, name ="count"),
]
