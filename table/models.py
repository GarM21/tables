from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver



class TableRow(models.Model):
    sum_value = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"Row {self.id}, Sum_value {self.sum_value}"
    

class TableColumn(models.Model):
    def __str__(self):
        return f"Column {self.id}"
    

class TableCell(models.Model):
    row = models.ForeignKey(TableRow, related_name='cells', on_delete=models.CASCADE)
    column = models.ForeignKey(TableColumn, related_name='cells', on_delete=models.CASCADE)
    value = models.FloatField(null=True)

    class Meta:
        unique_together = ('row', 'column')

    def __str__(self):
        return f"Row: {self.row.id}, Column: {self.column.id}, Value: {self.value}"
