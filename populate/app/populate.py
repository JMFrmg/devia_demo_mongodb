###### populate #####
from pprint import pprint

import numpy as np
import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://admin:password@mongo')
db = client["gallica"]
articles = db.press_article

for article in articles.find():
    pprint(article)

df_articles = pd.read_parquet("data/gallica_presse_1.parquet")

articles_dict = df_articles.to_dict("records")

for article in articles_dict:
    post_id = articles.insert_one(article).inserted_id
    print(post_id)