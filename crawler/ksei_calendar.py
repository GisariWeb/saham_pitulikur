import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def crawl_ksei_calendar(url="https://www.ksei.co.id/ksei-calendar"):
    """
    Crawls the KSEI calendar page and extracts event data.

    Args:
        url: The URL of the KSEI calendar page.

    Returns:
        A list of dictionaries, where each dictionary
 represents an event
        with keys: 'date', 'day', 'description'.
        Returns None if there's an error during the process.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the calendar table (adjust the selector if needed)
        calendar_table = soup.find('table', class_='table table-bordered')
        if not calendar_table:
            print("Error: Calendar table not found on the page.")
            return None
        
        # Find all rows in the calendar
        rows = calendar_table.find_all('tr')
        
        events = []
        # Iterate through rows (skip header row)
        for row in rows[1:]: 
            cols = row.find_all('td')
            if len(cols) >= 3:
                date_str = cols[0].text.strip()
                day = cols[1].text.strip()
                description = cols[2].text.strip()
                
                # convert date_str to isoformat
                date_obj = datetime.strptime(date_str, '%d %B %Y')
                date = date_obj.strftime('%Y-%m-%d')
                
                events.append({
                    'date': date,
                    'day': day,
                    'description': description
                })
        return events

    except requests.exceptions.RequestException as e:
        print(f"Error during HTTP request: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def save_to_json(data, filename="ksei_calendar.json"):
    """
    Saves the crawled data to a JSON file.

    Args:
        data: The data to save (a list of dictionaries).
        filename: The name of the JSON file.
    """
    if data:
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving data to JSON: {e}")
    else:
        print("No data to save.")

if __name__ == "__main__":
    ksei_events = crawl_ksei_calendar()
    save_to_json(ksei_events)