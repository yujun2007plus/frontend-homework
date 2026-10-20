# 前端作业1：页面布局

根据设计图完成的页面布局作业。

## 文件说明

- `作业提交-单文件.html`：**单文件版**，字体（子集化）与图片全部以 base64 内嵌，交这一个文件即可完整显示
- `build_single.py`：单文件版的生成脚本（fonttools 字体子集化 + base64 内嵌）
- `index.html`：作业页面源文件（多文件版，引用素材字体与图片）
- `font-awesome.min.css` / `fonts/`：作业附件素材中的 Font Awesome 图标字体与书法字体（书法.ttf）
- `images/`：作业附件素材中的 HTML5 / CSS3 图标图片
- `preview.png`：页面渲染效果截图

## 实现要点

- 标题「万物互联、极致体验」使用素材中的书法字体（`@font-face` 引入 `fonts/书法.ttf`）
- HTML5 / CSS3 盾牌图标使用素材中的图片实现
- 「平台支持」四个图标（苹果、微信、显示器、笔记本）使用素材中的 Font Awesome iconfont 实现
- 布局使用 flex 实现两栏介绍与四栏平台支持，介绍文字两端对齐、末行居中

## 使用方法

直接用浏览器打开 `index.html` 即可。
