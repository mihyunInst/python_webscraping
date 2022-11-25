import requests
res = requests.get("http://google.com")
res.raise_for_status()
#print("응답코드: ", res.status_code)

#if res.status_code == requests.codes.ok:
#    print("정상")
#else:
#    print("문제발생:",res.status_code)

print(len(res.text))
print(res.text)

#파일로 만들어서 확인하기
#           파일이름   쓰기모드(w)  인코딩설정    해당설정명
with open("mygoogle.html", 'w', encoding='utf8') as f:
    f.write(res.text)