# Android Kernel Compatibility Index

Android 设备与 Linux 内核版本兼容性索引。

本仓库收集整理**公开可查**的 Android 设备信息，包括厂商、机型代号、内核版本、SoC 型号与 KMI 版本，用于设备识别与兼容性对照。

**本仓库不含任何可执行文件、二进制模块或操作指引。**

---

## 数据用途

- 设备信息对照查询（这个机型用的是哪个内核版本）
- 内核版本与 SoC 组合的兼容性参考
- 设备型号与内部代号的映射查询

适用于应用开发者的设备适配、系统信息工具的数据补充、以及 Android 设备档案整理。

---

## 文件结构

```
kernel_compat.json     主数据文件（schema 2）
snapshot/              历史快照
tools/                 生成脚本
upstream.json          数据来源清单
```

---

## 数据格式

```json
{
  "schema": 2,
  "title": "Android Kernel Compatibility Index",
  "license": "CC-BY-4.0",
  "total": 122,
  "entries": [
    {
      "vendor": "vivo",
      "device": "iQOO 13",
      "models": ["iqoo 13"],
      "kernel": "6.6.30",
      "kernel_family": "6.6",
      "soc_names": ["天玑9400"],
      "kmi": "",
      "codename": "",
      "build": "",
      "file_size": 176544
    }
  ]
}
```

### 字段说明

| 字段 | 含义 |
|---|---|
| `vendor` | 设备厂商 |
| `device` | 设备商品名 |
| `models` | 可用于匹配的型号字符串（小写） |
| `kernel` | Linux 内核三段版本号（如 `6.6.118`） |
| `kernel_family` | 内核主次版本（如 `6.6`） |
| `soc_names` | SoC 商品名或内部代号 |
| `kmi` | 内核模块接口版本 |
| `codename` | 设备代号 |
| `build` | 系统构建号 |
| `file_size` | 对应内核模块的字节数，用于校验数据一致性 |

---

## 当前覆盖

| 项 | 数量 / 比例 |
|---|---|
| 设备条目 | 122 |
| 厂商 | 7 |
| 内核版本覆盖率 | 71% |
| 机型型号覆盖率 | 88% |
| SoC 覆盖率 | 53% |

### 厂商分布

| 厂商 | 条目 |
|---|---|
| vivo / iQOO | 36 |
| Samsung | 34 |
| Google Pixel | 29 |
| Xiaomi / Redmi | 13 |
| OPPO | 5 |
| realme | 1 |
| 其他 | 4 |

---

## 数据来源

所有数据来自以下公开来源，均为社区维护的开放数据：

- [hmascs/KSuRoot](https://github.com/hmascs/KSuRoot) — 基础设备目录
- [alex193a/Root-My-Pixel](https://github.com/alex193a/Root-My-Pixel) — Pixel 机型档案（kernelRelease + KMI）
- [newazbenalam/Root-My-Galaxy-Payloads](https://github.com/newazbenalam/Root-My-Galaxy-Payloads) — 三星机型档案
- 各厂商官网公开参数页 — 用于核对 SoC 型号与机型对应关系

数据整理遵循「**只做元信息汇总，不转载二进制内容**」的原则。

---

## 版本号匹配规则

内核版本按三段数字比对，后缀不参与匹配：

```
6.6.118-android16-5-gb2a8769   →   取 6.6.118 参与比对
```

这是 Linux 内核版本标识的通用做法，与上游项目保持一致。

---

## 数据更新

数据由脚本自动生成并定期同步：

```bash
python3 gen_neutral.py          # 生成索引
python3 sync_to_github.py       # 同步到本仓库
```

---

## 许可

本仓库数据采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 协议发布。

可自由复制、分发、修改，需保留出处署名。

---

## 声明

- 本仓库仅为**设备信息记录**，不提供任何软件、工具、模块或技术方案
- 所有数据均来自公开渠道，不含任何非公开信息
- 数据准确性以设备厂商官方公布信息为准，如有出入请提交 Issue 指正
- 本仓库与任何设备厂商无隶属关系
