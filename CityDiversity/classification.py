import transformers
import json


businesses = []
reviews = []

with open('CityDiversity/philadelphia_reviews.json', 'r') as file:
    for line in file:
        reviews = json.loads(line)
        break
classifier = transformers.pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion')
classifications = []
for business in reviews: 
    specific_reviews = reviews[business]
    for rev in specific_reviews:
        classifications.append(classifier(rev))
        #append values 
       



     
