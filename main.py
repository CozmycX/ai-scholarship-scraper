from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import csv

# Setup driver
driver = webdriver.Chrome()

keywords = ["cybersecurity", "technology", "minority", "financial"]

results = []

def scrape_bold():
    print("Scraping Bold.org...")
    driver.get("https://www.bold.org/scholarships/")
    time.sleep(5)

    try:
        cards = driver.find_elements(By.CLASS_NAME, "ScholarshipCard")

        for card in cards:
            text = card.text.lower()

            if any(keyword in text for keyword in keywords):
                results.append({
                    "source": "Bold.org",
                    "description": text
                })
    except Exception as e:
        print("Error scraping Bold:", e)


def save_json():
    with open("scholarships.json", "w") as f:
        json.dump(results, f, indent=4)


def save_csv():
    with open("scholarships.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["source", "description"])
        writer.writeheader()
        writer.writerows(results)


def main():
    scrape_bold()
    save_json()
    save_csv()

    print(f"Saved {len(results)} scholarships.")


main()
driver.quit()
