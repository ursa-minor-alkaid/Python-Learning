# 练习 1：智能电费计算器

useage = int(input("请输入本月用电量（度）："))
total_cost = 0

if useage <= 100:
    total_cost = useage * 0.5
elif useage > 100 and useage <= 200:
    total_cost = 50 + (useage - 100) * 0.8
else:
    total_cost = 50 + 80 + (useage - 200) * 1.2

print(f"本月用电量：{useage}度，应缴电费：{total_cost}元")

if useage >= 500:
    print("用电量过高，请注意节约用电！")

# 练习 2：寻找质数

for i in range(2,101):

    for j in range(2,i):
        if i % j == 0:
            break

    else:
        print(f"{i} 是质数")

print("----- 循环结束 -----")

