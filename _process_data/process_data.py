from __database.preprocess_database.get_database import get_database
from get_sampled_frames_from_video.sample_frames_from_video_interval import get_frames_from_video
from predict_skeletons.model1.predict_skeleton import model1_predict_skeleton
from predict_skeletons.predict_skeletons import predict_skeletons


def get_data_from_db_row(db_row):
    url = db_row['url']
    start_time = db_row['start']
    end_time = db_row['end']
    return [url, start_time, end_time]


def main():
    # TODO: make model1_predict_skeleton as a script parameter
    db = get_database()
    for index, db_row in db.iterrows():
        num_samples = 10  # todo: define it as a script parameter

        function_parameters = get_data_from_db_row(db_row) + [num_samples]
        frames = get_frames_from_video(*function_parameters)  # todo: get it from the preprocessed database
        skeletons = predict_skeletons(frames, model1_predict_skeleton)
    # todo: save the skeletons to the processed database as np.array


if __name__ == '__process_data__':
    main()
