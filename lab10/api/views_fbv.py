from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Company
from api.serializers import CompanyModelSerializer, VacancySerializer


@api_view(['GET', 'POST'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanyModelSerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompanyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'ERROR': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return Response({'ERROR': str(e)})
    if request.method == 'GET':
        vacancies = company.vacancies
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
