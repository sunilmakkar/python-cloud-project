import requests
import pandas as pd
from tabulate import tabulate  # Import tabulate for table formatting

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
            'company_name': job['company']['name'],
            'country': country,
            'city': city,
            'job_name': job['name'],
            'job_type': job['type'],
            'date': date,
        }
        jobs.append(job_info)
    
    df = pd.DataFrame(jobs)
    return df
