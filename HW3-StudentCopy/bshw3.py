# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
from bs4 import BeautifulSoup
import re
import localcop.png as logo


#logo = Image.open("logo.png")



base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'lxml')

for tag in soup.find_all(class_ = "html not-front logged-in two-sidebars page-node page-node- page-node-11581 node-type-general-page section-programs"):
	for thing in tag(id = "body-inside"):
		for close in thing(class_ = "body-inside2"):
			for x in close(class_ = "field field-name-body field-type-text-with-summary field-label-hidden"):
				for ima in x(class_ = "field-item even"):
					for img in ima.find_all("img"):
						img["src"] = "https://media.licdn.com/mpr/mpr/shrinknp_200_200/p/4/005/08e/305/09e69c2.jpg"


for tag in soup.find_all():
	for string in tag.prettify().split():
		if "student" in string and "href" not in string:
			None





htm = soup.prettify("utf-8")
with open("proj3.html", "wb") as file:
    file.write(htm)



