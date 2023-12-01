from bs4 import BeautifulSoup
import requests
import pandas as pd
# web_url = 'https://www.utep.edu/nusiness/people/faculty-profiles.html'

# page_to_scrape = requests.get(web_url)

# soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

# emails = soup.findAll('span', attrs={'class':'email'})

# for tag in emails:
#     print(tag)

web_url = 'https://www.utep.edu/extendeduniversity/cid/people/'

page_to_scrape = requests.get(web_url)
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

emails = soup.findAll('span', attrs={'class': 'email'})
phones = soup.findAll('span', attrs={'class': 'phone'})  

data = []

for email, phone in zip(emails, phones): #zip =  iterate over both emails and phones simultaneously
    email_text = email.text.strip()
    phone_text = phone.text.strip()
    print(f"Email: {email_text}, Phone: {phone_text}")

    data.append({'Email': email_text, 'Phone': phone_text})
df = pd.DataFrame(data)

#Export DataFrame to a CSV file
csv_filename = 'contacts.csv'
df.to_csv(csv_filename, index=False)