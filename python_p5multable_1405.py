#A script that prints the multiplication table) and displays it neatly in the output.

# for i in range(1,11):
#     for j in range(1,11):
#         print("{:5}".format(i*j), end=" ")
#     print()

n = int(input(" enter n :"))
for i in range(1,n+1):           # n+1 : so than n itself is calculate, rather than a value less than it.
    for j in range(1,n+1):
        print("{:5}".format(i*j), end=" ")   # printing and formatting the multiplication table.
    print()

 #complete

  