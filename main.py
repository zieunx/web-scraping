import sys
import time
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import private.private_key as key

browser = webdriver.Chrome("./chromedriver")

login_url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
id = key.insta_id
password = key.insta_password
browser.get(login_url)
time.sleep(1)

id_input = browser.find_element_by_name("username")
id_input.clear()
id_input.send_keys(id)
password_input = browser.find_element_by_name("password")
password_input.clear()
password_input.send_keys(password)
password_input.submit()
time.sleep(3)

# 인스타 검색 -------------------------------------
keyword = "레터링케이크"
url = "https://www.instagram.com/explore/tags/{}".format(keyword)

browser.get(url)
time.sleep(3)

# 검색 결과 추출 -----------------------------------
content_count = browser.find_element_by_css_selector(".g47SY").text.replace(',', '')

browser.find_element_by_css_selector("div.v1Nh3.kIKUG._bz0w").click()
time.sleep(3)

post_detail_soup = BeautifulSoup(browser.page_source, features="html.parser")
for i in range(int(content_count)):
    time.sleep(1)
    print('====================={}====================='.str(i))
    # 게시글 상세 데이터 추출 예시
    print("\n* 게시글 id")
    print("  > {}".format(browser.current_url))
    print("  > {}".format(
        browser.find_element_by_class_name("c-Yi7").get_attribute("href"))
    )

    print("\n* 회원 id")
    print("  > {}".format(post_detail_soup.find("div", {"class": "e1e1d"}).find("a").get("href")))

    print("\n* 위치")

    if post_detail_soup.find("a", {"class": "O4GlU"}):
        print("  > {}".format(post_detail_soup.find("a", {"class": "O4GlU"}).text))
        print("  > {}".format(post_detail_soup.find("a", {"class": "O4GlU"}).get("href")))

    print("\n* 이미지")
    print("  > {}".format(post_detail_soup.find("img", {"class": "FFVAD"}).get("src")))

    print("\n* 좋아요")
    print("  > {}".format(post_detail_soup.find("div", {"class": "Nm9Fw"}).find("span").text))

    print("\n* 게시글 내용")
    print("  > {}".format(post_detail_soup.find("div", {"class": "C4VMK"}).text))
    WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.HBoOv.coreSpriteRightPaginationArrow')))
    browser.find_element_by_css_selector('a.HBoOv.coreSpriteRightPaginationArrow').click()


# ------- test
# 파일만들기
# with open("test/게시글상세페이지.html", "w", encoding="utf8") as f:
#     html = browser.page_source
#     f.write(html)

# ------------------------------------------------------------------------

# 다음 게시글


# sys.exit()
