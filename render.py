from django.shortcuts import render
from .forms import ExcelUploadForm
from .models import YourModel

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['c:\Users\User\Desktop\django_excel_to_model.models.xlsx']
            imported_data = YourModel().from_excel(excel_file)
            for data in imported_data:

                YourModel.objects.create(**data)
            return render(request, 'Вход.html')
    else:
        form = ExcelUploadForm()
    return render(request, 'вход.html', {'form': form})