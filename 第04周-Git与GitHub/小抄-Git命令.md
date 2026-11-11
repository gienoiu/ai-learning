# Git 速查小抄（第 4 周用）

> Git 是「代码的时光机」：每次 commit 就是拍一张快照，什么时候改坏了，都能翻回去。

## 1. 三个区域，先建立直觉

```text
你的文件夹          暂存区            历史快照
（工作区）   add→  （staging）  commit→ （repository）
```

- 改了文件 → 只是工作区变了，Git 还没记
- `git add` → 把改动放进暂存区（"准备提交"）
- `git commit` → 拍快照，存进历史
- `git push` → 把本地历史传到 GitHub（远程仓库）

## 2. 最常用的 8 条命令

| 命令 | 干什么 | 什么时候用 |
|---|---|---|
| `git init` | 把一个文件夹变成 Git 仓库 | 一个项目只做一次 |
| `git status` | 看现在哪些文件改了、哪些没提交 | 每次动手前先看一眼 |
| `git add .` | 把所有改动放进暂存区 | 提交前 |
| `git commit -m "说明"` | 拍快照 | 每完成一小步 |
| `git log --oneline` | 看历史快照 | 忘了自己改过啥 |
| `git remote add origin <地址>` | 记住远程仓库地址 | 一个项目只做一次 |
| `git push` | 本地 → GitHub | 每次提交后 |
| `git clone <地址>` | 把别人的项目整个下载下来 | 用别人的代码 |

再补三条常用的：

| 命令 | 干什么 |
|---|---|
| `git diff` | 看还没 add 的改动具体改了哪几行 |
| `git pull` | 把 GitHub 上的新东西拉下来 |
| `git restore <文件>` | 丢弃还没 add 的改动（小心用） |

## 3. 一次完整的流程

```powershell
cd "C:\Users\伊鑫\Documents\deepseek-harness\default-workspace\ai-learning"
git status                    # 看看有什么
git add .                     # 全放进暂存区
git status                    # 确认变绿
git commit -m "第 2 周：5 个小程序"
git push                      # 传到 GitHub
```

## 4. 报错对照表

| 报错 | 原因 | 解决 |
|---|---|---|
| `Please tell me who you are` | 没配 user.name / user.email | 回去配身份 |
| `Support for password authentication was removed` | GitHub 不再支持输密码 | 用浏览器授权（Git Credential Manager），别输密码 |
| `failed to push some refs` | 远程有你本地没有的提交 | `git pull --rebase origin main` 再 push |
| `not a git repository` | 当前目录不是仓库 | `cd` 到 ai-learning |
| `src refspec main does not match any` | 还没有 commit，或分支不叫 main | 先 commit，再 `git branch -M main` |
| `fatal: destination path already exists` | 同名文件夹已存在 | 换个目录，或给 clone 加别的名字 |
| 中文文件名显示成 `\346\226\207...` | 没关路径转义 | `git config --global core.quotepath false` |

## 5. 怎么读别人的 README

看一个开源项目，先找这四样：

1. **这是什么**（第一段话 + 截图）
2. **怎么装**（Installation / 安装）：`pip install ...` 还是 `npm install ...`
3. **怎么跑**（Usage / 使用）：那个命令就是"跑起来"的钥匙
4. **依赖和环境**（Requirements / Dependencies）：需不需要额外装东西

再看三样判断靠不靠谱：
- **最后更新时间**（两年没更新的别碰）
- **Star 数**（不是绝对，但 0 star 的要小心）
- **Issues**（有人提问、有人回答 = 活的）

## 6. 克隆别人的项目

```powershell
git clone https://github.com/用户名/仓库名.git
cd 仓库名
dir
```

`clone` 会把整个项目（包括历史记录）下载成一个文件夹。项目大、网速慢时用：

```powershell
git clone --depth 1 https://github.com/用户名/仓库名.git
```

`--depth 1` = 只下载最新一次快照，不做完整历史，快很多。
