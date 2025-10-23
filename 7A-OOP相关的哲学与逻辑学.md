# OOP相关的哲学与逻辑学

时间：`2025年10月23日`

## 1. Plato

### Theory of Forms（理念论）

- **理念/理型**：Plato refers to **Forms** as abstract representations that are **templates** or **patterns** for real world objects or characteristics of objects.
  - 理型是一个抽象的、完美的、永恒不变的模板或蓝图。它存在于一个超越我们感官世界的理念世界中。
- **“殊相”**：The flower is said to be **a particular** that inherits its qualities from the **forms**, one of which is beauty.
  - The form of true beauty is constant and unchanging, whereas a flower may possess beauty for a while, but ultimately looses it when it withers and dies. 
  - 这些具体事物是“理型”的不完美复制品或实例
  - Being abstract, **forms exist independently of the particulars or real world objects** that inherit their qualities. 
- **“分有”**：a flower is said to **partake** of the form of beauty. It’s beautiful, but we never see true beauty. [^Plato and Object Oriented Programming]

### OOP and Theory of Forms

- **“理型”（Form） ≈ OOP的“类”（Class）**
  - 两者都是抽象的模板/蓝图，定义了事物的本质特征，但本身并非实体 [^Plato and Object Oriented Programming]
  - The qualities of **Forms** are that they are unchanging, incorruptible, and non-physical, which are all true of **classes**, since classes do not have state, and so cannot be changed or corrupted, and they are essentially non-physical since they can’t be interacted with directly. [^Object-Oriented Programming - Plato’s Paradigm]
- **“殊相”（Particular） ≈ OOP的“对象”（Object）**
  - 两者都是根据模板创造出来的具体实例，是现实世界（或程序运行中）真实存在的东西 
  - “对象”是根据“类”这个蓝图创建出来的具体实例。可以根据一个 `OfficeChair（办公椅）` 的类，创建出许多个具体的办公椅对象，比如 `我的办公椅`、`你的办公椅` [^Plato and Object Oriented Programming]

### How Does This Help Me Code?

> Coding with this analogy in mind, we can ensure that **our classes truly represent idealised and non-physical progenitors of objects**, and that **objects are only implemented and stateful offspring from classes**. 
> 
> Classes should basically define the Form of the thing you are describing. 
> 
> Of course, most classes in real code don’t have anything to do with real-world things like chairs and stools, nevertheless, the exercise of thinking about the true essence of what you are describing will result in better OOP code. [^Object-Oriented Programming - Plato’s Paradigm]

---

## 2. Aristotle

原文详见 `assets`：[[Aristotle and Object-Oriented Programming]]

### 继承结构与三段论

$$
\frac{\begin{array}{c} 大前提 \\ 小前提 \end{array}}{结论}
$$

- **大前提 (Major Premise)**：这是一个关于一个普遍概念（属，Genus）的普遍性陈述。
  - 例如，*所有哺乳动物都会哺乳*。
  - 这是对一个通用基类（Base Class / Superclass）的功能定义
- **小前提 (Minor Premise)**：这是一个陈述，将一个更特殊的概念（种，Species）归入那个普遍概念。
  - 例如，*所有人类都是哺乳动物*
  - 这是通过关键字来声明一个派生类（Derived Class / Subclass）继承自基类
- **结论 (Conclusion)**：基于以上两个前提，逻辑上必然推导出的新知识。
  - 例如，*因此，所有人类都会哺乳*
  - 结论不是由程序员显式写出的，而是由编译器或运行时环境自动推导并强制执行的 [^Aristotle and Object-Oriented Programming]

### OOP的基础：分类

- **OOP的起点：分类**。当一个程序员面对一个复杂问题（例如开发一个银行系统）时，他首先要做的就是识别出问题领域中的核心概念，比如“账户 (Account)”、“客户 (Customer)”、“交易 (Transaction)”。
- 程序员通过编写一个 `class` 来将这个概念固化下来。一个 `class` 就是程序员对一个概念的“定义”
- 编程的核心活动是思考和建模，而不是敲代码。一个类的设计质量，直接取决于程序员对相应概念“简单领悟”的深度和准确性。[^Aristotle and Object-Oriented Programming]

---

## 3. Mid Ages Philosophy

<mark>待收集</mark>

[^Plato and Object Oriented Programming]: https://www.richardfarrar.com/plato-and-object-oriented-programming/
[^Object-Oriented Programming - Plato’s Paradigm]: https://gavindou.ch/blog/oop-platos-paradigm
[^Aristotle and Object-Oriented Programming]: assets