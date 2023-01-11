import pandas as pd
test = [{'contentType': 'Article', 'identifier': 'doi:10.1007/s42064-022-0152-2', 'language': 'en',
         'url': [{'format': '', 'platform': '', 'value': 'http://dx.doi.org/10.1007/s42064-022-0152-2'}],
         'title': 'Review of space relative navigation based on angles-only measurements',
         'creators': [{'creator': 'Gong, Baichun'}, {'creator': 'Wang, Sha'}, {'creator': 'Li, Shuang'},
                      {'creator': 'Li, Xianqiang'}], 'publicationName': 'Astrodynamics', 'openaccess': 'false',
         'doi': '10.1007/s42064-022-0152-2', 'publisher': 'Springer', 'publicationDate': '2023-06-01',
         'publicationType': 'Journal', 'issn': '2522-0098', 'volume': '7', 'number': '2',
         'genre': ['ReviewPaper', 'Review Article'], 'startingPage': '131', 'endingPage': '152', 'journalId': '42064',
         'copyright': '©2022 Tsinghua University Press', 'abstract': 'Relative navigation is a key enabling technology for space missions such as on-orbit servicing and space situational awareness. '
                                                                     'Given that there are several special advantages of space relative navigation using angles-only measurements from passive optical sensors,'
                                                                     ' angles-only relative navigation is considered as one of the best potential approaches in the field of space relative navigation. '
                                                                     'However, angles-only relative navigation is well-known for its range observability problem. '
                                                                     'To overcome this observability problem, many studies have been conducted over the past decades. '
                                                                     'In this study, we present a comprehensive review of state-of-the-art space relative navigation based on angles-only measurements. '
                                                                     'The emphasis is on the observability problem and solutions to angles-only relative navigation, where the review of the solutions is categorized'
                                                                     ' into four classes based on the intrinsic principle: complicated dynamics approach, multi-line of sight (multi-LOS) approach, '
                                                                     'sensor offset center-of-mass approach, and orbit maneuver approach. Then, the flight demonstration results of angles-only relative '
                                                                     'navigation in the two projects are briefly reviewed. Finally, conclusions of this study and recommendations for further research are presented.',
         'subjects': ['Engineering', 'Aerospace Technology and Astronautics', 'Space Sciences (including Extraterrestrial Physics, Space Exploration and Astronautics)', 'Vibration, Dynamical Systems, Control']}]

# # print(len(test[0].get('contentType')))
# contentType = test[0]['contentType']
# title = test[0]['title']
# author = test[0]['creators']
# doi = test[0]['url'][0]['value']
# openaccess = test[0]['openaccess']
# publicationType = test[0]['publicationType']
# publisher = test[0]['publisher']
# publicationDate = test[0]['publicationDate']
# abstract = test[0]['abstract']
# subjects = test[0]['subjects']
#
# data = pd.DataFrame({'contentType': contentType,
#                      'title': title,
#                      'author': author,
#                      'doi': doi,
#                      'openaccess': openaccess,
#                      'publicationType': publicationType,
#                     'publisher': publisher,
#                      'publicationDate': publicationDate,
#                      'abstract': abstract,
#                      'subjects': subjects})
#
# print(data)

test2 = [{'contentType': 'Article', 'identifier': 'doi:10.1007/s44243-022-00003-6', 'language': 'en', 'url': [{'format': '', 'platform': '', 'value': 'http://dx.doi.org/10.1007/s44243-022-00003-6'}], 'title': 'Launch editorial', 'creators': [{'creator': 'Wu, Zhiqiang Siegfried'}], 'publicationName': 'Frontiers of Urban and Rural Planning', 'openaccess': 'true', 'doi': '10.1007/s44243-022-00003-6', 'publisher': 'Springer', 'publicationDate': '2023-12-01', 'publicationType': 'Journal', 'issn': '2731-6661', 'volume': '1', 'number': '1', 'genre': ['EditorialNotes', 'Editorial'], 'startingPage': '1', 'endingPage': '2', 'journalId': '44243', 'copyright': '©2023 The Author(s)', 'abstract': '', 'subjects': ['Architecture / Design', 'Landscape Architecture']}, {'contentType': 'Article', 'identifier': 'doi:10.1007/s44243-022-00005-4', 'language': 'en', 'url': [{'format': '', 'platform': '', 'value': 'http://dx.doi.org/10.1007/s44243-022-00005-4'}], 'title': 'Thoughts and exploration of spatial planning system in the new era', 'creators': [{'creator': 'Wang, Kai'}, {'creator': 'Hu, Jingjing'}], 'publicationName': 'Frontiers of Urban and Rural Planning', 'openaccess': 'true', 'doi': '10.1007/s44243-022-00005-4', 'publisher': 'Springer', 'publicationDate': '2023-12-01', 'publicationType': 'Journal', 'issn': '2731-6661', 'volume': '1', 'number': '1', 'genre': ['OriginalPaper', 'Research Article'], 'startingPage': '1', 'endingPage': '6', 'journalId': '44243', 'copyright': '©2023 The Author(s)', 'abstract': 'Spatial planning is a core requirement and a major initiative in the construction of ecological civilization in China, and the related work is in a process of gradual improvement and perfection. Based on the need of natural environment, urbanization and human well-being, this paper discusses the contents and technical directions of the current spatial planning in China from the national, regional and habitat levels, in the hope that it will be benefit current planning practice and provide references for further refinement of spatial planning system and technical routes in China.', 'subjects': ['Architecture / Design', 'Landscape Architecture']}]

df = pd.DataFrame(test2)
print(df)