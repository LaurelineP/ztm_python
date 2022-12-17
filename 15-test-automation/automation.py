from selenium import webdriver
from selenium.webdriver.common.by import By

from save_test import save_test
URL_SELENIUM_FORM = 'https://demo.seleniumeasy.com/basic-first-form-demo.html'


def get_selenium_browser():
	options = webdriver.ChromeOptions()
	options.add_experimental_option("detach", True)
	chrome = webdriver.Chrome(options=options)
	return chrome


def test_url( url ):
	try:
		chrome = get_selenium_browser()
		chrome.get(url)

		# 0 - Checking url title
		expected_title = "selenium easy demo"
		has_correct_title: bool = expected_title in chrome.title.lower()
		assert(has_correct_title)

		# DEMO PRACTICE 1 : WRITE AND DISPLAY A MESSAGE
		# 1 - Demo practice - Get the input to write a message into it
		message = 'hello'
		input_txt = chrome.find_element(By.ID, 'user-message')
		input_txt.clear()
		input_txt.send_keys(message)

		# 1 - Demo practice - Get the button show message clicked
		show_message_btn = chrome.find_element(By.CLASS_NAME, "btn-default")
		show_message_text = show_message_btn.get_attribute('innerHTML')
		show_message_btn.click()

		# 1 - Demo practice - Checking the message has been displayed after click action
		message_displayed = chrome.find_element(By.ID, "display")
		expected_displayed_message = message_displayed.get_attribute('innerText')

		is_correct_displayed_message = message == expected_displayed_message
		print(expected_displayed_message == message)

		assert(is_correct_displayed_message)
		assert( message in chrome.page_source )

		# DEMO PRACTICE 2 : WRITE IN 2 INPUTS AND DISPLAY A THE SUM
		# 2 Demo practice -
		numbers = [1, 2]
		for i in range(len(numbers)):
			input_id = f'sum{i+1}'
			input_el = chrome.find_element(By.ID, input_id)
			input_el.send_keys(numbers[i])

		get_goal_btn = filter(
			lambda el: el.get_attribute('innerText') == 'Get Total',
			chrome.find_elements(By.CLASS_NAME, 'btn-default')
			)


		# save_test(url, f'''
		# - has_correct_title: { has_correct_title }
		# 	- value: chrome.title
		# ''')

		""
	except:
		print('fail')

	finally:
		chrome.close()
		chrome.quit()


# chrome.quit()


test_url(URL_SELENIUM_FORM)