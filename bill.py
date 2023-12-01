import random
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def get_existing_links(sheet_name):
    wb = openpyxl.load_workbook('links.xlsx')
    sheet = wb[sheet_name]
    existing_links = [cell.value for cell in sheet['A'] if cell.value]
    return existing_links

def clean_link(link):
    parsed_link = urlparse(link)
    clean_link = parsed_link.scheme + "://" + parsed_link.netloc + parsed_link.path
    return clean_link

def save_to_excel(link, sheet_name, link_suffix=""):
    wb = openpyxl.load_workbook('links.xlsx')
    sheet = wb[sheet_name]
    sheet.append([link + link_suffix])
    wb.save('links.xlsx')

url = "https://www.congress.gov/search?pageSize=250&pageSort=documentNumber%3Adesc&q={%22source%22:%22legislation%22,%22bill-status%22:[%22floor%22,%22passed-one%22]}"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(service=Service('./chromedriver'), options=chrome_options)
driver.get(url)

wait = WebDriverWait(driver, 10)
elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//a[starts-with(@href, "/bill/118th-congress/house-bill/")]')))

# Find all the link elements
elements = driver.find_elements(By.XPATH, '//a[starts-with(@href, "/bill/118th-congress/house-bill/")]')
links = [element.get_attribute('href') for element in elements]

# Get existing links from the used workbook sheet
existing_links_used = get_existing_links('used')

# Select a link that has not been selected before
random_link = None
while not random_link or random_link in existing_links_used:
    random_link = random.choice(links)

# Save the original link to the used sheet in the Excel file
save_to_excel(random_link, 'used')

# Clean the link
simple_link = clean_link(random_link.split('?s=1&r')[0])
# Remove the additional parameters from the link
simple_link = random_link.split('/cosponsors')[0]
simple_link = simple_link.split('/all-actions')[0]

# Save the cleaned link to the both sheets in the Excel file
save_to_excel(simple_link, 'Sheet')
save_to_excel(simple_link, 'text', '/text')

driver.quit()
