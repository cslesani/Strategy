"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),
    path('strategic_tools/',include('strategic_tools.urls')),
    path('finance_tools/', include('financial_tools.urls')),
    path('hr_tools/', include('hr_tools.urls')),
    path('marketing_tools/', include('marketing_tools.urls')),
    path('ops_tools/', include('ops_tools.urls')),
    path('tech_tools/', include('tech_tools.urls')),
    path('reporting_tools/', include('reporting_tools.urls')),

]
