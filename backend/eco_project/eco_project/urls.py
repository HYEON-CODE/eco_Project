from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/mission/', include("Mission.urls")),
    path('api/member/', include("member.urls")),
    path('api/mileage/', include("mileage.urls")),
    path('api/news/', include("news.urls")),
    path('api/stock/', include("stock.urls")),
]