import sqlite3
import pandas as pd
from matplotlib import pyplot as plt


def store_data_to_sql(df, table_name):
    conn = sqlite3.connect("../analysis.db")
    df.to_sql(table_name, conn, if_exists="append", index=False)
    conn.close()
    return df

    return df['Research_Papers_Title'].tolist()


def fetch_titles_from_table(table_name):
    conn = sqlite3.connect('../analysis.db')  # Use the correct path to your database
    query = "SELECT Research_Papers_Title FROM block_chain"
    df = pd.read_sql(query, conn)
    conn.close()
    return df['Research_Papers_Title'].tolist()


# Fetch titles from both tables
block_chain_titles = fetch_titles_from_table('block_chain')
research_papers_titles = fetch_titles_from_table('Research Papers')


# Define a function to count keyword occurrences in titles
def count_keywords(titles, keywords):
    keyword_counts = {keyword: 0 for keyword in keywords}

    for title in titles:
        for keyword in keywords:
            if keyword.lower() in title.lower():
                keyword_counts[keyword] += 1

    return keyword_counts


# Define the keywords we're interested in
keywords = ['Blockchain', 'AI', "Machine Learning"]

# Count occurrences of keywords in both tables
block_chain_keyword_counts = count_keywords(block_chain_titles, keywords)
research_papers_keyword_counts = count_keywords(research_papers_titles, keywords)

# Prepare data for plotting
data = {
    'Blockchain': [block_chain_keyword_counts['Blockchain'], research_papers_keyword_counts['Blockchain']],
    'Data Science': [block_chain_keyword_counts['AI'], research_papers_keyword_counts['AI']],
'Machine Learning': [block_chain_keyword_counts['Machine Learning'], research_papers_keyword_counts['Machine Learning']],

}


# Create a DataFrame to organize the data
df_comparison = pd.DataFrame(data, index=['Block_chain', 'Research Papers'])
# Print data structures to verify
print("block_chain_keyword_counts:", block_chain_keyword_counts)
print("research_papers_keyword_counts:", research_papers_keyword_counts)
print("df_comparison DataFrame:\n", df_comparison)

# Plotting the data as a bar chart
df_comparison.plot(kind='bar', figsize=(6, 5))
plt.title('Comparison of Blockchain vs Data Science in Research Papers')
plt.ylabel('Count of Occurrences')
plt.xlabel('Table')
plt.xticks(rotation=0)
plt.tight_layout()

# Show the plot
plt.show()
