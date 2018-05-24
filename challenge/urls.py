from django.urls import path


from .views import list_all

urlpatterns = [
    path('list/', list_all),
]