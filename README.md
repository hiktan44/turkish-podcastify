# Turkish Podcastify

This project is a Turkish podcast generation system based on Podcastfy.

## Features
- Generate podcasts from Turkish web content
- Convert text to speech in Turkish
- Support for multiple voices
- Automatic text processing

## Setup
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create .env file with your API keys:
```
OPENAI_API_KEY=your-key
GOOGLE_API_KEY=your-key
ELEVENLABS_API_KEY=your-key
```

## Usage
Run the main script:
```bash
python create_podcast.py
```

## Requirements
- Python 3.11+
- FFmpeg
- Required API keys (OpenAI, Google, ElevenLabs)
