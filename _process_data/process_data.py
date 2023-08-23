import numpy as np
from PIL import Image

from __database.preprocess_database.download_db import download_db
from __database.preprocess_database.get_database import get_firebase_bucket, get_firebase_database
from get_sampled_frames_from_video.sample_frames_from_video_interval import get_frames_from_video
from predict_skeletons.model1.model1_predict_skeleton import model1_predict_skeleton
from predict_skeletons.predict_skeletons import predict_skeletons
from __database.preprocess_database.database_api import DatabaseAPI


def main():
    # bucket = get_firebase_bucket()
    # db = get_firebase_database()
    # reps = download_db(db, bucket)
    database_api = DatabaseAPI(None)
    reps = database_api.download_reps()
    for rep in reps:
        frame_paths = [frame_path for _, frame_path in rep.images]
        # frames = [np.array(Image.open(frame_path)) for frame_path in frame_paths]
        # TODO: make model1_predict_skeleton as a script parameter
        skeletons = predict_skeletons(frame_paths, model1_predict_skeleton)
        # todo: save the skeletons to the processed database as np.array
    print(reps)


# if __name__ == '__process_data__':
main()
