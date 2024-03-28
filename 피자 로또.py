# 피자를 주문하는 자판기
print("파이썬 피자에 오신것을 환영합니다!")

size = input('피자 사이즈를 선택해주세요(S. M. L)')
if (size == 'S'):
    price = 15000
elif (size == 'M'):
    price = 20000
else (size == 'L'):
    price = 30000

pepperoni = input('페퍼로니 추가? YES(Y) or NO(N) > ').upper()
cheese = input('치즈 추가? YES(Y) or NO(N) > ').upper()
coke = input('콜라 추가? YES(Y) or NO(N) > ').upper()
coupon_use = input('쿠폰을 사용하시겠습니까? YES(Y) or NO(N) > ').upper()

if(coupon_use == 'Y'):
    coupon_price= int(input('사용하실 쿠폰의 금액을 입력해주세요(예시> 2000 > )'))
    price -= coupon_price

if(pepperoni == 'Y'):
    price += 2000
if(cheese == 'Y'):
    price += 3000
if(coke == 'Y'):
    price += 1000

print(f'총 지불하실 금액은 {price}원 입니다.')