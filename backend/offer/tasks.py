from celery import shared_task
from django.core.mail import send_mail
from internet_auction.settings import EMAIL_HOST_USER,EMAIL_HOST_PASSWORD


@shared_task
def send_offer_rejection(email):
    title = f'Dear {email}'
    message = 'Your offer waw rejected'
    print(EMAIL_HOST_PASSWORD)
    mail_sent = send_mail(title, message, EMAIL_HOST_USER, [email, ])
    return mail_sent
