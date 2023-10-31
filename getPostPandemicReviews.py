import json

filepath = "yelp_dataset/yelp_academic_dataset_review.json"
def getReviewsRange(startYear, endYear):
    with open(filepath, 'r') as file:
        num_reviews_to_get = 500  # Adjust this number to the desired number of reviews
        reviews_collected = 0
        everything = []
        for line in file:
            review = json.loads(line)
            #post-pandemic is any review April 2020 onwards
            if 'date' in review:
                for i in range(startYear, endYear + 1):
                    if review['date'].startsWith(i + "")):
                        everything.append(review)
                        reviews_collected += 1
                        if reviews_collected >= num_reviews_to_get:
                            break
        with open("reviews_postPandemic.json", "w") as outfile:
            json.dump(everything, outfile)

def asianFilter():
    categories = set(['Japanese','Korean','Chinese','Sushi','Thai',"Vietnamese",
                    "Indonesian", 'Thai', "Conveyor Belt Sushi", "Hot Pot",
                    "Cantonese","Taiwanese", "Ramen", "Shanghainese","Dim Sum",
                    "Izakaya", "Sushi Bars", "Hong Kong Style Cafe","Asian Fusion",
                    "Teppanyaki", "Pan Asian", "Malaysian", "Bangladeshi","Bubble Tea",
                    "Mongolian","Burmese","Cambodian","Japanese Curry","Oriental","Szechuan",
                    "Laotian","Himalayan/Nepalese"])

