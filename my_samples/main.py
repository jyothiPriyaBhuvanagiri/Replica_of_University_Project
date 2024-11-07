# main.py

from scraping import scrape_data
from database import store_data_to_sql, load_data_from_sql
from analysis import analyze_data
from visualization import plot_publication_volume, plot_interactive_publication_volume

def main():
    df = scrape_data()
    store_data_to_sql(df)
    df = load_data_from_sql()
    df = analyze_data(df)
    plot_publication_volume(df)
    plot_interactive_publication_volume(df)

if __name__ == "__main__":
    main()
