import random
ugen = []
for agents in range(1):
    uas = ['SM-J320H','SM-J3109','SM-J320FN','SM-J320P','SM-J320F','SM-J320M','SM-J320Y','SM-J320A','SM-J320G','SM-J327T1','SM-J320V','SM-J320YZ','SM-J320W8','SM-J320ZN','SM-J320N0','SM-J320R4']
    ft = ['SM-M625F','LM-K525', 'NID-1050','SM-A3051','CPH2069','RMX3286','A101XM','SM-A505GT','WKG-LX9','SM-A4260','Infinix X680C','RMX3265','GLA-LX1','Redmi 4X','V2204','vivo 2018','PCB-T104','2201122G','Infinix X688B','RMP2106','OXF-AN10','Infinix X6835B','CPH2399','SM-F731B','SM-T515','CPH2209','M2101K6R','V2135','SM-M307FN','JLN-LX3','CPH2123','Lenovo TB-X605F','V2110','RMX3572','LM-X420']
    an = ['9','8']
    aru = ['{density=3.0,width=1080,height=2480}','{density=2.75,width=720,height=1612}','{density=3.0,width=1080,height=2400}','{density=2.75,width=720,height=1520}','{density=3.0,width=1080,height=2408}','{density=3.0,width=1080,height=2340}','{density=3.0,width=1080,height=2376}','{density=3.0,width=1080,height=2404}','{density=3.0,width=1080,height=2404}','{density=2.75,width=720,height=1280}','{density=3.0,width=1080,height=2408}','{density=2.75,width=720,height=1440}','{density=2.75,width=720,height=1280}','{density=3.0,width=1080,height=2448}','{density=3.0,width=1080,height=2448}','{density=3.0,width=1080,height=2448}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2412}','{density=3.0,width=1080,height=2160}','{density=3.0,width=1440,height=3040}','{density=3.0,width=1080,height=2340}','{density=3.0,width=1080,height=2340}','{density=3.0,width=1080,height=2340}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1440,height=3120}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2400}','{density=2.75,width=720,height=1640}','{density=2.75,width=720,height=1440}','{density=2.75,width=720,height=1600}','{density=2.75,width=720,height=1600}','{density=3.0,width=1080,height=2408}','{density=3.0,width=1080,height=2408}','{density=3.0,width=1080,height=2408}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2246}','{density=3.0,width=1080,height=2400}','{density=2.75,width=720,height=1612}']
    su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
    xg = ['armeabi-v7a:armeabi','arm64-v8a','armeabi-v8a:armeabi','arm64-v8a:armeabi']
    fr = ['en_US','en_GB','es_LA','fr_FR','en_PK','id_IN']
    cv = ['airtel','IND airtel','Nepal Telecom','Jio 4G','Jazz','UFONE','Zong 4G','Telenor']
    ap = random.choice(fr)
    af = random.choice(aru)
    fd = random.choice(cv)
    ux = random.choice(an)
    fo = random.choice(xg)
    ub = random.choice(uas)
    efg = random.choice(ft)
    se = random.choice(su)
    so = random.choice(su)
    ua = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/219.0.0.46.114;FBBV/633638093;FBDM/{density=2.75,width=720,height=1280};FBLC/"+ap+";FBRV/481419572;FBCR/"+fd+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+ub+";FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
    ugen.append(ua)
