import requests
from bs4 import BeautifulSoup
import urllib.parse
from urllib.request import urlretrieve
import base64
import os
import winsound



def download_and_convert_to_pdf(url, output_filename):
    headers = {
    'Host': 'cdn77.papertrell.com',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
}
    try:
        session = requests.Session()
        # Download the binary data from the URL
        response1 = session.get(url)
        binary_data = response1.content

        # Decode the binary data using base64
        decoded_data = base64.b64decode(binary_data)

        # Write the decoded data to a PDF file
        with open(output_filename, 'wb') as pdf_file:
            pdf_file.write(decoded_data)

        print(f"PDF file '{output_filename}' created successfully!")
        winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
    except Exception as e:
        print(f"Error: {e}")



#change the id value..only if you purchased the book




url = 'https://digital.amarchitrakatha.com/viewer/?id=005835110'






headers = {
    'Host': 'digital.amarchitrakatha.com',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://digital.amarchitrakatha.com/id005835096/Akbar',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9'
}

cookies = {
    'elggperm': '3B90404B9938C405A6101E86C04FC96E',
    'ASP.NET_SessionId': 'hx32ms4bbcxhcpzhqwtbezyw',
    '__stripe_mid': 'f8d3e9fc-380e-4dbc-add7-444018c271894a3156'
}

response = requests.get(url, headers=headers, cookies=cookies)
# Assuming you have the HTML content stored in a variable called 'html'
soup = BeautifulSoup(response.content, 'html.parser')
specific_class = 'viewer pdf'  # Replace with the actual class name

# Find all <iframe> tags with the specific class
iframe_tags = soup.find_all("iframe", {"class": specific_class})
path=soup.title.string.strip().replace(" ","_")
print("name Allocated : ",path)

# Retrieve the src attribute from each <iframe> tag
for iframe in iframe_tags:
    src_url = "https://digital.amarchitrakatha.com/" + iframe['src']
    encoded_string = src_url.split("file=")[1]
# Decode the URL-encoded string 
    decoded_string = urllib.parse.unquote(encoded_string)
    file_extension_index = decoded_string.find(".data")
    if file_extension_index != -1:
       extracted_part = decoded_string[:file_extension_index] +".data"
       print(extracted_part)
       output_filename=path+".pdf"
     #  output_filename="mahadevaeva4"+".pdf"
       print("Please Hold On...")
       download_and_convert_to_pdf(extracted_part, output_filename)
