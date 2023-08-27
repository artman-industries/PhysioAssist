import numpy as np
import cv2
from PIL import Image, ImageDraw


def create_graph_image(array):
    """
    Create a graph image for a given NumPy array.

    Parameters:
        array (np.ndarray): NumPy array.

    Returns:
        PIL.Image.Image: Generated graph image.
    """
    width, height = 800, 400  # Image dimensions
    padding = 50  # Padding around the graph

    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    max_value = np.max(array)
    normalized_array = array / max_value

    num_points = len(array)
    x_spacing = (width - 2 * padding) / (num_points - 1)

    for i, value in enumerate(normalized_array):
        x = padding + i * x_spacing
        y = height - padding - value * (height - 2 * padding)
        draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill="blue")

    return img


# Example usage
n = 10  # Length of arrays
num_graphs = 5  # Number of arrays/graphs

# Generate sample data: list of NumPy arrays
array_list = [np.random.rand(n) for _ in range(num_graphs)]

# Create and save graph images using OpenCV and PIL
for i, array in enumerate(array_list):
    graph_image = create_graph_image(array)
    cv2.imwrite(f"graph_{i + 1}.png", cv2.cvtColor(np.array(graph_image), cv2.COLOR_RGB2BGR))
