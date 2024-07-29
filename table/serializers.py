from rest_framework import serializers
from .models import TableCell, TableRow, TableColumn

class TableCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableCell
        fields = ['id', 'row', 'column', 'value']

class TableRowSerializer(serializers.ModelSerializer):
    cells = TableCellSerializer(many=True, read_only=True)

    class Meta:
        model = TableRow
        fields = ['id', 'sum_value', 'cells']

class TableColumnSerializer(serializers.ModelSerializer):
    cells = TableCellSerializer(many=True, read_only=True)

    class Meta:
        model = TableColumn
        fields = ['id', 'cells']