from unittest import TestCase

from spotifyapp.models import Artist, Song, Album
from spotifyapp.serializers import ArtistSerializer,  AlbumSerializer, SongSerializer

# class TestArtistSerializer(TestCase):
#     def setUp(self) -> None:
#         pass
#         # Artist.objects.create(
#         #     name="li",
#         #     yonalish="Rep",
#         #     description="afafwefssdggsgsf"
#         # )
#
#     # def test_artist(self):
#     #     a = Artist.objects.all()
#     #     malumot = ArtistSerializer(a, many=True)
#     #     self.assertTrue(malumot.data[0]["id"] == 1)
#     #     self.assertEqual(malumot.data[0]["id"], 1)
#
#     def test_validate_name(self):
#         artist = {
#             "id": 1,
#             "name": "M",
#             "yonalish": "Rep",
#             "description": "Repper"
#         }
#         ser = ArtistSerializer(data=artist)
#         #assert ser.is_valid() == False
#         self.assertFalse(ser.is_valid())
#         assert ser.errors['name'][0] == "Siz birdona harf kiritingiz"
#
#
#     def test_valid(self):
#         artist = {
#             "id": 1,
#             "name": "Miyagi",
#             "yonalish": "Rep",
#             "description": "Repper"
#         }
#         ser = ArtistSerializer(data=artist)
#         assert ser.is_valid() == True
#         self.assertTrue(ser.is_valid())
#
#




# class TestSongSerializer(TestCase):
#     def setUp(self) -> None:
#         pass
#
#
# #     def test_album(self):
# #         s = Album.objects.all()
# #         malumot = AlbumSerializer(s, many=True)
# #         assert malumot.data[0]["title"] == "Yamakasi"
# #         assert malumot.data[0]["date"] == "2022-01-31"
# #         assert malumot.data[0]["artist"] == 1
#
#
#
#     def test_validate_source(self):
#         song = {
#             "id": 1,
#             "title": "Yamakasi",
#             "duration": "00:02:15",
#             "source": "https://www.youtube.com/afasfssfa.AVI"
#         }
#         ser = SongSerializer(data=song)
#         assert ser.is_valid() == False
#         self.assertFalse(ser.is_valid())
#         assert ser.errors['source'][0] == "Bunaqa qo'shiq  formati yoq "
#         print(ser.errors)
#
#
#     def test_valid(self):
#         song = {
#             "id": 1,
#             "title": "Yamakasi",
#             "duration": "00:02:15",
#             "source": "https://www.youtube.com/afasfssfa.mp4"
#         }
#         ser = SongSerializer(data=song)
#         assert ser.is_valid() == True
#         self.assertTrue(ser.is_valid())
#

class TestArtstSerializer(TestCase):
    def setUp(self) -> None:
        pass


    def test_validate_image(self):
        image = {
            "id": 1,
            "name": "Miyagi",
            "yonalish": "Rep",
            "description": "Repper",
            "image": "https://www.youtube.com/afasfssfa.gpr"
        }
        ser = ArtistSerializer(data=image)
        assert ser.is_valid() == False
        self.assertFalse(ser.is_valid())
        assert ser.errors['image'][0] == "Bunaqa rasm formati yoq"
        print(ser.errors)


    def test_valid(self):
        image = {
            "id": 1,
            "name": "Miyagi",
            "yonalish": "Rep",
            "description": "Repper",
            "image": "https://www.youtube.com/afasfssfa.jpg"
        }
        ser = ArtistSerializer(data=image)
        assert ser.is_valid() == True
        self.assertTrue(ser.is_valid())

