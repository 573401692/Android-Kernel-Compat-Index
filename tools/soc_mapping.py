#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vivo / iQOO / 小米 芯片映射表
vivo 数据全部来自 vivo 官网参数页 (vivo.com.cn/vivo/param/*) 与产品页；
小米部分来自载荷文件名内嵌的 SoC 代号 + 机型公开规格。
"""

# 机型关键词（小写） -> (芯片名, 部件号, SoC厂商, 来源等级)
VIVO_SOC = {
    # ---- vivo X 系列 ----
    'vivo x200 pro mini': ('天玑 9400', 'MT6993', 'mediatek', 'official'),
    'vivo x200s':         ('天玑 9400+', 'MT6993+', 'mediatek', 'official'),
    'vivo x200 pro':      ('天玑 9400', 'MT6993', 'mediatek', 'official'),
    'vivo x200':          ('天玑 9400', 'MT6993', 'mediatek', 'official'),
    # ---- iQOO ----
    'iqoo neo10 pro+':    ('骁龙 8 至尊版', 'SM8750', 'qualcomm', 'official'),
    'iqoo neo10 pro':     ('天玑 9400', 'MT6993', 'mediatek', 'official'),
    'iqoo neo11':         ('骁龙 8 至尊版', 'SM8750', 'qualcomm', 'official'),
    'iqoo neo8':          ('天玑 9200', 'MT6985', 'mediatek', 'official'),
    'iqoo 13':            ('骁龙 8 至尊版', 'SM8750', 'qualcomm', 'official'),
    'iqoo 11':            ('骁龙 8 Gen2', 'SM8550', 'qualcomm', 'infer'),
    'iqoo z10 turbo+':    ('天玑 9400+', 'MT6993+', 'mediatek', 'official'),
    'iqoo z10 turbo':     ('天玑 8400', 'MT6991', 'mediatek', 'official'),
    'iqoo 12':            ('骁龙 8 Gen3', 'SM8650', 'qualcomm', 'infer'),
    # ---- vivo Pad ----
    'vivo pad5 pro':      ('天玑 9400', 'MT6993', 'mediatek', 'official'),
}

XIAOMI_SOC = {
    'sm8750':   ('骁龙 8 Elite', 'SM8750', 'qualcomm', 'embedded'),
    'sm8650':   ('骁龙 8 Gen3', 'SM8650', 'qualcomm', 'embedded'),
    'sm8550':   ('骁龙 8 Gen2', 'SM8550', 'qualcomm', 'embedded'),
    '8g2':      ('骁龙 8 Gen2', 'SM8550', 'qualcomm', 'embedded'),
    'mt6991':   ('天玑 8400', 'MT6991', 'mediatek', 'embedded'),
    'mt6895':   ('天玑 8000/8100/8200', 'MT6895', 'mediatek', 'embedded'),
    'k70 ultra': ('天玑 9300+', 'MT6989', 'mediatek', 'infer'),
    'k40':      ('骁龙 870', 'SM8250', 'qualcomm', 'infer'),
    'alioth':   ('骁龙 870', 'SM8250', 'qualcomm', 'infer'),
    '8e5':      ('骁龙 8 Elite Gen5', 'SM8850', 'qualcomm', 'infer'),
    'jinghu':   ('骁龙 8 Gen3', 'SM8650', 'qualcomm', 'infer'),
    'dizi':     ('骁龙 8 Gen3', 'SM8650', 'qualcomm', 'infer'),
}

SOURCES = {
    'official': '官网参数页实测',
    'embedded': '载荷文件名内嵌代号',
    'infer':    '机型公开规格推断',
}


def match_vivo(text):
    t = text.lower()
    for k in sorted(VIVO_SOC.keys(), key=len, reverse=True):
        if k in t:
            v = VIVO_SOC[k]
            return {'soc': v[0], 'part': v[1], 'socVendor': v[2], 'src': v[3]}
    return None


def match_xiaomi(text):
    t = text.lower()
    for k in sorted(XIAOMI_SOC.keys(), key=len, reverse=True):
        if k in t:
            v = XIAOMI_SOC[k]
            return {'soc': v[0], 'part': v[1], 'socVendor': v[2], 'src': v[3]}
    return None