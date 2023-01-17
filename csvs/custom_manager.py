
from django.utils import formats

from sales import models


class CustomManager(models.Sale):
    def custom_update_or_create(self,*args, **kwargs):
        date_time_value = kwargs.pop('date', None)
        if date_time_value:
            kwargs['date'] = self.get_date_value(date_time_value)
        return super(CustomManager, self).create(*args, **kwargs)

    def get_date_value(self, value):
         input_formats = [
            '%d-%m-%y %H:%M',
            '%d-%y-%m %H:%M',
            '%m-%d-%y %H:%M',
            '%m-%y-%d %H:%M',
            '%y-%m-%d %H:%M',
            '%y-%d-%m %H:%M',
            '%d/%m/%y %H:%M',
            '%d/%y/%m %H:%M',
            '%m/%d/%y %H:%M',
            '%m/%y/%d %H:%M',
            '%y/%m/%d %H:%M',
            '%y/%d/%m %H:%M'
         ]

         for format in input_formats:
            try:
                return self.strptime(value, format)
            except (ValueError, TypeError):
                continue

    def strptime(self, value, format):
        return datetime.datetime.strptime(value, format)