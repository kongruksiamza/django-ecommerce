"""djangoworkshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from django.conf.urls.static import static
from django.conf import settings

    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('category/<slug:category_slug>',views.index,name="product_by_category"),
    path('product/<slug:category_slug>/<slug:product_slug>',views.productPage,name='productDetail'),
    path('cart/add/<int:product_id>',views.addCart,name="addCart"),
    path('cartdetail/',views.cartdetail,name="cartdetail"),
    path('cart/remove/<int:product_id>',views.removeCart,name="removeCart"),
    path('account/create',views.signUpView,name="signUp"),
    path('account/login',views.signInView,name="signIn"),
    path('account/logout',views.signOutView,name="signOut"),
    path('search/',views.search,name='search'),
    path('orderHistory/',views.orderHistory,name="orderHistory"),
    path('order/<int:order_id>',views.viewOrder,name="orderDetails"),
    path('cart/thankyou',views.thankyou,name='thankyou')
]

# product/fashion/shoes-men
# product/toys/lego

if settings.DEBUG :
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

