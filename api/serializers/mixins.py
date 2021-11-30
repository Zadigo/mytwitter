from feed.utils import text_analyzer
from feed.models import Hashtag

class SerializerMixin:
    def _create_mentions_and_hashtags(self, obj, text):
        mentions, hashtags, _ = text_analyzer(text)
        hashtag_objs = []
        for hashtag in hashtags:
            if hashtag.startswith('#'):
                value_to_add = hashtag.split('#')[-1]
                new_hashtag, created = Hashtag.objects.get_or_create(name=value_to_add)
                hashtag_objs.append(new_hashtag)
        obj.hashtags.add(*hashtag_objs)
        return obj
    
    def save(self, request, **kwargs):
        """Implements a request parameter on the save
        method for the Serializer"""
        
        validated_data = {**self.validated_data, **kwargs}

        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(request, validated_data)

        if self.instance is None:
            raise ValueError('Instance is was not created')

        return self.instance
    
