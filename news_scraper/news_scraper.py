import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"

def get_tech_news():
    """Function to scrape the latest tech news from Hacker News"""
    response = requests.get(URL)
    
    if response.status_code != 200:
        print("Failed to retrieve data.")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    stories = soup.find_all('a', class_='storylink')
    
    print("Latest Tech News from Hacker News:\n")
    for idx, story in enumerate(stories[:10], start=1):  # Limit to top 10 stories
        title = story.get_text()
        link = story['href']
        print(f"{idx}. {title}\nLink: {link}\n")
        
def main():
    """Main function to execute the scraping"""
    get_tech_news()

if __name__ == "__main__":
    main()