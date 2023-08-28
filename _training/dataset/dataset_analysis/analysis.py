import numpy as np
from PIL import Image, ImageDraw, ImageFont


def create_column_graphs(data, headers=None, graph_height=300, graph_width=400, padding=10, line_color=(0, 0, 255),
                         bg_color=(255, 255, 255)):
    """
    Create a row of graphs for each column in a 2D array with headers, axes, grid, and padding using OpenCV and Pillow.

    Args:
        data (numpy.ndarray): The input 2D array.
        headers (list): List of header strings for each column.
        graph_height (int): Height of the graph images.
        graph_width (int): Width of the graph images.
        padding (int): Padding around the graphs.
        line_color (tuple): Color of the graph lines in RGB format.
        bg_color (tuple): Background color of the graph images in RGB format.

    Returns:
        PIL.Image: An image containing the row of graphs.
    """
    num_columns = data.shape[1]
    num_rows = data.shape[0]

    total_height = graph_height + (2 * padding)
    total_width = num_columns * (graph_width + padding)

    combined_img = Image.new('RGB', (total_width, total_height), bg_color)
    draw = ImageDraw.Draw(combined_img)

    font = ImageFont.load_default()

    x_offset = 0
    for col_index in range(num_columns):
        column_data = data[:, col_index]
        max_value = np.max(column_data)
        min_value = np.min(column_data)
        value_range = max_value - min_value

        # Draw the header
        if headers:
            header_text = headers[col_index]
            header_text_size = draw.textbbox((0, 0), header_text, font=font)
            header_width, header_height = header_text_size[2] - header_text_size[0], header_text_size[3] - \
                                          header_text_size[1]
            header_position = (x_offset + (graph_width - header_width) // 2, padding // 2)
            draw.text(header_position, header_text, fill=(0, 0, 0), font=font)

        # Draw the graph area
        graph_area = (
        x_offset + padding, padding + header_height, x_offset + graph_width - padding, graph_height + padding)
        draw.rectangle(graph_area, outline=(0, 0, 0))

        # Draw the axes
        draw.line([(graph_area[0], graph_area[3]), (graph_area[2], graph_area[3])], fill=(0, 0, 0))  # X-axis
        draw.line([(graph_area[0], graph_area[3]), (graph_area[0], graph_area[1])], fill=(0, 0, 0))  # Y-axis

        # Draw the grid
        x_grid_step = (graph_area[2] - graph_area[0]) / (len(column_data) - 1)
        y_grid_step = (graph_area[3] - graph_area[1]) / (value_range + 1)

        for i in range(1, len(column_data)):
            x = graph_area[0] + i * x_grid_step
            draw.line([(x, graph_area[1]), (x, graph_area[3])], fill=(200, 200, 200))

        for i in range(1, value_range + 1):
            y = graph_area[3] - i * y_grid_step
            draw.line([(graph_area[0], y), (graph_area[2], y)], fill=(200, 200, 200))

        # Draw the graph lines
        x_step = (graph_area[2] - graph_area[0] - 2 * padding) / (len(column_data) - 1)
        y_scale = (graph_area[3] - graph_area[1] - 2 * padding) / value_range

        prev_point = None
        for i, value in enumerate(column_data):
            x = graph_area[0] + padding + i * x_step
            y = graph_area[3] - padding - (value - min_value) * y_scale

            if prev_point is not None:
                draw.line([prev_point, (x, y)], fill=line_color, width=2)

            prev_point = (x, y)

        x_offset += graph_width + padding

    return combined_img


# Example usage
if __name__ == "__main__":
    # Replace this with your actual data
    data = np.random.randint(0, 100, size=(25, 7))
    headers = ["Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6", "Column 7"]

    # Create and display the combined image with the row of graphs
    combined_graphs = create_column_graphs(data, headers)
    combined_graphs.show()
    # You can also save the combined image using combined_graphs.save("combined_graphs.png")
