from .models import TableCell, TableRow
from django.db.models import Sum

def update_row_sum(row):
    sum_value = TableCell.objects.filter(row__id=row).aggregate(sum_value=Sum('value'))
    TableRow.objects.filter(id=row).update(sum_value=sum_value['sum_value'])