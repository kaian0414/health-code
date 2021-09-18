import select

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import Select

# 為了打開Chrome
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
chrome = r'C://Program Files (x86)//Google//Chrome//Application//chromedriver.exe' # 本機chromedriver的位置
driver = webdriver.Chrome(executable_path=chrome, options=option)

# browser大小設為手機大小, 為了截圖好用
driver.set_window_size(375, 812) # iphone XS

# 前往網頁
driver.get('https://app.ssm.gov.mo/healthPHD/page/index.html')

# 個人資料, 全部都是String
name = ''
sex = ''
id_card = ''
phone = ''
birth_year = ''
birth_month = ''
birth_day = ''
search_address = ''
complete_address = ''

if sex == '女':
    sex = 'option[3]'
elif sex == '男':
    sex = 'option[2]'

# 進入
driver.switch_to.frame('pageToolsbar_frame')
driver.find_element_by_xpath('/html/body/div[2]/a').click()
driver.find_element_by_name('agreement').click()
driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[2]/a').click()

# 填表
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[42]/div/input').send_keys(name)
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[44]/div/select/' + sex).click() # female

# 出生年月日為下拉選單, 找出其value作出比
selectYear = Select(driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[45]/div/div[2]/select'))
selectYear.select_by_value(birth_year)
selectMonth = Select(driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[45]/div/div[3]/select'))
selectMonth.select_by_value(birth_month)
selectDay = Select(driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[45]/div/div[4]/select'))
selectDay.select_by_value(birth_day)

# driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[45]/div/div[2]/select/option[' + str(2021-birth_year+2) + ']').click() # year
# driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[45]/div/div[3]/select/option[' + str(birth_month+1) + ']').click() # month
# driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[45]/div/div[4]/select/option[' + str(birth_day+1) + ']').click() # day

driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[47]/div[1]/div/div[1]/label/input').click() # 澳門居民身份證
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[47]/div[3]/div[2]/div[1]/div[1]/input').send_keys(id_card) # 身份證number
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[49]/div/div[1]/div[1]/div/div/label/input').click() # 澳門
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[1]/div[49]/div/div[1]/div[2]/div/input').send_keys(phone) # 澳門電話號碼

driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[2]/div[3]/div/div/div[3]/label/input').click() # 沒有以上症狀
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[3]/div[3]/div/div/div[2]/label/input').click() # 沒有接觸COVID-19病人
driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[4]/div/div[4]/div/div/label/input').click() # 旅居史: 澳門

driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/button').click() # 下一步

# 登記地址

# 用身份證明局的地址
# driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div/div/label/input').click()

# 手動登記地址
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div/div/label/input').click()  # 選擇現在登記地址
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/button').click()  # 按開填地址
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[1]/input').send_keys(search_address) # 輸入大廈
time.sleep(0.5) # 因為手動輸入關鍵字後, 要比少少時間等個page loading出官方版地址的選項

# 檢查是否所需的官方版地址, 正確才選
span_name = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[2]/ul/li/a/span[text()="' + complete_address +'"]')
if span_name:
    span_name.click() # 選大廈, 街道已自動填寫

driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/button').click()  # 下一步

# 確認已填入的資料
driver.find_element_by_xpath('/html/body/div[4]/a').click()  # 下一步

# 是否同意儲存
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[4]/div/div/label/input').click() # 不同意儲存, 因為下次登入都是會python由0開始重填
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[9]/div[2]/div[1]').click() # 提交本地

# 成功生成健康碼

# 截圖及儲存
time.sleep(5) # 因為提交後, 要比少少時間等個page loading出健康碼, 等一陣先截圖
driver.save_screenshot('../../../Dropbox/healthy_code.png')

driver.close()
