from  django.urls import path

from .views import ShoppingCart, ShoppingCartUpdate, ShoppingCartDelete


urlpatterns = [
   path('cart-items/', ShoppingCart.as_view()),
   path('update-item/<int:id>', ShoppingCartUpdate.as_view()),
   path('delete-item/<int:id>', ShoppingCartDelete.as_view())
]