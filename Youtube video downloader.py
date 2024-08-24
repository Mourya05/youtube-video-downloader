from pytube import YouTube

def download_youtube_video(url, path="."):
    try:
        yt = YouTube(url)

        stream = yt.streams.get_highest_resolution()

        print(f"Downloading '{yt.title}'...")
        stream.download(output_path=path)
        print(f"Download complete! Saved to {path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    video_url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the destination folder (leave blank for current directory): ")
    download_youtube_video(video_url, save_path if save_path else ".")
