import json 
import transformers
philly_reviews = []

with open('philadelphia_reviews.json') as json_data:
    data = json.load(json_data)
    count = 0 
    for val in data: 
        philly_reviews.extend(data[val])
        count += len(data[val])
        if count >= 24000: break
classifier = transformers.pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion')
for rev in philly_reviews:
        review = rev['text'] if len(rev['text'])<=512 else rev['text'][:512]
        rev['classification'] = classifier(review)[0]['label']
with open("philly_reviews_with_emotion.json", "w") as outfile:
        json.dump(philly_reviews, outfile)