from bs4 import BeautifulSoup
import re
from markdownify import markdownify as md

# Your HTML code snippet
html_code = '''
<pre><code class="mb-5px" data-language="python"><span class="cm-keyword">def</span> <span class="cm-def">dir_reduc</span>(<span class="cm-variable">a</span>):
    <span class="cm-variable">i</span> <span class="cm-operator">=</span> <span class="cm-number">0</span>
    <span class="cm-keyword">while</span> <span class="cm-variable">i</span> <span class="cm-operator">&lt;</span> <span class="cm-builtin">len</span>(<span class="cm-variable">a</span>) <span class="cm-operator">-</span> <span class="cm-number">1</span>:
        <span class="cm-keyword">if</span> <span class="cm-builtin">len</span>(<span class="cm-variable">a</span>[<span class="cm-variable">i</span>]) <span class="cm-operator">==</span> <span class="cm-builtin">len</span>(<span class="cm-variable">a</span>[<span class="cm-variable">i</span><span class="cm-operator">+</span><span class="cm-number">1</span>]) <span class="cm-keyword">and</span> (<span class="cm-variable">a</span>[<span class="cm-variable">i</span>] <span class="cm-operator">!=</span> <span class="cm-variable">a</span>[<span class="cm-variable">i</span><span class="cm-operator">+</span><span class="cm-number">1</span>]):
            <span class="cm-variable">a</span>.<span class="cm-property">pop</span>(<span class="cm-variable">i</span>)
            <span class="cm-variable">a</span>.<span class="cm-property">pop</span>(<span class="cm-variable">i</span>)
            <span class="cm-variable">i</span> <span class="cm-operator">=</span> <span class="cm-number">0</span>
        <span class="cm-keyword">else</span>:
            <span class="cm-variable">i</span><span class="cm-operator">+=</span><span class="cm-number">1</span>
    <span class="cm-keyword">return</span> <span class="cm-variable">a</span>
</code></pre>
'''
print(md(html_code, code_language="python"))



import requests
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


tabs = {}

driver = webdriver.Chrome()
driver.get("https://github.com/login")

tabs["gh_main"] = driver.current_window_handle

uname = driver.find_element(By.ID, "login_field")
uname.send_keys(user)

pwd = driver.find_element(By.ID, "password")
pwd.send_keys(password)

login = driver.find_element(By.NAME, "commit")
login.click()
time.sleep(1)

driver.switch_to.new_window("tab")
driver.get("https://www.codewars.com/users/sign_in")
tabs["cw_main"] = driver.current_window_handle
cw_login = driver.find_element(By.TAG_NAME, "button")
cw_login.click() 
time.sleep(1)

driver.switch_to.new_window("tab")
driver.get("https://www.codewars.com/users/Career-Nandish/completed_solutions")
tabs["cw_solutions"] = driver.current_window_handle
time.sleep(1)

driver.switch_to.window(tabs["cw_main"])
driver.close()
driver.switch_to.window(tabs["cw_solutions"])

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


completed = driver.find_element(By.XPATH, 
    "//a[contains(text(), 'Completed')]")

total_completed =  re.search(r"(\d+)", completed.text).group()

print("total_completed", total_completed)

elements = driver.find_elements(By.XPATH, 
    "//div[@class='list-item-solutions']")


for elem in elements:
    kyu_element = elem.find_element(By.TAG_NAME, "span")
    print("kyu", kyu_element.text)

    title = elem.find_element(By.TAG_NAME, "a")
    print("title", title.text)

    code = elem.find_element(By.TAG_NAME, "code")

    soup = BeautifulSoup(code, 'html.parser')
    code_text = soup.get_text()

    print("Extracted Code:\n", code_text)



katas = {}


time.sleep(5)
driver.quit()

