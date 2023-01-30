import requests
from bs4 import BeautifulSoup
import pandas as pd

query = 'Reservoir Engineering'
num_results = 3

url = f'http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={num_results}'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'xml')

titles = [title.text for title in soup.find_all('title')[-num_results:]]
paper_links = [paperlink.text for paperlink in soup.find_all('id')[-num_results:]]
published_dates = [publishedDate.text for publishedDate in soup.find_all('published')[-num_results:]]
abstracts = [abstract.text for abstract in soup.find_all('summary')[-num_results:]]
# authors = [author.text for author in soup.find_all('name')]


print(len([[title] for title in titles]))
print(len([[paper_link] for paper_link in paper_links]))
print(len([[published_date] for published_date in published_dates]))
print(len([[abstract] for abstract in abstracts]))

#
# dataset = pd.DataFrame({
#
#     'title': titles,
#     'paper_link': paper_links,
#     'published_date': published_dates,
#     'abstract': abstracts,
#     # 'author': authors
#
# })

# print(dataset.head())
#
# import pandas as pd
# import requests
# api_key = '790713ded66fe0dd637dd61f70925146'
# headers = {'Authorization': 'Bearer {}'.format(api_key)}  # Setting the authorization key in the headers
# search_api_url = 'https://api.springernature.com/metadata/json'  # URL for the API endpoint
# payload = dict(api_key=api_key, q="Machine Learning in Healthcare", p=1)  # Payload for the GET \
# # request
# response = requests.get(search_api_url, headers=headers, params=payload).json()
# # Convert response to Pandas DataFrame
#
# print(pd.DataFrame(response['records']))

