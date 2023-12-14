import json
from collections import defaultdict
import csv

#Non chinese Before COVID
NCBC_b_id_to_ratings = defaultdict(list)
file_path = "COVID19Timeline/NonChineseBeforeCOVID.json"
with open(file_path, "r") as file:
    json_data = json.load(file)
    for review in json_data:
        business_id = review.get("business_id")
        stars = review.get("stars")

        if business_id is not None and stars is not None:
            NCBC_b_id_to_ratings[business_id].append(stars)
NCBC_b_id_to_avg_rating = {}
for business_id, ratings in NCBC_b_id_to_ratings.items():
    if ratings:
        avg_rating = sum(ratings) / len(ratings)
        NCBC_b_id_to_avg_rating[business_id] = avg_rating

#print(CBC_b_id_to_avg_rating)

#find for Non Chinese After COVID (NCAC)
NCAC_b_id_to_ratings = defaultdict(list)
file_path = "COVID19Timeline/NonChineseAfterCOVID1.json"
with open(file_path, "r") as file:
    json_data = json.load(file)
    for review in json_data:
        business_id = review.get("business_id")
        stars = review.get("stars")

        if business_id is not None and stars is not None:
            NCAC_b_id_to_ratings[business_id].append(stars)
NCAC_b_id_to_avg_rating = {}
for business_id, ratings in NCAC_b_id_to_ratings.items():
    if ratings:
        avg_rating = sum(ratings) / len(ratings)
        NCAC_b_id_to_avg_rating[business_id] = avg_rating


# Find the difference for each business_id
rating_difference = defaultdict(list)
for business_id in set(NCBC_b_id_to_avg_rating) & set(NCAC_b_id_to_avg_rating):
    difference = NCAC_b_id_to_avg_rating[business_id] - NCBC_b_id_to_avg_rating[business_id]
    rating_difference[business_id] = [NCBC_b_id_to_avg_rating[business_id], NCAC_b_id_to_avg_rating[business_id]]

with open("COVID19Timeline/covidRatingsNC.csv", mode = "w", newline="") as csv_file:
    field_names = ["Business_id", "Pre Covid Avg Rating", "Post Covid Avg Rating"]
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    for business_id, ratings in rating_difference.items():
        writer.writerow({
            "Business_id": business_id,
            "Pre Covid Avg Rating": ratings[0],  # Assuming pre_covid_avg_rating is the first element
            "Post Covid Avg Rating": ratings[1]  # Assuming post_covid_avg_rating is the second element
        })
