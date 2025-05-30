from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import Profile

@receiver(user_signed_up)
def save_user_profile_on_signup(sender, request, user, **kwargs):
    user.profile.ip_address = request.META.get('REMOTE_ADDR')
    user.profile.save() 