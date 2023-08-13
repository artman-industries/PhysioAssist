from get_database.get_database import get_database
from get_sampled_frames_from_video.sample_frames_from_video_interval import get_frames_from_video
from predict_skelaton.model1.predict_skeleton import predict_skeletons


def get_data_from_db_row(db_row):
    url = db_row['url']
    start_time = db_row['start']
    end_time = db_row['end']
    return [url, start_time, end_time]


def main():
    db = get_database()
    for index, db_row in db.iterrows():
        num_samples = 10  # todo: define it as a script parameter

        function_parameters = get_data_from_db_row(db_row) + [num_samples]
        frames = get_frames_from_video(*function_parameters)
        skeletons = predict_skeletons(frames)
        # todo: save the skeletons to the db


if __name__ == '__process_data__':
    main()
