from urllib.parse import urlparse, parse_qs


def get_video_id_from_url(youtube_url):
    parsed_url = urlparse(youtube_url)
    query_params = parse_qs(parsed_url.query)

    if 'v' in query_params:
        video_id = query_params['v'][0]
        return video_id

    return None


def is_number_around(a, b, tolerance=1e-2):
    """
    Check if number 'a' is around number 'b' within a specified tolerance.

    Args:
        a (float): The first number.
        b (float): The second number to compare with.
        tolerance (float, optional): The tolerance level for considering 'a' to be around 'b'. Defaults to 1e-6.

    Returns:
        bool: True if 'a' is within the specified tolerance of 'b', False otherwise.
    """
    absolute_difference = abs(a - b)
    return absolute_difference <= tolerance
