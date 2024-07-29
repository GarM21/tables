from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, mixins
from .models import TableCell, TableRow, TableColumn
from .serializers import TableCellSerializer, TableRowSerializer, TableColumnSerializer
from .services import update_row_sum

class TableCellViewSet(viewsets.ModelViewSet):
    queryset = TableCell.objects.all()
    serializer_class = TableCellSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        update_row_sum(request.data['row'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        update_row_sum(request.data['row'])

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        row = instance.row.id
        self.perform_destroy(instance)
        update_row_sum(row)
        return Response(status=status.HTTP_204_NO_CONTENT)

class TableRowViewSet(viewsets.ModelViewSet):
    queryset = TableRow.objects.all()
    serializer_class = TableRowSerializer

class TableColumnViewSet(viewsets.ModelViewSet):
    queryset = TableColumn.objects.all()
    serializer_class = TableColumnSerializer