from urllib.parse import urlparse, parse_qs

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def visualize_rep(rep, dimension_headers=None):
    """
    Visualize each dimension of vectors in two lines over time using subplots in Plotly.

    Parameters:
    - rep (numpy.ndarray): 2D NumPy array with dimensions NxD.
                           N: number of vectors (timestamps)
                           D: dimension of each vector
    - dimension_headers (list or None): List of headers for each dimension. If None, no headers will be added.

    Returns:
    - None (displays the plot)
    """

    # Get the number of timestamps (N) and dimension (D)
    N, D = rep.shape

    # Determine the number of rows and columns for subplots
    rows = (D + 1) // 2  # Round up to the nearest integer

    # Create subplots for each dimension
    fig = make_subplots(rows=rows, cols=2, subplot_titles=dimension_headers,
                        shared_xaxes=False, shared_yaxes=False, vertical_spacing=0.1, horizontal_spacing=0.2)

    # Add traces for each dimension to the subplots
    for dim in range(D):
        row = dim // 2 + 1  # Determine the row for the subplot
        col = dim % 2 + 1   # Determine the column for the subplot
        trace = go.Scatter(x=list(range(N)), y=rep[:, dim], mode='lines', name=f'Dimension {dim + 1}')
        fig.add_trace(trace, row=row, col=col)

    # Update layout
    fig.update_layout(title_text='Visualization of Dimensions over Time', showlegend=False)

    # Show the plot
    fig.show()


# def visualize_rep(rep: np.ndarray):
#     """
#     Visualize each entry of vectors over time using a line plot with Plotly.
#
#     Parameters:
#     - data (numpy.ndarray): 2D NumPy array with dimensions NxD.
#                            N: number of vectors (timestamps)
#                            D: dimension of each vector
#
#     Returns:
#     - None (displays the plot)
#     """
#
#     # Get the number of timestamps (N) and dimension (D)
#     N, D = rep.shape
#
#     # Determine the number of rows and columns for subplots
#     rows = (D + 1) // 2  # Round up to the nearest integer
#
#     # Create subplots for each dimension
#     fig = make_subplots(rows=rows, cols=2, subplot_titles=[f'Dimension {dim + 1}' for dim in range(D)],
#                         shared_xaxes=False, shared_yaxes=False, vertical_spacing=0.1, horizontal_spacing=0.2)
#
#     # Add traces for each dimension to the subplots
#     for dim in range(D):
#         row = dim // 2 + 1  # Determine the row for the subplot
#         col = dim % 2 + 1  # Determine the column for the subplot
#         trace = go.Scatter(x=list(range(N)), y=rep[:, dim], mode='lines', name=f'Dimension {dim + 1}')
#         fig.add_trace(trace, row=row, col=col)
#
#     # Update layout
#     fig.update_layout(title_text='Visualization of Dimensions over Time', showlegend=False)
#
#     # Show the plot
#     fig.show()


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
