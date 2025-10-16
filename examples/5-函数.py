# 练习 1：用户信息格式化器

def print_user_profile(name,age,city="保密",*tags):
    # 打印用户信息

    if tags:
        # 如果 tags 元组不为空，用 ", " 连接所有标签
        tags_str = ", ".join(tags)
    else:
        tags_str = "无"

    print(f"姓名：{name}，年龄：{age}，城市：{city}，标签：{tags_str}")

print_user_profile("西瓜",18,"北京","帅","高","富")

# 练习 2：批量处理学生成绩

def process_scores(scores,*,bonus,min_score=0):
    count = 0
    sum_scores = sum(scores)
    avg_score = sum_scores / len(scores)

    for i in scores:
        i = i + bonus
        if i < min_score:
            min_score = i

        if i >= 60:
            count += 1

    return avg_score, count

student_scores = [55, 80, 43, 65, 71, 92]
original_avg, passed_count = process_scores(student_scores, bonus=5, min_score=50)

print(f"原始成绩列表: {[55, 80, 43, 65, 71, 92]}")
print(f"修改后的成绩列表: {student_scores}")
print(f"原始平均分: {original_avg:.2f}")
print(f"及格人数: {passed_count}")

# 练习 3：使用匿名函数创建一个简单的 "操作" 计算器

operations = [
    lambda a,b: a + b,
    lambda a,b: a - b,
    lambda a,b: a % b
]

a,b = 15,4

ab_sum = operations[0](a,b)
ab_diff = operations[1](a,b)
ab_mod = operations[2](a,b)

print(f"{a} + {b} = {ab_sum}")
print(f"{a} - {b} = {ab_diff}")
print(f"{a} % {b} = {ab_mod}")