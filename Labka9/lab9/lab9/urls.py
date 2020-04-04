"""lab9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from api.views import companies
from api.views import companyDetails
from api.views import companyVacancies
from api.views import vacancies
from api.views import vacancyDetails
from api.views import vacancyTop
urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', companies),
    path('companies/<int:company_id>/', companyDetails),
    path('companies/<int:company_id>/vacancies/', companyVacancies),
    path('vacancies/', vacancies),
    path('vacancies/<int:vacancy_id>/', vacancyDetails),
    path('vacancies/top_ten', vacancyTop)
]
