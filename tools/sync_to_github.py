#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Android-Kernel-Compat-Index 同步脚本
只推送纯数据与文档，不推送任何二进制或可执行内容
"""
import base64
import json
import os
import sys
import time
import urllib.request
import urllib.error

TOK = os.environ.get('GH_TOK', '')
OWNER = '573401692'
REPO = 'Android-Kernel-Compat-Index'
BRANCH = 'main'
BASE = '/storage/emulated/0/小西/AI项目/RootToolbox'
ARC = BASE + '/github_archive'
API = 'https://api.github.com'


def req(method, url, data=None):
    body = None
    headers = {
        'Authorization': 'Bearer ' + TOK,
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'compat-index-sync',
    }
    if data is not None:
        body = json.dumps(data).encode()
        headers['Content-Type'] = 'application/json'
    r = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            return resp.status, json.loads(resp.read().decode() or '{}')
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode() or '{}')
        except Exception:
            return e.code, {'message': 'http error'}
    except Exception as e:
        return -1, {'message': str(e)}


def get_sha(path):
    s, d = req('GET', '%s/repos/%s/%s/contents/%s?ref=%s' % (API, OWNER, REPO, path, BRANCH))
    if s == 200 and isinstance(d, dict):
        return d.get('sha')
    return None


def put_file(local_path, remote_path, msg):
    if not os.path.exists(local_path):
        print('  SKIP 不存在: %s' % remote_path)
        return False
    raw = open(local_path, 'rb').read()
    data = {
        'message': msg,
        'content': base64.b64encode(raw).decode(),
        'branch': BRANCH,
    }
    sha = get_sha(remote_path)
    if sha:
        data['sha'] = sha
    s, d = req('PUT', '%s/repos/%s/%s/contents/%s' % (API, OWNER, REPO, remote_path), data)
    if s in (200, 201):
        act = '更新' if sha else '新增'
        print('  ✓ %s  %-38s %7d B' % (act, remote_path, len(raw)))
        return True
    print('  ✗ 失败 %-38s HTTP %s  %s' % (remote_path, s, d.get('message')))
    return False


def main():
    if not TOK:
        print('缺少 GH_TOK')
        return 1

    print('=' * 66)
    print('目标: https://github.com/%s/%s' % (OWNER, REPO))
    print('=' * 66)

    jobs = [
        (ARC + '/README.md', 'README.md', 'docs: 数据说明'),
        (ARC + '/LICENSE', 'LICENSE', 'docs: 添加 CC BY 4.0 许可'),
        (ARC + '/kernel_compat.json', 'kernel_compat.json', 'data: 设备内核兼容性索引'),
        (ARC + '/upstream.json', 'upstream.json', 'data: 数据来源清单'),
        (BASE + '/gen_neutral.py', 'tools/gen_neutral.py', 'tools: 索引生成脚本'),
        (BASE + '/sync_to_github.py', 'tools/sync_to_github.py', 'tools: 同步脚本'),
        (BASE + '/soc_mapping.py', 'tools/soc_mapping.py', 'tools: SoC 名称映射表'),
    ]

    ok = fail = 0
    for local, remote, msg in jobs:
        if put_file(local, remote, msg):
            ok += 1
        else:
            fail += 1
        time.sleep(0.35)

    print('')
    print('完成: 成功 %d  失败 %d' % (ok, fail))
    return 0 if fail == 0 else 2


if __name__ == '__main__':
    sys.exit(main())