from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import getpass as getP
import time 
import os
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
usernameStr = str(input("Username: "))
passwordStr = getP.getpass("Password: ")

driver = webdriver.Chrome(os.environ['SELENIUM_DRIVER'], options=chrome_options)
driver.get("https://handins.ccs.neu.edu/login")
username = driver.find_element_by_id("user_username")
username.click()
username.send_keys(usernameStr)
password = driver.find_element_by_id("user_password")
password.click()
password.send_keys(passwordStr)
time.sleep(3)
login = driver.find_element_by_name("commit")
login.click()
cs2500 = driver.find_element_by_link_text("CS2500: Fundamentals of Computer Science I")
cs2500.click()
assignmentsButton = driver.find_element_by_link_text("Assignments")
assignmentsButton.click()
trs = driver.find_elements_by_tag_name("tr")
assignments = {}
ungradedAssignments = {}
filteredAssignments = {}
for tr in trs:
    tds = tr.find_elements_by_tag_name("td")
    if tds:
        name = tds[0].text
        assignments[name] = {"Name" : tds[0].text,
                             "Due Date" : tds[1].text,
                            "Possible Points" : tds[2].text,
                             "Score" : tds[3].text}
driver.quit()
# Parsing Out Unneeded Value
for (key, value) in assignments.items():
    if value["Score"] == "" or value["Score"] == "∅":
        ungradedAssignments[key] = value
    else:
        if value["Possible Points"] != "":
            filteredAssignments[key] = value

# Calculating the Grade
totalPoints = 1
possiblePoints = 0.0
for assign in filteredAssignments.values():
    print(assign)
    if assign["Score"] != "" and assign["Score"] != "∅":
        possiblePoints += float(assign["Possible Points"])
        totalPoints += (float(assign["Score"]) * float(assign["Possible Points"])/100)
grade = totalPoints/possiblePoints
print(totalPoints)
print(possiblePoints)
print("Current Grade: ", grade)





