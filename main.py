# import os
# import requests
# from bs4 import BeautifulSoup
# url = "https://linkedin.com/"
# result = os.popen(f"curl {url}robots.txt").read()
# result_data_set = {"Disallowed":[], "Allowed":[]}

# for line in result.split("\n"):
#     if line.startswith('Allow'):    # this is for allowed url
#         result_data_set["Allowed"].append(line.split(': ')[1].split(' ')[0])    # to neglect the comments or other junk info
#     elif line.startswith('Disallow'):    # this is for disallowed url
#         result_data_set["Disallowed"].append(line.split(': ')[1].split(' ')[0])    # to neglect the comments or other junk info


# def get_keywords(url):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     keywords = [meta.attrs.get("content") for meta in soup.find_all("meta", attrs={"name": "keywords"})]
#     return keywords

# keywords = get_keywords(url)
# print(keywords)
# import requests
# import re
# import json

# url = "https://linkedin.com/robots.txt"

# response = requests.get(url)
# content = response.content.decode('utf-8')

# # Disallow paths
# user_agents = {}
# current_user_agent = None
# pattern = re.compile(r'User-agent: (.+)')
# for line in content.split('\n'):
#     match = pattern.match(line)
#     if match:
#         current_user_agent = match.group(1)
#         user_agents[current_user_agent] = {'disallow_paths': [], 'crawl_delay': None, 'sitemap_urls': []}
#     elif current_user_agent:
#         if line.startswith('Disallow: '):
#             user_agents[current_user_agent]['disallow_paths'].append(line[len('Disallow: '):])
#         elif line.startswith('Crawl-delay: '):
#             user_agents[current_user_agent]['crawl_delay'] = line[len('Crawl-delay: '):]
#         elif line.startswith('Sitemap: '):
#             user_agents[current_user_agent]['sitemap_urls'].append(line[len('Sitemap: '):])

# # Convert to JSON
# json_data = json.dumps(user_agents, indent=4)
# print(json_data)
"""
import requests

url = "https://www.youtube.com"

# Add a mobile user agent
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
headers2 = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36'}
# Make the request with the mobile user agent
response = requests.get(url, headers=headers2)

# Check if the page has a mobile viewport meta tag
is_mobile_compatible = False
if 'viewport' in response.text.lower() and 'content="width=device-width' in response.text.lower():
    is_mobile_compatible = True

if is_mobile_compatible:
    print("The page is mobile compatible")
else:
    print("The page is not mobile compatible")
    """

from test.testDB import RunTest

RunTest()
