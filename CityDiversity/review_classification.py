'''
This file uses a model that was pretrained on the yelp polarity dataset. 
It tells us whether or not the review is positive or negative.
https://huggingface.co/ydshieh/bert-base-uncased-yelp-polarity?text=I+like+you.+I+love+you
'''
from transformers import pipeline
import json

businesses = []
reviews = []
with open('CityDiversity/philadelphia_reviews.json', 'r') as file:
    for line in file:
        reviews = json.loads(line)
        break
classifier = pipeline("text-classification",model='ydshieh/bert-base-uncased-yelp-polarity')
classifications = []
l = 0 
for business in reviews: 
    specific_reviews = reviews[business]
    for rev in specific_reviews:
        review = rev['text'] if len(rev['text'])<=512 else rev['text'][:512]
        classifications.append((rev['review_id'],classifier(review)))
with open("philly_review_classification.json", "w") as outfile:
        json.dump(classifications, outfile)

    
       



     
