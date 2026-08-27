#!/usr/bin/env python3
import os
"""
SAGA Oracle · 合盘引擎
用法: python3 hepan.py J_Y J_MO J_D J_H J_MALE J_Y2 J_MO2 J_D2 J_H2 J_MALE2
两组生辰: 人A(年月日时性别) 人B(年月日时性别)
性别: male/female
"""
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ziwei_engine import cast, ZHI, PN

# 六合: 子丑 寅亥 卯戌 辰酉 巳申 午未
LIUHE = {0:1, 1:0, 2:11, 11:2, 3:10, 10:3, 4:9, 9:4, 5:8, 8:5, 6:7, 7:6}
# 六冲: 子午 丑未 寅申 卯酉 辰戌 巳亥
LIUCHONG = {0:6, 6:0, 1:7, 7:1, 2:8, 8:2, 3:9, 9:3, 4:10, 10:4, 5:11, 11:5}
# 三合: 申子辰 寅午戌 巳酉丑 亥卯未
SANHE = [(8,0,4),(2,6,10),(5,9,1),(11,3,7)]
# 天干合: 甲己 乙庚 丙辛 丁壬 戊癸
GANHE = {0:5,5:0,1:6,6:1,2:7,7:2,3:8,8:3,4:9,9:4}

def check_sanhe(a,b):
    for group in SANHE:
        if a in group and b in group: return True
    return False

