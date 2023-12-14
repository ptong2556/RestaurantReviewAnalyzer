# How to Run
```
python BeforeCOVID.py
python AfterCOVID.py
```
- This will create extract Chinese and Non Chinese restaurant data from before and after COVID (Feb 2020) as ChineseBeforeCOVID.json, NonChineseBeforeCOVID.json, ChineseAfterCOVID.json, NonChineseAfterCOVID.json respectively.

```
python ratingsC.py
python ratingNC.py
```
- This will extract the average difference for each business_id (post - pre covid) and create ratingsChinese.csv and ratingsNonChinese.csv respectively.

```
python statistics.py
```
- This will run the t-tests performed for Chinese vs. Non Chinese rating differences. This uses the previously generated ratingsChinese.csv and ratingsNonChinese.csv
```
python visual_box.py
```
- This will create a visual box plot to show rating differences for Chinese and Non-Chinese Restaurants.

```
python csvgenerateChinese.py
python csvgenerateNonChinese.py
```
- This will create covidRatingsChinese.csv and covidRatingsNC.csv respectively which will have Business_id,Pre Covid Avg Rating,Post Covid Avg Rating as columns
```
python statistics1.py
```
- This will run the t-tests performed for Chinese and Non Chinese to compare pre vs post COVID. This uses the previously generated covidRatingsChinese.csv and covidRatingsNC.csv