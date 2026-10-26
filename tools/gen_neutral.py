#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成中立版设备兼容性索引
- 只保留公开设备信息：厂商 / 机型 / 内核版本 / 芯片 / KMI / 文件大小
- 移除执行命令、校验值等可被解读为操作指引的字段
- 输出纯数据 JSON，不含任何可执行内容
"""
import json
import os
import datetime

BASE = '/storage/emulated/0/小西/AI项目/RootToolbox'
SRC = BASE + '/assets/payloads.json'
OUT_DIR = BASE + '/github_archive'
OUT = OUT_DIR + '/kernel_compat.json'

os.makedirs(OUT_DIR, exist_ok=True)

d = json.load(open(SRC, encoding='utf-8'))
entries = d.get('entries', [])

out_entries = []
for e in entries:
    rec = {
        'vendor': e.get('vendor', ''),
        'device': e.get('name', ''),
        'models': e.get('models', []),
        'kernel': e.get('kernel', ''),
        'kernel_family': e.get('kernelFamily', ''),
        'soc_names': e.get('socs', []),
        'kmi': e.get('kmi', ''),
        'codename': e.get('codename', ''),
        'build': e.get('build', ''),
        'file_size': e.get('size', 0),
    }
    out_entries.append(rec)

out = {
    'schema': 2,
    'title': 'Android Kernel Compatibility Index',
    'description': '公开可查的 Android 设备与内核版本兼容性对照数据，仅含设备元信息，不含任何可执行内容。',
    'license': 'CC-BY-4.0',
    'generated': datetime.datetime.now().strftime('%Y-%m-%d'),
    'total': len(out_entries),
    'fields': {
        'vendor': '设备厂商',
        'device': '设备商品名',
        'models': '可用于匹配的型号字符串（小写）',
        'kernel': 'Linux 内核三段版本号',
        'kernel_family': '内核主次版本',
        'soc_names': 'SoC 商品名或代号',
        'kmi': '内核模块接口版本',
        'codename': '设备代号',
        'build': '系统构建号',
        'file_size': '对应内核模块文件字节数',
    },
    'entries': out_entries,
}

json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('输出: %s' % OUT)
print('条目: %d' % len(out_entries))
print('大小: %.1f KB' % (os.path.getsize(OUT) / 1024.0))

# 统计
from collections import Counter
v = Counter(e['vendor'] for e in out_entries if e['vendor'])
k = Counter(1 for e in out_entries if e['kernel'])
s = Counter(1 for e in out_entries if e['soc_names'])
m = Counter(1 for e in out_entries if e['models'])
n = len(out_entries)
print('')
print('厂商分布:')
for name, c in v.most_common():
    print('  %-12s %d' % (name, c))
print('')
print('字段覆盖: 内客 %d%%  芯片 %d%%  型号 %d%%' % (
    sum(k.values()) * 100 // n, sum(s.values()) * 100 // n, sum(m.values()) * 100 // n))