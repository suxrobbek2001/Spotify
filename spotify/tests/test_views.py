from unittest import TestCase
from django.test import Client
from spotifyapp.models import Artist, Song, Album
from spotifyapp.serializers import ArtistSerializer,  AlbumSerializer, SongSerializer

class TestArtstViews(TestCase):
    def setUp(self) -> None:
        self.cl = Client()

    def test_get_artist(self):
        natija = self.cl.get("/artist/1/")
        assert natija.status_code == 200
        m = natija.data
        print(m)
        self.assertTrue(len(m) !=0)
        self.assertEqual(m["name"], "MiyaGi & Andy Panda")
        self.assertEqual(m['yonalish'], 'Hip-Hop/Rep')


    def test_get_album(self):
        natija = self.cl.get("/album/1/")
        assert natija.status_code == 200
        m = natija.data
        print(m)
        self.assertTrue(len(m) !=0)
        self.assertEqual(m["title"], "Yamakasi")
        self.assertEqual(m['date'], '2022-01-31')
        self.assertEqual(m['artist'], 1)

    def test_get_song(self):
        natija = self.cl.get("/song/1/")
        assert natija.status_code == 200
        m = natija.data
        print(m)
        self.assertTrue(len(m) !=0)
        self.assertEqual(m["title"], "MiyaGi & Andy Panda - Yamakasi")
        self.assertEqual(m['duration'], '00:04:10')
        self.assertEqual(m['album'], 1)

