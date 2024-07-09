# # Create your views here.
# from django.conf import settings
# from django.core.mail import EmailMessage
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from django.utils.translation import gettext_lazy as _

# from sharehub.users.models import CustomUser
# from sharehub.users.token import account_activation_token


# def send_email_verification(user: CustomUser) -> None:
#     """
#     Send an email to the user with a verification link.
#     """
#     uid = urlsafe_base64_encode(force_bytes(user.pk))
#     token = account_activation_token.make_token(user)
#     domain = settings.DOMAIN
#     url = f"{domain}/users/activate/{uid}/{token}/"
#     subject = _("Activate your account")
#     message = _("Please activate your account by clicking the link below.")
#     email = EmailMessage(subject, message, to=[user.email])
#     email.send()
#     return None


# def send_email_verification_async(user: CustomUser) -> None:
#     """
#     Send an email to the user with a verification link asynchronously.
#     """
#     thread = Thread(target=send_email_verification, args=(user,))
#     thread.start()
#     return None


# def send_email_password_reset(user: CustomUser) -> None:
#     """
#     Send an email to the user with a password reset link.
#     """
#     uid = urlsafe_base64_encode(force_bytes(user.pk))
#     token = account_activation_token.make_token(user)
#     domain = settings.DOMAIN
#     url = f"{domain}/users/reset/{uid}/{token}/"
#     subject = _("Reset your password")
#     message = _("Please reset your password by clicking the link below.")
#     email = EmailMessage(subject, message, to=[user.email])
#     email.send()
#     return None
