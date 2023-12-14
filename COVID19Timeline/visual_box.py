import csv
import seaborn as sns
import matplotlib.pyplot as plt

# Read data from the Chinese CSV file
data_chinese = []
with open("COVID19Timeline/ratingsChinese.csv", mode="r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        rating_difference = float(row["Rating Difference"])
        data_chinese.append(rating_difference)

# Read data from the Non-Chinese CSV file
data_nonchinese = []
with open("COVID19Timeline/ratingsNonChinese1.csv", mode="r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        rating_difference = float(row["Rating Difference"])
        data_nonchinese.append(rating_difference)

import pandas as pd
df_chinese = pd.DataFrame(data_chinese, columns=["Rating Difference"])
df_nonchinese = pd.DataFrame(data_nonchinese, columns=["Rating Difference"])
df_combined = pd.concat([df_chinese.assign(Group="Chinese"), df_nonchinese.assign(Group="Non-Chinese")])

plt.figure(figsize=(10, 6))
sns.boxplot(x="Rating Difference", y="Group", data=df_combined, palette="Set3")

plt.xlabel('Rating Difference')
plt.ylabel('Group')
plt.title('Box Plot of Rating Differences for Chinese and Non-Chinese Businesses')

plt.show()