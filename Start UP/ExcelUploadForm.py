import pandas as pd
from django.shortcuts import render
from .forms import ExcelUploadForm
from .models import YourModel

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)
            for index, row in df.iterrows():
                YourModel.objects.create(**row.to_dict())
            return render(request, 'success.html')
    else:
        form = ExcelUploadForm()
    return render(request, 'upload.html', {'form': form})