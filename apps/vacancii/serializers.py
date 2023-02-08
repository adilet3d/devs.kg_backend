from rest_framework import serializers

from apps.vacancii.models import Vacancii


class VacanciiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vacancii
        fields=(
            'id','doljnost','oklad','type','description',
        )
        read_only_fields=('company',)