# YouTube MP3 Downloader

A small Python project I made to download audio from YouTube videos and convert it to MP3.

## Features

- Downloads audio from a YouTube video
- Converts audio to MP3 at 192 kbps
- Saves the file using the video's title
- Downloads only the selected video, not the entire playlist
- Works from the terminal with a pasted YouTube URL

## Requirements

- Python 3.10+
- [FFmpeg](https://ffmpeg.org/)
- [Node.js](https://nodejs.org/)

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

Make sure FFmpeg and Node.js are installed and available in your system PATH.

## Usage

Run the program:

```bash
python main.py
```

Paste the YouTube video URL when prompted. The resulting MP3 file will be saved in the current folder.

## Cost

Free to use.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
