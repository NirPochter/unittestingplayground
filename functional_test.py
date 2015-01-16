from selenium import webdriver
import unittest

class NewVisiterTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# User goes to the website.
		self.browser.get('http://localhost:8000')

		# He sees the job title that talks about a todo list. 
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text )

		# He is invited to enter todo entries.
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'), 
			'Enter a to-do item'
		)

		# He types 'Buy peacock feathers'
		inputbox.send_keys('Buy peackock feathers')

		#Upon hitting enter, the page updates and lists the first todo item in the list.
		inputbox.send_keys(keys.ENTER)

		table= self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: By peacock feathers' for row in rows)
		)

		# Need to add more tests. 		# He is invited to enter todo entries.

		self.Fail
		

if __name__ == '__main__':
	unittest.main(warnings='ignore')