

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from shopkart import views

urlpatterns = [

    # path('',views.home,name='home'),
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProdCatDetail, name='ProdCatDetail')
]
