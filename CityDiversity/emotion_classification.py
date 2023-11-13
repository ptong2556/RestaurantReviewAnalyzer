'''
This file uses a model using Distilbert and finetuned on an emotion dataset. 
It gives us a little more specificity regarding the emotion of the reviews.
https://huggingface.co/bhadresh-savani/distilbert-base-uncased-emotion
'''
from transformers import pipeline
import json

businesses = []
reviews = []

with open('philadelphia_reviews.json', 'r') as file:
    for line in file:
        reviews = json.loads(line)
        break
classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion')
classifications = []
for business in reviews: 
    specific_reviews = reviews[business]
    for rev in specific_reviews:
        review = rev['text'] if len(rev['text'])<=512 else rev['text'][:512]
        classifications.append((rev['review_id'],classifier(review)))
with open("philly_emotion_classification.json", "w") as outfile:
        json.dump(classifications, outfile)
    
       



     
