filepath = 'readme.txt'

content = '''안녕하세요, 반갑습니다.
이 파일은 테스트 파일 저작을 위해 작성된 텍스트 문서입니다.
조금 낯설더라도 포기하지 마세요.'''

with open(filepath, 'w', encoding='utf-8') as file:
    file.write(content)


with open(filepath, 'r', encoding='utf-8') as file:
    lines = file.readlines()

print(f'파일명: {filepath}')
line_number = 1
for line in lines:
    print(f'{line_number}: {line.strip()}')
    line_number += 1
