from django.db import models

class Registration(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]
    user = models.CharField(max_length=50)
    enrollment = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    qr_code = models.ImageField(upload_to="qr_codes/")
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    unique_id = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
