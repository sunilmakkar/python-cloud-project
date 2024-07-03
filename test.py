import requests
import pandas as pd
from tabulate import tabulate

def fetch_jobs_data(url):
    # Fetch JSON data from the API
    response = requests.get(url)
    data = response.json()
    return data

def manipulate_data(data):
    jobs = []
    for job in data['results']:
        # Extracting country and city from locations
        locations = job['locations']
        country = locations[0]['name'] if locations else None
        city = locations[1]['name'] if len(locations) > 1 else None
        
        # Extracting date part from publication date
        publication_date = job['publication_date']
        date = publication_date.split('T')[0] if publication_date else None
        
        job_info = {
            'Publication Date': date,
            'Job Type': job['type'],
            'Job': job['name'],
            'Company': job['company']['name'],
            'City': city,
            'Country': country,
        }
        jobs.append(job_info)
    
    df = pd.DataFrame(jobs)
    return df

def display_table(df):
    # Format DataFrame as a table using tabulate with 'fancy_grid' formatting
    table = tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False)
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

