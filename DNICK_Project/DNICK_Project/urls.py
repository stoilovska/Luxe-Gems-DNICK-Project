"""
URL configuration for DNICK_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from LuxeGems.views import home, card, rings, detail, bracelets, watches, charms, earrings, registry, login, add, \
    add_to_cart, delete_cart, payment, thanks
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('home/', home, name="home"),
                  path('card/', card, name="card"),
                  path('add-to-cart/<int:jewelry_id>/', add_to_cart, name='add_to_cart'),
                  path('rings/', rings, name="rings"),
                  path('jewelry/<int:jewelry_id>/', detail, name="detail"),
                  path('bracelets/', bracelets, name="bracelets"),
                  path('watches/', watches, name="watches"),
                  path('charms/', charms, name="charms"),
                  path('earrings/', earrings, name="earrings"),
                  path('registry/', registry, name="registry"),
                  path('login/', login, name="login"),
                  path('add/', add, name="add"),
                  path('deleteCard/', delete_cart, name="delete_cart"),
                  path('payment/', payment, name="payment"),
                  path('thanks/', thanks, name="thanks"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
