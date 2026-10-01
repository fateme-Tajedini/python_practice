#    . while و حلقه in اسکریپتی برای حذف یک عدد تکراری در لیست بااستفاده از عملگر

# numbers= [0,1,3,0,0,8,100,10,0]

# while 0 in numbers:
#     numbers.remove(0)
#     print(numbers)

#complete



numbers=[1,2,4,6,7,8,9,10]

if 0 in numbers:

    while 0 in numbers:
     numbers.remove(0)
     print(numbers)
else:
   print(" 0 is not exist")

# complete
# اسکریپتی که اول چک میکنه عنصر در لیست وجود داره یانه بعد نمامی تکرار های عنصر از لیست حذف میکنه 