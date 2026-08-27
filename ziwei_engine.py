#!/usr/bin/env python3
"""
SAGA Oracle · 紫微斗数排盘引擎
用法: python3 ziwei_engine.py YYYY MM DD HH [name] [male/female]
HH = 24小时制整点(15=下午3点)
"""
import sys
from lunarcalendar import Converter, Solar, Lunar

GAN = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
ZHI = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
PN = ['命宫','兄弟','夫妻','子女','财帛','疾厄','迁移','仆役','官禄','田宅','福德','父母']

def s2l(y,m,d):
    s=Solar(y,m,d);l=Converter.Solar2Lunar(s);return l.year,l.month,l.day
def tz(h):return(h+1)//2%12
def mg(lm,tz):return(2+lm-1-tz)%12
def sg(lm,tz):return(2+lm-1+tz)%12

WUHU={'甲':2,'己':2,'乙':4,'庚':4,'丙':6,'辛':6,'丁':8,'壬':8,'戊':0,'癸':0}
def pg(yg,p):return(WUHU[yg]+p-2)%10

NAYIN=[('甲','子','金'),('乙','丑','金'),('丙','寅','火'),('丁','卯','火'),
('戊','辰','木'),('己','巳','木'),('庚','午','土'),('辛','未','土'),
('壬','申','金'),('癸','酉','金'),('甲','戌','火'),('乙','亥','火'),
('丙','子','水'),('丁','丑','水'),('戊','寅','土'),('己','卯','土'),
('庚','辰','金'),('辛','巳','金'),('壬','午','木'),('癸','未','木'),
('甲','申','水'),('乙','酉','水'),('丙','戌','土'),('丁','亥','土'),
('戊','子','火'),('己','丑','火'),('庚','寅','木'),('辛','卯','木'),
('壬','辰','水'),('癸','巳','水'),('甲','午','金'),('乙','未','金'),
('丙','申','火'),('丁','酉','火'),('戊','戌','木'),('己','亥','木'),
('庚','子','土'),('辛','丑','土'),('壬','寅','金'),('癸','卯','金'),
('甲','辰','火'),('乙','巳','火'),('丙','午','水'),('丁','未','水'),
('戊','申','土'),('己','酉','土'),('庚','戌','金'),('辛','亥','金'),
('壬','子','木'),('癸','丑','木'),('甲','寅','水'),('乙','卯','水'),
('丙','辰','土'),('丁','巳','土'),('戊','午','火'),('己','未','火'),
('庚','申','木'),('辛','酉','木'),('壬','戌','水'),('癸','亥','水')]

def get_ju(gi,zi):
    g,z=GAN[gi],ZHI[zi]
    for a,b,e in NAYIN:
        if a==g and b==z:return{'水':2,'木':3,'金':4,'土':5,'火':6}[e]

