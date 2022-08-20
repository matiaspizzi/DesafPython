from django.contrib import admin
from django.urls import path
from Portfolio.views import home
from AppModels.views import relatives

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('relatives/', relatives)
]
