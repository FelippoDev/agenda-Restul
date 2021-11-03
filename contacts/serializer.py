from django.db import models
from rest_framework import serializers
from .models import ContactsList


class ContactsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsList
        fields = '__all__'
