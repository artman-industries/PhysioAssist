import os

import firebase_admin
from firebase_admin import credentials, firestore, storage
import string
import random

from __global.rep_object import RepObject
from __global.skeleton import Skeleton


class DatabaseAPI:
    """
    A class for interacting with Firebase Firestore and Storage.

    Attributes:
        cred_path (str): Path to the Firebase service account credentials JSON file.

    Methods:
        __init__(self, cred_path)
        init_firestore(self)
        init_storage(self)
        random_word(length)
    """

    def __init__(self, cred_path):
        """
        Initialize the DatabaseAPI instance.

        Args:
            cred_path (str): Path to the Firebase service account credentials JSON file.
        """
        if cred_path is None:
            cred_path = r'C:\Users\DJISI\Desktop\technion\simester7\project\PhysioAssist\physioassistent-firebase-adminsdk-fae3q-8648769f21.json'
        print(cred_path)
        # "C:/Users/Alon/Documents/Studies/Spring 2023/Project in Artificial Intellijence/PhysiAssist/physioassistent-firebase-adminsdk-fae3q-8648769f21.json"

        self.cred_path = cred_path
        self.db = self.init_firestore()
        self.bucket = self.init_storage()

    def init_firestore(self):
        """
        Initialize and return a Firestore client.

        Returns:
            firestore.client.Client: A Firestore client instance.
        """
        cred = credentials.Certificate(self.cred_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        return db

    def init_storage(self):
        """
        Initialize and return a Storage bucket.

        Returns:
            storage.bucket.Bucket: A Storage bucket instance.
        """
        cred = credentials.Certificate(self.cred_path)
        bucket_name = self.random_word(10)
        bucket_app = firebase_admin.initialize_app(cred, {
            'storageBucket': 'physioassistent.appspot.com'  # Replace with your storage bucket URL
        }, name=bucket_name)
        bucket = storage.bucket(app=bucket_app)
        return bucket

    @staticmethod
    def random_word(length):
        """
        Generate a random string of lowercase letters.

        Args:
            length (int): The length of the random string to generate.

        Returns:
            str: The random string.
        """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def get_reps(self):
        reps_collection = self.db.collection('reps')
        docs = reps_collection.stream()
        rep_dicts = [doc.to_dict() for doc in docs]
        return rep_dicts

    def add_rep(self, doc_name, url, start, end):
        self.db.collection("reps").document(doc_name).set({"url": url, "start": start, "end": end})

    def upload_frame_to_rep(self, file_name, rep_name, file, timestamp, frame_number):
        self.bucket.blob(file_name).upload_from_string(file,
                                                       content_type="image/jpeg")  # Upload the frame to the bucket
        print(f"Uploaded frame with name {file_name} to bucket")

        self.db.collection("reps").document(rep_name).collection("frames").add(
            {"blob_url": self.bucket.blob(file_name).public_url,
             "blob_name": file_name,
             "timestamp": timestamp,
             "frame_number": frame_number}
        )

    @staticmethod
    def download_image_from_blob(bucket, blob_name, rep_folder):
        blob = bucket.blob(blob_name)
        file_name = blob_name
        destination_file_name = os.path.join(rep_folder, file_name)
        print(f'{destination_file_name=}')
        blob.download_to_filename(destination_file_name)
        return destination_file_name

    def download_reps(self, db_folder_name='db'):
        os.mkdir(db_folder_name)
        reps_collection = self.db.collection('reps')
        rep_docs = reps_collection.stream()
        reps = []
        for rep_doc in rep_docs:
            rep_id = rep_doc.id  # Using rep_doc's ID as the folder name
            rep_folder_name = os.path.join(db_folder_name, rep_id)
            os.mkdir(rep_folder_name)
            rep_folder = os.path.join(os.path.join(os.getcwd(), db_folder_name), rep_id)
            rep = RepObject(rep_id)
            for collection_ref in rep_doc.reference.collections():
                frame_docs = collection_ref.stream()
                for frame_doc in frame_docs:
                    blob_name = frame_doc.to_dict()['blob_name']
                    frame_number = frame_doc.to_dict()['frame_number']
                    destination_file_name = self.download_image_from_blob(self.bucket, blob_name, rep_folder)
                    rep.add_frame(frame_number, destination_file_name)
            reps.append(rep)
        return reps

    def save_skeleton(self, rep_id, model_name, frame_number, skeleton_dict):
        rep_ref = self.db.collection("reps").document(rep_id)
        rep_ref.collection("skeletons").document(model_name).set({"name": model_name})  # todo: add more data
        model_ref = rep_ref.collection("skeletons").document(model_name)
        model_ref.collection('skeletons').document(str(frame_number)).set(skeleton_dict)

    def get_skeletons(self, rep_id, model_name):
        rep_ref = self.db.collection("reps").document(rep_id)
        model_collection = rep_ref.collection("skeletons").document(model_name).collection("skeletons")
        docs = model_collection.stream()
        skeletons = [Skeleton.from_dict(doc.to_dict()) for doc in docs]
        return skeletons

    def get_rep_ids(self):
        reps_collection = self.db.collection('reps')
        docs = reps_collection.stream()
        rep_ids = [doc.id for doc in docs]
        return rep_ids
