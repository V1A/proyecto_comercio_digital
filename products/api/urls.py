from django.urls import path

from products.api.views.general_views import MeasureUnitListAPIView, CategoryProductListAPIView, IndicadorListAPIView


urlpatterns = [
  path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
  path('indicator/', IndicadorListAPIView.as_view(), name = 'indicator'),
  path('category_product/', CategoryProductListAPIView.as_view(), name = 'category_product')
]