def zw_pos(ju,d):
    q,r=d//ju,d%ju
    if r==0:return(2+q)%12
    elif r%2==0:return(2+q+r//2)%12
    else:return(2+q+r//2-1)%12

def tf_pos(zw):return(4-zw+12)%12

ZWS={'紫微':0,'天机':-1,'太阳':-3,'武曲':-4,'天同':-5,'廉贞':-8}
TFS={'天府':0,'太阴':1,'贪狼':2,'巨门':3,'天相':4,'天梁':5,'七杀':6,'破军':10}

def place_stars(z,t):
    s={}
    for n,o in ZWS.items():
        p=(z+o+12)%12;s.setdefault(p,[]).append(n)
    for n,o in TFS.items():
        p=(t+o+12)%12;s.setdefault(p,[]).append(n)
    return s

LUCUN={'甲':2,'乙':3,'丙':4,'丁':5,'戊':6,'己':7,'庚':8,'辛':9,'壬':11,'癸':0}
QY={g:(v+1)%12 for g,v in LUCUN.items()}
TL={g:(v-1)%12 for g,v in LUCUN.items()}
TK={'甲':1,'乙':0,'丙':11,'丁':11,'戊':1,'己':0,'庚':1,'辛':2,'壬':3,'癸':3}
TYAO_KW={'甲':7,'乙':8,'丙':3,'丁':3,'戊':7,'己':8,'庚':7,'辛':6,'壬':5,'癸':5}
HL={'子':3,'丑':2,'寅':1,'卯':0,'辰':11,'巳':10,'午':9,'未':8,'申':7,'酉':6,'戌':5,'亥':4}
TX={z:(v+6)%12 for z,v in HL.items()}
ZF={i:(3+i)%12 for i in range(1,13)}
YB={i:(10-(i-1)+12)%12 for i in range(1,13)}
TXING={i:(8+i)%12 for i in range(1,13)}
TYAO={i:(1+i-1)%12 for i in range(1,13)}
WC={i:(10-i+12)%12 for i in range(12)}
WQ={i:(4+i)%12 for i in range(12)}
SH={'甲':{'禄':'廉贞','权':'破军','科':'武曲','忌':'太阳'},'乙':{'禄':'天机','权':'天梁','科':'紫微','忌':'太阴'},'丙':{'禄':'天同','权':'天机','科':'文昌','忌':'廉贞'},'丁':{'禄':'太阴','权':'天同','科':'天机','忌':'巨门'},'戊':{'禄':'贪狼','权':'太阴','科':'右弼','忌':'天机'},'己':{'禄':'武曲','权':'贪狼','科':'天梁','忌':'文曲'},'庚':{'禄':'太阳','权':'武曲','科':'太阴','忌':'天同'},'辛':{'禄':'巨门','权':'太阳','科':'文曲','忌':'文昌'},'壬':{'禄':'天梁','权':'紫微','科':'武曲','忌':'破军'},'癸':{'禄':'破军','权':'巨门','科':'太阴','忌':'贪狼'}}

# ========== v2 新增星 ==========
TIANGUAN={'甲':7,'乙':4,'丙':5,'丁':2,'戊':3,'己':9,'庚':11,'辛':9,'壬':10,'癸':6}
TIANFU_STAR={'甲':9,'乙':8,'丙':0,'丁':11,'戊':3,'己':2,'庚':6,'辛':5,'壬':6,'癸':5}
TIANMA={'寅':8,'午':8,'戌':8,'申':2,'子':2,'辰':2,'巳':11,'酉':11,'丑':11,'亥':5,'卯':5,'未':5}
TIANWU_M={1:5,5:5,9:5,2:8,6:8,10:8,3:2,7:2,11:2,4:11,8:11,12:11}
JIESHEN_M={1:8,2:8,3:10,4:10,5:0,6:0,7:2,8:2,9:4,10:4,11:6,12:6}
YINSHA_M={1:2,7:2,2:0,8:0,3:10,9:10,4:8,10:8,5:6,11:6,6:4,12:4}
TIANYUE_M={1:10,2:5,3:4,4:2,5:7,6:3,7:11,8:7,9:2,10:6,11:10,12:2}
TIANSHUI_M={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12}
FIRE_START={'寅':1,'午':1,'戌':1,'申':2,'子':2,'辰':2,'巳':3,'酉':3,'丑':3,'亥':9,'卯':9,'未':9}
BELL_START={'寅':3,'午':3,'戌':3,'申':10,'子':10,'辰':10,'巳':9,'酉':9,'丑':9,'亥':10,'卯':10,'未':10}
JIEKONG={'甲':(8,9),'己':(8,9),'乙':(6,7),'庚':(6,7),'丙':(4,5),'辛':(4,5),'丁':(2,3),'壬':(2,3),'戊':(0,1),'癸':(0,1)}
FEILIAN_Y={0:8,1:9,2:10,3:5,4:6,5:7,6:2,7:3,8:4,9:11,10:0,11:1}

DI_KONG={'子':8,'丑':7,'寅':6,'卯':5,'辰':4,'巳':3,'午':2,'未':1,'申':0,'酉':11,'戌':10,'亥':9}
DI_JIE={'子':2,'丑':3,'寅':4,'卯':5,'辰':6,'巳':7,'午':8,'未':9,'申':10,'酉':11,'戌':0,'亥':1}
GUCHEN={'子':2,'丑':2,'寅':5,'卯':5,'辰':5,'巳':8,'午':8,'未':8,'申':11,'酉':11,'戌':11,'亥':2}
GUASHU={'子':10,'丑':10,'寅':1,'卯':1,'辰':1,'巳':4,'午':4,'未':4,'申':7,'酉':7,'戌':7,'亥':10}
TIAN_KU={'子':6,'丑':5,'寅':4,'卯':3,'辰':2,'巳':1,'午':0,'未':11,'申':10,'酉':9,'戌':8,'亥':7}
TIAN_XU={'子':6,'丑':7,'寅':8,'卯':9,'辰':10,'巳':11,'午':0,'未':1,'申':2,'酉':3,'戌':4,'亥':5}

def cast(y,mo,d,h,name="",is_male=False):
    lr=s2l(y,mo,d)
    ly,lm,ld=lr
    yg=GAN[(ly-4)%10];yz=ZHI[(ly-4)%12];t=tz(h)
    m=mg(lm,t);s=sg(lm,t);gi=pg(yg,m);j=get_ju(gi,m)
    z=zw_pos(j,ld);tf=tf_pos(z);ms=place_stars(z,tf)
    all_s={}
    for pos,stars in ms.items():
        for s2 in stars:all_s.setdefault(pos,set()).add(s2)
    for sn,pos in[('禄存',LUCUN[yg]),('擎羊',QY[yg]),('陀罗',TL[yg]),('天魁',TK[yg]),('天钺',TYAO_KW[yg])]:all_s.setdefault(pos,set()).add(sn)
    for sn,pos in[('红鸾',HL[yz]),('天喜',TX[yz])]:all_s.setdefault(pos,set()).add(sn)
    for sn,pos in[('左辅',ZF[lm]),('右弼',YB[lm]),('天刑',TXING[lm]),('天姚',TYAO[lm])]:all_s.setdefault(pos,set()).add(sn)
    for sn,pos in[('文昌',WC[t]),('文曲',WQ[t])]:all_s.setdefault(pos,set()).add(sn)
    for sn,pos in[('地空',DI_KONG[yz]),('地劫',DI_JIE[yz]),('孤辰',GUCHEN[yz]),('寡宿',GUASHU[yz]),('天哭',TIAN_KU[yz]),('天虚',TIAN_XU[yz])]:all_s.setdefault(pos,set()).add(sn)
    # v2 新增星
    for sn,pos in[('天官',TIANGUAN[yg]),('天福',TIANFU_STAR[yg]),('天马',TIANMA[yz]),('天空',((ly-4)%12+1)%12),('蜚廉',FEILIAN_Y[(ly-4)%12])]:all_s.setdefault(pos,set()).add(sn)
    for sn,pos in[('天巫',TIANWU_M[lm]),('解神',JIESHEN_M[lm]),('阴煞',YINSHA_M[lm]),('天月',TIANYUE_M[lm]),('天碎',TIANSHUI_M[lm])]:all_s.setdefault(pos,set()).add(sn)
    for sn,pos in[('火星',(FIRE_START[yz]+t)%12),('铃星',(BELL_START[yz]+t)%12)]:all_s.setdefault(pos,set()).add(sn)
    for sn,pos in[('封诰',(2+t)%12),('台辅',(6+t)%12)]:all_s.setdefault(pos,set()).add(sn)
    for sn,pos in[('龙池',(4+(ly-4)%12)%12),('凤阁',(10-(ly-4)%12+12)%12)]:all_s.setdefault(pos,set()).add(sn)
    for sn,pos in[('天才',(m+(ly-4)%12)%12),('天寿',(s+(ly-4)%12)%12)]:all_s.setdefault(pos,set()).add(sn)
    # 恩光: 文昌位+日-2, 天贵: 文曲位+日-2
    wc_pos=WC[t];wq_pos=WQ[t]
    for sn,pos in[('恩光',(wc_pos+ld-2)%12),('天贵',(wq_pos+ld-2)%12)]:all_s.setdefault(pos,set()).add(sn)
    # 三台: 左辅位+日-1, 八座: 右弼位-(日-1)
    zf_pos=ZF[lm];yb_pos=YB[lm]
    for sn,pos in[('三台',(zf_pos+ld-1)%12),('八座',(yb_pos-ld+1+12*100)%12)]:all_s.setdefault(pos,set()).add(sn)
    # 截空: 年干定两位
    for pos in JIEKONG[yg]:all_s.setdefault(pos,set()).add('截空')
    # 天伤固定仆役, 天使固定疾厄
    pn_index=PN.index('仆役');sv_index=PN.index('疾厄')
    for sn,pos in[('天伤',(m-pn_index+12)%12),('天使',(m-sv_index+12)%12)]:all_s.setdefault(pos,set()).add(sn)
    pal={}
    for i in range(12):
        pos=(m-i+12)%12;pal[PN[i]]={'stars':all_s.get(pos,set()),'is_shen':pos==s,'pos':pos}
    abs_zw=z
    if abs_zw in[0,6,3,9]:geju="紫府格(四正位)稳守"
    elif abs_zw in[4,10,1,7]:geju="紫相格(四墓位)建维护"
    else:geju="杀破狼格(四生位)破拆重建"
    zw_cowork=[]
    for n,o in ZWS.items():
        if (z+o+12)%12==z and n!='紫微':zw_cowork.append(n)
    for n,o in TFS.items():
        if (tf+o+12)%12==z:zw_cowork.append(n)
    is_yang=(ly-4)%2==0
    direction=1 if (is_yang and is_male) or (not is_yang and not is_male) else -1
    dayun_list=[]
    for i in range(12):
        age_from=j+i*10;age_to=age_from+9
        pos=(m+direction*i+12)%12
        pname=PN[(m-pos+12)%12]
        dayun_list.append((age_from,age_to,ZHI[pos],pname))
    sihua=SH[yg]
    return{'name':name,'ly':ly,'lm':lm,'ld':ld,'yg':yg,'yz':yz,
        'ming_pos':m,'shen_pos':s,'ju':j,'zw':z,'tf':tf,
        'geju':geju,'zw_cowork':zw_cowork,'sihua':sihua,
        'palaces':pal,'dayun':dayun_list}

def print_chart(chart):
    p=chart
    print(f"\n{'='*60}")
    print(f"{p['name']} 紫微斗数排盘")
    print(f"{'='*60}")
    print(f"农历:{p['ly']}年{p['lm']}月{p['ld']}日 年干:{p['yg']}")
    print(f"命宫:{ZHI[p['ming_pos']]} 局:{p['ju']} 紫微:{ZHI[p['zw']]} 天府:{ZHI[p['tf']]} 身宫:{ZHI[p['shen_pos']]}")
    print(f"格局:{p['geju']}")
    print(f"紫微同宫:{'+'.join(p['zw_cowork']) if p['zw_cowork'] else '独坐'}")
    print(f"四化:{p['sihua']}")
    for name_p in PN:
        pal=p['palaces'][name_p]
        sh=" ★身宫" if pal['is_shen'] else ""
        stars=' '.join(sorted(pal['stars'])) if pal['stars'] else '(空宫)'
        du=""
        for af,at,zhi,pn in p['dayun']:
            if pn==name_p:du=f" [{af}-{at}岁]"
        print(f"  {name_p}({ZHI[pal['pos']]}): {stars}{sh}{du}")

if __name__=="__main__":
    if len(sys.argv)<5:
        print("用法: python3 ziwei_engine.py YYYY MM DD HH [name] [male/female]")
        sys.exit(1)
    y,mo,d,h=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
    name=sys.argv[5] if len(sys.argv)>5 else ""
    is_male=len(sys.argv)>6 and sys.argv[6].lower().startswith('m')
    chart=cast(y,mo,d,h,name,is_male)
    print_chart(chart)
