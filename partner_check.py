#!/usr/bin/env python3
"""
SAGA Oracle · 伴侣需求匹配引擎 (通用版)
用法: python3 partner_check.py YYYY MM DD HH [male/female]
需求模板可自定义。修改 REQUIREMENTS 列表即可适配不同用户的需求模型。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ziwei_engine import cast, ZHI, PN

REQUIREMENTS = [
    {"id":1,"name":"有谋略","desc":"命宫有天机 或 福德有天机/天府/天梁",
     "check":lambda c:any(s in c['palaces']['命宫']['stars'] for s in['天机']) or any(s in c['palaces']['福德']['stars'] for s in['天机','天府','天梁'])},
    {"id":2,"name":"专一","desc":"夫妻宫有太阴 且 天刑",
     "check":lambda c:'太阴' in c['palaces']['夫妻']['stars'] and '天刑' in c['palaces']['夫妻']['stars']},
    {"id":3,"name":"以我为中心","desc":"夫妻宫有天魁",
     "check":lambda c:'天魁' in c['palaces']['夫妻']['stars']},
    {"id":4,"name":"关键时刻不拉胯","desc":"疾厄宫有破军 且 破军化权",
     "check":lambda c:'破军' in c['palaces']['疾厄']['stars'] and c['sihua'].get('权')=='破军'},
    {"id":5,"name":"不说但做","desc":"命宫有巨门 或 天机",
     "check":lambda c:'巨门' in c['palaces']['命宫']['stars'] or '天机' in c['palaces']['命宫']['stars']},
    {"id":6,"name":"深情","desc":"夫妻宫有太阴 且 福德宫有天姚",
     "check":lambda c:'太阴' in c['palaces']['夫妻']['stars'] and '天姚' in c['palaces']['福德']['stars']},
    {"id":7,"name":"财务稳定","desc":"夫妻宫有禄存 或 财帛宫有禄存/天府",
     "check":lambda c:'禄存' in c['palaces']['夫妻']['stars'] or '禄存' in c['palaces']['财帛']['stars'] or '天府' in c['palaces']['财帛']['stars']},
    {"id":8,"name":"审美在线","desc":"命宫有天同 或 夫妻宫有天同",
     "check":lambda c:'天同' in c['palaces']['命宫']['stars'] or '天同' in c['palaces']['夫妻']['stars']},
    {"id":9,"name":"持续宠爱","desc":"夫妻宫有天同 或 太阴",
     "check":lambda c:'天同' in c['palaces']['夫妻']['stars'] or '太阴' in c['palaces']['夫妻']['stars']},
]

def check_partner(y,mo,d,h,is_male=True):
    chart=cast(y,mo,d,h,"候选",is_male)
    print(f"\n{'='*60}\n伴侣需求匹配 · {y}-{mo:02d}-{d:02d} {h:02d}:00\n{'='*60}")
    print(f"格局:{chart['geju']}")
    for pn in['命宫','夫妻','疾厄','福德','财帛']:
        p=chart['palaces'][pn];print(f"{pn}({ZHI[p['pos']]}): {' '.join(sorted(p['stars']))}")
    print(f"身宫:{ZHI[chart['shen_pos']]} 四化:{chart['sihua']}\n{'='*60}")
    score=0
    for req in REQUIREMENTS:
        m=req["check"](chart);print(f"  {'✓' if m else '✗'} [{req['id']}] {req['name']}")
        if m:score+=1
        else:print(f"      缺: {req['desc']}")
    print(f"\n  得分: {score}/{len(REQUIREMENTS)}")
    print(f"  评级: {'高匹配' if score>=7 else '中等' if score>=5 else '低匹配' if score>=3 else '不匹配'}")
    return score

if __name__=="__main__":
    if len(sys.argv)<5:print("用法: python3 partner_check.py YYYY MM DD HH [male/female]");sys.exit(1)
    y,mo,d,h=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
    is_male=len(sys.argv)>5 and sys.argv[5].lower().startswith('m')
    check_partner(y,mo,d,h,is_male)
