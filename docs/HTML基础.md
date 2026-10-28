# HTML 基础笔记

## 语义化标签

- `<header>` / `<footer>` / `<main>` / `<nav>` / `<article>` / `<section>` / `<aside>`
- 语义化有利于 SEO 和可访问性（屏幕阅读器）

## 常用表单元素

| 标签 | 用途 |
| --- | --- |
| `<input type="text">` | 单行文本 |
| `<textarea>` | 多行文本 |
| `<select>` | 下拉选择 |
| `<button>` | 按钮 |

## 图片优化

- 使用 `loading="lazy"` 懒加载
- 通过 `srcset` 提供不同分辨率
- 字体子集化 + base64 内嵌可减少请求数
