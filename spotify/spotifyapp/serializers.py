from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from spotifyapp.models import Artist, Song, Album


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

    def validated_name(self, qiymat):
        if len(qiymat) <= 1:
            raise ValidationError(detail="Siz birdona harf kiritingiz")
        return qiymat

    def validate_image(self, qiymat):
        if not qiymat.endswith(".jpg") or qiymat.endswith(".png"):
            raise ValidationError(detail="Bunaqa rasm formati yoq")
        return qiymat

class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

    def validate_source(self, qiymat ):
        if not qiymat.endswith(".mp4"):
            raise ValidationError(detail="Bunaqa qo'shiq  formati yoq ")
        return qiymat


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

    def validate_cover(self, qiymat ):
        if not qiymat.endswith(".mp4"):
            raise ValidationError(detail="Bunaqa qo'shiq  formati yoq ")
        return qiymat

