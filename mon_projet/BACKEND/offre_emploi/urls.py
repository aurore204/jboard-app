from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('offre_emplois/', include('offre_emplois.urls')),

]