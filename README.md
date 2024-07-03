# Project Title

Data Python Cloud Project: Scraping Job Data and Uploading to S3

## Project Description

This project involves scraping job data from a website's API, processing it into JSON format, and converting it into a CSV file. The CSV file is then uploaded to an S3 bucket for storage and further analysis.

## Table of Contents (Optional)

- [How to Install and Run the Project](#how-to-install-and-run-the-project)
- [How to Use the Project](#how-to-use-the-project)
- [How to do Tests](#how-to-do-tests)

## How to Install and Run the Project

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/sunilmakkar/python-cloud-project.git
   cd python-cloud-project ```

2. **Install Dependencies:**

Ensure you have Python installed. Install necessary dependencies using pip:

```
    pip install -r requirements.txt
```

3. **Run the Script:**

Run the Pthon script to scrape job data, convert it into a CSV file, and upload it to S3.

```
    python main.py
```
## How to Install and Run the Project

- Ensure you have access to the website's API from which job data is being scraped.
- Configure API credentials and endpoint URLs in config.toml or environment variables.
- Run the script as described in the run.sh script to automate the scraping, processing, and uploading process.

## How to Install and Run the Project

- Tests can be implemented using Python's built-in unittest module or other testing frameworks.
- Write test cases to validate scraping functionality, CSV conversion, and S3 upload.

- Run tests using:

```
    python -m unittest test.py
```
