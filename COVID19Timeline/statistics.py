import csv
from scipy.stats import ttest_ind

chinese_csv_file_path = "COVID19Timeline/ratingsChinese.csv"
non_chinese_csv_file_path = "COVID19Timeline/ratingsNonChinese1.csv"

chinese_ratings = []
with open(chinese_csv_file_path, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        rating = float(row.get("Rating Difference"))
        chinese_ratings.append(rating)

non_chinese_ratings = []
with open(non_chinese_csv_file_path, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        rating = float(row.get("Rating Difference"))
        non_chinese_ratings.append(rating)

t_statistic, p_value = ttest_ind(chinese_ratings, non_chinese_ratings)
print("T-statistic:", t_statistic)
print("P-value:", p_value)

if p_value < 0.05:
    print("The difference between the ratings of Chinese and non-Chinese restaurants is statistically significant.")
else:
    print("There is no statistically significant difference between the ratings of Chinese and non-Chinese restaurants.")
