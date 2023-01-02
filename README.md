# 每日早报 自用版 | [点击前往原仓库](https://github.com/flow2000/news)

![news-service](https://socialify.git.ci/YandaoLab/news-service/image?font=Bitter&language=1&name=1&owner=1&pattern=Circuit%20Board&theme=Auto)

### 简介

60秒读懂世界

### 效果

立即访问：[news.ydlk.cc (v2)](https://news.yudlk.cc/)

#### Vercel 一键部署（**推荐**）

#### v1 - 原仓库版本

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/flow2000/news/tree/v1)

#### v2 - 此仓库版本

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FYandaoLab%2Fnews-service&project-name=news-service&repository-name=news-service&demo-title=Yandao%20Daily&demo-description=Daily%20Report%20Project&demo-url=https%3A%2F%2Fnews.ydlk.cc%2F&demo-image=https%3A%2F%2Fsocialify.git.ci%2FYandaoLab%2Fnews-service%2Fimage%3Ffont%3DBitter%26language%3D1%26name%3D1%26owner%3D1%26pattern%3DCircuit%2520Board%26theme%3DAuto)

### Docker 一键部署

#### v1

```markdown
docker run -itd --name=news --restart=always -p 9134:8888 flow2000/news:1.0.0
```

#### v2

```markdown
docker run -itd --name=news --restart=always -p 9134:8888 flow2000/news:2.0.0
```

### API

GET：`https://news.ydlk.cc/60s`，返回今日新闻json数据

##### 请求参数

| 参数名           | 位置  | 类型   | 必填 | 示例值 |说明  |
| :--------------- | :---- | :----- | :--: | :--------------------- | :--------------------- |
| `offset` | `query` | `int` |  否  | `0` |说明：`0` 为今天，`1` 为昨天，依次类推                            |

GET：`https://news.ydlk.cc/weibo`，返回微博热搜json数据

##### 请求参数：无

GET：`https://news.ydlk.cc/bili`，返回B站热搜json数据

##### 请求参数：无

GET：`https://news.ydlk.cc/bing`，返回必应热搜json数据

##### 请求参数：无

更多详情请点击：[每日早报API](https://news.panghai.top/docs)

