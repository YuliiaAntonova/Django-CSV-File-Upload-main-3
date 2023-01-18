import django_tables2 as tables
from .models import Sale


class PersonTable(tables.Table):
    class Meta:
        model = Sale
        template_name = "django_tables2/bootstrap.html"
        fields = (
                  'PLZ',
                  'Summe',
                  )
