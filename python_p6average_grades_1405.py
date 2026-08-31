# whileبرنامه ای بنویسید که معدل کاربر را بگیرد درحلقه 
# اگر بالای17 بود به کاربر بگه (افرین)
# اگر بین 12 تا 17 بود میگه (تنبل نباش)
#اگرزیر 12 بود میگه (افتادی)



# score = float(input("Enter score:"))
# score1 = float(input("Enter score:"))
# score2 = float(input("Enter score:"))
# avg = (score + score1 + score2)/3
# print(avg)

# if avg > 17:
#     print("goodjub")
# if 12<avg<17:
#     print("dont lazy")
# if avg<12:
#     print("you fall")

# complete


# forباحلقه 

grades = []
for i in range(6):
    score = float(input("Enter score:"))
    grades.append(score)
    print()
    
avg = sum(grades)/len(grades)

if 0<= avg <= 20:
    if avg > 17:
        print((round(avg,2)) ,": goodjub")
    elif 12<avg<17:
        print((round(avg,2)) , ": don't be lazy")
    elif avg<12:
        print((round(avg,2)) ,": you failed")



#complete but in need of revison and improvement. 
# کامل اما نیازمند بازنگری و بهبود

# مشکلات :
# 
#چک کردن اعشاری و هم صحیح بودن اعداد: complete
# نمایش تنها دو رقم بعد اعشار در نمایش میانگین :complete
#  محدود نبودن تعداد نمرات به 6 تا بلکه پیدا کردن  یک دستور کلی برای محاسبه و دریافت هر تعداد نمره از کاربر
# در صورت امکان نوشتن برنامه با حلقه whille



