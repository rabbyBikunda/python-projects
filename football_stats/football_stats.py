import requests
import json
from datetime import datetime

API_KEY = ''
BASE_URL = 'https://api-football-v1.p.rapidapi.com/v3/'

headers = {
    'x-rapidapi-host': 'api-football-v1.p.rapidapi.com'
}

def get_live_scores():
    """Fetches live football scores and match statistics."""
    url = f"{BASE_URL}fixtures"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return
    data = response.json()
    if data['response']:
        for match in data['response']:
            home_team = match['teams']['home']['name']
            away_team = match['teams']['away']['name']
            score_home = match['goals']['home']
            score_away = match['goals']['away']
            status = match['fixture']['status']['long']
            print(f"{home_team} vs {away_team}")
            print(f"Score: {score_home} - {score_away}")
            print(f"Status: {status}")
            print("-" * 30)
    else:
        print("No live matches at the moment.")

def get_match_statistics(fixture_id):
    """Fetches detailed statistics for a specific match."""
    url = f"{BASE_URL}fixtures/statistics?fixture={fixture_id}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return
    data = response.json()
    if data['response']:
        stats = data['response'][0]
        print(f"Match Statistics for Fixture ID {fixture_id}:")
        for stat in stats['statistics']:
            print(f"{stat['type']}: {stat['value']}")
            print("-" * 30)
    else:
        print("No statistics available for this match.")

def main():
    """Main function to interact with the user."""
    print("Welcome to the Live Football Scores and Statistics App!\n")
    while True:
        print("1. View Live Scores")
        print("2. View Match Statistics")
        print("3. Exit")
        choice = input("Please select an option (1/2/3): ")
        if choice == '1':
            get_live_scores()
        elif choice == '2':
            fixture_id = input("Enter the fixture ID: ")
            get_match_statistics(fixture_id)
        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
