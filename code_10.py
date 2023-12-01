from yelpapi import YelpAPI
import pandas as pd
from textblob import TextBlob

api_key = "MGnh-hJTrE638MnSSs8ReaxTaWFVC_IGnz1gCH1udRKm5M4bNkh0rq9yvo0efDMiVh3dc14aUQk85IjNrI2GlLh5Ues71mrwWevx78r_-2J3_8No8xot6RHa_DtJZXYx"
yelp_api_instance = YelpAPI(api_key)
search_term = 'service'
location_term = 'El Paso, TX'

search_results = yelp_api_instance.search_query(
    term = search_term, location = location_term,
    sort_by = 'rating', limit = 20, 
)
print(search_results)

for business in search_results['businesses']:
    print('\n')
    print(business)

# result_df = pd.DataFrame.from_dict(search_results['businesses'])
# print(result_df)
# result_df.to_csv('api_results.csv', index=False) #PARA GRADUARDLO COMO CSV

# Get reviews for amar business
id_for_reviews = 'amar-el-paso'
reviews_response = yelp_api_instance.reviews_query(id=id_for_reviews)

# for review in reviews_response['reviews']:
#     print("\n")
#     print(review)
    
# Analyze the sentiment of each review
for review in reviews_response['reviews']:
    # Create a TextBlob object
    blob = TextBlob(review['text'])
    # Print the review and its sentiment polarity
    print("\nReview: ", review['text'])
    print("Sentiment Polarity: ", blob.sentiment.polarity)