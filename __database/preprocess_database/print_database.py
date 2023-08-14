from __database.preprocess_database.get_database import *
from IPython.display import display

db = get_database()
print(db.keys())
display(db)
