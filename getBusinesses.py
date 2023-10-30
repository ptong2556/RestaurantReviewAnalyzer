import json

with open('yelp_dataset/yelp_academic_dataset_business.json', 'r') as file:
    num_businesses_to_get = 100 # Adjust this number to the desired number of reviews
    businesses_collected = 0
    city = 'Santa Barbara'
    city_formatted = city.lower().replace(" ","_")
    data = []
    for line in file:
        biz = json.loads(line)
        if biz['city'] == city: 
            data.append(biz)
            businesses_collected += 1
        if businesses_collected >= num_businesses_to_get:
            break
    filename = city_formatted+"_businesses.json"
    with open(filename, "w") as outfile:
        json.dump(data, outfile)