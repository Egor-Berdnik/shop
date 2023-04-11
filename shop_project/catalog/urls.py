from django.urls import path
from catalog.views import ProducersListView, DiscountsListView, PromocodesListView, \
    ProductsListView, CategoriesListView, CategoryProductsView, ProducerProductView, DiscountProductsView, BasketView
# CategoryView

urlpatterns = [

    #Client
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('categories/<int:category_id>/', CategoryProductsView.as_view(), name='category-products'),

    path('producers/', ProducersListView.as_view(), name='producer'),
    path('producers/<int:producer_id>/', ProducerProductView.as_view(), name='producer-products'),

    path('discounts/', DiscountsListView.as_view(), name='discount'),
    path('discounts/<int:discount_id>/', DiscountProductsView.as_view(), name='discount-products'),

    path('promocodes/', PromocodesListView.as_view(), name='promocodes'),
    path('products/', ProductsListView.as_view(), name='products'),

    #Customer
    path('cart/', BasketView.as_view(), name='user-basket')
]
