import time
import requests

# chrome 드라이버 모듈
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib import request

# edge 드라이버 모듈
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions
from urllib.request import urlretrieve
import os


# edgedriver==============================================
m_service = Service(executable_path = r'E:\money\msedgedriver.exe')
m_options = EdgeOptions()
m_options.add_experimental_option("detach", True)
m_driver = webdriver.Edge(service = m_service, options= m_options)


# 이미지 다운===============================================
# imagecreator 접속
m_driver.get("https://www.bing.com/images/create?FORM=SYDBIC")
draw = m_driver.find_element(By.XPATH, '//*[@id="sb_form_q"]')
#draw.send_keys("고양이 아이콘 그려줘")
keyword_draw = input('그리고싶은 아이콘을 입력하세요 : ')
keyword_tag = input('대표적인 태그를 입력하세요 : ')
draw.send_keys(keyword_draw)
draw.send_keys("\n")
m_driver.implicitly_wait(30)

# img src 찾아서 list에 저장
find_img = m_driver.find_elements(By.CLASS_NAME, 'mimg')
time.sleep(2)
src_list = []
# 중복 src가 있을시 추가하지 않음
for img in find_img:
    if img.get_attribute('src') not in src_list:
        src_list.append(img.get_attribute('src'))

time.sleep(5)
print(src_list)
time.sleep(2)

# 폴더-없을 시 생성
path_folder = 'E:/down/'
if not os.path.isdir(path_folder):
    os.mkdir(path_folder)

m_driver.implicitly_wait(5)

# 이미지 다운로드
i = 0

for link in src_list:
    i += 1
    urlretrieve(link, path_folder + keyword_tag + f'{i}.jpg')

m_driver.implicitly_wait(10)
m_driver.quit()


'''
# chromedriver==================================================
# 브라우저 꺼짐 방지 옵션
options = ChromeOptions()
options.add_experimental_option("detach", True)
# 파일 다운로드 경로 변경
options.add_experimental_option('prefs', {"download.default_directory": r"E:\\upload"})
# os에 설치된 크롬 브라우저 사용하도록 실행
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
'''

'''
# jpg png ----> svg로 변환============================================================
driver.get("https://convertio.co/kr/jpg-svg/")
time.sleep(2)

#파일 변환
driver.find_element(By.XPATH, '//*[@id="pc-upload-add"]').send_keys(r"E:\down\cat1.jpg")
time.sleep(2)
convert_img = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/button')
convert_img.click()
#driver.implicitly_wait(15)
time.sleep(15)
covert_bt = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr/td[6]/a')
covert_bt.click()
time.sleep(15)
driver.quit()
'''

'''
# 더나은 프로젝트 주소 이동==============================================================
driver.get("https://thenounproject.com/")
driver.implicitly_wait(5)

# 로그인 창으로 이동===============================
login_path = driver.find_element(By.XPATH, '//*[@id="site-header"]/div[2]/div/div[2]/div/div[2]/div/button[1]')
driver.execute_script("arguments[0].click();", login_path)
driver.implicitly_wait(3)
# id, passwd 입력 ----------로그인 입력 실패시 다시 입력하게 while문 써주면 좋을듯
#keyword_id = input('ID를 입력해주세요 : ')
#keyword_passwd = input('PASSWD를 입력해주세요 : ')

# 1) ID 입력 
driver.switch_to.window(driver.window_handles[0])
id_box = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div/div/label[1]/input')
#id_box.send_keys(keyword_id)
id_box.send_keys('사용자 아이디')
driver.implicitly_wait(3)
# 2) PASSWD 입력
passwd_box = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div/div/label[2]/input')
#passwd_box.send_keys(keyword_passwd)
passwd_box.send_keys('사용자 비밀번호')
driver.implicitly_wait(3)
# 3) 로그인버튼 클릭
login_bt = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div/div/button[1]')
login_bt.click()
time.sleep(3)


# 아이콘 올리기====================================
# 1) 페이지 접속
step1 = driver.find_element(By.XPATH, '//*[@id="site-header"]/div[1]/div/div[1]/div[1]/div/div/div[1]/nav/ul/li[5]/a')
driver.execute_script("arguments[0].click();", step1)
driver.implicitly_wait(3)
step2 = driver.find_element(By.XPATH, '//*[@id="introduction"]/div[1]/a[2]')
step2.click()
driver.implicitly_wait(3)
step3 = driver.find_element(By.XPATH, '//*[@id="upload-process"]/div/div[1]/div[3]/button')
driver.execute_script("arguments[0].click();", step3)
driver.implicitly_wait(3)
step4 = driver.find_element(By.XPATH, '//*[@id="upload-process"]/div/div[2]/div[2]/a[1]')
driver.execute_script("arguments[0].click();", step4)
driver.implicitly_wait(3)

# 2) 파일 업로드 - 업로드, 이름지정, 태그지정, 제출
upload_svg = driver.find_element(By.XPATH, '//*[@id="file-input"]')
upload_svg.send_keys(r"E:\\upload\cat1.svg")
driver.implicitly_wait(5)

input_name = driver.find_element(By.XPATH, '//*[@id="icon-forms"]/li/form/div/div[1]/input')
input_name.send_keys("favorite")
input_tags = driver.find_element(By.XPATH, '//*[@id="icon-forms"]/li/form/div/div[2]/div[2]/input')
input_tags.send_keys("like")

submit_bt = driver.find_element(By.ID, "submit-icons")
#driver.execute_script("arguments[0].click();", submit_bt)
'''
