import csv
from scipy.stats import ttest_ind
#Business_id,Pre Covid Avg Rating,Post Covid Avg Rating
chinese_csv_file_path = "COVID19Timeline/covidRatingsChinese.csv"
non_chinese_csv_file_path = "COVID19Timeline/covidRatingsNC.csv"

chinese_pre = []
chinese_post = []
with open(chinese_csv_file_path, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        pre = float(row.get("Pre Covid Avg Rating"))
        post = float(row.get("Post Covid Avg Rating"))
        chinese_pre.append(pre)
        chinese_post.append(post)

nonchinese_pre = []
nonchinese_post = []
with open(non_chinese_csv_file_path, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        pre = float(row.get("Pre Covid Avg Rating"))
        post = float(row.get("Post Covid Avg Rating"))
        nonchinese_pre.append(pre)
        nonchinese_post.append(post)

t_statistic, p_value = ttest_ind(chinese_pre, chinese_post)
#print("T-statistic:", t_statistic)
print("P-value for Chinese Pre vs Post:", p_value)

t_statistic, p_value = ttest_ind(nonchinese_pre, nonchinese_post)
#print("T-statistic:", t_statistic)
print("P-value for NonChinese Pre vs Post:", p_value)