# SAGA Oracle · 占卜引擎 (通用版)

四套命理算法引擎，只输出结构数据，不输出叙事解读。

## 文件
- divination_engine.py — 梅花易数 / 塔罗(78张) / 能量日报 / 自检
- ziwei_engine.py — 紫微斗数排盘(53颗星)
- hepan.py — 合盘引擎
- partner_check.py — 伴侣需求匹配(模板可自定义)

## 用法
python3 divination_engine.py meihua N1 N2 N3
python3 divination_engine.py tarot [张数] [N1 N2 N3]
python3 divination_engine.py verify
python3 ziwei_engine.py YYYY MM DD HH [name] [male/female]
python3 hepan.py Y1 M1 D1 H1 [M1] Y2 M2 D2 H2 [M2]
python3 partner_check.py YYYY MM DD HH [male/female]

## 依赖
pip install lunarcalendar

## 版本
v2 (2026-08-27): 变卦修复 / 互卦新增 / 塔罗78张 / 紫微53颗星 / 3个bug修复
