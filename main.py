from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# Setup driver
driver = webdriver.Chrome()

# Target website (example)
driver.get("https://www.bold.org/scholarships/")

time.sleep(5)

scholarships = []

elements = driver.find_elements(By.CLASS_NAME, "ScholarshipCard")

keywords = ["cybersecurity", "technology", "minority", "financial"]

for el in elements:
    title = el.text.lower()

    if any(keyword in title for keyword in keywords):
        scholarships.append(title)

# Save to JSON
with open("scholarships.json", "w") as f:
    json.dump(scholarships, f, indent=4)

print("Scraping complete. Saved to scholarships.json")

driver.quit()
