"""myportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from about.views import firstpage, thanks_page
from projects.views import Project
from .settings import DEBUG


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', firstpage, name='title'),
    path('<int:pk>', Project.as_view(), name='project_url'),
    path('thanks', thanks_page, name='thanks')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
