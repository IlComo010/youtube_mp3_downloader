# YouTube MP3 Downloader

A simple Python tool that downloads audio from a YouTube video and converts it to MP3 using yt-dlp and FFmpeg.

## Features

- Download audio from a YouTube video
- Convert audio to MP3
- Set the output quality to 192 kbps
- Use the video title as the output filename
- Download a single video, even when the URL contains playlist parameters

## Requirements

- Python 3.10 or newer
- FFmpeg
- Node.js (for the configured JavaScript runtime)

## Installation

Clone the repository:

```bash
git clone https://github.com/IlComo010/youtube_mp3_downloader.git
cd youtube_mp3_downloader
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Make sure FFmpeg and Node.js are installed and available on your system PATH.

## Usage

Run the program:

```bash
python main.py
```

Paste the YouTube URL when prompted.

The resulting MP3 file is saved in the current working directory.

## License

No license has been specified yet.