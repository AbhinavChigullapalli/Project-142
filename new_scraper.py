from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

brown_dwarf_data = []

def scrape_more_data(hyperlink):
    print(hyperlink)
    
    ## ADD CODE HERE ##
    try:
        url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

        page = requests.get(url)

        soup = bs(page.text, 'html.parser')

        star_table = soup.find_all('table')

        table_rows = star_table[7].find_all('tr')

        star_list = []

        for tr_tag in soup.find_all("tr",attrs={"class":"fact_row"}):
            td_tags = tr_tag.find_all("td")

            for td_tag in td_tags:
                try:
                    star_list.append(td_tag.find_all("div", attrs={"class":"value"}[0].contents[0]))
                except:
                    star_list.append("")

        brown_dwarf_data.append(star_list)

    except:
        time.sleep(1)
        scrape_more_data(hyperlink)



# Call method

print(brown_dwarf_data)

# Remove '\n' character from the scraped data
scraped_data = []

for row in brown_dwarf_data:
    replaced = []
    ## ADD CODE HERE ##
    for el in row:
        el = el.replace("/n", "")
        replaced.append(el)
    
    scraped_data.append(replaced)

print(scraped_data)

headers = ["star_name", "radius", "mass", "distance_data"]

new_planet_df_1 = pd.DataFrame(scraped_data,columns = headers)

# Convert to CSV
new_planet_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")
