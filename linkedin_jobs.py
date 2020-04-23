## All Imports
from driverutils import ChromeBot
from time import sleep
import pandas as pd

## Parameters
URL_LINKEDIN = 'https://br.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas?position=1&pageNum=0'

# XPATHS
DESCRIPTION = '//*[@id="main-content"]/section/div[2]/section[2]/div'
JOB_CRITERIA='//*[@id="main-content"]/section/div[2]/section[2]/ul'
JOB_TITLE = '//*[@id="main-content"]/section/div[2]/section[1]/div[1]/div[1]/a/h2'
COMPANY = '//*[@id="main-content"]/section/div[2]/section[1]/div[1]/div[1]/h3[1]/span[1]'
LOCATION = '//*[@id="main-content"]/section/div[2]/section[1]/div[1]/div[1]/h3[1]/span[2]'
JOB_RESULTS_BAR = '//*[@id="main-content"]/div/section/ul/li'

## Classes and Functions

## Execution

# Scrap with Selenium
c = ChromeBot()
c.driver.implicitly_wait(5)
c.driver.get(URL_LINKEDIN)

all_description = []
all_locations = []
all_titles = []
all_company = []
all_criterias = []

len_results = 0
print(len_results)
all_results = c.driver.find_elements_by_xpath(JOB_RESULTS_BAR)
print(len(all_results))
while len(all_results)>len_results:
    for r in all_results[len_results:]:
        r.click()
	sleep(1)
        description = c.driver.find_element_by_xpath(DESCRIPTION).text
        location = c.driver.find_element_by_xpath(LOCATION).text
        company = c.driver.find_element_by_xpath(COMPANY).text
        title = c.driver.find_element_by_xpath(JOB_TITLE).text
        criteria = c.driver.find_element_by_xpath(JOB_CRITERIA).text

        all_description.append(description)
        all_locations.append(location)
        all_titles.append(title)
        all_company.append(company)
        all_criterias.append(criteria)

	print(all_locations)
	print(all_company)
	print(all_titles)

    len_results = len(all_results)
    all_results = c.driver.find_elements_by_xpath('//*[@id="main-content"]/div/section/ul/li')
    print(len_results)
    print(len(all_results))

# Export to CSV
export_data = {'company':all_company, 'title':all_titles, 'location': all_locations, 'criteria':all_criterias, 'description':all_description}
df = pd.DataFrame(export_data)
print(df.head())
df.to_csv('linkedin_data_science_jobs.csv')

