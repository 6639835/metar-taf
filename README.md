# METAR Data Collector

自动收集和存储航空气象报告（METAR）数据的GitHub项目。

## 功能特性

- 🕐 **自动化采集**: 使用GitHub Actions每分钟自动下载最新的METAR数据
- 📦 **数据处理**: 自动下载、解压gzip文件，提取XML数据
- 📁 **结构化存储**: 按时间戳创建目录结构，便于数据管理和查询
- 🔄 **版本控制**: 所有数据变更自动提交到Git仓库，保持完整的历史记录

## 数据来源

数据来源于美国国家气象局航空气象中心：
- **URL**: https://aviationweather.gov/data/cache/metars.cache.xml.gz
- **更新频率**: 每分钟更新一次
- **数据格式**: XML格式的METAR报告

## 目录结构

```
metar-taf/
├── .github/
│   └── workflows/
│       └── download-metar.yml    # GitHub Actions工作流
├── scripts/
│   └── download_metar.py         # 数据下载脚本
├── data/                         # 数据存储目录
│   └── YYYY/                     # 年份
│       └── MM/                   # 月份
│           └── DD/               # 日期
│               └── HH-MM/        # 小时-分钟
│                   ├── metars_YYYYMMDD_HHMM UTC.xml
│                   └── download_info.txt
└── README.md
```

### 数据文件命名规则

- **XML文件**: `metars_YYYYMMDD_HHMM UTC.xml`
- **元数据文件**: `download_info.txt` (包含下载时间、来源URL、文件大小等信息)

## 如何使用

### 1. Fork或Clone此仓库

```bash
git clone https://github.com/yourusername/metar-taf.git
cd metar-taf
```

### 2. 启用GitHub Actions

1. 在GitHub仓库页面，点击 "Actions" 标签页
2. 如果看到禁用提示，点击 "Enable GitHub Actions"
3. GitHub Actions将根据配置的cron计划自动运行

### 3. 手动触发下载（可选）

如果需要立即测试或手动下载数据：

1. 进入仓库的 "Actions" 页面
2. 选择 "Download METAR Data" workflow
3. 点击 "Run workflow" 按钮

### 4. 本地运行脚本（可选）

```bash
# 安装依赖
pip install requests

# 运行下载脚本
python scripts/download_metar.py
```

## 配置说明

### GitHub Actions工作流 (.github/workflows/download-metar.yml)

- **触发时机**: 每分钟的第0秒执行 (`cron: '0 * * * *'`)
- **运行环境**: Ubuntu最新版本
- **权限**: 需要写入仓库内容的权限

### Python脚本 (scripts/download_metar.py)

- **依赖**: requests库
- **功能**: 下载、解压、验证XML、创建目录结构、保存文件
- **错误处理**: 包含下载失败、解压错误、文件保存等异常处理

## 数据格式

METAR数据包含全球各机场的气象观测报告，包括：
- 风速风向
- 能见度
- 天气现象
- 云层信息
- 温度和露点
- 气压信息

## 注意事项

1. **GitHub Actions限制**: 免费账户每月有2000分钟的Actions运行时间限制
2. **存储空间**: 大量的历史数据会占用仓库存储空间
3. **网络依赖**: 脚本依赖外部数据源的可用性
4. **时区**: 所有时间戳都使用UTC时间

## 贡献

欢迎提交Issues和Pull Requests来改进这个项目！

## 许可证

本项目采用MIT许可证，详见LICENSE文件。

## 相关链接

- [FAA Aviation Weather Center](https://aviationweather.gov/)
- [METAR格式说明](https://en.wikipedia.org/wiki/METAR)
- [GitHub Actions文档](https://docs.github.com/en/actions)
