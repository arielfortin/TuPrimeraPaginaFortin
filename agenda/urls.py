from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'agenda'
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('Agenda.urls')),
    #path('', views.index, name='index'),
    path('', views.inicio, name='inicio'),  # tu vista principal
    path('professionals/', views.ProfessionalListView.as_view(), name='professional_list'),
    path('professionals/<int:pk>/', views.ProfessionalDetailView.as_view(), name='professional_detail'),
    path('professionals/new/', views.professional_create, name='professional_create'),
    path('services/new/', views.service_create, name='service_create'),
    path('shifts/new/', views.shift_create, name='shift_create'),
    path('appointments/new/', views.appointment_create, name='appointment_create'),
    path('search/', views.search, name='search'),
]
