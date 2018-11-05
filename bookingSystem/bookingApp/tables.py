from .models import Vehicle
import django_tables2 as tables


class SeatTable(tables.Table):
    class Meta:
        models = Vehicle
        # fields=("seatType","seatPrice")
        template_name = 'django_tables2/bootstrap4.html'
