import pandas as pd
import requests
import openai
import streamlit as st

SEARCH_API_KEY = '########################################'
OPENAI_API_KEY = '########################################'
openai.api_key = OPENAI_API_KEY

def perform_search(entity, query_template):
    query = query_template.replace("[Entity]", entity)
    url = f'https://api.bing.microsoft.com/v7.0/search?q={query}'
    headers = {'Ocp-Apim-Subscription-Key': SEARCH_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def parse_search_results_with_llm(results_text, entity):
    prompt = f"Summarize the main information about {entity} based on the following search results:\n\n{results_text}"
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

st.title("AI-Powered Web Search and Parsing Tool")
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    st.write(df.head())

    column_choice = st.selectbox("Select the column with entities", df.columns)
    query_template = st.text_input("Enter your query template (use [Entity] as placeholder)",
                                   "Find the latest news about [Entity]")

    if st.button("Run Search"):
        st.write("Starting search for each entity...")
        results = []

        for entity in df[column_choice]:
            search_result = perform_search(entity, query_template)
            if search_result:
                snippets = ' '.join([item['snippet'] for item in search_result.get('webPages', {}).get('value', [])])
                structured_result = parse_search_results_with_llm(snippets, entity)
                results.append({"Entity": entity, "Result": structured_result})
            else:
                results.append({"Entity": entity, "Result": "No results found"})

        results_df = pd.DataFrame(results)
        st.write("Search Results:")
        st.write(results_df)

        csv = results_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Results as CSV", data=csv, file_name="search_results.csv", mime="text/csv")
