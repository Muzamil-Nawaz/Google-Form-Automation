import requests
from selenium import webdriver 
tinyurl = "INSERT_EXTENSION"
resp = requests.get("http://tinyurl.com/{}".format(tinyurl))
# use chrome via driver = webdriver.Chrome() 
driver = webdriver.Firefox()

driver.get(resp.url)
full_name = "INSERT_FULL_NAME"
sid = "INSERT_YOUR_SID"

js = """
document.querySelectorAll("div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl")[0].click(); 
document.querySelectorAll("div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl")[2].click(); 
document.querySelectorAll("input.quantumWizTextinputPaperinputInput")[0].value = "{full_name}";
document.querySelectorAll("input.quantumWizTextinputPaperinputInput")[1].value = "{sid}";
document.querySelectorAll("input.quantumWizTextinputPaperinputInput")[2].value = FB_PUBLIC_LOAD_DATA_[1][1][4][4][0][4][0][2][0];
""".format(full_name=full_name,sid=sid)
driver.execute_script(js)