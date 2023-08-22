from __database.preprocess_database.get_database import get_database, get_firebase_bucket, get_firebase_database
from get_sampled_frames_from_video.sample_frames_from_video_interval import get_frames_from_video
from predict_skeletons.model1.model1_predict_skeleton import model1_predict_skeleton
from predict_skeletons.predict_skeletons import predict_skeletons
import os


def download_image_from_blob(bucket, blob_url):
    blob = bucket.blob('leo.png')
    file_name = "example.jpg"
    destination_file_name = os.path.join(os.getcwd(), file_name)
    blob.download_to_filename(destination_file_name)


def main():
    bucket = get_firebase_bucket()
    db = get_firebase_database()

    reps_collection = db.collection('reps')
    rep_docs = reps_collection.stream()

    for rep_doc in rep_docs:
        for collection_ref in rep_doc.reference.collections():
            frame_docs = collection_ref.stream()
            for frame_doc in frame_docs:
                blob_url = frame_doc.to_dict()['blob_url']
                download_image_from_blob(bucket, blob_url)
                break
        break
    # TODO: make model1_predict_skeleton as a script parameter
    # db = get_database()
    # for index, db_row in db.iterrows():
    #     num_samples = 25  # todo: define it as a script parameter
    #
    #     function_parameters = get_data_from_db_row(db_row) + [num_samples]
    #     frames = get_frames_from_video(*function_parameters)  # todo: get it from the preprocessed database
    #     skeletons = predict_skeletons(frames, model1_predict_skeleton)
    # todo: save the skeletons to the processed database as np.array


# if __name__ == '__process_data__':
main()
