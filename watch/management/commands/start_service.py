from django.core.management.base import BaseCommand
import time
def Work():
    from watch.views import CheckCLI 
    while True:
        CheckCLI()
        time.sleep(10)
        
class Command(BaseCommand):
    def handle (*args,**kwargs):
        print ("Starting service messaging.")
        Work()