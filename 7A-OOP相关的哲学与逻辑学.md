# OOP相关的哲学与逻辑学

时间：`2026年8月10日`

**注意：OOP 不仅指 python**

## 1. Plato

### 理念论（Theory of Forms）

- **理念/理型**：Plato refers to **Forms** as abstract representations that are **templates** or **patterns** for real world objects or characteristics of objects.
  - 理型是一个抽象的、完美的、永恒不变的模板或蓝图。它存在于一个超越我们感官世界的理念世界中。
- **“殊相”**：The flower is said to be **a particular** that inherits its qualities from the **forms**, one of which is beauty.
  - The form of true beauty is constant and unchanging, whereas a flower may possess beauty for a while, but ultimately looses it when it withers and dies. 
  - 这些具体事物是“理型”的不完美复制品或实例
  - Being abstract, **forms exist independently of the particulars or real world objects** that inherit their qualities. 
- **“分有”**：a flower is said to **partake** of the form of beauty. It’s beautiful, but we never see true beauty. [^Plato and Object Oriented Programming]

### OOP 和理念论

- **“理型”（Form） ≈ OOP 的“类”（Class）**
  - 两者都是抽象的模板/蓝图，定义了事物的本质特征，但本身并非实体 [^Plato and Object Oriented Programming]
  - The qualities of **Forms** are that they are unchanging, incorruptible, and non-physical, which are all true of **classes**, since classes do not have state, and so cannot be changed or corrupted, and they are essentially non-physical since they can’t be interacted with directly. [^Object-Oriented Programming - Plato’s Paradigm]
- **“殊相”（Particular） ≈ OOP 的“对象”（Object）**
  - 两者都是根据模板创造出来的具体实例，是现实世界（或程序运行中）真实存在的东西 
  - “对象”是根据“类”这个蓝图创建出来的具体实例。可以根据一个 `OfficeChair（办公椅）` 的类，创建出许多个具体的办公椅对象，比如 `我的办公椅`、`你的办公椅` [^Plato and Object Oriented Programming]
- **“分有” ≈ OOP 的“实例化”**

### How Does This Help Me Code?

> Coding with this analogy in mind, we can ensure that **our classes truly represent idealised and non-physical progenitors of objects**, and that **objects are only implemented and stateful offspring from classes**. 
> 
> Classes should basically define the Form of the thing you are describing. 
> 
> Of course, most classes in real code don’t have anything to do with real-world things like chairs and stools, nevertheless, the exercise of thinking about the true essence of what you are describing will result in better OOP code. [^Object-Oriented Programming - Plato’s Paradigm]

---

## 2. Aristotle

原文详见 `assets`：[[Aristotle and Object-Oriented Programming]]

### 三段论

**三段论第一格的AAA式**

$$
\small
\frac{
    \begin{array}{c}
      大前提 \quad A具有a属性 \quad M—P（中项—大项） \\
      小前提 \quad B属于A \quad S—M（小项—中项） 
    \end{array}
  }
  {结论 \quad B有a属性 \quad S—P（小项—大项）}
$$

示例：

$$
\footnotesize
\frac{
    \begin{array}{c}
      所有哺乳动物都会哺乳 \\
      所有人类都是哺乳动物 
    \end{array}
  }
  {因此，所有人类都会哺乳}
$$

- **大前提 (Major Premise)**：这是一个关于一个普遍概念（***属，Genus***）的普遍性陈述。
- **小前提 (Minor Premise)**：这是一个陈述，将一个更特殊的概念（***种，Species***）归入那个普遍概念。
- **结论 (Conclusion)**：基于以上两个前提，逻辑上必然推导出的新知识。

### OOP 和三段论

- 三段论思想 $\rightarrow$ 继承
  - **大前提 ≈ 通用基类**（Base Class / Superclass）/父类
  - **小前提 ≈ 特殊派生类**（Derived Class / Subclass）/子类
  - **结论完成了继承**
- **OOP的起点：分类**
  - 当一个程序员面对一个复杂问题（例如开发一个银行系统）时，他首先要做的就是识别出问题领域中的核心概念，比如“账户 (Account)”、“客户 (Customer)”、“交易 (Transaction)”。
  - 程序员通过编写一个 `class` 来将这个概念固化下来。一个 `class` 就是程序员对一个概念的“定义”
  - **编程的核心活动是思考和建模，而不是敲代码**。一个类的设计质量，直接取决于程序员对相应概念“简单领悟”的深度和准确性。[^Aristotle and Object-Oriented Programming]


[^Plato and Object Oriented Programming]: https://www.richardfarrar.com/plato-and-object-oriented-programming/
[^Object-Oriented Programming - Plato’s Paradigm]: https://gavindou.ch/blog/oop-platos-paradigm
[^Aristotle and Object-Oriented Programming]: assets