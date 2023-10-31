import json
city = input("Enter city to extract businesses from: ").lower()
with open('yelp_dataset/yelp_academic_dataset_business.json', 'r') as file:
    businesses_collected = {}
    business_information = {}
    for line in file:
        biz = json.loads(line)
        if biz['city'].lower() == city and biz['business_id'] not in businesses_collected:
               if biz['categories'] and 'Restaurants' in biz['categories'] and 'Bakeries' not in biz['categories'] and 'Bars' not in biz['categories'] and 'Coffee & Tea' not in biz['categories']:  
                business_information[biz['business_id']] = biz
                businesses_collected[biz['business_id']]= 0
    if " " in city: city = city.replace(" ","_")
    with open(city+"_businesses.json", "w") as outfile:
         json.dump(business_information, outfile)