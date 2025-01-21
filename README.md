# 🎥 YouTube Video Downloader 📥

A simple and user-friendly desktop application to download YouTube videos with just one click! Built using Python and `yt-dlp`, this tool allows you to easily save your favorite videos locally for offline viewing.

---

## ✨ Features
- 📌 Download YouTube videos in the **best available quality** (video + audio combined).
- 🖱️ Simple and clean graphical user interface (GUI) built with **Tkinter**.
- 🔍 Automatically fetches video titles and saves them as filenames.
- 🛠️ Supports a wide range of YouTube video formats and resolutions.

---

## 🖥️ Application Preview

The app has a clean and modern UI with a centered layout:
- Paste the video link in the input box.
- Click the "Download Video" button.
- View status messages like "Downloading..." or "Downloaded Successfully!".

---

## 🛠️ Installation

Follow these steps to set up and run the application:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/youtube-video-downloader.git
cd youtube-video-downloader
```

### 2. Install Dependencies
Make sure you have Python installed on your system. Then, install the required packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python youtube_vid_dl.py
```

---

## 🚀 How to Use

1. Open the application.
2. Copy the YouTube video link you want to download.
3. Paste the link into the input field.
4. Click the **"Download Video"** button.
5. Wait for the status to show **"Downloaded Successfully!"** 🎉

---

## 📋 Requirements
- Python 3.7 or later
- `yt-dlp` for downloading videos
- Standard Tkinter library (pre-installed with Python)

---

## 🗂️ Project Structure
```plaintext
youtube-video-downloader/
│
├── youtube_vid_dl.py   # Main application script
├── requirements.txt    # Dependencies for the project
├── README.md           # Project documentation
```

---

## 🔧 Troubleshooting

If you encounter issues while downloading videos:
1. Ensure you have a stable internet connection.
2. Update the `yt-dlp` library to the latest version:
   ```bash
   pip install --upgrade yt-dlp
   ```
3. Verify that the YouTube link is valid and accessible.

---

## 💡 Future Enhancements
- Add support for downloading only audio files (e.g., MP3).
- Allow users to choose the video resolution before downloading.
- Include a progress bar for real-time download tracking.
