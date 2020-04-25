from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.models import Company
from api.serializers import CompanyModelSerializer, VacancySerializer

class CompanyListAPIView(APIView):

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanyModelSerializer(companies, many=True)
        return Response(serializer.data)



    def post(self, request):
        serializer = CompanyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'ERROR': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CompanyVacanciesAPIView(APIView):

    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return Response({'ERROR': str(e)})



    def get(self, request, id):
        company = self.get_object(id)
        vacancies = company.vacancies
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)