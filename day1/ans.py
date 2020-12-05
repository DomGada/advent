file = open("input.txt", "r")
nums = []
for line in file:
    nums.append(line)

for i in range(0,len(nums)-2):
    for j in range(1,len(nums)-1):
        for k in range(2, len(nums)):
            if int(nums[i]) + int(nums[j]) + int(nums[k]) == 2020:
                print(int(nums[i])*int(nums[j])*int(nums[k]))
