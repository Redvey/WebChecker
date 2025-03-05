import requests
import socket
import pandas as pd
import concurrent.futures

# Read website domains from websites.txt
with open("websites.txt", "r") as file:
    websites = [line.strip() for line in file if line.strip()]

data = []

def process_website(idx, website):
    url = f"http://{website}"
    try:
        # Get IP address
        ip_address = socket.gethostbyname(website)

        # Determine IP class
        first_octet = int(ip_address.split('.')[0])
        if first_octet <= 127:
            ip_class = "Class A"
        elif first_octet <= 191:
            ip_class = "Class B"
        elif first_octet <= 223:
            ip_class = "Class C"
        else:
            ip_class = "Class D/E"

        # Send a request to check response
        response = requests.get(url, timeout=2)
        reply = f"HTTP {response.status_code}"

    except socket.gaierror:
        ip_class, reply = "Unknown", "Domain not found"
    except requests.RequestException:
        reply = "No response"

    return [idx, website, url, ip_class, reply]

# Use ThreadPoolExecutor for faster execution
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(lambda args: process_website(*args), enumerate(websites, start=1))

# Collect data
data = list(results)

# Create a DataFrame
df = pd.DataFrame(data, columns=["Serial No.", "Domain Name", "Address (URL)", "IP Class", "Reply"])

# Save to Excel
df.to_excel("websites_data.xlsx", index=False)

print("Excel file 'websites_data.xlsx' created successfully!")
