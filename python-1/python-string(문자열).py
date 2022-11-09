from functools import total_ordering


print('hello world')
print("hello world ")

print('''
hello
world
''')
# todo : ''' 또는 """ 가 되면 띄어쓰기가 가능함.

print("'1' + '1'", '1' + '1');

# todo : 큰따옴표로 묶어버리면 개별로 인식으로 뱉어냄. 
# todo : 작은따옴표로 들어가면 string으로 들어가기 때문에 한글자씩을 붙임. 

print('hello world'*1000);
print("len('hello world'*1000)", len('hello world'*1000));


print("'hello world'.replace('world', 'universe')", 'hello world'.replace('world', 'universe'));

# todo : ""로 묶고 replace로 ''로 넣어서 돌리면 문자열을 바꿀수가 있음. 자바스크립트 replace랑 똑같음. 변수에 넣어서 문자열 찍고 변수에 replace('넣을문자열') console찍으면 나오는거랑 같은거임.