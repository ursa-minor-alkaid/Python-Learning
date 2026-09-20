# NCRE2 库

时间：`2026年9月11日`

## 1. turtle 模块

### 简介

- `turtle` 是 Python 的**标准库**模块（随解释器一起安装，`import turtle` 即可用），用于绘制图形
- 设计思想：想象屏幕上有一只"海龟"，它持有**状态**（位置、朝向、画笔颜色、画笔粗细、是否落笔……），通过命令改变状态并留下轨迹
- 海龟坐标系：
  - 屏幕中心为原点 `(0, 0)`
  - 向右为 x 正方向，向上为 y 正方向；
  - 朝向以"东"为 0°，**逆时针为正**

#### turtle 属于"即时模式"绘图

- **即时模式（immediate-mode）**：一种 2D 绘图范式——一块画布 + 一支"笔"，发出指令就立刻留下轨迹，画完即成像素，**不保留图形对象**。
  - turtle 和 HTML5 Canvas 都属于这一类（turtle 底层就是 Tkinter 的 Canvas 控件）
- 与之相对的是**保留模式（retained-mode）**：图形以对象形式存在场景树中（如 SVG 的 `<circle>`、Qt 的 QGraphicsItem），可单独选中、移动、修改，由框架负责重绘
- 后果：
  - turtle 画完后无法"点住一条线拖走"，想改只能 `undo()`/`clear()` 重画；
  - 这也是它和 matplotlib（保留模式，figure 里每个对象都可查询修改）的本质区别
- *turtle 与 Canvas 的关键差异在**坐标模型**：turtle 用相对/极坐标（"向前走、转身"，即航位推算 dead reckoning），Canvas 用绝对/直角坐标（`lineTo(x, y)`，方向要自己算三角函数）*

#### 定位与局限

- **主要用于教学**：官方文档明确说明，turtle 源自 1967 年的 Logo 语言，最初是"供教师在课堂中使用的教学工具"。实际使用场景几乎全部集中在编程教学、初学者练手项目（贪吃蛇、Pong 等）、分形/生成艺术演示、算法可视化
- **性能差**：底层基于 Tkinter，逐条命令同步绘制，画大量图元时极慢，不适合渲染复杂图形
- **能力有限**：没有真正的游戏引擎能力（精灵管理、音效、帧循环优化），也不适合数据图表和专业 GUI 开发
- 因此**实际工作中很少使用**，替代方案：
  - 数据可视化 → `matplotlib` / `plotly`
  - 小游戏 → `pygame`
  - 专业图形/GUI → `Qt` / `OpenGL` / Web Canvas
- 对二级考试而言：
  - 掌握命令表和读程序写输出即可，不必深入
  - Turtle 题对系统给出的代码**不得做任何修改**，只允许补全指定行数，否则本题 0 分

### turtle 操作

#### 三类基本操作

turtle 的命令可以分为三类：

**控制海龟运动（改变位置/朝向）**

| 函数 | 作用 |
|---|---|
| `turtle.fd(d)` / `forward(d)` | 向当前方向前进 d 像素（d 可为负，表示后退） |
| `turtle.bk(d)` / `backward(d)` | 后退 d 像素 |
| `turtle.lt(a)` / `left(a)` | 左转 a 度 |
| `turtle.rt(a)` / `right(a)` | 右转 a 度 |
| `turtle.seth(a)` / `setheading(a)` | 设置绝对朝向为 a 度（不转身，直接设定） |
| `turtle.goto(x, y)` | 移动到坐标 (x, y)（绝对坐标） |
| `turtle.setx(x)` / `sety(y)` | 只设置横/纵坐标 |
| `turtle.circle(r, extent)` | 绘制一个指定半径 r 和角度 extent 的圆或弧形；圆心默认在海龟**左侧**（注意：**是海龟的左侧而不是画布的左侧**），r 为负时圆心在右侧 |
| `turtle.home()` | 设置当前画笔位置为原点，朝向东 |
| `turtle.dot(size, color)` | 绘制一个指定直径 size 和颜色 color 的圆点 |
| `turtle.undo()` | 撤销画笔的最后一步动作 |

**控制画笔（影响"留下什么轨迹"）**

