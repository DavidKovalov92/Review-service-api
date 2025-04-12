from django.core.mail import send_mail

from review_service_api.settings import EMAIL_YAMDB


def send_confirmation_code(email, confirmation_code):
    send_mail(
        subject='Код підтверждення',
        message=f'Ваш код підтверждення: {confirmation_code}',
        from_email=EMAIL_YAMDB,
        recipient_list=(email,),
        fail_silently=False,
    )
