"""iaq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.documentation import include_docs_urls  # Documentation
from rest_framework.schemas import get_schema_view  # Schemas
from django.shortcuts import redirect

import devices.views

schema_view = get_schema_view(title='Indoor Air Quality API')  # Schema Title

urlpatterns = [
    path('', lambda request: redirect('api/docs/', permanent=False)),  # redirect root to docs/
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/registration/', include('rest_auth.registration.urls')),
    path('api/rooms/', include('rooms.urls')),
    path('api/devices/', include('devices.urls')),
    path('api/devices/<int:pk>/values', devices.views.device_values),
    path('api/events/', include('events.urls')),
    path('api/docs/', include_docs_urls(title='Indoor Air Quality API', description='API for Indoor Air Quality Systems')),
    path('api/schema/', schema_view),
]
