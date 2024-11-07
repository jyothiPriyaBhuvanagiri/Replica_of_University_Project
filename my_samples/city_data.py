import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import plotly.express as px


# Step 1: Scraping Data
def scrape_data():
    # Implement scraping logic or use static data for demonstration
    data = {
        'year': [2018, 2018, 2019, 2019, 2020, 2020, 2021, 2021, 2022, 2022],
        'num_publications': [50, 60, 65, 70, 80, 85, 95, 100, 110, 115],
        'topic': ['AI', 'Data Science', 'AI', 'Data Science', 'AI', 'Data Science', 'AI', 'Data Science', 'AI',
                  'Data Science']
    }
    return pd.DataFrame(data)


# Step 2: Storing Data in SQL
def store_data_to_sql(df):
    conn = sqlite3.connect("../research_data.db")
    df.to_sql("publications", conn, if_exists="replace", index=False)
    conn.close()


# Step 3: Loading and Cleaning Data
def load_data_from_sql():
    conn = sqlite3.connect("../research_data.db")
    df = pd.read_sql("SELECT * FROM publications", conn)
    conn.close()
    return df


# Step 4: Analyzing Data
def analyze_data(df):
    df['growth_rate'] = df.groupby('topic')['num_publications'].pct_change() * 100
    df['growth_rate'] = df['growth_rate'].round(2)
    return df


# Step 5: Visualizations with Matplotlib and Plotly
def plot_publication_volume(df):
    plt.figure(figsize=(10, 6))
    for topic in df['topic'].unique():
        topic_data = df[df['topic'] == topic]
        plt.plot(topic_data['year'], topic_data['num_publications'], label=topic)
    plt.title("Publication Volume Over Time by Topic")
    plt.xlabel("Year")
    plt.ylabel("Number of Publications")
    plt.legend(title="Topic")
    plt.show()


def plot_interactive_publication_volume(df):
    fig = px.line(df, x='year', y='num_publications', color='topic', markers=True,
                  title="Interactive Publication Volume Over Time by Topic")
    fig.show()


# Main pipeline function
def main():
    # Scrape data
    df = scrape_data()
    store_data_to_sql(df)

    # Load, analyze, and visualize
    df = load_data_from_sql()
    df = analyze_data(df)
    plot_publication_volume(df)
    plot_interactive_publication_volume(df)


# Run the pipeline
if __name__ == "__main__":
    main()
