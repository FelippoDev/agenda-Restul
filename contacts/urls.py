from django.urls import path
from . import views


app_name='contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/list/', views.contact_list, name='list'),
    path('contacts/<int:id>/', views.detail_view, name='detail-view'),
    path('contacts/create/', views.create, name='create'),
    path('contacts/<int:id>/update/', views.update_contact, name='delete'),
    path('contacts/<int:id>/delete/', views.delete_contact, name='update'),
]