from django.urls import path
from users.api.api import user_api_view, user_detail_api_view

urlpatterns = [
  path('usuario/', user_api_view, name = 'usuario_api_view'),
  path('usuario/<int:id>', user_detail_api_view, name = 'usuario_detail_api_view')
]
