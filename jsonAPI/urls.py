from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from data import views

router = routers.DefaultRouter()
router.register(r'data', views.DataViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/',admin.site.urls),
    path('home/',views.home,name="data-home")
]
