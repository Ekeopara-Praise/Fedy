import streamlit as st
import pandas as pd

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.write("")

with col2:
    st.image("logo.PNG")

with col3:
    st.write("")

st.text_input('Enter keywords or phrases')
st.slider('Select number of papers', 1, 50)
st.button('search')

test2 = [{'contentType': 'Article', 'identifier': 'doi:10.1007/s44243-022-00003-6', 'language': 'en',
          'url': [{'format': '', 'platform': '', 'value': 'http://dx.doi.org/10.1007/s44243-022-00003-6'}],
          'title': 'Launch editorial', 'creators': [{'creator': 'Wu, Zhiqiang Siegfried'}],
          'publicationName': 'Frontiers of Urban and Rural Planning', 'openaccess': 'true',
          'doi': '10.1007/s44243-022-00003-6', 'publisher': 'Springer', 'publicationDate': '2023-12-01',
          'publicationType': 'Journal', 'issn': '2731-6661', 'volume': '1', 'number': '1',
          'genre': ['EditorialNotes', 'Editorial'], 'startingPage': '1', 'endingPage': '2', 'journalId': '44243',
          'copyright': '©2023 The Author(s)', 'abstract': '',
          'subjects': ['Architecture / Design', 'Landscape Architecture']},
         {'contentType': 'Article', 'identifier': 'doi:10.1007/s44243-022-00005-4', 'language': 'en',
          'url': [{'format': '', 'platform': '', 'value': 'http://dx.doi.org/10.1007/s44243-022-00005-4'}],
          'title': 'Thoughts and exploration of spatial planning system in the new era',
          'creators': [{'creator': 'Wang, Kai'}, {'creator': 'Hu, Jingjing'}],
          'publicationName': 'Frontiers of Urban and Rural Planning', 'openaccess': 'true',
          'doi': '10.1007/s44243-022-00005-4', 'publisher': 'Springer', 'publicationDate': '2023-12-01',
          'publicationType': 'Journal', 'issn': '2731-6661', 'volume': '1', 'number': '1',
          'genre': ['OriginalPaper', 'Research Article'], 'startingPage': '1', 'endingPage': '6', 'journalId': '44243',
          'copyright': '©2023 The Author(s)',
          'abstract': 'Spatial planning is a core requirement and a major initiative in the construction of ecological civilization in China, and the related work is in a process of gradual improvement and perfection. Based on the need of natural environment, urbanization and human well-being, this paper discusses the contents and technical directions of the current spatial planning in China from the national, regional and habitat levels, in the hope that it will be benefit current planning practice and provide references for further refinement of spatial planning system and technical routes in China.',
          'subjects': ['Architecture / Design', 'Landscape Architecture']}]

df = pd.DataFrame(test2)

# df = pd.DataFrame(test)
processed_table = pd.DataFrame()

processed_table['title'] = df['title']
processed_table['authors'] = df['creators'].apply(lambda x: [i['creator'] for i in x])
# processed_table['authors'] = processed_table.explode('authors')
processed_table['year'] = df['publicationDate']
processed_table['doi'] = df['url'].apply(lambda x: x[0]['value'])
processed_table['abstract'] = df['abstract']

st.table(processed_table)


# download
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')


csv = convert_df(processed_table)

st.download_button(
    "Download Papers",
    csv,
    "FedySearch_Papers.csv",
    key="download-csv"
)

# st.number_input('Enter number of papers', 1, 50)
#
#
# st.radio('Pick one', ['High', 'Low'])
# st.selectbox('Select one', ['High', 'Low'])
# st.multiselect('Choose', [1, 2, 3, 4, 5])
# st.slider('Pick number of papers', 1,50)
# st.balloons()
# st.markdown('this is a header')
# st.title("my first try")
# st.write('Hi, Praise.... Is working')
