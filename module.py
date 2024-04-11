import random
ugen=[]
for agents in range(10000):
	rr = random.randint
	rc = random.choice
	
	# Oppo device details
	and_oppo = rc(['14', '11', '10'])
	model_oppo = rc(['CPH2415', 'CPH2455', 'CPH2471','CPH2373','CPH2071', 'CPH2349', 'CPH1923', 'CPH2239', 'CPH1959', 'CPH1943', 'CPH2387', 'CPH1909', 'CPH1912', 'CPH1939', 'CPH2121', 'CPH1725'])
	chrome_oppo = f"{str(rr(80, 444))}.0.{str(rr(3000, 6500))}.{str(rr(11, 499))}"
	
	# Infinix device details
	models_inf = rc(['X511', 'X6823C', 'X6511', 'X6511B', 'X5516C','X5515F'])
	ch_inf = f"{str(rr(80, 999))}.0.{str(rr(3200, 6500))}.{str(rr(11, 999))}"
	
	# Facebook Hua device details
	fb_hua = f"{str(rr(100, 490))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
	
	# Vivo device details
	and_vivo = f"{str(rr(11, 14))}"
	models_vivo = rc(['V2022', 'V2023', 'V2025','V2027', 'V2220A', 'V2164A','V2030','V2059A', 'vivo 1904', 'V2205','vivo 2015','V2046','V2021'])
	
	# Realme device details
	models_re = rc(['RMX1903', 'RMX1919', 'RMX1941','RMX1833','RMX3242', 'RMX3393', 'RMX3242','RMX3506','RMX2101', 'RMX3161', 'RMX3478','RMX1831'])
	buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
	ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
	
	# Samsung device details
	ad_sam = rc(['10', '7.0', '14', '11'])
	models_sam = rc(['SM-G361F', 'SM-A013G','SM-A022M','SM-S124DL','SM-A025A','SM-A032F','SM-A136U','SM-A205GN','SM-A226B','SM-A226BR','SM-A300H', 'SM-A5009', 'SM-S901N', 'SM-A600P','SM-J327AZ', 'Redmi Note 9 Pro','V2029','V2020','V2028','SM-N981N','M2012K11C','21061119AL','SM-A260G','SM-A127M','SM-J737T','M2105K81AC'])
	ch_sam = f"{str(rr(52, 124))}.0.{str(rr(2200, 6500))}.{str(rr(11, 199))}"
	
	# Generating user-agent strings
	u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {model_oppo} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36"
	u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; Infinix {models_inf} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_inf} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
	u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36 VivoBrowser/18.9.0.0"
	u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_re} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
	u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
	
	ua = rc([u1, u2, u3, u4, u5])
	ugen.append(ua)
