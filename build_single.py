# -*- coding: utf-8 -*-
"""生成单文件版作业页面：字体子集化后与图片一起以 base64 内嵌到一个 HTML 中"""
import base64
import io
from fontTools import subset

BASE = r"D:\D盘\前端作业\前端作业1\html5-page"


def subset_font(path, text=None, unicodes=None):
    opts = subset.Options()
    opts.flavor = "woff2"
    # iconfont 需要保留 PUA 码位
    opts.ignore_missing_unicodes = True
    font = subset.load_font(path, opts)
    ss = subset.Subsetter(opts)
    if text:
        ss.populate(text=text)
    if unicodes:
        ss.populate(unicodes=unicodes)
    ss.subset(font)
    buf = io.BytesIO()
    font.save(buf)
    return base64.b64encode(buf.getvalue()).decode()


def b64file(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# 1. 书法字体：只保留标题用到的字符
shufa_b64 = subset_font(BASE + r"\fonts\书法.ttf", text="万物互联、极致体验")

# 2. Font Awesome：只保留 apple/weixin/desktop/laptop 四个图标
fa_b64 = subset_font(
    BASE + r"\fonts\fontawesome-webfont.ttf",
    unicodes=[0xF179, 0xF1D7, 0xF108, 0xF109],
)

# 3. 图片
img1_b64 = b64file(BASE + r"\images\1.png")
img2_b64 = b64file(BASE + r"\images\2.png")

INTRO_TEXT = (
    "【HTML5】HTML5不仅仅是HTML规范的当前最新版本，HTML5进化的重大意义还在于"
    "HTML5从技术层面带来了八个类别的革新。HTML5规范以“用户至上”为宗旨。"
    "也就是说在遇到冲突时，规范的优先级为：用户&gt;页面作者&gt;实现者（浏览器）"
    "&gt;规范开发者（W3C/WHATWG）&gt;纯理论。除此之外，HTML5还引入了一种新的"
    "安全模型来保证HTML5足够安全。"
)

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>万物互联、极致体验</title>
  <style>
    /* 素材中的书法字体（已子集化并内嵌），用于页面标题 */
    @font-face {{
      font-family: "shufa";
      src: url(data:font/woff2;base64,{shufa_b64}) format("woff2");
    }}

    /* 素材中的 Font Awesome 图标字体（已子集化并内嵌） */
    @font-face {{
      font-family: "FontAwesome";
      src: url(data:font/woff2;base64,{fa_b64}) format("woff2");
    }}

    .fa {{
      display: inline-block;
      font: normal normal normal 14px/1 FontAwesome;
      -webkit-font-smoothing: antialiased;
    }}

    .fa-apple:before {{ content: "\\f179"; }}
    .fa-weixin:before {{ content: "\\f1d7"; }}
    .fa-desktop:before {{ content: "\\f108"; }}
    .fa-laptop:before {{ content: "\\f109"; }}

    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    body {{
      background: #fff;
      color: #000;
      font-family: "Microsoft YaHei", "微软雅黑", sans-serif;
    }}

    .container {{
      width: 730px;
      margin: 0 auto;
      padding: 20px 0 60px;
    }}

    /* 标题：毛笔书法字体 */
    .main-title {{
      text-align: center;
      font-family: "shufa", "STXingkai", "华文行楷", "楷体", serif;
      font-size: 48px;
      font-weight: normal;
      margin: 20px 0 40px;
    }}

    /* 两栏介绍区 */
    .intro {{
      display: flex;
      justify-content: space-between;
    }}

    .intro-item {{
      width: 47%;
      text-align: center;
    }}

    .intro-item .icon {{
      height: 64px;
      margin-bottom: 24px;
    }}

    .intro-item p {{
      font-size: 14px;
      line-height: 2.2;
      text-align: justify;
      text-align-last: center;
    }}

    /* 平台支持区 */
    .platform {{
      margin-top: 60px;
    }}

    .platform h2 {{
      text-align: center;
      font-size: 26px;
      margin-bottom: 40px;
    }}

    .platform-list {{
      display: flex;
      justify-content: space-between;
      text-align: center;
    }}

    .platform-item {{
      flex: 1;
    }}

    .platform-item .fa {{
      font-size: 42px;
      margin-bottom: 24px;
    }}

    .platform-item .name {{
      font-size: 14px;
      font-weight: bold;
    }}
  </style>
</head>
<body>
  <div class="container">
    <!-- 页面标题 -->
    <h1 class="main-title">万物互联、极致体验</h1>

    <!-- HTML5 / CSS3 介绍 -->
    <div class="intro">
      <div class="intro-item">
        <img class="icon" src="data:image/png;base64,{img1_b64}" alt="HTML5">
        <p>{INTRO_TEXT}</p>
      </div>
      <div class="intro-item">
        <img class="icon" src="data:image/png;base64,{img2_b64}" alt="CSS3">
        <p>{INTRO_TEXT}</p>
      </div>
    </div>

    <!-- 平台支持 -->
    <div class="platform">
      <h2>平台支持</h2>
      <div class="platform-list">
        <div class="platform-item">
          <i class="fa fa-apple"></i>
          <div class="name">原生移动APP开发</div>
        </div>
        <div class="platform-item">
          <i class="fa fa-weixin"></i>
          <div class="name">微信公共平台开发</div>
        </div>
        <div class="platform-item">
          <i class="fa fa-desktop"></i>
          <div class="name">网站开发</div>
        </div>
        <div class="platform-item">
          <i class="fa fa-laptop"></i>
          <div class="name">桌面应用开发</div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""

out = BASE + r"\作业提交-单文件.html"
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
import os
print("OK", out, os.path.getsize(out), "bytes")
