import csv
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from monitoring.models import Device,Reading
class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('csv_file')
    def handle(self,*args,**opts):
        with open(opts['csv_file']) as f:
            for r in csv.DictReader(f):
                d,_=Device.objects.get_or_create(name=r['device_name'])
                Reading.objects.get_or_create(
                    device=d,timestamp=parse_datetime(r['timestamp']),
                    defaults={'power':float(r['power']),'status':r['status']}
                )
        self.stdout.write(self.style.SUCCESS('Imported'))
