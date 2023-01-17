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
                        order_number_ideal=row[0],
                        order_number_shop=row[1],
                        created_at=row[2],
                        processed_at=row[3],
                        status=row[4],
                        currency=row[5],
                        total_price_with_shipping=row[6],
                        total_price_without_shipping=row[7],
                        total_shipping=row[8],
                        customer_email=row[9],
                        customer_phone=row[10],
                        shipping_address_address1=row[11],
                        shipping_address_address2=row[12],
                        shipping_address_city=row[13],
                        shipping_address_country=row[14],
                        shipping_address_given_name=row[15],
                        shipping_address_family_name=row[16],
                        shipping_address_zip=row[17],
                        shipping_address_salutation=row[18],
                        billing_address_address1=row[19],
                        billing_address_address2=row[20],
                        billing_address_city=row[21],
                        billing_address_country=row[22],
                        billing_address_given_name=row[23],
                        billing_address_family_name=row[24],
                        billing_address_zip=row[25],
                        billing_address_salutation=row[26],
                        fulfillment_carrier=row[27],
                        fulfillment_type=row[28],
                        fulfillment_transaction_code=row[29],
                        fulfillment_options=row[30],
                        payment_method=row[31],
                        payment_transaction_id=row[32],
                        merchant_id=row[33],
                        merchant_name=row[34],
                        total_item_price=row[35],
                        item_price=row[36],
                        former_price=row[37],
                        price_range_amount=row[38],
                        quantity=row[39],
                        sku=row[40],
                        title=row[41],
                        delivery_time=row[42],
                        voucher_code=row[43],
                        refund_ids=row[44],
                        refund_amounts=row[45],
                        refund_statuses=row[46],
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
