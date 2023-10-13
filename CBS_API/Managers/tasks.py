from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
from celery import shared_task


@shared_task(routing_key="cbs")
def send_verification_email(email, code):
    """
    Sends a verification email to the specified email address with the provided verification code.

    Parameters:
        email (str): The email address to send the verification email to.
        code (str): The verification code.

    Returns:
        None
    """
    subject = "Mesika CBS Verification Code"
    message = f"Your verification code is: {code}"
    sender_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, sender_email, recipient_list)


# @shared_task(routing_key="cbs")
# def send_password_customer_email(user_id):
#     from customers.models import Customers

#     try:
#         customer = Customers.objects.get(pk=user_id)
#     except Customers.DoesNotExist:
#         return

#     token = default_token_generator.make_token(customer)
#     customer.password_reset_token = token
#     customer.password_reset_token_created_at = timezone.now()
#     customer.save()
#     reset_link = f"http://192.168.68.12:9000/customer/password-reset/{token}/"
#     message = f'Click on the <a href="{reset_link}">link</a> to reset your password.'

#     send_mail(
#         "Mesika CBS Password Reset",
#         message,
#         settings.DEFAULT_FROM_EMAIL,
#         [customer.email],
#         fail_silently=False,
#         html_message=message,
#     )


@shared_task(routing_key="cbs")
def send_password_manager_email(user_id):
    from Managers.models import Managers

    try:
        manager = Managers.objects.get(pk=user_id)
    except Managers.DoesNotExist:
        return

    token = default_token_generator.make_token(manager)
    manager.password_reset_token = token
    manager.password_reset_token_created_at = timezone.now()
    manager.save()
    reset_link = f"http://192.168.68.12:9000/staffs/password-reset/confirm/{token}/"
    message = f'Click on the <a href="{reset_link}">link</a> to reset your password.'

    send_mail(
        "Mesika CBS Password Reset",
        message,
        settings.DEFAULT_FROM_EMAIL,
        [manager.email],
        fail_silently=False,
        html_message=message,
    )


@shared_task(routing_key="cbs")
def send_user_password(email, password):
    """
    Sends an email to a user with their password and email address.

    Parameters:
        email (str): The email address of the user.
        password (str): The password of the user.

    Returns:
        None
    """
    subject = "Mesika CBS Credentials"
    link = "http://localhost:8000/"
    message = f"Your account credentials are:\npassword: {password}\nemail: {email}\nlink: {link}"
    sender_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, sender_email, recipient_list)
