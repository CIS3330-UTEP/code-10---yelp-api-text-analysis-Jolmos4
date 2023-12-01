from yelpapi import YelpAPI
import pandas as pd
from textblob import TextBlob  # For sentiment analysis

api_key = "MGnh-hJTrE638MnSSs8ReaxTaWFVC_IGnz1gCH1udRKm5M4bNkh0rq9yvo0efDMiVh3dc14aUQk85IjNrI2GlLh5Ues71mrwWevx78r_-2J3_8No8xot6RHa_DtJZXYx"
yelp_api_instance = YelpAPI(api_key)
search_term = 'service'
location_term = 'El Paso, TX'

# Search for businesses related to service in El Paso
search_results = yelp_api_instance.search_query(term=search_term, location=location_term, sort_by='rating', limit=20)

# Convert search results to DataFrame
result_df = pd.DataFrame.from_dict(search_results['businesses'])

# Get reviews for a specific business
id_for_reviews = 'amar-el-paso'
reviews_response = yelp_api_instance.reviews_query(id=id_for_reviews)

# Analyze each review for sentiment and commonly used words
for review in reviews_response['reviews']:
    analysis = TextBlob(review['text'])
    print(f"Sentiment of Review: {analysis.sentiment}")
    print(f"Common Words: {pd.Series(analysis.words).value_counts().head()}")

# Save results to a CSV file
result_df.to_csv('api_results.csv', index=False)
