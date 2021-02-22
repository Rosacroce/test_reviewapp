import spacy
import streamlit as st
import pandas as pd
from Explanation import show_explanation

#nlp = spacy.load("en_core_web_sm")


if __name__ == "__main__":

    # Add title on the page
    st.title("Test Heroku Pipelines & Review Apps")

    # Filters
    # For testing purposes the filter is currently implemented on the 'Document Naam' column of the database.
    st.sidebar.markdown("**Filters**")
    year_min = 3
    year_max = 12
    filter_year = st.sidebar.slider("Publicatiejaar", year_min, year_max, (year_min, year_max), 1)


    # Ask user for input text
    input_sent = st.text_input("Text Input")
    df = pd.DataFrame({
        'Document Naam': list(range(3, 12)),
        'Matching score': list(range(4, 13)),
        'URL': list(range(4, 13)),
        'Matching sentences': list(range(4, 13)),
        })

    # df showing filtered values
    df_write = df[(df['Document Naam'] >= filter_year[0]) & (df['Document Naam'] <= filter_year[1])]

    for index, row in df_write.iterrows():
        st.markdown(f"## Document Naam: {row['Document Naam']}")
        st.markdown(f"**Matching score:** {row['Matching score']}")
        st.markdown(f"**URL:** {row['URL']}")
        st.markdown(f"**Matching sentences:** {row['Matching sentences']}")


    ##
    show_explanation()
