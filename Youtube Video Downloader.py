from tkinter import *
import yt_dlp

# Create main application window
root = Tk()
root.geometry('600x400')
root.resizable(0, 0)
root.title("YouTube Video Downloader")

# App Title Label
Label(root, text='YouTube Video Downloader', font='arial 20 bold', fg='red').pack(pady=20)

# Instruction Label
Label(root, text='Paste the link of the YouTube video below:', font='arial 14').pack(pady=10)

# Enter Link
link = StringVar()
Entry(root, width=50, textvariable=link, font='arial 12').pack(pady=10)

# Function to Download Video
def Downloader():
    status_label.config(text='Downloading...', fg='blue')  # Update status label
    root.update()  # Refresh UI to show progress
    try:
        # yt-dlp download options
        ydl_opts = {
            'format': 'best',  # Downloads the best video + audio stream
            'outtmpl': '%(title)s.%(ext)s',  # Saves with the video title as filename
        }
        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([str(link.get())])

        status_label.config(text='Downloaded Successfully!', fg='green')  # Success message
    except Exception as e:
        status_label.config(text='Error: Unable to download', fg='red')  # Error message
        print(f"Error: {e}")  # Debugging: Print full error details in console

# Download Button
Button(root, text='Download Video', font='arial 15 bold', bg='black', fg='white',
       command=Downloader, padx=10, pady=5).pack(pady=20)

# Status Label
status_label = Label(root, text='', font='arial 12')
status_label.pack(pady=10)

# Run the application
root.mainloop()

#is it running?????
