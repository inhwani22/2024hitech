#%%
print("롤러코스터를 타러 오셨군요!")
height = int(input("키가 몇 cm 입니까?"))

if height >= 120:
    print("롤러코스터를 탈 수 있습니다!")
    age = int(input("당신은 몇살입니까?"))
    if age < 12:
        print("무료입니다!")
    elif age <=18:
        print("7천원입니다")
    else:
        print("만2천원입니다")
else:
    print("죄송하지만 롤러코스터를 탈 수 없어요.")    
# %%
