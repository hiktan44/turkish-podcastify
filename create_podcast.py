from podcastfy.client import generate_podcast
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API anahtarlarını ayarla
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
os.environ['GEMINI_API_KEY'] = os.getenv('GOOGLE_API_KEY')
os.environ['ELEVENLABS_API_KEY'] = os.getenv('ELEVENLABS_API_KEY')

def create_podcast():
    url = 'https://www.webtekno.com/apple-vision-pro-2024-yilinin-ilk-ceyreginde-satisa-sunulacak-h138663.html'
    
    try:
        print('Podcast oluşturuluyor...')
        print('URL:', url)
        
        result = generate_podcast(
            urls=[url]
        )
        
        print('Podcast oluşturuldu:', result)
        return result
        
    except Exception as e:
        print('Hata:', str(e))
        return None

if __name__ == '__main__':
    output = create_podcast()
    if output:
        print('\nPodcast\'i dinlemek için:')
        print(f"afplay '{output}'")