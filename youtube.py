from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    if "youtu.be" in url:
        return url.split("/")[-1]
    elif "youtube.com" in url:
        return url.split("v=")[-1].split("&")[0]


def get_video_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(
        video_id=video_id, languages=["ru"]
    )
    full_text = " ".join([item["text"] for item in transcript])
    return full_text
