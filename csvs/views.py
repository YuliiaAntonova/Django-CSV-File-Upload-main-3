from django.shortcuts import render
from django.views.generic import TemplateView
from django_tables2 import SingleTableView

from .forms import CsvModelForm
from .models import Csv
import csv

from sales.models import Sale
from sales.tables import PersonTable


def handle(request, *args, **options):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, "r") as f_in:
            data = csv.reader(f_in)

            for i, row in enumerate(data):
                if i == 0:
                    pass
                else:
                    Sale.objects.create(
                        PLZ=row[17],
                        Summe=row[6],
                    )

            obj.activated = True
            obj.save()

    return render(request, 'csvs/upload.html', {'form': form})


class AboutView(TemplateView):
    template_name = 'about.html'


class aboutview(SingleTableView):
    model = Sale
    table_class = PersonTable
    template_name = 'people.html'
