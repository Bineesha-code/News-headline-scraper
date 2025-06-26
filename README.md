News Headlines Web Scraper
--------------------------

Description:
A simple Python script to scrape top news headlines from a website. Headlines are saved into a text file for offline viewing or further processing.

Features:
- Fetches HTML content of a public news website
- Saves all collected headlines into a text file
- Handles network errors
- 
Functions:
- Uses requests to send an HTTP GET request to fetch webpage content
- Parses HTML using BeautifulSoup to locate '<h2>' and '<title>' elements
- Extracts and stores each headline in a list
- Writes all collected headlines into 'headlines.txt'
- Demonstrates basic Python concepts: string manipulation, list handling, loops, conditionals, file I/O

Tools used:
- Python 3 – Core programming language used to build the scraper.
- BeautifulSoup – HTML parsing and content extraction.
- Requests – To fetch HTML content from the news site.
- VS Code – Used to write and edit the  script.
- Terminal / Command Prompt – Interface to run and test the script.


