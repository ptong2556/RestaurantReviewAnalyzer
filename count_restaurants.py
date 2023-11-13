import json
city = input("Enter city to extract reviews from: ").lower()
with open('yelp_dataset/yelp_academic_dataset_business.json', 'r') as file:
    businesses_collected = {}
    business_information = {}
    asian_count = 0
    count = 0
    for line in file:
        biz = json.loads(line)
        if city.lower() in biz['city'].lower() and biz['business_id'] not in businesses_collected:
                if biz['categories'] and 'Restaurants' in biz['categories'] and  'Bakeries' not in biz['categories'] and 'Bars' not in biz['categories'] and 'Coffee & Tea' not in biz['categories']:  
                    business_information[biz['business_id']] = biz
                    count += 1
                if biz['categories'] and 'Chinese' in biz['categories']:
                    asian_count += 1
print("Total Restaurant Count: " + str(count))
print("Total Chinese Restaurant Count: " + str(asian_count))
