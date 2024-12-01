from podcastfy.client import generate_podcast
import pytest
import os

def test_podcast_generation():
    url = 'https://www.webtekno.com/apple-vision-pro-2024-yilinin-ilk-ceyreginde-satisa-sunulacak-h138663.html'
    result = generate_podcast(urls=[url])
    assert result is not None
    assert os.path.exists(result)