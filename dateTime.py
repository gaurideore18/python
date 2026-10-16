# from dateTime import datatime
# current_datetime=datatime.now()
# new_datetime=current_datetime-timedelta(minutes=10)


# current date time now
# from dateTime import datatime,timedelta
# current_datetime=datatime.now()
# print('current_datetime',current_datetime)

# how to find anagram number
# num1=input('Enter the anagram number')
# num2=input('Enter the anagram number')
# if sorted(num1)==sorted(num2):
#     print('this is anagram number')
# else:
#     print("this is not anagram number")


list = [1, 2, 3, 45, 5, 6, 7, 7, 8, 1]

# dub = set()
# seen = set()
# for i in list:
#     if i in seen:
#         dub.add(i)
#     else:
#         seen.add(i)
# print(dub)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max = list[0]
for i in list:
    if i > max:
        max = i
print(max)
