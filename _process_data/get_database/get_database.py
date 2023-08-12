import pandas as pd

spreadsheet_id = '1KubCg5KQWX-JBghAJHWcc-jVf7lVNfuccFohX5TRa1k'
range_name = 'sheet1'


def get_database() -> pd.DataFrame:
    videos_sheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&sheet={range_name}"
    videos_desc_list = pd.read_csv(videos_sheet_url)
    return videos_desc_list
