import re
# 정규식 라이브러리 re

# ca?e
p = re.compile("ca.e") 
# . : 하나의 문자를 의미 > care, cafe, case | caffe(X)
# ^ : 문자열의 시작 > ^de : desk, destination | fade(X)
# $ : 문자열의 끝 > se$ : case, base | session(X)

#m = p.match("caffe")
def print_match(m):
    if m:
        print('m.group()::',m.group()) # 정규식과 매칭이 되므로 출력 | 아니면 에러발생
        print('m.string:: ',m.string)
        print('m.start()::',m.start())
        print('m.end()::',m.end())
        print('m.span()::',m.span())
    else:
        print("매칭되지않음")

#m = p.match("case") # match: 주어진 문자열의 처음부터 일치하는지 확인
#print_match(m) #함수호출 매개변수로 m 전달

#m = p.search("good care") # search: 주어진 문자열 중에 일치하는게 있는가
#print_match(m)

#lst = p.findall("good care") #['care']
lst = p.findall("good care cafe") #['care','cafe']


# 1. p=re.compile("원하는 형태")
# 2. m=p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") :  주어진 문자열 중에 일치하는게 있는지
# 4. lst = p.findall("good care cafe") : 일치하는 모든것을 "리스트==배열" 형태로 반환