| 函数 | 作用 |
|---|---|
| `turtle.pendown()` / `pd()` | 落笔，移动时留下轨迹 |
| `turtle.penup()` / `pu()` | 提笔，移动时不画线（用于"跳转"到某处再画） |
| `turtle.pensize(n)` | 画笔粗细 |
| `turtle.pencolor(c)` | 画笔颜色 |
| `turtle.fillcolor(c)` | 填充颜色 |
| `turtle.color(a, b)` | 同时设置画笔色 a 和填充色 b |
| `turtle.begin_fill()` | 填充图形前，调用该方法 |
| `turtle.end_fill()` | 填充图形结束 |
| `turtle.filling()` | 返回填充的状态，`True` 为填充，`False` 为未填充 |
| `turtle.clear()` | 清空当前窗口，但不改变当前画笔的位置 |
| `turtle.reset()` | 清空当前窗口，并重置位置等状态为默认值 |
| `turtle.write(str, font=None)` | 在当前海龟位置输出字符串，可指定 font 字体，如 `font=("Arial", 12, "normal")` |
| `turtle.stamp()` | 在当前状态盖一个"海龟印章"（`clear()` 会清除印章，`reset()` 全部重置） |

**全局控制（影响整块画布）**

| 函数 | 作用 |
|---|---|
| `turtle.setup(w, h)` | 设置窗口大小 |
| `turtle.title(s)` | 设置窗口标题 |
| `turtle.bgcolor(c)` | 设置背景颜色 |
| `turtle.speed(n)` | 设置画笔的绘制速度，参数为 0~10 之间，`0` 为最快 |
| `turtle.hideturtle()` / `showturtle()` | 隐藏/显示画笔（海龟本体） |
| `turtle.isvisible()` | 如果 turtle 可见，则返回 `True` |
| `turtle.screensize(w, h, bg)` | 设置画布窗口的宽度、高度和背景颜色 |
| `turtle.done()` | 保持窗口不关闭（绘图程序最后一句） |
| `turtle.colormode(m)` | 颜色模式：`1.0` 表示 RGB 用 0~1 浮点；`255` 表示用 0~255 整数 |

#### 查询状态

- `turtle.position()`：当前位置
- `turtle.heading()`：当前朝向
- `turtle.isdown()`：画笔是否落下

#### 颜色的三种写法

```python
turtle.pencolor("red")              # 1. 颜色字符串
turtle.pencolor("#FF6347")          # 2. 十六进制
turtle.colormode(255)
turtle.pencolor(255, 99, 71)        # 3. RGB 三元组（受 colormode 控制取值范围）
```

*配合 `colorsys` 标准库可以用 HSV 生成彩虹色：*

```python
import colorsys
r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0)  # h 取 0~1 遍历即得彩虹
```

---

## 2. jieba 库（中文分词）

**定位**：最流行的中文**分词**第三方库。英文靠空格天然分词，中文没有空格，jieba 通过内置中文词库 + 图结构和动态规划算法找到最大概率词组来完成切分。

**安装与导入**：

```bash
pip install jieba
```

```python
import jieba
```

**三种分词模式**：

| 模式 | 参数 | 特点 | 适用场景 |
|---|---|---|---|
| 精准模式 | `cut_all=False`（默认） | 把句子精准切分，无冗余 | 文本分析 |
| 全模式 | `cut_all=True` | 扫描出所有可能的词语，有冗余 | 快速提取 |
| 搜索引擎模式 | `cut_for_search()` | 在精准模式基础上对长词再次切分，提高召回率 | 搜索引擎 |

**常用函数**：

| 函数名 | 描述 |
|---|---|
| `jieba.lcut(s)` | 精确模式，返回一个**列表**类型 ← **必须会** |
| `jieba.lcut(s, cut_all=True)` | 全模式，返回一个列表类型 |
| `jieba.lcut_for_search(s)` | 搜索引擎模式，返回一个列表类型 |
| `jieba.add_word(w)` | 向分词词典中增加新词 w |

- 对应的 `jieba.cut()` 系列参数相同，但返回**生成器**而非列表
- 自定义词典：`jieba.add_word("清华北")` 添加新词、`jieba.del_word()` 删除、`jieba.suggest_freq()` 调整词频

示例：

```python
import jieba

s = "我来到北京清华大学"

jieba.cut(s)                # 生成器（惰性），需用 join 或 list 转换
jieba.lcut(s)               # 返回列表 ← 考试最常用
# ['我', '来到', '北京', '清华', '大学']

jieba.lcut(s, cut_all=True) # 全模式
# ['我', '来到', '北京', '清华', '清华大学', '华大', '大学']

jieba.lcut_for_search(s)    # 搜索引擎模式
# ['我', '来到', '北京', '清华', '华大', '大学', '清华大学']
```

- 拼接结果：`print("/".join(jieba.lcut(s)))`