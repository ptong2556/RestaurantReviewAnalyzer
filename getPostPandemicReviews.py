import json
with open('yelp_dataset/yelp_academic_dataset_review.json', 'r') as file:
    num_reviews_to_get = 500  # Adjust this number to the desired number of reviews
    reviews_collected = 0
    everything = []
    for line in file:
        review = json.loads(line)
        #post-pandemic is any review April 2020 onwards 
        if 'date' in review and review['date'].startswith('2022') or 'date' in review and review['date'].startswith('2021') or ('date' in review and review['date'].startswith('2020-04')):
            everything.append(review)
            reviews_collected += 1
            if reviews_collected >= num_reviews_to_get:
                break
    with open("reviews_postPandemic.json", "w") as outfile:
        json.dump(everything, outfile)