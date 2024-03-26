import requests

# 예시로 requests를 사용하여 웹에서 텍스트를 가져옵니다.
r = requests.get('https://example.com')

# 'naver.txt' 파일을 쓰기 모드로 엽니다.
with open("naver.txt", "w") as f:
    # 텍스트를 파일에 씁니다.
    f.write(r.text)
    # 파일에 대한 정보를 출력합니다.
    print("파일명:", f.name)  # 파일명 출력
    print("파일 모드:", f.mode)  # 파일 모드 출력
    print("파일 닫혀있는지 여부:", f.closed)  # 파일이 닫혀있는지 여부 출력
