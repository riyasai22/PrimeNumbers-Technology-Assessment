from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'

driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)  # time for dynamic content to load

soup = BeautifulSoup(driver.page_source, 'html.parser')
postings = soup.find(class_='datatable').find('tbody')

# Extract required fields from each posting
for posting in postings.find_all('tr')[:5]:
    date = posting.find_all('td')[0].text
    quest_no=posting.find_all('td')[1].text
    category_code = posting.find_all('td')[2].text
    bid = posting.find_all('td')[3].text
    closing_date = posting.find_all('td')[4].text
    city = posting.find_all('td')[5].text
    country= posting.find_all('td')[6].text
    state= posting.find_all('td')[7].text
    owner= posting.find_all('td')[8].text
    solicitor= posting.find_all('td')[8].text
    posting_type= posting.find_all('td')[9].text


    # Display the extracted information
    print("1. Est. Value Notes:", category_code)
    print('2. Description:',
          f'    \n - Bid Name :{bid} '
          f'    \n - Owner: {owner} '
          f'    \n - Posting Type: {posting_type}')
    print("3. Closing Date:", closing_date)
    print("\n")

driver.quit()  # Close the browser

