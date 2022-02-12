from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from spotifyapp.models import Artist, Song, Album

from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["name", "yonalish"]

    def get_queryset(self):
        artists = Artist.objects.all()
        soz = self.request.query_params.get("search")
        if soz is not None:
            artists = Artist.objects.annotate(
                similarity=TrigramSimilarity("name", soz)
            ).filter(similarity__gte=0.4).order_by("-similarity")
        return artists


    @action(detail=True, methods=['GET'])
    def albums(self, request, *args, **kwargs):
        artist = self.get_object()
        al = Album.objects.filter(artist=artist)
        ser = AlbumSerializer(al, many=True)
        return Response(ser.data)

    # @action(detail=True, methods=['GET', 'POST'])
    # def album(self, request, *args, **kwargs):
    #     artist = self.get_object()
    #     al = request.data
    #     ser = AlbumSerializer(data=al, many=True)
    #     if ser.is_valid():
    #         ser.save()
    #     return Response(ser.data)


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [OrderingFilter, ]
    ordering_fields = ["date", ]


    @action(detail=True, methods=['GET'])
    def songs(self, request, *args, **kwargs):
        album = self.get_object()
        ab = Song.objects.filter(album=album)
        ser = SongSerializer(ab, many=True)
        return Response(ser.data)

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [OrderingFilter, ]
    ordering_fields = ["duration", ]

    @action(detail=True, methods=['GET'])
    def album(self, request, *args, **kwargs):
        song = self.get_object()
        al = Album.objects.filter(id=song.album.id)
        ser = AlbumSerializer(al, many=True)
        return Response(ser.data)