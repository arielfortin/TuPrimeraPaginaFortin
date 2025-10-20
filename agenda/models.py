from django.db import models
from django.urls import reverse

class Professional(models.Model):
    name = models.CharField("Nombre", max_length=120)
    specialty = models.CharField("Especialidad", max_length=80, help_text="ej: Barbero, Educador, Consultor")
    bio = models.TextField("Biografía", blank=True)
    photo = models.ImageField("Foto", upload_to="professionals/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.specialty}"

    def get_absolute_url(self):
        return reverse('agenda:professional_detail', args=[self.pk])


class Service(models.Model):
    name = models.CharField("Servicio", max_length=100)
    duration_minutes = models.PositiveSmallIntegerField("Duración (minutos)", default=30)
    price = models.DecimalField("Precio", max_digits=8, decimal_places=2, null=True, blank=True)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name="services")

    def __str__(self):
        return f"{self.name} ({self.duration_minutes} min) - {self.professional.name}"


class Shift(models.Model):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name="shifts")
    date = models.DateField("Fecha")
    start_time = models.TimeField("Hora inicio")
    end_time = models.TimeField("Hora fin")
    max_clients = models.PositiveSmallIntegerField("Capacidad máxima", default=1)

    class Meta:
        unique_together = ("professional", "date", "start_time")  # evita duplicados exactos

    def __str__(self):
        return f"{self.professional.name} - {self.date} {self.start_time.strftime('%H:%M')}"


class Appointment(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name="appointments")
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    client_name = models.CharField("Nombre cliente", max_length=120)
    client_phone = models.CharField("Teléfono", max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cita: {self.client_name} - {self.shift}"

    def get_absolute_url(self):
        return reverse('agenda:appointment_detail', args=[self.pk])
