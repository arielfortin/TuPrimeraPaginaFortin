from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Professional, Service, Appointment, Shift
from .forms import ProfessionalForm, ServiceForm, AppointmentForm, ShiftForm
from django.db.models import Q
from django.urls import reverse_lazy

def index(request):
    professionals = Professional.objects.all()[:6]
    return render(request, 'agenda/index.html', {'professionals': professionals})

# List & detail for professionals
class ProfessionalListView(generic.ListView):
    model = Professional
    template_name = 'agenda/professional_list.html'
    context_object_name = 'professionals'
    paginate_by = 12

class ProfessionalDetailView(generic.DetailView):
    model = Professional
    template_name = 'agenda/professional_detail.html'
    context_object_name = 'professional'

# Create views (function-based for clarity)
def professional_create(request):
    if request.method == 'POST':
        form = ProfessionalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agenda:professional_list')
    else:
        form = ProfessionalForm()
    return render(request, 'agenda/professional_form.html', {'form': form})

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:professional_list')
    else:
        form = ServiceForm()
    return render(request, 'agenda/service_form.html', {'form': form})

def shift_create(request):
    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:professional_list')
    else:
        form = ShiftForm()
    return render(request, 'agenda/shift_form.html', {'form': form})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # opcional: validar capacidad
            appointment = form.save(commit=False)
            shift = appointment.shift
            if shift.appointments.count() >= shift.max_clients:
                form.add_error('shift', 'Este turno ya alcanzó su capacidad máxima.')
            else:
                appointment.save()
                return redirect('agenda:index')
    else:
        form = AppointmentForm()
    return render(request, 'agenda/appointment_form.html', {'form': form})

# Búsqueda simple sobre Professional
def search(request):
    q = request.GET.get('q', '').strip()
    results = Professional.objects.none()
    if q:
        results = Professional.objects.filter(
            Q(name__icontains=q) | Q(specialty__icontains=q) | Q(bio__icontains=q)
        )
    return render(request, 'agenda/search_results.html', {'query': q, 'results': results})


def inicio(request):
    return HttpResponse("¡Bienvenido a la Agenda Online!")

# Create your views here.
