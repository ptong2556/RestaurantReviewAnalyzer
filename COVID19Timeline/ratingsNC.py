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

#print(CAC_b_id_to_avg_rating)

# Find the difference for each business_id
rating_difference = {}
for business_id in set(NCBC_b_id_to_avg_rating) & set(NCAC_b_id_to_avg_rating):
    difference = NCAC_b_id_to_avg_rating[business_id] - NCBC_b_id_to_avg_rating[business_id]
    rating_difference[business_id] = difference
    #NEGATIVE means after is lower

with open("ratingsNonChinese.csv", mode = "w", newline="") as csv_file:
    field_names = ["Business_id", "Rating Difference"]
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    for key, value in rating_difference.items():
        writer.writerow({"Business_id": key, "Rating Difference": value})

overall_average_difference = sum(rating_difference.values()) / len(rating_difference)


# Print the results
#print("Average Ratings Before COVID:", CBC_b_id_to_avg_rating)
#print("Average Ratings After COVID:", CAC_b_id_to_avg_rating)
print("Rating Difference:", rating_difference)
print("Overall Average Difference:", overall_average_difference)