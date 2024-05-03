from django.http import HttpResponse
from django_excel_to_model.views import ExcelToModelMixin
from .models import UserProfile

class ExportToExcelView(ExcelToModelMixin):
    model = UserProfile
    fields = '_all_'

    def get(self, request, *args, **kwargs):
        queryset = self.model.objects.all()
        return self.to_excel(queryset)