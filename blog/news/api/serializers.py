from rest_framework import serializers
from ..models import News



class NewsSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='news:detail'
    )
    class Meta:
        model = News
        fields = ['author','title', 'creation_date', 'vote','url']
