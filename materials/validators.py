from  django.core.exceptions import ValidationError
from urllib.parse import urlparse
from rest_framework import serializers

class YouTubeURLValidator:
    def __call__(self, value):
        if not isinstance(value, str):
            raise ValidationError('URL должен быть строкой.')

        parsed_url = urlparse(value)
        if parsed_url.netloc not in ['www.youtube.com', 'youtube.com']:
            raise ValidationError(f'URL должен быть с домена youtube.com, а не {parsed_url.netloc}.')