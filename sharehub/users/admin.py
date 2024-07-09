import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import CustomUser

admin.site.register(CustomUser)


def export_users_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    writer.writerow(["username", "email", "first_name", "last_name"])
    users = queryset.values_list("username", "email", "first_name", "last_name")
    for user in users:
        writer.writerow(user)
    return response
