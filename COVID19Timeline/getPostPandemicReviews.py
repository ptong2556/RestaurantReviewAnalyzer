import json

filepath = "yelp_dataset/yelp_academic_dataset_review.json"
all_restaurants = []
all_reviews = []
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
                    if review['date'].startswith(str(i)):
                        everything.append(review)
                        reviews_collected += 1
                        if reviews_collected >= num_reviews_to_get:
                            break
        with open("reviews_postPandemic.json", "w") as outfile:
            json.dump(everything, outfile)

def asianInspiredBusinesses():
    # categories restaurants have been labeled with
    key_words = set(['Japanese','Korean','Chinese','Sushi','Thai',"Vietnamese",
                     "Indonesian", 'Thai', "Conveyor Belt Sushi", "Hot Pot",
                     "Cantonese","Taiwanese", "Ramen", "Shanghainese","Dim Sum",
                     "Izakaya", "Sushi Bars", "Hong Kong Style Cafe","Asian Fusion",
                     "Teppanyaki", "Pan Asian", "Malaysian", "Bangladeshi","Bubble Tea",
                     "Mongolian","Burmese","Cambodian","Japanese Curry","Oriental","Szechuan",
                     "Laotian","Himalayan/Nepalese"])

    all_restaurants = set()
    with open('yelp_dataset/yelp_academic_dataset_business.json', 'r', encoding="utf8") as file:
        for line in file:
            biz = json.loads(line)
            categories = biz['categories']

            if categories:
                categories = biz['categories'].split(",")

                restaurant = False
                bakeries = False
                bars = False
                coffee = False
                tea = False
                asian_inspired = False
                for category in categories:
                    category = category.strip()
                    if category == 'Restaurants':
                        restaurant = True
                    if category == 'Bakeries':
                        bakeries = True
                    if category == 'Bars':
                        bars = True
                    if category == 'Coffee':
                        coffee = True
                    if category == 'Tea':
                        tea = True
                    if category in key_words:
                        asian_inspired = True

                if bakeries or bars or coffee or tea:
                    continue

                if restaurant and asian_inspired:
                    all_restaurants.add(biz['business_id'])

    return all_restaurants

def asianBusinessReviews():
    all_restaurants = asianInspiredBusinesses()
    all_reviews = []
    with open(filepath, 'r', encoding="utf8") as file:
        for line in file:
            review = json.loads(line)
            if review: 
                id = review['business_id']
                if id in all_restaurants:
                    all_reviews.append(review)

    return all_reviews

def main():
    #all_restaurants = asianInspiredBusinesses()
    all_reviews = asianBusinessReviews()

if __name__ == "__main__":
    main()
