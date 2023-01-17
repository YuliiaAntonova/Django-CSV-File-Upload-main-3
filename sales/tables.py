import django_tables2 as tables
from .models import Sale


class PersonTable(tables.Table):
    class Meta:
        model = Sale
        template_name = "django_tables2/bootstrap.html"
        fields = ('order_number_ideal',
                  'order_number_shop',
                  'created_at',
                  'processed_at',
                  'status',
                  'currency',
                  'total_price_with_shipping',
                  'total_price_without_shipping',
                  'total_shipping',
                  'customer_email',
                  'customer_phone',
                  'shipping_address_address1',
                  'shipping_address_address2',
                  'shipping_address_city',
                  'shipping_address_country',
                  'shipping_address_given_name',
                  'shipping_address_family_name',
                  'shipping_address_zip',
                  'shipping_address_salutation',
                  'billing_address_address1',
                  'billing_address_address2',
                  'billing_address_city',
                  'billing_address_country',
                  'billing_address_given_name',
                  'billing_address_family_name',
                  'billing_address_zip',
                  'billing_address_salutation',
                  'fulfillment_carrier',
                  'fulfillment_type',
                  'fulfillment_transaction_code',
                  'fulfillment_options',
                  'payment_method',
                  'payment_transaction_id',
                  'merchant_id',
                  'merchant_name',
                  'total_item_price',
                  'item_price',
                  'former_price'
                  'price_range_amount',
                  'quantity',
                  'sku',
                  'title',
                  'delivery_time',
                  'voucher_code',
                  'refund_ids',
                  'refund_amounts',
                  'refund_statuses',
                  )
