# Not all of your arguments need to have default values. But Python will only accept functions defined with their parameters in a specific order. The required parameters need to occur before any parameters with a default argument.
# Make sure the parameters with default argument come last in the ()
import reqs as requests
from bs4 import BeautifulSoup

def get_id(html_id, website="http://coolsite.com"):
  request = requests.get(website)
  parsed_html = BeautifulSoup(website.content, features="html.parser")
  return parsed_html.find(id_=html_id)
