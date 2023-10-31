import json
all_categories = set()
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
            for category in categories:
                if category == 'Restaurants':
                    restaurant = True
                elif category == 'Bakeries':
                    bakeries = True
                elif category == 'Bars':
                    bars = True
                elif category == 'Coffee':
                    coffee = True
                elif category == 'Tea':
                    tea = True

            if bakeries or bars or coffee or category:
                continue

            if restaurant:
                for category in categories:
                    all_categories.add(category.strip())

filename = "categories.json"
with open(filename, "w", newline = "") as outfile:
    for item in list(all_categories):
        json.dump(item, outfile)
        outfile.write('\n')