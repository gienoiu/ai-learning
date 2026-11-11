# Python 速查小抄（第 2 周用）

> 不用背。写的时候忘了就翻，翻多了自然记住。
> 例子都可以复制到 `练习.py` 里跑一遍，看到输出比读十遍管用。

---

## 0. 怎么运行

```powershell
python 你的文件名.py
```

文件名用英文或拼音，**不能有空格**，结尾必须 `.py`。
终端要停在文件所在的那个文件夹（提示符里能看到文件夹名）。

---

## 1. 变量：给数据起个名字

```python
name = "小明"       # 字符串，用引号
age = 18            # 整数，不用引号
height = 1.75       # 小数
is_student = True   # 布尔值：True / False

print(name, age)    # 一次打印多个，用逗号隔开
print(type(age))    # <class 'int'> —— type 用来查类型
```

---

## 2. 输入和输出

```python
name = input("你叫什么名字？")    # input 拿到的一定是字符串
age = int(input("你几岁？"))      # 要当数字用就 int() 转一下

print("你好，" + name)
print(f"你今年 {age} 岁，明年 {age + 1} 岁")   # f-string：{} 里放变量或算式
```

> `"18" + 1` 会报错——字符串不能直接和数字相加。`int("18")` 才是 18。

---

## 3. 条件判断

```python
score = 85
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

> **冒号 `:` 不能少；下面那行必须缩进 4 个空格。** 这是 Python 的硬规矩。

---

## 4. 循环

**for**：知道要跑几次的时候用

```python
for i in range(5):        # 0 1 2 3 4（不含 5）
    print(i)

for i in range(1, 10, 2): # 1 3 5 7 9（从 1 到 9，每次 +2）
    print(i)
```

**while**：满足条件就一直跑

```python
n = 0
while n < 3:
    print("第", n, "次")
    n = n + 1
```

**嵌套循环**：循环里再套循环

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "×", j, "=", i * j)
```

---

## 5. 函数：把一段代码打包，起个名字

```python
def add(a, b):        # def = 定义函数
    result = a + b
    return result     # return = 把结果交出去

print(add(3, 5))      # 8
```

> 不写 `return` 的函数，返回值是 `None`（什么也没有）。

---

## 6. 列表 list：一串有顺序的东西

```python
scores = [85, 92, 78]
print(scores[0])       # 85，下标从 0 开始
print(len(scores))     # 3
scores.append(100)     # 末尾加一个
for s in scores:       # 挨个拿出来
    print(s)
```

---

## 7. 字典 dict：key → value 的对照表

```python
student = {"name": "小王", "score": 85}
print(student["name"])       # 小王
student["score"] = 90        # 改值
student["age"] = 18          # 加新的键

print(student.get("class", "没有这个键"))   # 取不到时给默认值，不报错

for k, v in student.items():                # 同时拿 key 和 value
    print(k, "=", v)
```

---

## 8. 五个最常遇到的报错

| 报错 | 意思 | 常见原因 |
|---|---|---|
| `SyntaxError` | 语法错误 | 少引号、少括号、少冒号 |
| `IndentationError` | 缩进错误 | if / for / def 下面那行没缩进 |
| `NameError: name 'xxx' is not defined` | 名字不认识 | 变量名打错，或还没定义就用了 |
| `TypeError` | 类型不对 | 字符串和数字直接相加、参数个数不对 |
| `KeyError` | 字典里没这个键 | 用 `d["key"]` 取了一个不存在的键 |

---

## 9. 写完自查三问

1. 每一行我都能说出它在干嘛吗？
2. 变量名看得懂吗？（`a`、`b`、`x` 这种过几天就忘了）
3. 输入奇怪的东西（比如年龄输「abc」）会怎样？

---

## 10. 一个小练习（热身用，不算作业）

打印 1 到 10 的和：

```python
total = 0
for i in range(1, 11):
    total = total + i
print(total)      # 55
```

试着改成「打印 1 到 10 里所有偶数的和」。
