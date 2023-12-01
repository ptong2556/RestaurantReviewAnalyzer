import json

filepath_review = "../yelp_dataset/yelp_academic_dataset_review.json"
filepath_business = "../yelp_dataset/yelp_academic_dataset_business.json"
all_restaurants = []
all_reviews = []
def getReviewsPostPandemic():
    after_reviews = []
    start_date = "2020-02"
    key_words = set(['Japanese','Korean','Chinese','Sushi','Thai',"Vietnamese",
                    "Indonesian", 'Thai', "Conveyor Belt Sushi", "Hot Pot",
                    "Cantonese","Taiwanese", "Ramen", "Shanghainese","Dim Sum",
                    "Izakaya", "Sushi Bars", "Hong Kong Style Cafe","Asian Fusion",
                    "Teppanyaki", "Pan Asian", "Malaysian", "Bangladeshi","Bubble Tea",
                    "Mongolian","Burmese","Cambodian","Japanese Curry","Oriental","Szechuan",
                    "Laotian","Himalayan/Nepalese"])

    asian_restaurants = set()
    with open(filepath_business, 'r', encoding="utf8") as file:
        for line in file:
            biz = json.loads(line)
            categories = biz.get('categories', [])
            if categories:
                if any(word in categories for word in key_words):
                    asian_restaurants.add(biz['business_id'])

    with open(filepath_review, 'r', encoding="utf8") as file:
        for line in file:
            review = json.loads(line)
            if review['business_id'] in asian_restaurants and review.get('date', '') >= start_date:
                after_reviews.append(review)

    with open("COVID19Timeline/afterCOVID.json", "w") as outfile:
        json.dump(after_reviews, outfile)

def main():
    getReviewsPostPandemic()

if __name__ == "__main__":
    main()

