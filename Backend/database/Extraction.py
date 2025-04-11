import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Database Setup
DB_NAME = "crop_state_market.db"


def create_tables():
    """Creates the necessary tables in SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create Commodities Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Commodities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')

    # Create States Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS States (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')

    # Create Markets Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Markets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("Database and tables created successfully!")


# Function to close the popup
def close_popup(driver):
    """Closes popup on Agmarknet website."""
    try:
        popup = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'popup-onload'))
        )
        close_button = popup.find_element(By.CLASS_NAME, 'close')
        driver.execute_script("arguments[0].click();", close_button)
        print("Popup closed successfully")
        time.sleep(2)
    except TimeoutException:
        print("No popup found, proceeding...")


# Function to scrape commodities, states, and markets
def scrape_data():
    """Scrapes commodities, states, and markets from Agmarknet and stores in SQLite."""

    # Initialize Selenium WebDriver
    driver = webdriver.Chrome()
    driver.get("https://agmarknet.gov.in/SearchCmmMkt.aspx")

    # Close popup if it appears
    close_popup(driver)

    # Connect to SQLite database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Scrape Commodities
    print("Scraping Commodities...")
    commodity_dropdown = Select(driver.find_element(By.ID, 'ddlCommodity'))
    for option in commodity_dropdown.options[1:]:  # Skip the first empty option
        commodity = option.text.strip().title()  # Capitalize first letter
        cursor.execute("INSERT OR IGNORE INTO Commodities (name) VALUES (?)", (commodity,))

    # Scrape States
    print("Scraping States...")
    state_dropdown = Select(driver.find_element(By.ID, 'ddlState'))
    for option in state_dropdown.options[1:]:  # Skip the first empty option
        state = option.text.strip().title()
        cursor.execute("INSERT OR IGNORE INTO States (name) VALUES (?)", (state,))

    # Scrape Markets (Only after selecting a state)
    print("Scraping Markets...")
    first_state = state_dropdown.options[1].text.strip()  # Get first valid state
    state_dropdown.select_by_visible_text(first_state)  # Select first valid state
    time.sleep(2)  # Allow market dropdown to update

    market_dropdown = Select(driver.find_element(By.ID, 'ddlMarket'))
    for option in market_dropdown.options[1:]:  # Skip the first empty option
        market = option.text.strip().title()
        cursor.execute("INSERT OR IGNORE INTO Markets (name) VALUES (?)", (market,))

    # Commit and close database
    conn.commit()
    conn.close()
    print("Scraping completed and data stored successfully!")

    # Close browser
    driver.quit()


# Run database setup and scraping
if __name__ == "__main__":
    create_tables()
    scrape_data()
