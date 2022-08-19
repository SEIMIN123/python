str = ["egoing", "sori", "maru"];
grades = [3,5,6]; 

print("str[0]", str[1]);
print("len(str)", len(str));

print("min(grades)", min(grades));
print("max(grades)", max(grades));

# todo : 자바스크립트 배열하고 똑같음. min 문자열로 하는건 설명하려고 저렇게 한거고 min / max로 확인해보면 제일 작은숫자 제일 큰 숫자가 확인이 됨.


import statistics

print("statistics.mean(grades)", statistics.mean(grades));

# todo : statistics라는 평균값 모듈을 불러와서 mean은 평균값을 내는 것 grades의 평균값을 냄.

import random 
print(random.choice(str));

# todo : 제비뽑기를 하고 싶다 싶으면 random 모듈 불러와서 choice를 쓰면 랜덤으로 뽑힘. 이걸로 예도 들수도 있을 것 같고 여러가지 적용할수 있을듯.