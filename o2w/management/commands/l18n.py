from django.core.management.base import BaseCommand, CommandError
import os

class Command(BaseCommand):
    args = '<langs>'
    help = 'Update the translations'

    def handle(self, *args, **options):
                
        try:
            os.mkdir("app/locale", 0777)
        except:
            pass

        for lang in args:
            try:
                os.mkdir("app/locale/%s" % lang, 0777)
            except:
                pass
                
        ret = os.system("cd app; django-admin makemessages --all")

