from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(email, pin_code):
    subject = 'Your PIN Code'
    message = f'Your PIN code is: {pin_code}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])