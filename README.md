# 🎙️ Turkish Podcastify

Türkçe web içeriklerini otomatik olarak podcast'e dönüştüren bir araç.

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

## 📖 İçindekiler
- [Özellikler](#özellikler)
- [Gereksinimler](#gereksinimler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Konfigürasyon](#konfigürasyon)
- [SSS](#sss)
- [Sorun Giderme](#sorun-giderme)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## ✨ Özellikler
- 🌐 Türkçe web sitelerinden otomatik içerik çıkarma
- 🗣️ Doğal dil işleme ile metni konuşma diline çevirme
- 🎧 Yüksek kaliteli ses sentezi
- 📱 Farklı ses tonları ve konuşma stilleri
- 📝 Otomatik transkript oluşturma
- 🔄 Batch işleme desteği

## 🛠️ Gereksinimler
- Python 3.11 veya üstü
- FFmpeg
- API Anahtarları:
  - OpenAI API
  - Google Cloud API
  - ElevenLabs API

## ⚙️ Kurulum

1. Repository'yi klonlayın:
```bash
git clone https://github.com/hiktan44/turkish-podcastify.git
cd turkish-podcastify
```

2. Python sanal ortamı oluşturun:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac için
# veya
venv\\Scripts\\activate  # Windows için
```

3. Gereksinimleri yükleyin:
```bash
pip install -r requirements.txt
```

4. .env dosyasını oluşturun:
```bash
cp .env.example .env
```

5. API anahtarlarınızı .env dosyasına ekleyin:
```env
OPENAI_API_KEY=your-openai-key
GOOGLE_API_KEY=your-google-key
ELEVENLABS_API_KEY=your-elevenlabs-key
```

## 🚀 Kullanım

### Basit Kullanım
```python
from podcastfy.client import generate_podcast

# Tek bir URL'den podcast oluşturma
url = "https://example.com/article"
result = generate_podcast(urls=[url])
```

### İleri Düzey Kullanım
```python
# Birden fazla URL ile podcast oluşturma
urls = [
    "https://example.com/article1",
    "https://example.com/article2"
]

result = generate_podcast(
    urls=urls,
    config={
        'style': 'conversational',
        'voice': 'tr-TR'
    }
)
```

## ⚙️ Konfigürasyon

### Ses Ayarları
| Parametre | Açıklama | Varsayılan Değer |
|-----------|----------|------------------|
| style | Konuşma stili | 'conversational' |
| voice | Ses tonu | 'tr-TR' |
| speed | Konuşma hızı | 1.0 |

### Çıktı Formatları
- MP3
- WAV
- OGG

## 📘 SSS

### S: API anahtarlarını nereden alabilirim?
C: Her servis için adımlar:
- OpenAI: https://platform.openai.com/api-keys
- Google Cloud: https://console.cloud.google.com/
- ElevenLabs: https://elevenlabs.io/docs/api-reference/quick-start

### S: FFmpeg kurulumu nasıl yapılır?
C: İşletim sistemine göre kurulum:
- Mac: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`
- Windows: [FFmpeg İndirme Sayfası](https://ffmpeg.org/download.html)

## 🔧 Sorun Giderme

### Genel Hatalar ve Çözümleri
1. ModuleNotFoundError
```bash
pip install -r requirements.txt --upgrade
```

2. FFmpeg Hatası
```bash
# FFmpeg'in kurulu olduğunu kontrol edin
ffmpeg -version
```

## 👥 Katkıda Bulunma
1. Fork yapın
2. Feature branch oluşturun
3. Değişikliklerinizi commit edin
4. Branch'inizi push edin
5. Pull Request oluşturun

## 📄 Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.

## 📞 İletişim
- GitHub Issues
- Email: [adresiniz@example.com]

## 🙏 Teşekkürler
Bu proje aşağıdaki açık kaynak projeleri kullanmaktadır:
- [Podcastfy](https://github.com/souzatharsis/podcastfy)
- [FFmpeg](https://ffmpeg.org/)
- [Python-dotenv](https://github.com/theskumar/python-dotenv)
