import requests
from bs4 import BeautifulSoup
import re # Regular expressions
import sys # For argument parsing

# Exception Handling
# Can now paste the URL after the function call (CLI tool)
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED talk URL")

# url = "https://www.ted.com/talks/ethan_hawke_give_yourself_permission_to_be_creative"
r = requests.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, features='html.parser')

for val in soup.findAll("script"):
    if(re.search("talkPage.init", str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

mp4_url = result_mp4.split('"')[20]

# To find the correct video (this has to be automated better)
# for s in mp4_url:
#     print(s)

print("Downloading video from: " + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in: " + file_name)

r = requests.get(mp4_url)

with open(file_name, 'wb') as f:
    f.write(r.content)

print("Download finished")
