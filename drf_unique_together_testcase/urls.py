from django.contrib import admin
from django.urls import path, include

from drf_unique_together_testcase.api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.get_urls())),
]
