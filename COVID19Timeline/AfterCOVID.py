import json

filepath_review = "yelp_dataset/yelp_academic_dataset_review.json"
filepath_business = "yelp_dataset/yelp_academic_dataset_business.json"
all_restaurants = []
all_reviews = []
def getReviewsPostPandemic():
    asian = []
    nonasian = []
    start_date = "2020-02"
    end_date = "2022-01"
    key_words = set(["Chinese"])

    chinese_restaurants = set()
    with open(filepath_business, 'r', encoding="utf8") as file:
        for line in file:
            biz = json.loads(line)
            categories = biz.get('categories', [])
            if categories:
                if any(word in categories for word in key_words):
                    chinese_restaurants.add(biz['business_id'])

    with open(filepath_review, 'r', encoding="utf8") as file:
        for line in file:
            review = json.loads(line)
            if review.get('date', '') >= start_date and review.get('date', '') < end_date:
                if review['business_id'] in chinese_restaurants:
                    asian.append(review)
                else:
                    nonasian.append(review)

    with open("COVID19Timeline/ChineseAfterCOVID1.json", "w") as outfile:
        json.dump(asian, outfile)
    with open("COVID19Timeline/NonChineseAfterCOVID1.json", "w") as outfile:
        json.dump(nonasian, outfile)

def main():
    getReviewsPostPandemic()

if __name__ == "__main__":
    main()

