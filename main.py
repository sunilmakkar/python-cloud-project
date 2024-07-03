import requests
import pandas as pd
from tabulate import tabulate  # Import tabulate for table formatting
from data_manipulation import manipulate_data

def fetch_jobs_data(url):
    # Fetch JSON data from the API
    response = requests.get(url)
    data = response.json()
    return data

def display_table(df):
    # Format DataFrame as a table using tabulate
    table = tabulate(df, headers='keys', tablefmt='fancy_grid')
    print(table)

def main():
    url = 'https://www.themuse.com/api/public/jobs?page=50'  # Update with your API URL
    jobs_data = fetch_jobs_data(url)
    manipulated_df = manipulate_data(jobs_data)
    
    # Display the manipulated DataFrame as a table
    display_table(manipulated_df)
    
    # Save manipulated data to CSV locally
    csv_filename = 'manipulated_data.csv'
    manipulated_df.to_csv(csv_filename, index=False)
    print(f"\nManipulated data saved to {csv_filename}")

if __name__ == '__main__':
    main()
