from django.shortcuts import render
from django.http import JsonResponse
from api.models import Company
from api.models import Vacancy

def companies(request):
    companiesList = Company.objects.all()
    companies_json = [company.to_json() for company in companiesList]
    return JsonResponse(companies_json, safe=False)

def companyDetails(request, company_id):
        company = Company.objects.get(id=company_id)
        return JsonResponse(company.to_json())

def companyVacancies(request, company_id):
        vacanciesList = Vacancy.objects.filter(company__id=company_id)
        vacancies_json = [vacancy.to_json() for vacancy in vacanciesList]
        return JsonResponse(vacancies_json, safe=False)

def vacancies(request):
    vacancies = Vacancy.objects.all();
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancyDetails(request, vacancy_id):
        vacancy = Vacancy.objects.get(id=vacancy_id);
        return JsonResponse(vacancy.to_json())


def vacancyTop(request):
    vacanciesList = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacanciesList]
    return JsonResponse(vacancies_json, safe=False)

# Create your views here.
