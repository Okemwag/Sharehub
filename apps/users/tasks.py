from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import gettext_lazy as _
from celery import shared_task

from .models import CustomUser


# send email for account activation
@shared_task
def send_email_verification(user_id: int) -> None:
    """
    Send an email to the user with a verification link.
    """
    user = CustomUser.objects.get(id=user_id)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    domain = settings.DOMAIN
    url = f"{domain}/users/activate/{uid}/{token}/"
    subject = _("Activate your account")
    message = _("Please activate your account by clicking the link below.")
    email = EmailMessage(subject, message, to=[user.email])
    email.send()
    return None


