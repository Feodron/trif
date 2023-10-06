from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import serve, static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('main.urls')),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('orders/', include('orders.urls')),
    re_path(
        r"^static/(?P<path>.*)$",
        serve,
        {"document_root": settings.STATICFILES_DIRS[0]}
        )
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
