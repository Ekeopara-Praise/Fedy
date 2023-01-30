import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="👋",
)

st.write("# Welcome to FedySearch! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    FedySearch is a research federated search system, designed for researchers and 
    students, giving them the ability to search and download a collection of literatures with organic information 
    such as **name of authors**, **titles**, **doi**, **publication date**, **abstract** etc. from multiple sources. **👈 Select a demo from the 
    sidebar** to see what FedySearch can do!
    
    ### Integrated Publication Sources
    While sourcing for publication sources, FedySearch in its prototype stage, currently runs on the following sources;
    - [**Springer**](https://link.springer.com/)
    - [**arXiv**](https://arxiv.org/)
    - To be updated
    
    ### Key Advantages of FedySearch?
    - Easier collaborative research
    - Faster Publication Sourcing
    - Efficient filtered research based on research interests
    - Customizable and reproducible codes for developers and researchers to improve on
    - Faster access to large pull of Literatures and publications leveraging API connections
    - Open source tool under steady improvement
            
    ### Open for contributors
    FedySearch welcomes contributions from other developers and non-developers, 
    and if you’re one kindly contact Praise by email ekeoparapraise@gmail.com 
    or [linkedln](https://www.linkedin.com/in/praiseekeopara/)


    Copyright (c) 2023 [Praise Ekeopara](https://www.linkedin.com/in/praiseekeopara)
"""
)