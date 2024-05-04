from django.http import HttpResponse
from .models import UserProfile, ExcelToModelMixin

class ExportToExcelView(ExcelToModelMixin):
    model = UserProfile
    fields = '_all_'

    def get(self, request, *args, **kwargs):
        queryset = self.model.objects.all()
        return self.to_excel(queryset)