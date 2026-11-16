nums = [1, 20, 1, 20, 1, 20, 1, 20]

#внутри списка
for i in range(1, len(nums), 2):
    nums[i] *= 2

print(nums)




#с созданием нового списка
nums = [1, 20, 1, 20, 1, 20, 1, 20]
new_nums = []
for i in range(0, len(nums)):
    if i % 2 != 0:
        new_nums.append(nums[i] * 2)
    else:
        new_nums.append(nums[i])
print(new_nums)





#предельно коротко(по строчкам) и нечитаемо
nums = [1, 20, 1, 20, 1, 20, 1, 20]
nums = [x * 2 if i % 2 else x for i, x in enumerate(nums)]
print(nums)

#чуть краче
nums = [1, 20, 1, 20, 1, 20, 1, 20]
nums = [x * (1 + i % 2) for i, x in enumerate(nums)]
print(nums)