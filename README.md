# python-web-scraper
A simple webscraper written in python using "requests" module
# usage:
call scrape(base_url, dict_dir, correct_status_code), where
  base_url = the web_url to scrape
  dict_dir = the directory of a dictionary of words to try
  correct_status_code = responce status code, which will cause the tried url to be added to the found url list
might add recursive functionality too
