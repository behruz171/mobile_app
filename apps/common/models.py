from django.db import models


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True


class Sponsor(BaseModel):
    class SponsorStatus(models.TextChoices):
        NEW = 'new', 'New'
        MODERATION = 'moderation', 'Moderation'
        APPROVED = 'approved', 'Approved'
        CANCELED = 'canceled', 'Canceled'
    class PaymentType(models.TextChoices):
        CASH = 'cash', 'Cash'
        BY_CARD = 'by_card', 'By card'

    class UserType(models.TextChoices):
        PHYSICAL = 'physical', 'Physical'
        LEGAL = 'legal', 'Legal'
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    wallet = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=SponsorStatus.choices, default=SponsorStatus.NEW)
    payment_type = models.CharField(max_length=20, choices=PaymentType.choices, null=True)
    company_name = models.CharField(max_length=200, null=True)
    user_type = models.CharField(max_length=20, choices=UserType.choices, default=UserType.PHYSICAL)

    def __str__(self):
        return self.full_name
    

class University(BaseModel):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Student(BaseModel):
    class DegreeType(models.TextChoices):
        BACHELOR = 'bachelor', 'Bachelor'
        MASTER = 'master', 'Master'
    full_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=20, choices=DegreeType.choices, default=DegreeType.BACHELOR)
    university = models.ForeignKey(University, on_delete=models.PROTECT, related_name='students')
    contract = models.DecimalField(max_digits=12, decimal_places=2)
    phone_number = models.CharField(max_length=20)


    def __str__(self):
        return self.full_name
    


class StudentSponser(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='sponsor_amounts')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name = 'student_amounts')
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.student} - {self.sponsor}"
    
