from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
driver = webdriver.Chrome()

driver.get("https://www.rebuy.de")
driver.maximize_window()
WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.ID, "cookiebanner")))
driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
search = driver.find_element_by_css_selector("ry-header ry-search-input > ry-fullscreen-in-place  form[method='get']  input[name='q']")
search.send_keys ("bentley little")
search.send_keys(Keys.ENTER)

# driver.find_element_by_css_selector(".border-0.btn.btn-blue.btn-icon.rounded-0 > ry-svg-icon > .svg-icon-0d977fc42d").click()
driver.execute_script("window.scrollTo(0, 200)")
WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "ry-product:nth-of-type(1) > .border.d-block.product.px-4.text-decoration-none.w-100 > .my-4.my-sm-0.row  .my-3.title")))
driver.find_element_by_css_selector("ry-product:nth-of-type(1) > .border.d-block.product.px-4.text-decoration-none.w-100 > .my-4.my-sm-0.row  .my-3.title").click()
driver.find_element_by_css_selector("div:nth-of-type(5) > .mb-4  .d-flex.flex-column.flex-even.justify-content-center").click()
driver.find_element_by_css_selector(".btn-primary.btn-lg").click()

WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[class='ry-modal-content p-4']")))
driver.find_element_by_css_selector("[class='mt-4 col-12 col-sm-6 order-sm-1']").click()
WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
driver.find_element_by_css_selector(".btn-primary").click()


# sleep(10)
# driver.quit()

