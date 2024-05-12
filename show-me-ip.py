import requests
import smtplib
from email.mime.text import MIMEText

def send_email(current_ip):
    sender = 'Your gmail'  # 이 부분은 Gmail 을 이용해주세요.
    password = 'Your gmail app password'  # Gmail 을 2단계 보안 설정하고 앱 비밀번호를 설정한 후 입력하세요.
    receiver = 'Your receive email'  # 받는 이메일 주소


    msg = MIMEText(f'Your external IP address is: {current_ip}')
    msg['Subject'] = 'External IP Address Update'
    msg['From'] = sender
    msg['To'] = receiver


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

def check_ip():
    current_ip = requests.get('https://api.ipify.org').text
    send_email(current_ip)

if __name__ == "__main__":
    check_ip()


# exe 파일로 만들고싶다면 pyinstaller 를 설치하고 pyinstaller --onefile show-me-ip.py 를 입력해서 컴파일하세요.
# 컴파일 후 윈도우 작업스케줄러로 반복 실행을 설정하면 매일 설정한 시간으로 외부ip가 메일로 보내집니다.