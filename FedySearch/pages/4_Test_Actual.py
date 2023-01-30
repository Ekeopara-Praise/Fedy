"""
[<author>
<name>Yusef Maleki</name>
</author>, <author>
<name>Bahram Ahansaz</name>
</author>]
"""
"""
[<author>
<name>Yusef Maleki</name>
</author>, <author>
<name>Bahram Ahansaz</name>
</author>, <author>
<name>Vahid Shaghaghi</name>
</author>, <author>
<name>G. Massimo Palma</name>
</author>, <author>
<name>Giuliano Benenti</name>
</author>]
"""
""""
api_key = 'NS9FXsf7e3dkP8KO6xoVbMAG5JLmgra2'
headers = {'Authorization': 'Bearer {}'.format(api_key)}  # Setting the authorization key in the headers
search_api_url = 'https://api.core.ac.uk/'  # URL for the API endpoint
search_keyword = 'Technology'
number_of_papers = '1'
payload = {'api_key': api_key, 'text': search_keyword, 'limit': number_of_papers}  # Payload for the GET \
# request
response = requests.get(search_api_url, headers=headers, params=payload)
print(response.url)
if (
        response.status_code != 204 and
        response.headers["Content-Type"].strip().startswith("application/json")
):
    try:
        print(response.json())

    except:

        print('Error!')  # decide how to handle a server that's misbehaving to this extent


"""
ls = ['Yusef Maleki', 'Bahram Ahansaz', 'Vahid Shaghaghi', 'G. Massimo Palma', 'Giuliano Benenti']

"""
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <link href="http://arxiv.org/api/query?search_query%3Dall%3Atechnology%20in%20health%26id_list%3D%26start%3D0%26max_results%3D2" rel="self" type="application/atom+xml"/>
  <title type="html">ArXiv Query: search_query=all:technology in health&amp;id_list=&amp;start=0&amp;max_results=2</title>
  <id>http://arxiv.org/api/ofrffHNSaVbFCpiuvKWMkd9wSFY</id>
  <updated>2023-01-18T00:00:00-05:00</updated>
  <opensearch:totalResults xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">2040339</opensearch:totalResults>
  <opensearch:startIndex xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">0</opensearch:startIndex>
  <opensearch:itemsPerPage xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">2</opensearch:itemsPerPage>
  <entry>
    <id>http://arxiv.org/abs/1511.02281v1</id>
    <updated>2015-11-07T01:58:51Z</updated>
    <published>2015-11-07T01:58:51Z</published>
    <title>Robotics Technology in Mental Health Care</title>
    <summary>  This chapter discusses the existing and future use of robotics and
intelligent sensing technology in mental health care. While the use of this
technology is nascent in mental health care, it represents a potentially useful
tool in the practitioner's toolbox. The goal of this chapter is to provide a
brief overview of the field, discuss the recent use of robotics technology in
mental health care practice, explore some of the design issues and ethical
issues of using robots in this space, and finally to explore the potential of
emerging technology.
</summary>
    <author>
      <name>Laurel D. Riek</name>
    </author>
    <arxiv:doi xmlns:arxiv="http://arxiv.org/schemas/atom">10.1016/B978-0-12-420248-1.00008-8</arxiv:doi>
    <link title="doi" href="http://dx.doi.org/10.1016/B978-0-12-420248-1.00008-8" rel="related"/>
    <arxiv:journal_ref xmlns:arxiv="http://arxiv.org/schemas/atom">Artificial Intelligence in Behavioral Health and Mental Health
  Care (2015) 185-203;</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/1511.02281v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/1511.02281v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cs.RO" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.RO" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.CY" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.HC" scheme="http://arxiv.org/schemas/atom"/>
    <category term="I.2.9; J.3" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2010.13111v1</id>
    <updated>2020-10-25T13:08:42Z</updated>
    <published>2020-10-25T13:08:42Z</published>
    <title>Develop Health Monitoring and Management System to Track Health
  Condition and Nutrient Balance for School Students</title>
    <summary>  Health Monitoring and Management System (HMMS) is an emerging technology for
decades. Researchers are working on this field to track health conditions for
different users. Researchers emphasize tracking health conditions from an early
stage to the human body. Therefore, different research works have been
conducted to establish HMMS in schools. Researchers propose different
frameworks and technologies for their HMMS to check student's health condition.
In this paper, we introduce a complete and scalable HMMS to track health
conditions and nutrient balance for students from primary school. We define
procedures step by step to establish a robust HMMS where big data methodologies
can be used for further prediction for diseases.
</summary>
    <author>
      <name>Mohammad Ali</name>
    </author>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">10 Pages, 3 Figures, 4 Tables</arxiv:comment>
    <link href="http://arxiv.org/abs/2010.13111v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/2010.13111v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cs.HC" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.HC" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
</feed>


"""

# # Lets  start
# import requests
# import pandas as pd
# from fastapi import FastAPI
#
#
# # define the API key
# api_key = '790713ded66fe0dd637dd61f70925146'
# # headers contain the api key.
# headers = {'Authorization': 'Bearer {}'.format(api_key)}
#
#
# # search_api_url = f'https://api.springernature.com/metadata/json?api_key=790713ded66fe0dd637dd61f70925146&q=Technology&s=1&p={p}'
#
# search_api_url = 'https://api.springernature.com/metadata/json'
#
# payload = {'api_key': api_key, 'q': 'Technology', 'p': 2}
#
# response = requests.get(search_api_url, headers=headers, params=payload) # timeout=2)
#
# res = response.json()
#
# # print(response.url)
# # # print(response.headers)
# # print(response.json())
# # print(response.status_code)
#
# print(res['records'])
