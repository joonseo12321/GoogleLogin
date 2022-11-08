from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess


if __name__ == "__main__":
    print('구글 아이디와 비밀번호를 입력하세요.')
    gmailId, passWord = map(str, input().split())

    try:

        subprocess.Popen(
            r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe '
            r'--remote-debugging-port=9222 --user-data-dir="C:\chrometemp"'
        )  # 봇 탐지 우회를 위해 실제 사용하는 크롬의 디버깅 모드 실행

        option = Options()
        option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
        chromedriver_autoinstaller.install(True)

        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
                   'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
                   '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')  # gmail 로그인 주소
        driver.implicitly_wait(15)

        loginBox = driver.find_element("xpath", '//*[@id ="identifierId"]')  # 이메일 입력 폼
        loginBox.send_keys(gmailId)

        nextButton = driver.find_element("xpath", '//*[@id ="identifierNext"]')  # 다음 버튼
        nextButton.click()

        passWordBox = driver.find_element("xpath", '//*[@id ="password"]/div[1]/div / div[1]/input')  # 비밀번호 입력 폼
        passWordBox.send_keys(passWord)

        nextButton = driver.find_element("xpath", '//*[@id ="passwordNext"]')  # 다음 버튼
        nextButton.click()

        print('로그인에 성공했습니다.')

    except Exception as error:
        print('로그인 실패 에러: {}'.format(error))
