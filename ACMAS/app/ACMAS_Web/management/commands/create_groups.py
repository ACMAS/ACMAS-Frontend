import logging

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

GROUPS = ["Moderators", "APO"]
MODELS = ["moderationqueue", "uploadedfile"]
PERMISSIONS = ["view", "add", "change", "delete"]


class Command(BaseCommand):
    help = "Creates read only default permission groups for users"

    def handle(self, *args, **options):
        for group in GROUPS:
            new_group, created = Group.objects.get_or_create(name=group)
            for model in MODELS:
                for permission in PERMISSIONS:
                    name = "Can {} {}".format(permission, model)
                    print("Creating {}".format(name))

                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning(
                            "Permission not found with name '{}'.".format(name)
                            )
                        continue

                    new_group.permissions.add(model_add_perm)

        print("Created default group and permissions.")
