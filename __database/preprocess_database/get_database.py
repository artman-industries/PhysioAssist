import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
import random
import string

spreadsheet_id = '1KubCg5KQWX-JBghAJHWcc-jVf7lVNfuccFohX5TRa1k'
range_name = 'sheet1'

cred_path = r'C:\Users\DJISI\Desktop\technion\simester7\project\PhysioAssist\physioassistent-firebase-adminsdk-fae3q-8648769f21.json'


# "C:/Users/Alon/Documents/Studies/Spring 2023/Project in Artificial Intellijence/PhysiAssist/physioassistent-firebase-adminsdk-fae3q-8648769f21.json"

def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def get_database() -> pd.DataFrame:
    videos_sheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&sheet={range_name}"
    videos_desc_list = pd.read_csv(videos_sheet_url)
    return videos_desc_list


def get_firebase_database():
    cred = credentials.Certificate(cred_path)

    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db


def get_firebase_bucket():
    cred = credentials.Certificate(cred_path)
    # this code create random string for unique name of the bucket

    bucket_name = random_word(10)
    bucket_app = firebase_admin.initialize_app(cred, {
        'storageBucket': 'physioassistent.appspot.com'
    }, name=bucket_name)
    bucket = storage.bucket(app=bucket_app)
    return bucket
