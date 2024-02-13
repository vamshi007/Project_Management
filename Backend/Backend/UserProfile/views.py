"""
    UserProfile views
"""

from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile


@csrf_exempt
def create_user(request):
    """
    :param request:
    :return:
    """
    if request.method == "POST":
        username = request.POST.get("username")
        passcode = request.POST.get("passcode")
        email_ID = request.POST.get("email_ID")
        location = request.POST.get("location")
        extension_line = request.POST.get("extension_line")

        print(username, passcode, email_ID, location, extension_line)

        if User.objects.filter(username=username).exists():
            print("exist")
        else:
            print("not exist")

        # Create a new User instance
        user = User.objects.create_user(
            username=username, email=email_ID, password=passcode
        )
        group, created = Group.objects.get_or_create(name="Managers")
        print(group)
        user.groups.add(group)
        user.save()
        # Create a UserProfile instance with additional fields
        user_profile = UserProfile(
            user=user,
            email_ID=email_ID,
            location=location,
            extension_line=extension_line,
        )
        user_profile.save()
        return HttpResponse("account created")
