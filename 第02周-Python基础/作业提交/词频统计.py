text = "我爱学习，学习使我快乐"
counts ={}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
for ch, n in counts.items():
    print(f"{ch}:{n}")
max_ch=""
max_n = 0
for ch, n in counts.items():
    if n > max_n:
        max_ch = ch
        max_n = n
print(f"出现最多的是：{max_ch}，共 {max_n} 次")