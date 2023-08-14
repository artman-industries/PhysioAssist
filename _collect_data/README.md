collect data into:
https://docs.google.com/spreadsheets/d/1KubCg5KQWX-JBghAJHWcc-jVf7lVNfuccFohX5TRa1k/edit#gid=0

in the form of:
url	| creator | angle | start | end | how many pepole are in the frame | note?


# YouTube Video Data Collection Tool

The YouTube Video Data Collection Tool is a Python project designed to simplify the process of downloading YouTube videos, selecting specific time intervals, sampling frames, and storing the collected data into a database. This tool is particularly useful for data collection tasks that require extracting frames from YouTube videos for analysis, research, or machine learning purposes.

## Prerequisites

Before using this tool, ensure you have the following prerequisites installed:

- Python (version X.X)
- [youtube-dl](https://github.com/ytdl-org/youtube-dl) library for downloading YouTube videos.
- [OpenCV](https://opencv.org/) library for image processing.
- [Database](https://link-to-your-database-library) library for storing the collected data.

## Getting Started

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/your-username/your-repository.git
    ```

2. Install the required Python libraries using pip:

    ```
    pip install youtube-dl opencv-python database-library
    ```

3. Navigate to the `_collect_data` folder:

    ```
    cd your-repository/_collect_data
    ```

4. Open the `collect_data.py` file and set the appropriate configurations, such as the database connection details.

## How to Use

1. Run the `collect_data.py` script:

    ```
    python collect_data.py
    ```

2. The script will prompt you to enter a YouTube video URL.

3. Specify the begin and end times (in seconds) for the interval you want to sample from.

4. Enter the desired number of frames to sample from the specified interval.

5. The tool will download the video, sample frames, and store them in the database.

## Configuration

You can customize the behavior of the tool by modifying the `collect_data.py` script:

- `DATABASE_URL`: The URL or connection details for your database.
- `VIDEO_OUTPUT_PATH`: The path where downloaded videos will be saved.
- `FRAME_OUTPUT_PATH`: The path where sampled frames will be saved.
- Other parameters related to video quality, format, and database operations.

## Note

- Make sure to comply with YouTube's terms of service and respect copyright regulations when using this tool.
- Handle database connections and data storage securely to protect sensitive information.

## Acknowledgments

This tool was inspired by the need to simplify the process of collecting data from YouTube videos for various research and analysis tasks.

## License

This project is licensed under the [MIT License](LICENSE).
