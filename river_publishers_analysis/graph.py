
import sqlite3


def test_query():
    conn = sqlite3.connect('../analysis.db')  # Use the correct path to your database
    cursor = conn.cursor()

    # Test the query to check if we can fetch titles
    cursor.execute("SELECT Research_Papers_Title FROM block_chain")
    rows = cursor.fetchall()

    if rows:
        print("Data from block_chain table:")
        for row in rows:
            print(row)
    else:
        print("No data found in block_chain table.")

    conn.close()


test_query()

