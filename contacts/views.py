from django.shortcuts import render, HttpResponse
import requests
from requests import api
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ContactsList
from .serializer import ContactsListSerializer
from contacts import serializer

@api_view(['GET'])
def index(request):
    api_urls = {
        'list': '/contacts/list',
        'update' : '/contacts/<int:id>/update/',
        'delete': '/contacts/<int:id>/delete/',
        'create': '/contacts/create/',
        'Detail View': '/contacts/<int:id>/'
    }
    return Response(api_urls)



@api_view(['GET'])
def contact_list(request):
    contacts = ContactsList.objects.all().order_by('-id')
    if contacts == None:
        data = {'contacts': 'There is no contact created.'}
        return Response(data)
    else:
        serializer = ContactsListSerializer(contacts, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def detail_view(request, id):
    contacts = ContactsList.objects.filter(id=id).first()
    if contacts != None:
        serializer = ContactsListSerializer(contacts, many=False)
        return Response(serializer.data)
    else:
        data = {'contacts': 'There is no contact with that id.'}
        return Response(data)


@api_view(['POST'])
def create(request):
    serializer = ContactsListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['PUT'])
def update_contact(request, id):
    contact = ContactsList.objects.filter(id=id).first()
    serializer = ContactsListSerializer(instance=contact, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_contact(request, id):
    contact = ContactsList.objects.filter(id=id).first()
    contact.delete()

    return Response("Item successfully deleted")