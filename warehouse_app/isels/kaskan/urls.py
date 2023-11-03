from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('_index.urls')),
    path('isels/', include('isels.urls')),
    path('upload_center/', include('import_excel_db.urls')),
    path('in_out/', include('in_out.urls')),

    path('admin/', admin.site.urls),

]