def hepan(y1,mo1,d1,h1,male1,y2,mo2,d2,h2,male2):
    c1=cast(y1,mo1,d1,h1,"人A",male1)
    c2=cast(y2,mo2,d2,h2,"人B",male2)
    
    print(f"\n{'='*70}")
    print(f"合盘分析: {c1['name']} x {c2['name']}")
    print(f"{'='*70}")
    
    # 年干支关系
    g1=(c1['ly']-4)%10; g2=(c2['ly']-4)%10
    z1=(c1['ly']-4)%12; z2=(c2['ly']-4)%12
    
    print(f"\n【年柱关系】")
    print(f"  人A: {c1['yg']}{c1['yz']} | 人B: {c2['yg']}{c2['yz']}")
    
    gan_he = GANHE.get(g1)==g2
    zhi_he = LIUHE.get(z1)==z2
    zhi_chong = LIUCHONG.get(z1)==z2
    zhi_sanhe = check_sanhe(z1,z2)
    
    if gan_he: print(f"  天干合: ✓ ({c1['yg']}+{c2['yg']}合)")
    else: print(f"  天干合: ✗")
    if zhi_he: print(f"  地支六合: ✓ ({c1['yz']}+{c2['yz']}合)")
    else: print(f"  地支六合: ✗")
    if zhi_sanhe: print(f"  地支三合: ✓ ({c1['yz']}+{c2['yz']}三合)")
    if zhi_chong: print(f"  地支六冲: ⚠ ({c1['yz']}+{c2['yz']}冲)")
    
    he_count = sum([gan_he, zhi_he, zhi_sanhe])
    chong_count = 1 if zhi_chong else 0
    print(f"  合计: {he_count}合 {chong_count}冲")
    
    # 命宫关系
    m1=c1['ming_pos']; m2=c2['ming_pos']
    print(f"\n【命宫对位】")
    print(f"  人A命宫({ZHI[m1]}): {' '.join(sorted(c1['palaces']['命宫']['stars']))}")
    print(f"  人B命宫({ZHI[m2]}): {' '.join(sorted(c2['palaces']['命宫']['stars']))}")
    diff=(m2-m1)%12
    if diff==0: rel="同位(同频共振)"
    elif diff==1 or diff==11: rel="邻位(肩并肩)"
    elif diff==6: rel="对冲(面对面)"
    elif check_sanhe(m1,m2): rel="三合(鼎足)"
    elif LIUHE.get(m1)==m2: rel="六合(暗合)"
    else: rel=f"间隔{diff}位"
    print(f"  关系: {rel}")
    
    # 夫妻宫对位
    print(f"\n【夫妻宫对位】")
    sp1=c1['palaces']['夫妻']; sp2=c2['palaces']['夫妻']
    print(f"  人A夫妻({ZHI[sp1['pos']]}): {' '.join(sorted(sp1['stars']))}")
    print(f"  人B夫妻({ZHI[sp2['pos']]}): {' '.join(sorted(sp2['stars']))}")
    huaji1 = c1['sihua'].get('忌') in sp1['stars']
    huaji2 = c2['sihua'].get('忌') in sp2['stars']
    if huaji1: print(f"  ⚠ 人A夫妻宫坐化忌({c1['sihua']['忌']}化忌) = 情劫/接收端报错")
    if huaji2: print(f"  ⚠ 人B夫妻宫坐化忌({c2['sihua']['忌']}化忌) = 情劫/接收端报错")
    if not huaji1 and not huaji2: print(f"  双方夫妻宫均无化忌 = 无结构性情劫")
    
    # 身宫对位
    print(f"\n【身宫对位】")
    s1=c1['shen_pos']; s2=c2['shen_pos']
    for pn in PN:
        if c1['palaces'][pn]['pos']==s1:
            p1_name=pn; p1_stars=' '.join(sorted(c1['palaces'][pn]['stars']))
        if c2['palaces'][pn]['pos']==s2:
            p2_name=pn; p2_stars=' '.join(sorted(c2['palaces'][pn]['stars']))
    print(f"  人A身宫: {p1_name}({ZHI[s1]}) {p1_stars}")
    print(f"  人B身宫: {p2_name}({ZHI[s2]}) {p2_stars}")
    
    # 格局对比
    print(f"\n【格局对比】")
    print(f"  人A: {c1['geju']} 紫微+{'+'.join(c1['zw_cowork']) if c1['zw_cowork'] else '独坐'}")
    print(f"  人B: {c2['geju']} 紫微+{'+'.join(c2['zw_cowork']) if c2['zw_cowork'] else '独坐'}")
    if '杀破狼' in c1['geju'] and '杀破狼' in c2['geju']:
        print(f"  → 双杀破狼(双破) 拆了谁建?")
    elif '杀破狼' in c1['geju'] and '杀破狼' not in c2['geju']:
        print(f"  → 一破一守 A破B守")
    elif '杀破狼' not in c1['geju'] and '杀破狼' in c2['geju']:
        print(f"  → 一守一破 A守B破")
    else:
        print(f"  → 双守型 稳但缺破局力")
    
    # 疾厄对比(战损层)
    print(f"\n【疾厄对比(身体/战损)】")
    je1=c1['palaces']['疾厄']; je2=c2['palaces']['疾厄']
    print(f"  人A疾厄({ZHI[je1['pos']]}): {' '.join(sorted(je1['stars']))}")
    print(f"  人B疾厄({ZHI[je2['pos']]}): {' '.join(sorted(je2['stars']))}")
    pojun1='破军' in je1['stars']; pojun2='破军' in je2['stars']
    if pojun1 and pojun2:
        print(f"  → 双破军在疾厄: 双方身体都是战场 武器都锁在身体里")
    elif pojun1: print(f"  → 人A破军在疾厄(武器锁身体) 人B没有")
    elif pojun2: print(f"  → 人B破军在疾厄(武器锁身体) 人A没有")
    
    # 四化互动
    print(f"\n【四化互动】")
    print(f"  人A: {c1['sihua']}")
    print(f"  人B: {c2['sihua']}")
    # 检查A的化忌是否打到B的命宫
    a_ji_star = c1['sihua'].get('忌')
    b_ming_stars = c2['palaces']['命宫']['stars']
    if a_ji_star in b_ming_stars:
        print(f"  ⚠ 人A化忌({a_ji_star})打到人B命宫")
    b_ji_star = c2['sihua'].get('忌')
    a_ming_stars = c1['palaces']['命宫']['stars']
    if b_ji_star in a_ming_stars:
        print(f"  ⚠ 人B化忌({b_ji_star})打到人A命宫") if b_ji_star else None
    
    # 子女宫对比
    print(f"\n【子女宫对比】")
    cz1=c1['palaces']['子女']; cz2=c2['palaces']['子女']
    print(f"  人A子女({ZHI[cz1['pos']]}): {' '.join(sorted(cz1['stars']))}")
    print(f"  人B子女({ZHI[cz2['pos']]}): {' '.join(sorted(cz2['stars']))}")
    shared = cz1['stars'] & cz2['stars']
    if shared: print(f"  共有星: {' '.join(shared)} (子女信号共振)")
    
    # 大运当前
    print(f"\n【当前大运】")
    for af,at,zhi,pn in c1['dayun']:
        if af<=43<=at: print(f"  人A当前大运: {pn}({zhi}) [{af}-{at}岁]")
    for af,at,zhi,pn in c2['dayun']:
        if af<=42<=at: print(f"  人B当前大运: {pn}({zhi}) [{af}-{at}岁]")

if __name__=="__main__":
    if len(sys.argv)<11:
        print("用法: python3 hepan.py Y1 MO1 D1 H1 M1 Y2 MO2 D2 H2 M2")
        print("M = male/female")
        sys.exit(1)
    args=sys.argv
    hepan(int(args[1]),int(args[2]),int(args[3]),int(args[4]),args[5].lower().startswith('m'),
          int(args[6]),int(args[7]),int(args[8]),int(args[9]),args[10].lower().startswith('m'))
