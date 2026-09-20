# -*- coding: utf-8 -*-
"""Python 二级考试 turtle 常用函数示例：彩虹螺旋 · 星月夜"""

import turtle
import colorsys

# ---------- 1. 画布与全局设置 ----------
turtle.setup(880, 720)                        # 设置窗口尺寸
turtle.title("Turtle 炫彩图形 · Python 二级")  # 设置窗口标题
turtle.bgcolor("#0B0E14")                     # 深夜色背景
turtle.colormode(1.0)                         # 启用 0~1 浮点 RGB 颜色
turtle.speed(0)                               # 最快速度绘制
turtle.pensize(3)                             # 画笔粗细

# ---------- 2. 彩虹螺旋 ----------
SEGMENTS = 28
for i in range(SEGMENTS):
    turtle.pencolor(*colorsys.hsv_to_rgb(i / SEGMENTS, 1.0, 1.0))
    turtle.circle(16 + i * 5, 180)            # 半圆逐圈放大
    turtle.lt(10)                             # 每半圈偏转，形成螺旋

# ---------- 3. 金色五角星 ----------
turtle.penup()
turtle.goto(-60, 150)
turtle.seth(90)                               # 朝向正上方
turtle.pendown()
turtle.color("orange", "gold")                # 同时设置描边色与填充色
turtle.begin_fill()
for _ in range(5):
    turtle.fd(110)
    turtle.rt(144)
turtle.end_fill()

# ---------- 4. 圆月 ----------
turtle.penup()
turtle.goto(210, -160)
turtle.pendown()
turtle.fillcolor("#F5F5DC")                   # 仅设置填充色
turtle.begin_fill()
turtle.circle(34)
turtle.end_fill()

# ---------- 5. 坐标签名与小海龟印章 ----------
turtle.penup()
turtle.goto(-410, -330)                       # 移到左下角空白区，避开图案
turtle.seth(0)                                # 摆正朝向，印章才不会歪
turtle.shape("turtle")                        # 切换海龟造型
turtle.shapesize(2, 2)                        # 放大造型
turtle.stamp()                                # 盖一个"小海龟"印章
turtle.goto(-370, -335)                       # 印章右侧书写文字
turtle.write(
    f"当前位置 {turtle.position()} ｜ 朝向 {turtle.heading():.0f}°",
    align="left",
    font=("Microsoft YaHei", 13, "normal"),
)
turtle.hideturtle()                           # 隐藏海龟

turtle.done()                                 # 保持窗口
