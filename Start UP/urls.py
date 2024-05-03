from django.urls import path
from .views import registration_view, ExportToExcelView

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('export/', ExportToExcelView.as_view(), name='file:///C:/Users/User/AppData/Local/Temp/Rar$EXa14288.41501/rest12/index.html'),
]