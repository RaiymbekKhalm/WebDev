from rest_framework import serializers
from api.models import Company, Vacancy

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    city = serializers.CharField()
    address = serializers.CharField(style={'base_template': 'textarea.html'})


    def create(self, valide_data):
        company = Company.objects.create(name=valide_data.get('name'), description=valide_data.get('description'),
                                         city=valide_data.get('city'), address=valide_data.get('address'))
        return company


    def update(self, instead, valide_data):
        instead.name = valide_data.get('name', instead.name)
        instead.description = valide_data.get('description', instead.description)
        instead.city = valide_data.get('city', instead.city)
        instead.address = valide_data.get('address', instead.address)
        instead.save()
        return instead


class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')



class VacancySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    salary = serializers.FloatField()
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company_id')




class CompanyWithVacanciesSerializer(serializers.ModelSerializer):
    vacancies = VacancySerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address', 'vacancies')