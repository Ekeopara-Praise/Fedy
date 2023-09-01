# # # import libraries
from dataclasses import dataclass
import requests  # Library for making HTTP requests
import pandas as pd  # Library for data manipulation and analysis
import streamlit as st
from bs4 import BeautifulSoup


# Using dataclass decorator to define the FedySearch class as a dataclass
@dataclass
class FedySearch:
    search_keyword: str
    number_of_papers: int


class Springer(FedySearch):
    # Function to call the API and retrieve the data
    def Springer_API_Call(self):
        """
        Make API Call to Springer for Academic Publication Data
        
        This method makes an API call to the Springer API to retrieve academic publication data based
        on provided search criteria. The retrieved data is converted into a Pandas DataFrame.
        
        Returns:
        pd.DataFrame: A DataFrame containing raw academic publication data from the Springer API.
        """

        api_key = '790713ded66fe0dd637dd61f70925146'
        headers = {'Authorization': 'Bearer {}'.format(api_key)}  # Setting the authorization key in the headers
        search_api_url = 'https://api.springernature.com/metadata/json'  # URL for the API endpoint
        payload = dict(api_key=api_key, q=self.search_keyword, p=self.number_of_papers)  # Payload for the GET \
        # request
        response = requests.get(search_api_url, headers=headers, params=payload).json()
        # Convert response to Pandas DataFrame
        return pd.DataFrame(response['records'])

    # Function for processing the data
    def Springer_Processed_Table(self) -> pd.DataFrame:
        """
        Process Academic Publication Data from Springer API
        
        This method retrieves academic publication data from the Springer API through the
        'Springer_API_Call' method and processes it into a structured Pandas DataFrame.
        
        Returns:
            pd.DataFrame: A DataFrame containing processed publication data with columns
            for title, publication date, DOI, and abstract.
        """

        processed_table = pd.DataFrame()
        messy_data = self.Springer_API_Call()

        processed_table['title'] = messy_data['title']
        # processed_table['authors'] = messy_data['creators'].apply(lambda x: [i['creator'] for i in x])
        processed_table['date'] = messy_data['publicationDate']
        processed_table['doi'] = messy_data['url'].apply(lambda x: x[0]['value'])
        processed_table['abstract'] = messy_data['abstract']

        return processed_table


class Arxiv(FedySearch):

    def Arxiv_Processed_Table(self) -> pd.DataFrame:
        """
        Process Academic Publication Data from arXiv API
        
        This method makes an API call to the arXiv API to retrieve academic publication data based
        on provided search criteria. The retrieved data is processed and organized into a Pandas DataFrame.
        
        Returns:
            pd.DataFrame: A DataFrame containing processed academic publication data from the arXiv API.
        """

        url = f'http://export.arxiv.org/api/query?search_query=all:{self.search_keyword}&start=0&max_results={self.number_of_papers}'
        data = requests.get(url)
        soup = BeautifulSoup(data.content, 'html.parser')

        titles = [title.text for title in soup.find_all('title')[-self.number_of_papers:]]
        paper_links = [paperlink.text for paperlink in soup.find_all('id')[-self.number_of_papers:]]
        published_dates = [publishedDate.text for publishedDate in soup.find_all('published')[-self.number_of_papers:]]
        abstracts = [abstract.text for abstract in soup.find_all('summary')[-self.number_of_papers:]]
        # authors = [author.text for author in soup.find_all('name')]

        dataset = pd.DataFrame({

            'title': titles,
            'paper_link': paper_links,
            'published_date': published_dates,
            'abstract': abstracts,
            # 'author': authors

        })

        return dataset


# Streamlite Application

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.write("")

with col2:
    st.title(".......FedySearch 📚")
    st.markdown("*An API-Powered Publication Searching Tool*")
    st.write("")

with col3:
    st.write("")

st.write("")
journal = st.radio('Select Journal', ['None', 'Springer', 'Arxiv'])
keyword = st.text_input('Enter keywords or phrases')
numpaper = st.slider('Select number of papers', 1, 100)

if st.button('search'):

    if journal == "None":
        st.error('Please select from any of the available journals!')

    elif keyword == "":
        st.error('Please enter a keyword or phrase!')

    elif journal == "Springer":
        app = Springer(keyword, numpaper)
        data = app.Springer_Processed_Table()
        st.dataframe(data)


        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')


        csv = convert_df(data)

        st.download_button(
            "Download Papers",
            csv,
            "FedySearch_Papers.csv",
            key="download-csv"
        )

    elif journal == "Arxiv":
        app = Arxiv(keyword, numpaper)
        data = app.Arxiv_Processed_Table()
        st.dataframe(data)


        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')


        csv = convert_df(data)

        st.download_button(
            "Download Papers",
            csv,
            "FedySearch_Papers.csv",
            key="download-csv"
        )
