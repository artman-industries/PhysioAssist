import numpy as np
from PIL import Image

from __database.preprocess_database.download_db import download_db
from __database.preprocess_database.get_database import get_firebase_bucket, get_firebase_database

from __global.skeleton import Skeleton
from predict_skeletons.model1.model1_predict_skeleton import model1_predict_skeleton
from predict_skeletons.predict_skeletons import predict_skeletons
from __database.preprocess_database.database_api import DatabaseAPI


def main():
    # bucket = get_firebase_bucket()
    # db = get_firebase_database()
    # reps = download_db(db, bucket)
    database_api = DatabaseAPI(None)
    reps = database_api.download_reps('model1')  # todo: change the name
    for rep in reps:
        frame_paths = [frame_path for _, frame_path in rep.images]
        frame_ids = [frame_id for frame_id, _ in rep.images]
        # frames = [np.array(Image.open(frame_path)) for frame_path in frame_paths]
        # TODO: make model1_predict_skeleton as a script parameter
        skeletons = predict_skeletons(frame_paths, model1_predict_skeleton)

        # rs = np.array([1, 2])
        # ls = np.array([3, 2])
        # moc = np.array([5, 5])
        # skeleton1 = Skeleton(right_shoulder=rs, left_shoulder=ls, right_knee=moc, left_hip=moc, right_hip=moc,
        #                      right_ankle=moc,
        #                      left_ankle=moc, right_elbow=moc, left_elbow=moc, right_wrist=moc, left_wrist=moc,
        #                      left_knee=moc)
        # skeletons = [skeleton1]

        # todo: save the skeletons to the processed database as np.array
        for skeleton, frame_id in zip(skeletons, frame_ids):
            database_api.save_skeleton(rep.rep_id, 'model1', frame_id, skeleton.to_dict())


# if __name__ == '__process_data__':
main()
