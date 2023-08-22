from urllib.parse import urlparse, parse_qs


def get_video_id_from_url(youtube_url):
    parsed_url = urlparse(youtube_url)
    query_params = parse_qs(parsed_url.query)

    if 'v' in query_params:
        video_id = query_params['v'][0]
        return video_id

    return None
