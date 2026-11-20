import re
import requests
from bs4 import BeautifulSoup
import time
import random
import csv

red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
yellow = "\033[33m"
reset = "\033[39m"

print("Welcome to " + green + "emailGuesser" + reset + "!\nDeveloped by " + blue + "White Hat Inspector (@WHInspector)" + reset + ".\nFor feedback and/or questions send me a private message on " + blue + "https://twitter.com/whinspector" + reset)
print("")

while True:
	name_input = input(yellow + 'Please enter name: ' + reset)
	last_name_input = input(yellow + "Please enter surname: " + reset)
	birth_input = input(yellow + "Please enter birth year (or no): " + reset)
	username_input = input(yellow + "Please enter username (or no): " + reset)
	skype_input = "blank"
	while skype_input != "y" and skype_input != "n":
		skype_input = input(yellow + "Would you like to automatically add to the pool Skype usernames from people using this name in Skype? (y/n) " + reset)
		if skype_input != "y" and skype_input != "n":
			print(red + "Please input 'y' or 'n'!" + reset)
			
	if len(birth_input) != 4:
		birth_input = "no"

	extra_formats_input = input(yellow + "Would you like to add more e-mail formats apart from the preconfigured ones? (y/n) " + reset)
	while extra_formats_input != "y" and extra_formats_input != "n":
		print(red + "Please select a valid input." + reset)
		extra_formats_input = input(yellow + "Would you like to add more combinations than the preconfigured ones? (y/n) " + reset)

	extra_formats = []
	if extra_formats_input == "y":
		extra_formats = input(yellow + "Provide all extra formats you wish to examine, separated by commas: " + reset).split(",")

	domain = []
	while domain == [] or domain == ['']:
		domain = input(yellow + "Please enter domains separated by a single comma: " + reset).split(",")
		if domain == ['']:
			print(red + "You must input at least one domain to be searched!" + reset)

	emails = []
	emails_for_verification = []
	final_emails = []
	final_emails_text = []

	startSearching = time.perf_counter()

	for dom in domain:
		structure = ["first!!", "f!!last!!", "f!!.last!!", "f!!_last!!", "last!!f!!", "last!!.f!!", "last!!_f!!", "l!!first!!", "l!!.first!!", "l!!_first!!", "first!!l!!", "first!!.l!!", "first!!_l!!", "last!!first!!", "last!!.first!!", "last!!_first!!", "first!!last!!", "first!!.last!!", "first!!_last!!", "first!!last!!1", "first!!last!!.1", "f!!last!!1", "f!!last!!.1", "first!!.last!!1", "first!!.last!!.1"]

		if extra_formats_input == "y":
			for inputs in extra_formats:
				structure.append(inputs)

		if birth_input != "no":
			structure.append("last!!first!!" + birth_input)
			structure.append("first!!last!!" + birth_input)
			structure.append("f!!last!!" + birth_input)
			structure.append("f!!.last!!" + birth_input)
			structure.append("f!!_last!!" + birth_input)
			structure.append("first!!.l!!" + birth_input)
			structure.append("first!!_l!!" + birth_input)
			structure.append("last!!.first!!" + birth_input)
			structure.append("first!!.last!!" + birth_input)
			structure.append("last!!_first!!" + birth_input)
			structure.append("first!!_last!!" + birth_input)
			structure.append("last!!first!!" + birth_input[2:])
			structure.append("first!!last!!" + birth_input[2:])
			structure.append("f!!last!!" + birth_input[2:])
			structure.append("f!!.last!!" + birth_input[2:])
			structure.append("f!!_last!!" + birth_input[2:])
			structure.append("first!!.l!!" + birth_input[2:])
			structure.append("first!!_l!!" + birth_input[2:])
			structure.append("last!!.first!!" + birth_input[2:])
			structure.append("first!!.last!!" + birth_input[2:])
			structure.append("last!!_first!!" + birth_input[2:])
			structure.append("first!!_last!!" + birth_input[2:])
			structure.append("last!!first!!." + birth_input)
			structure.append("first!!last!!." + birth_input)
			structure.append("f!!last!!." + birth_input)
			structure.append("f!!.last!!." + birth_input)
			structure.append("f!!_last!!." + birth_input)
			structure.append("first!!.l!!." + birth_input)
			structure.append("first!!_l!!." + birth_input)
			structure.append("last!!.first!!." + birth_input)
			structure.append("first!!.last!!." + birth_input)
			structure.append("last!!_first!!." + birth_input)
			structure.append("first!!_last!!." + birth_input)
			structure.append("last!!first!!_" + birth_input)
			structure.append("first!!last!!_" + birth_input)
			structure.append("f!!last!!_" + birth_input)
			structure.append("f!!.last!!_" + birth_input)
			structure.append("f!!_last!!_" + birth_input)
			structure.append("first!!.l!!_" + birth_input)
			structure.append("first!!_l!!_" + birth_input)
			structure.append("last!!.first!!_" + birth_input)
			structure.append("first!!.last!!_" + birth_input)
			structure.append("last!!_first!!_" + birth_input)
			structure.append("first!!_last!!_" + birth_input)
			structure.append("last!!first!!." + birth_input[2:])
			structure.append("first!!last!!." + birth_input[2:])
			structure.append("f!!last!!." + birth_input[2:])
			structure.append("f!!.last!!." + birth_input[2:])
			structure.append("f!!_last!!." + birth_input[2:])
			structure.append("first!!.l!!." + birth_input[2:])
			structure.append("first!!_l!!." + birth_input[2:])
			structure.append("last!!.first!!." + birth_input[2:])
			structure.append("first!!.last!!." + birth_input[2:])
			structure.append("last!!_first!!." + birth_input[2:])
			structure.append("first!!_last!!." + birth_input[2:])
			structure.append("last!!first!!_" + birth_input[2:])
			structure.append("first!!last!!_" + birth_input[2:])
			structure.append("f!!last!!_" + birth_input[2:])
			structure.append("f!!.last!!_" + birth_input[2:])
			structure.append("f!!_last!!_" + birth_input[2:])
			structure.append("first!!.l!!_" + birth_input[2:])
			structure.append("first!!_l!!_" + birth_input[2:])
			structure.append("last!!.first!!_" + birth_input[2:])
			structure.append("first!!.last!!_" + birth_input[2:])
			structure.append("last!!_first!!_" + birth_input[2:])
			structure.append("first!!_last!!_" + birth_input[2:])

		if username_input != "no":
			structure.append(username_input)

			if birth_input != "no":
				structure.append(username_input + birth_input)
				structure.append(username_input + birth_input[2:])
				structure.append(username_input + "." + birth_input)
				structure.append(username_input + "_" + birth_input)
				structure.append(username_input + "." + birth_input[2:])
				structure.append(username_input + "_" + birth_input[2:])

		if skype_input == "y":
			print("")
			print("Searching Skype users...")
			url = "https://www.skypli.com/search/" + name_input + "%20" + last_name_input
			page = requests.get(url)
			soup = BeautifulSoup(page.content, "html.parser")
			results = soup.find(class_="search-results__title")
			if page.status_code != 500:
				if results.text.strip() != "0 results for " + name_input + " " + last_name_input:
					print(results.text.strip() + ". Autocompleting list of e-mail usernames...")
					results = soup.find_all(class_="search-results__block-info-username")
					for n in results:
						test_text = n.text.strip()
						if test_text.find(".cid.") == -1:
							if test_text.find("live:") != -1:
								if len(test_text) != 21:
									structure.append(test_text[5:])

									if test_text[-1].isdigit() == True and test_text[-2] == "_":
										structure.append(test_text[5:-2])
									if test_text[-1].isdigit() == True and test_text[-2].isdigit() == True and test_text[-3] == "_":
										structure.append(test_text[5:-3])
							else:
								structure.append(test_text)
				else:
					print("No results on Skype for this name!")
			else:

				url = "https://tools.epieos.com/skype.php"
				my_data = {"data": name_input + " " + last_name_input}
				page = requests.post(url, data=my_data)
				soup = BeautifulSoup(page.content, "html.parser")
				results = soup.find_all(class_="col-md-4 offset-md-4 mt-5 pt-3 border")
				check_results = soup.find(class_="col-md-4 offset-md-4 mt-5 pt-3 border")

				if len(results) >= 1 and "No skype account" not in check_results.text.strip():
					print("Found " + str(len(results)) + " Skype users with that name. Autocompleting list of e-mail usernames...")
					for n in results:
						test_text = n.text.strip()
						if test_text.find(".cid.") == -1:
							if test_text.find("live:") != -1:
								test_text = test_text[test_text.find("live:"):]
								if len(test_text) != 21:
									structure.append(test_text[5:])

									if test_text[-1].isdigit() == True and test_text[-2] == "_":
										structure.append(test_text[5:-2])
									if test_text[-1].isdigit() == True and test_text[-2].isdigit() == True and \
											test_text[-3] == "_":
										structure.append(test_text[5:-3])
							else:
								test_text = test_text[test_text.find("Id : ")+5:]
								structure.append(test_text)
				else:
					print("No results on Skype for this name!")



		found_first = False
		found_last = False
		for x in structure:
			if x.find("first!!") != -1:
				x = x.replace("first!!", name_input)
				found_first = True
			if x.find("last!!") != -1:
				x = x.replace("last!!", last_name_input)
				found_last = True
			if x.find("f!!") != -1:
				x = x.replace("f!!", name_input[0])
			if x.find("l!!") != -1:
				x = x.replace("l!!", last_name_input[0])
			emails.append(x + "@" + dom)


	regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

	for n in emails:

		addressToVerify = n

		match = re.match(regex, addressToVerify)
		if match == None:
			print("verifying " + red + n + reset + "... Bad Syntax")
		else:
			print("verifying " + green + n + reset + "... Good Syntax")
			emails_for_verification.append(n)

	if len(emails_for_verification) != 0:
		print("Checking e-mails with good syntax...")
	else:
		print("There is no e-mail with valid syntax to check.")

	if len(emails_for_verification) != 0:

		requestPwnedStartTimer = 0

		for mailcheck in emails_for_verification:

			url = "https://www.skypli.com/search/" + mailcheck
			page = requests.get(url)
			soup = BeautifulSoup(page.content, "html.parser")
			results = soup.find_all(class_="search-results__title")

			if page.status_code != 500:
				for n in results:
					if n.text.strip() == "1 results for " + mailcheck:
						final_emails_text.insert(0, mailcheck)
						print(blue + mailcheck + reset + " was found in Skype")
						result = soup.find(class_="search-results__block-info-username")
						url_new = "https://www.skypli.com/profile/" + result.text.strip()
						page_new = requests.get(url_new)
						soup_new = BeautifulSoup(page_new.content, "html.parser")
						mailcheck = blue + mailcheck + reset
						result_new = soup_new.find_all(class_="profile-box__table-value")
						for r in result_new:
							mailcheck = mailcheck + "\n" + r.text.strip()
						final_emails.insert(0, mailcheck + "\nMore info: " + url_new + "\n")
					elif n.text.strip() != "0 results for " + mailcheck:
						final_emails_text.insert(0, mailcheck)
						print(blue + mailcheck + reset + " was found in multiple Skype accounts")
						final_emails.insert(0, blue + mailcheck + reset + " Multiple skype accounts found: " + url + "\n")
					else:
						requestPwnedEndTimer = time.perf_counter()
						requestPwnedTimePassed = requestPwnedEndTimer - requestPwnedStartTimer

						randomTimePassed = random.randint(7, 11)
						if requestPwnedTimePassed < randomTimePassed:
							time.sleep(randomTimePassed - requestPwnedTimePassed)

						url = "https://haveibeenpwned.com/account/" + mailcheck
						page = requests.get(url)
						soup = BeautifulSoup(page.content, 'html.parser')
						results = soup.find_all(id="pwnCount")
						for n in results:
							if n.text.strip() == "Not pwned in any data breaches and found no pastes (subscribe to search sensitive breaches)":
								print(green + mailcheck + reset + " not found in breached database.")
							else:
								print(red + mailcheck + reset + " was found to be " + red + "Pwned!" + reset)
								final_emails_text.append(mailcheck)
								final_emails.append(red + mailcheck + reset + "\n")
						requestPwnedStartTimer = time.perf_counter()
			else:

				url = "https://tools.epieos.com/skype.php"
				my_data = {"data": mailcheck}
				page = requests.post(url, data=my_data)
				soup = BeautifulSoup(page.content, "html.parser")
				results = soup.find_all(class_="col-md-4 offset-md-4 mt-5 pt-3 border")
				avatars = soup.find_all(src=re.compile("avatar.skype.com"))

				for n in results:

					if len(results) == 1 and "No skype account" not in n.text.strip():
						final_emails_text.insert(0, mailcheck)
						print(blue + mailcheck + reset + " was found in Skype")
						find_name = n.text.strip().find("Name : ")
						find_skype_id = n.text.strip().find("Skype Id : ")
						end_text = n.text.strip().rfind("</p>")
						avatar = soup.find(src=re.compile("avatar.skype.com"))
						mailcheck = blue + mailcheck + reset + "\n" + n.text.strip()[find_name:find_skype_id] + "\n" + n.text.strip()[find_skype_id:end_text] + "\nAvatar : " + blue + str(avatar["src"]) + reset
						final_emails.insert(0, mailcheck + "\n")
					elif len(results) > 1:
						final_emails_text.insert(0, mailcheck)
						print(blue + mailcheck + reset + " was found in multiple Skype accounts")
						mailcheck = blue + mailcheck + reset + " --> Multiple skype accounts found: \n"
						for n in results:
							find_name = n.text.strip().find("Name : ")
							find_skype_id = n.text.strip().find("Skype Id : ")
							end_text = n.text.strip().rfind("</p>")
							mailcheck += n.text.strip()[find_name:find_skype_id] + "\n" + n.text.strip()[find_skype_id:end_text] + "\n\n"
						final_emails.insert(0, mailcheck + "\n")
					else:
						requestPwnedEndTimer = time.perf_counter()
						requestPwnedTimePassed = requestPwnedEndTimer - requestPwnedStartTimer

						randomTimePassed = random.randint(7, 11)
						if requestPwnedTimePassed < randomTimePassed:
							time.sleep(randomTimePassed - requestPwnedTimePassed)

						url = "https://haveibeenpwned.com/account/" + mailcheck
						page = requests.get(url)
						soup = BeautifulSoup(page.content, 'html.parser')
						results = soup.find_all(id="pwnCount")
						for n in results:
							if n.text.strip() == "Not pwned in any data breaches and found no pastes (subscribe to search sensitive breaches)":
								print(green + mailcheck + reset + " not found in breached database.")
							else:
								print(red + mailcheck + reset + " was found to be " + red + "Pwned!" + reset)
								final_emails_text.append(mailcheck)
								final_emails.append(red + mailcheck + reset + "\n")

						requestPwnedStartTimer = time.perf_counter()

	print("")
	print("-------------------------------------")
	print("")
	print("Emails found:\n")
	for finalEmail in final_emails:
		print(finalEmail)

	endSearching = time.perf_counter()

	if len(final_emails) != 0:
		print("")
		outputs = "0"
		while outputs != "1" and outputs != "2" and outputs != "3" and outputs != "4":
			outputs = input(yellow + "Would you like any outputs?\n[1] No\n[2] .txt file\n[3] .csv file\n[4] Both\nYour choice: " + reset)
			if outputs != "1" and outputs != "2" and outputs != "3" and outputs != "4":
				print(red + "Please select 1,2,3 or 4!" + reset)

		if outputs == "2" or outputs == "4":
			print("")
			print("Creating txt file...")
			f = open("results.txt", "w")
			for finalEmail in final_emails_text:
				f.write(finalEmail + "\n")
			print(f.name + " created!")
			f.close()

		if outputs == "3" or outputs == "4":
			print("")
			print("Creating csv file...")
			with open('resultscsv.csv', 'w', newline='') as resultscsv:
				resultswriter = csv.writer(resultscsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
				for finalEmail in final_emails_text:
					resultswriter.writerow([finalEmail])
			print("resultscsv.csv created!")
	else:
		print(red + "No e-mails found! :(" + reset)

	print("")
	if len(emails_for_verification) != 0:
		print(f"Your search lasted for {endSearching - startSearching:0.4f} seconds.\nEmails queried where {len(emails_for_verification)} in total.\nAverage verification time per e-mail address was {(endSearching - startSearching)/len(emails_for_verification):0.2f}.")
	else:
		print(f"Your search lasted for {endSearching - startSearching:0.4f} seconds.\nEmails queried where {len(emails_for_verification)} in total.")
	print("")
