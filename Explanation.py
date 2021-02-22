# flake8: noqa
import streamlit as st


def show_explanation() -> None:
    st.subheader("Hoe deze app werkt")
    st.write(f"""

Here we can write a lot! **search**

#### Filters
You can refine your query based on the publication year, paper content, field of study and author. You can also combine any of the filter for more granular searches.
- **Filter by year**: Select a time range for the papers. For example, drag both sliders to 2020 to find out the papers that will be presented at ACL 2020.
- **Field of Study level**: Microsoft Academic Graph uses a 6-level hierarchy where level 0 contains high level disciplines such as Computer science and level 5 contains the most granular paper keywords. This filter will change what's shown in the bar chart as well as the available options in the filter below.
- ** Fields of Study**: Select the Fields of Study to be displayed in the visualisations. The available options are affected by your selection in the above filter.
- **Search by author name**: Find an author's publications. **Note**: You need to type in the exact name.
- **Search by paper title**: Type in a paper title and find its most relevant relevant publications. You should use at least a sentence to receive meaningful results.
- **Number of search results**: Specify the number of papers to be returned when you search by paper title.
    """)

    st.subheader("About")
    st.write(
            f"""
We zijn [Artyficial](https://www.artyficial.info/).
U kunt ons op onze [website](https://www.artyficial.info/contact/) benaderen of met een email aan ai@artyficial.info
    """
        )

    st.subheader("Appendix: Data")
    st.write(f"""
Data was verzamelt op [website1](website1)
            [website2](website1)
[website3](website1)
""")