# 🍬 甜蜜实验室 (Sweet Lab)

**甜蜜制造机，搞怪也甜蜜！**

---

## ✨ 特性

- 📝 **藏头诗生成器** - 输入名字，生成浪漫/可爱/搞笑的藏头诗
- 💕 **情话生成器** - 5种风格，4种场景，帮你说情话
- 💬 **聊天话术助手** - 高情商回复、土味情话、话题开场白
- 💕 **爱情/友情测试器** - 输入名字/生日，测试契合度（纯属娱乐）
- 🎨 **头像风格化** - 5种滤镜风格（糖果色/二次元/复古/ins/素描）
- 🎮 **更多互动** - 情侣名生成、外号生成、真心话大冒险、每日抽签
- 🎨 **多种风格** - 浪漫古风、可爱卖萌、搞笑搞怪、直球表白、文艺小清新
- 🎬 **多种场景** - 初次见面、纪念日、表白、晚安

---

## 🚀 快速开始

### 安装

不需要安装！直接运行即可～

### 运行

```bash
# 查看帮助
python sweet_lab.py --help

# 生成藏头诗
python sweet_lab.py poem "小红"

# 指定风格
python sweet_lab.py poem "小明" --style cute

# 生成情话
python sweet_lab.py love

# 搞笑风格
python sweet_lab.py love --style funny

# 爱情测试
python sweet_lab.py test "小红" "小明"

# 土味情话
python sweet_lab.py chat --earthy

# 头像风格化
python sweet_lab.py avatar "头像.png" --style candy

# 情侣名生成
python sweet_lab.py interact couple_name --name1 "小红" --name2 "小明"

# 外号生成
python sweet_lab.py interact nickname --name "小红"

# 真心话大冒险
python sweet_lab.py interact truth_or_dare

# 每日抽签
python sweet_lab.py interact lucky_draw

# 列出所有风格
python sweet_lab.py styles
```

---

## 📖 详细说明

### 藏头诗生成器

**支持的风格**:
- `romantic` - 浪漫古风（默认）
- `cute` - 可爱卖萌
- `funny` - 搞笑搞怪
- `modern` - 现代文艺

**名字要求**: 2-4 个字

**示例**:
```bash
python sweet_lab.py poem "小红"
python sweet_lab.py poem "小明" --style cute
```

---

### 情话生成器

**支持的风格**:
- `romantic` - 温柔浪漫（默认）
- `funny` - 搞笑搞怪
- `cute` - 可爱卖萌
- `direct` - 直球表白
- `literary` - 文艺小清新

**支持的场景**:
- `first_meet` - 初次见面
- `anniversary` - 纪念日
- `confession` - 表白
- `goodnight` - 晚安

**示例**:
```bash
# 基础用法
python sweet_lab.py love

# 搞笑风格
python sweet_lab.py love --style funny

# 带上名字
python sweet_lab.py love --name "小红"

# 表白场景
python sweet_lab.py love --scene confession

# 组合使用
python sweet_lab.py love --style cute --name "小明" --scene first_meet
```

---

### 爱情/友情测试器

**注意**: 纯属娱乐！不要太当真哦～ 😂

**示例**:
```bash
# 爱情测试
python sweet_lab.py test "小红" "小明"

# 友情测试
python sweet_lab.py test "小红" "小丽" --type friendship

# 带生日（可选）
python sweet_lab.py test "小红" "小明" --birthday1 "2000-01-01" --birthday2 "2000-02-02"
```

---

### 头像风格化

**支持的风格**:
- `candy` - 🍬 糖果色（默认）
- `anime` - 🎮 二次元
- `vintage` - 📷 复古风
- `ins` - ✨ ins 风
- `sketch` - ✏️ 素描风

**注意**: 需要安装 OpenCV 哦！

**示例**:
```bash
# 糖果色风格
python sweet_lab.py avatar "头像.png" --style candy

# 二次元风格
python sweet_lab.py avatar "头像.png" --style anime

# 指定输出路径
python sweet_lab.py avatar "头像.png" --style candy --output "头像_candy.png"
```

---

### 更多互动功能

#### 情侣名生成
```bash
python sweet_lab.py interact couple_name --name1 "小红" --name2 "小明"
```

#### 外号生成
```bash
python sweet_lab.py interact nickname --name "小红"
```

#### 真心话大冒险
```bash
# 随机选择
python sweet_lab.py interact truth_or_dare

# 指定真心话
python sweet_lab.py interact truth_or_dare --choice truth

# 指定大冒险
python sweet_lab.py interact truth_or_dare --choice dare
```

#### 每日抽签
```bash
python sweet_lab.py interact lucky_draw
```

---

### 聊天话术助手

**支持的功能**:

1. **土味情话**
```bash
python sweet_lab.py chat --earthy
```

2. **高情商回复**
```bash
python sweet_lab.py chat --message "在干嘛" --style cute
```

3. **话题开场白**
```bash
python sweet_lab.py chat --scene first_chat
```

**支持的回复风格**:
- `flirty` - 撩人
- `cute` - 可爱
- `funny` - 搞笑
- `normal` - 正常

**支持的场景**:
- `first_chat` - 初次聊天
- `ambiguous` - 暧昧期
- `couple` - 情侣日常

---

## 📁 项目结构

```
sweet-lab/
├── sweet_lab.py         # 主程序
├── README.md            # 说明文档（就是这个）
└── core/                # 核心模块
    ├── __init__.py
    ├── poem_generator.py    # 藏头诗生成器
    ├── love_generator.py    # 情话生成器
    ├── love_tester.py       # 爱情/友情测试器
    └── chat_helper.py       # 聊天话术助手
```

---

## 🎯 使用场景

### 1. 想表白但不知道怎么说
```bash
python sweet_lab.py love --style romantic --scene confession
```

### 2. 想给 ta 写首藏头诗
```bash
python sweet_lab.py poem "小红" --style cute
```

### 3. 暧昧期想试探一下
```bash
python sweet_lab.py love --style funny
```

### 4. 不知道怎么回 ta 的消息
```bash
python sweet_lab.py chat --message "在干嘛" --style cute
```

### 5. 想知道和 ta 的契合度（纯属娱乐！）
```bash
python sweet_lab.py test "小红" "小明"
```

---

## 💡 提示

- 生成的文案仅供参考，可以自己再修改一下，更有诚意～
- 藏头诗可以多生成几次，选最喜欢的
- 搞笑风格很适合活跃气氛，但表白还是用浪漫/直球一点的好
- 带上名字会更有专属感哦～
- 爱情/友情测试器纯属娱乐！不要太当真！😂

---

## 📝 未来计划

- [ ] 头像生成器
- [ ] 图片生成（配文案）
- [ ] Web 界面
- [ ] 小程序版

---

## ❤️ 免责声明

本工具生成的文案/测试结果仅供参考，实际使用时请结合自己的真实情感，适当修改，更有诚意哦～

爱情/友情测试器纯属娱乐，请勿当真！

---

## 🍬 祝你好运！

希望甜蜜实验室能帮到你！加油！💖

---

**甜蜜制造机，搞怪也甜蜜！**
