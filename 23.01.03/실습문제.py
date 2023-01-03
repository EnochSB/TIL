# num = int(input('정수를 입력하세요 > '))
# if num % 2 :
#     print('홀수')
# else:
#     print('짝수')

dust = int(input('미세먼지 농도 > '))
if dust > 150:
    print('미세먼지 농도는 매우나쁨입니다.')
elif  dust > 80:
    print('미세먼지 농도는 나쁨입니다.')
elif dust > 30:
    print('미세먼지 농도는 보통입니다.')
elif dust < 0:
    print('올바른 미세먼지 농도를 입력해주세요.')
else:
    print('미세먼지 농도는 좋음입니다.')