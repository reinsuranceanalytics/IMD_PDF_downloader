import os
import datetime
import requests


def log_message(message):
    log_dir = "./downloads"
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "download_log.txt")
    with open(log_path, "a") as log:
        log.write(f"{datetime.datetime.now()}: {message}\n")


def create_directory(path):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)

def build_url(date):
    """Construct the IMD rainfall report URL based on a date."""
    date_str = date.strftime('%d%m%Y')  # Format: DDMMYYYY
    url = "https://mausam.imd.gov.in/Rainfall/DISTRICT_RAINFALL_DISTRIBUTION_COUNTRY_INDIA_cd.pdf"
    return url, f"IMD_DIST_daily_rainfall_{date_str}.pdf"

def download_pdf(url, save_path):
    """Download the PDF from the given URL and save to the specified path."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"✅ Downloaded: {os.path.basename(save_path)}")
        else:
            print(f"⚠️ Report not found or not yet published: {os.path.basename(save_path)} (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Error downloading file: {e}")

def download_imd_rainfall_report(date, save_dir):
    """Full workflow to download IMD district rainfall report for a given date."""
    create_directory(save_dir)
    url, filename = build_url(date)
    save_path = os.path.join(save_dir, filename)
    download_pdf(url, save_path)

if __name__ == "__main__":
    # Set today's date or a specific date
    today = datetime.date.today()
    # today = datetime.date(2024, 6, 26)  # Uncomment to simulate past date

    # Folder to save downloaded files
    download_folder = "./downloads"

    # Call main function
    download_imd_rainfall_report(today, download_folder)
