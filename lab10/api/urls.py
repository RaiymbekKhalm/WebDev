from django.urls import path
from api import views_fbv as v
from rest_framework_jwt.views import obtain_jwt_token




urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', v.company_list),
    path('companies/<int:id>/vacancies/', v.company_vacancies)
]
