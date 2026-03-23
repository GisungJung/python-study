#파일 오픈해서 쓰기
file=open("test.txt", "w")
for data in range(1,11):
  file.write(f'{data} line\n')
file.close()


#어펜드모드
with open("test.txt", "a", encoding="utf-8") as file:
    for data in range(1, 11):
        line = f"{data} 변수활용\n"
        file.write(line)

with open("test.txt", "r", encoding="utf-8") as file:
    for line in file:
        # .strip()을1 쓰면 문장 끝의 줄바꿈(\n)을 깔끔하게 지워줍니다.
        print(line)

with open("test.txt", "r", encoding="utf-8") as file:
    data=file.read()
    print(data)