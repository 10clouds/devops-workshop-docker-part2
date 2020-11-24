from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from hello import views

router = routers.DefaultRouter()
router.register(r'hellos', views.HelloView, 'hello')

urlpatterns = [
    path('admin/', admin.site.urls),         path('api/', include(router.urls))
]
