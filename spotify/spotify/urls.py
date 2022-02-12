from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view

from spotifyapp.views import ArtistViewSet, AlbumViewSet, SongViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Spotify clone API",
      default_version='v1',
      description="Spotify clone versiyasi",
      contact=openapi.Contact("Sukhrobbek Mukhammadjonov <surobbekmuxammadjonov2gmail.com>, <+998993930242>"),
   ),
   public=True,
)



r = DefaultRouter()
r.register("artist", ArtistViewSet)
r.register("album", AlbumViewSet)
r.register("song", SongViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(r.urls)),
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="swagger-doc"),
    path('doc/', schema_view.with_ui("redoc", cache_timeout=0), name="redoc-doc"),

]

