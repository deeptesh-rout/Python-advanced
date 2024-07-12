from datetime import UTC, datetime

import requests


def download_video(url: str) -> bytes:
    base_url = "https://downloadgram.net/wp-json/wppress/video-downloader/video?url="
    video_url = requests.get(base_url + url, timeout=10).json()[0]["urls"][0]["src"]
    return requests.get(video_url, timeout=10).content


if __name__ == "__main__":
    url = input("Enter Video/IGTV url: ").strip()
    file_name = f"{datetime.now(tz=UTC).astimezone():%Y-%m-%d_%H:%M:%S}.mp4"
    with open(file_name, "wb") as fp:
        fp.write(download_video(url))
    print(f"Done. Video saved to disk as {file_name}.")
