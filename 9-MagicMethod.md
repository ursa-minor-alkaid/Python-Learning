# Magic Method

时间：`2025年10月27日`

## 1. 简介：<mark style="background-color: #333; color: #fef08a;">“魔法”方法/属性与“语法糖”</mark>

- **特殊方法/特殊属性**也被称为 **“魔法”方法（Magic Method
）/属性**
  - 在Python中，使用双下划线开头和结尾的命名是一种特殊的命名约定。这些名称被官方称为 **“特殊方法 (Special Methods)”** 或 **“特殊属性 (Special Attributes)”**
  - 其定义是：由Python语言自身定义和保留的、用于实现特定语言特性或协议的名称。它们不是为用户直接调用而设计的，而是由Python解释器在特定操作发生时自动调用的。
  - 约定的社区俗称是 **“dunder”**，即 **“double underscore”** 的缩写
- **“语法糖”（Syntactic Sugar）**
  - 语法糖是指在编程语言中添加的某种语法，这种语法对语言的功能没有影响，但能让程序员更方便、更清晰地使用语言。它是一种“更甜美”的书写方式，其背后对应着更基础、更复杂的代码结构。
  - 换句话说，语法糖让代码写起来更简单，读起来更清晰，但它并没有创造任何新的计算机能力。解释器或编译器会负责将其“脱糖（Desugar）”，翻译成它背后等价的、更底层的形式。
  - 常见的Python语法糖示例：`+` 运算符就是 `__add__` 方法的语法糖

---

## 2. 已经学习的魔法方法

