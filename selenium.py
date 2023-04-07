import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver.set_window_size(700,700)
### Auto driver install
driver = webdriver.Chrome(ChromeDriverManager().install())
###
try:
    driver_path = chromedriver_autoinstaller.install()
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)
    driver.set_window_size(850,630)
except Exception:
    print("Driver Not found or Network Problem")
    sys.exit()
    
   ###### Element Find
  def visibil_element(driver, by, selector, wait=10): ### web element find and search
    element = False
    if by == 'name':
        byselector = By.NAME
    if by == 'xpath':
        byselector = By.XPATH
    if by == 'css':
        byselector = By.CSS_SELECTOR
    if by == 'id':
        byselector = By.ID
    try:
        element = WebDriverWait(driver, wait).until(
            EC.visibility_of_element_located((byselector, selector)))
    except Exception as e:
        # print(e)
        element = False
    if element == False:
        pass
        # print("visibil_element not find: ", selector)
    else:
        pass
        # print(selector)
    return element
