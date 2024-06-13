from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _


def send_post_notification(user, post):
    """
    Send an email to the user with a notification of a new post.
    """
    subject = _("New post notification")
    message = f"Hello {user.first_name},\n\nA new post has been added to the site.\n\nTitle: {post.title}\n\nContent: {post.content}\n\n"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
    return None

def confirm_email(user):
    """
    Send an email to the user to confirm their email.
    """
    subject = _("Confirm your email")
    message = f"Hello {user.first_name},\n\nPlease confirm your email address by clicking the link below.\n\n{user.get_confirmation_url()}\n\n"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
    return None