- `__init()__`、`__new__`：[7-面向对象](7-面向对象、类.md#5-初始化函数与析构函数)
- `__name__`：[8-模块与包](./8-模块与包.md#name-属性)

---

## 3. 属性的访问控制

- **属性访问控制（Attribute Access Control）** 是面向对象编程中的一个核心原则，指的是对一个对象的内部状态（即它的属性）的访问进行管理和限制的机制
  - 在很多语言中（如Java, C++），这通过 public, private, protected 等关键字来强制实现。
  - 但在Python中，理念是“We are consenting adults here”（我们都是负责任的成年人），并没有严格的私有属性。它更多地依赖约定，但这些约定并不能从根本上阻止访问。
- 使用魔法方法实现高级、自定义属性访问控制

**`__getattribute__(self, name)`**

- 无条件拦截；只要你尝试访问一个**对象**的**任何属性**，这个方法总是会被第一个调用
  - 作用：它是属性访问的第一道关卡。无论属性是否存在，它都会被触发。
  - 注意事项：这是最强大的，也是最危险的一个。因为它总是被调用，所以非常容易在其中写出无限递归的bug
- 示例：

  ```python
  class MyClass:
  def __getattribute__(self, name):
      print(f"正在访问属性 '{name}'...")
      # 错误示范：这会再次触发 __getattribute__，导致无限递归！
      # return self.name 
      # 正确方法：必须调用父类(object)的__getattribute__来获取属性值
      return object.__getattribute__(self, name)

  obj = MyClass()
  obj.x = 10
  print(obj.x)
  # 输出:
  # 正在访问属性 'x'...
  # 10
  ```

**`__getattr__(self, name)`**

- 触发时机：仅当属性查找失败时。当你试图访问一个不存在的属性时，Python在所有其他地方都找不到这个属性后，才会调用 `__getattr__` 作为最后的尝试。
  - 作用：它是一个“备用”或“后备”方法，用于处理那些不存在的属性访问请求。
  - 应用场景：可以用来实现动态属性、代理模式，或者返回一个默认值
- 示例：

  ```python
  class DynamicAttributes:
      def __init__(self):
          self.real_attribute = "I exist"

      def __getattr__(self, name):
          print(f"'{name}' 属性不存在，触发 __getattr__")
          return f"这是为 '{name}' 动态生成的值"

  d = DynamicAttributes()
  print(d.real_attribute)  # 访问存在的属性，不会触发 __getattr__
  print(d.fake_attribute)  # 访问不存在的属性，会触发 __getattr__
  # 输出:
  # I exist
  # 'fake_attribute' 属性不存在，触发 __getattr__
  # 这是为 'fake_attribute' 动态生成的值
  ```

**`__setattr__(self, name, value)`**

- 触发时机：当你尝试给一个属性赋值时（例如 `obj.some_attribute = 123`）
  - 作用：拦截所有的属性赋值操作
  - 应用场景：可以用于数据验证（如检查值的类型或范围）、记录属性变更日志等
  - 注意事项：和 `__getattribute__` 类似，也存在无限递归的风险
- 示例：

  ```python
  class SecureSetter:
      def __init__(self):
          self._age = 0

      def __setattr__(self, name, value):
          print(f"正在设置属性 '{name}' = {value}")
          if name == '_age':
              if not isinstance(value, int) or not (0 <= value <= 150):
                  raise ValueError("年龄必须是0-150之间的整数！")
          # 错误示范：self.name = value 会再次触发 __setattr__ 导致无限递归
          # 正确方法：直接操作实例的__dict__字典
          self.__dict__[name] = value

  s = SecureSetter()
  s._age = 25      # 成功
  try:
      s._age = 200 # 失败，会抛出ValueError
  except ValueError as e:
      print(e)
  # 输出:
  # 正在设置属性 '_age' = 25
  # 正在设置属性 '_age' = 200
  # 年龄必须是0-150之间的整数！
  ```

**`__delattr__(self, name)`**

- 触发时机：当你尝试删除一个属性时（例如 `del obj.some_attribute`）
  - 作用：拦截属性删除操作
  - 应用场景：可以用来防止某些重要属性被意外删除
- 示例：

  ```python
  class Undeletable:
      def __init__(self):
          self.permanent = "你不能删除我"
          self.temporary = "你可以删除我"

      def __delattr__(self, name):
          print(f"正在尝试删除属性 '{name}'")
          if name == 'permanent':
              raise AttributeError(f"属性 '{name}' 是受保护的，无法删除！")
          # 正确方法：调用父类的__delattr__
          super().__delattr__(name)

  u = Undeletable()
  del u.temporary
  print("temporary 已删除")
  try:
      del u.permanent
  except AttributeError as e:
      print(e)
  # 输出:
  # 正在尝试删除属性 'temporary'
  # temporary 已删除
  # 正在尝试删除属性 'permanent'
  # 属性 'permanent' 是受保护的，无法删除！
  ```

---

## 4. 对象的描述器

### 简介

- 如果说 `__getattr__` 家族方法对**整个对象的属性访问**进行拦截，那么**描述器（Descriptor）** 就是对**单个特定属性**进行精细化、可复用管理的强大工具
- 描述器是一个实现了“描述器协议”的类。所谓“描述器协议”，就是指一个类至少实现了以下三个“魔术方法”中的任意一个：
  - `__get__(self, instance, owner)`
  - `__set__(self, instance, value)`
  - `__delete__(self, instance)`
- 当**一个类的类属性被赋值为这个描述器类的实例**时，这个描述器实例就变成了那个属性的“管理者”。对这个属性的任何访问、赋值或删除操作，都会被这个描述器实例的相应方法（`__get__`, `__set__`, `__delete__`）所捕获和处理
- 核心思想：将对单个属性的访问逻辑，从主类中抽离出来，封装到一个独立的、可复用的描述器类中。

### 对象字典 `__dict__`

- 对象字典 `__dict__` 是一个内置于大多数Python对象实例中的特殊属性，它本身是一个字典，用来存储该实例的所有可写属性及其对应的值
- 当你执行一个看似简单的操作，比如 `obj.age = 30`，Python解释器在默认情况下的“幕后操作”其实就是：`obj.__dict__['age'] = 30`
- `__dict__` 是默认的属性存储区，而我们之前讨论的所有魔术方法和描述器，都是围绕着如何与这个默认存储区进行交互而设计的。它们要么是绕过它，要么是控制对它的访问

### `__get__`, `__set__`, `__delete__` 详解

**`__get__(self, instance, owner)`**

- 触发时机：当描述器管理的属性被读取时调用。
- 参数说明：
  - `self`: 描述器对象自身的实例
  - `instance`: 拥有者对象的实例。也就是我们正在通过哪个对象来访问这个属性。例如，执行 `my_obj.my_attr `时，`instance` 就是 `my_obj`
  - `owner`: 拥有者的类。例如，`instance` 是 `MyClass` 的一个实例，那么 `owner` 就是 `MyClass` 这个类本身
- 特殊情况：如果通过类来访问属性（如 MyClass.my_attr），instance 参数会是 None。这允许你定义当属性在类级别被访问时的不同行为。

**`__set__(self, instance, value)`**

- 触发时机：当描述器管理的属性被赋值时调用
- 参数说明：同上

**`__delete__(self, instance)`**

- 触发时机：当描述器管理的属性被删除时（使用 del 关键字）
- 参数说明：没有 `class`

---

## <mark>5. 自定义容器（Container）</mark>

<mark>在 Python 中，常见的容器类型有: dict, tuple, list, string。其中也提到过可容器和不可变容器的概念。其中 tuple, string 是不可变容器，dict, list 是可变容器</mark>



```python

```

```python

```

```python

```

```python

```

---

## 6. 运算符相关的魔术方法（简要介绍）

- **运算符相关的魔术方法（Operator-related Magic Methods）** 是指一系列特殊的、以双下划线开头和结尾的Python方法，它们能让你自定义一个类的实例如何响应内置的运算符，如 `+`, `==`, `[]`, `in` 等
  - 这个过程在编程术语中被称为 **“运算符重载”（Operator Overloading）**
- 核心思想：
  - 当Python解释器看到一个表达式，比如 `object1 + object2`，它实际上会尝试“翻译”这个操作，将其转换为一个方法调用：`object1.__add__(object2)`
  - 通过在自己的类中定义 `__add__` 方法，就等于告诉了Python：“当我的类的两个实例相加时，不要用默认的方式，而是执行我在这里写的这段代码”
- 使用目的：为了让代码更直观、更具可读性、更“Pythonic”
- 示例：`vector类`

  ```python
  import math

  class Vector:
      def __init__(self, x=0, y=0):
          self.x = x
          self.y = y

      # 响应 + 运算符
      def __add__(self, other):
          if not isinstance(other, Vector):
              return NotImplemented # 表示我不知道如何与这个类型相加
          # 返回一个新的 Vector 实例
          return Vector(self.x + other.x, self.y + other.y)

      # 响应 == 运算符
      def __eq__(self, other):
          if not isinstance(other, Vector):
              return False
          return self.x == other.x and self.y == other.y
  ```