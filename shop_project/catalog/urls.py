from django.urls import path
from catalog.views import ProducersListView, DiscountsListView, PromocodesListView, \
    ProductsListView, CategoriesListView, CategoryProductsView, ProducerProductView
# CategoryView

urlpatterns = [
    path('categories/', CategoriesListView.as_view()),
    path('categories/<int:category_id>/', CategoryProductsView.as_view(), name='category-products'),

    path('producers/', ProducersListView.as_view()),
    path('producers/<int:producer_id>/', ProducerProductView.as_view(), name='producer-products'),

    path('discounts/', DiscountsListView.as_view()),
    path('promocodes/', PromocodesListView.as_view()),
    path('products/', ProductsListView.as_view())
]


