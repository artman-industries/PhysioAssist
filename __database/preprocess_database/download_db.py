import os
import re
from __global.rep_object import RepObject


def download_image_from_blob(bucket, blob_url, blob_name, rep_folder):
    blob = bucket.blob(blob_name)
    file_name = blob_name
    destination_file_name = os.path.join(rep_folder, file_name)
    print(f'{destination_file_name=}')
    blob.download_to_filename(destination_file_name)
    return destination_file_name


def clean_filename(filename):
    # Remove invalid characters using regular expression
    cleaned_filename = re.sub(r'[\/:*?"<>|]', '_', filename)
    return cleaned_filename


def download_db(db, bucket):
    reps_collection = db.collection('reps')
    rep_docs = reps_collection.stream()
    db_folder_name = 'db'
    os.mkdir(db_folder_name)
    reps = []
    for rep_doc in rep_docs:
        rep_id = clean_filename(rep_doc.id)  # Using rep_doc's ID as the folder name
        rep_folder_name = os.path.join(db_folder_name, rep_id)
        os.mkdir(rep_folder_name)
        rep_folder = os.path.join(os.path.join(os.getcwd(), db_folder_name), rep_id)
        rep = RepObject(rep_id)
        for collection_ref in rep_doc.reference.collections():
            frame_docs = collection_ref.stream()
            for frame_doc in frame_docs:
                blob_url = frame_doc.to_dict()['blob_url']
                blob_name = frame_doc.to_dict()['blob_name']
                frame_number = frame_doc.to_dict()['frame_number']
                destination_file_name = download_image_from_blob(bucket, blob_url, blob_name, rep_folder)
                rep.add_frame(frame_number, destination_file_name)
        reps.append(rep)
    return reps
