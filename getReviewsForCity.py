import json
city = input("Enter city to extract reviews from: ").lower()
with open('yelp_dataset/yelp_academic_dataset_business.json', 'r') as file:
    businesses_collected = {}
    business_information = {}
    for line in file:
        biz = json.loads(line)
        if biz['city'].lower() == city and biz['business_id'] not in businesses_collected:
               if biz['categories'] and 'Restaurants' in biz['categories'] and  'Bakeries' not in biz['categories'] and 'Bars' not in biz['categories'] and 'Coffee & Tea' not in biz['categories']:  
                business_information[biz['business_id']] = biz

with open('yelp_dataset/yelp_academic_dataset_review.json', 'r') as file:
    total_restaurants = 0
    everything = {}
    for line in file:
        review = json.loads(line)
        if review['business_id'] in business_information and review['business_id'] not in everything:
            everything[review['business_id']] = [review]
            total_restaurants+=1
        elif review['business_id'] in business_information and review['business_id'] in everything:
            if len(everything[review['business_id']]) < 100: 
                everything[review['business_id']].append(review)
        if total_restaurants>=5000: break
    with open(city.replace(" ","_")+"_reviews.json", "w") as outfile:
        json.dump(everything, outfile)
               
