import traceback
try:
    00000/0000000
except:
    print(traceback.format_exc())
    
def firstline():
    lines = []
    with open(r"t1.txt", 'r') as fp:
        lines = fp.readlines()
    with open(r"t1.txt", 'w') as fp:
        for number, line in enumerate(lines):
            if number != 0:
                fp.write(line)
    return lines[0].replace("\n","")

def visibil_element(driver, by, selector, wait=10):
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
