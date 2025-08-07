from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "C:\\chromedriver\\chromedriver.exe"  # DOUBLE BACKSLASHES

options = Options()
options.add_argument('--headless')  # Optional
options.add_argument('--disable-gpu')

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=options)


# ✅ Load the website
driver.get("https://inshorts.com/en/read")
time.sleep(3)  # wait for JS to load

# ✅ Get page source after JS execution
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# ✅ Extract news headlines
headline_tags = soup.find_all("div", class_="news-card-title")

# ✅ Save to file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for tag in headline_tags:
        headline = tag.find("span").get_text(strip=True)
        file.write(headline + "\n")

driver.quit()
print("✅ Headlines scraped and saved to 'headlines.txt'")
