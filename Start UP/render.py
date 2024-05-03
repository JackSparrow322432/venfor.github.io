from django.shortcuts import render
from .forms import ExcelUploadForm
from .models import YourModel
from django_excel_to_model.models import ImportMixin

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            imported_data = ImportMixin().from_excel(excel_file)
            for data in imported_data:
                # Создание объектов модели Django и сохранение их в базе данных
                YourModel.objects.create(**data)
            return render(request, 'success.html')
    else:
        form = ExcelUploadForm()
    return render(request, 'upload.html', {'form': form})