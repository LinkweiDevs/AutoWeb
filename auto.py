from selenium.webdriver import Chrome
import time

browser = Chrome()
browser.get('https://duckduckgo.com')

search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('Manjaro Linux')
search_form.submit()

time.sleep(5)

browser.close()
quit()
