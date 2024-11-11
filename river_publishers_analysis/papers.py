import requests
from bs4 import BeautifulSoup
import pandas as pd  # You'll need pandas to create a DataFrame
from database import store_data_to_sql  # Assuming the function is in a file called 'database.py'

# URL of the webpage you want to scrape
url = 'https://journals.riverpublishers.com/index.php/JWE/issue/view/1919'

# Fetch the page content
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <a> tags with an id attribute (for titles)
    articles = soup.find_all('a', id=True)

    # Create lists to store titles and authors
    titles = []
    authors = []

    # Extract the id and title for each article
    for article in articles:
        # Extract the title (text inside the <a> tag)
        title = article.get_text(strip=True)

        # Extract the ID (article-<number>)
        article_id = article.get('id')

        author_tag = article.find_next('div', class_='authors')
        author_name = author_tag.get_text(strip=True) if author_tag else 'Unknown'

        # Add the title and author if valid
        if article_id and title:
            titles.append(title)
            authors.append(author_name)

    # Convert the lists of titles and authors into a pandas DataFrame
    if titles and authors:
        df = pd.DataFrame({
            "Research_Papers_Title": titles,
            "Authors": authors
        })

        # Print the titles and authors before storing them in the database
        print("Titles and Authors to be stored in the database:")
        print(df)

        # Store the data in the database
        store_data_to_sql(df, table_name="block_chain")
        print("Titles and authors successfully stored in the database.")
    else:
        print("No titles or authors found.")
else:
    print("Failed to retrieve the page")
