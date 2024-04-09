import random
ugen = []
for agents in range(10000):
	rr = random.randint
	rc = random.choice
	
	# Oppo device details
	and_oppo = rc(['14', '11', '10'])
	model_oppo = rc(['CPH1979', 'CPH1879', 'CPH2207','CPH2271','CPH2343', 'CPH2309', 'CPH2237', 'CPH1875', 'CPH2411', 'CPH2349', 'CPH1871', 'CPH1907', 'CPH2173', 'CPH1073', 'CPH2213', 'CP3504L'])
	chrome_oppo = f"{str(rr(80, 444))}.0.{str(rr(3000, 6500))}.{str(rr(11, 499))}"
	
	# Infinix device details
	models_inf = rc(['X652', 'X6826', 'X653', 'X626B', 'X682C','X650B'])
	ch_inf = f"{str(rr(80, 999))}.0.{str(rr(3200, 6500))}.{str(rr(11, 999))}"
	
	# Facebook Hua device details
	fb_hua = f"{str(rr(100, 490))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
	
	# Vivo device details
	and_vivo = f"{str(rr(11, 14))}"
	models_vivo = rc(['V2109', 'V2205', 'V2020CA','V2111A', 'vivo 1908', 'vivo 1909','V1930','V2026', 'V2034A', 'V2036A', 'V2201', 'V2110', 'V2035', 'V1965A', 'V2109','V2048','V1914A'])
	
	# Realme device details
	models_re = rc(['RMX1903', 'RMX1921', 'RMX1931','RMX3472','RMX2111', 'RMX3193', 'RMX2075', 'RMX2195', 'RMX3571','RMX3286'])
	buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
	ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
	
	# Samsung device details
	ad_sam = rc(['10', '7.0', '14', '11'])
	models_sam = rc(['JKM-LX2', 'SM-J810GF','SM-M305M','SM-G611K','MNA-LX9','SM-C7000','RMX2025','SM-S136DL', 'LM-F100N', 'BQ-8077L', 'SM-M135FU','SM-S515DL', 'M2012K11AG','M2007J17C', 'V2214', 'LG-D855', 'SM-S115DL','SM-J610F','SM-S367VL','SM-A600A','AMN-LX2','SM-N915A'])
	ch_sam = f"{str(rr(52, 124))}.0.{str(rr(2200, 6500))}.{str(rr(11, 199))}"
	
	# Generating user-agent strings
	u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))} {model_oppo} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36"
	u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; Infinix {models_inf} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_inf} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
	u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36 VivoBrowser/18.9.0.0"
	u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))} {models_re} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
	u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
	
	ua = rc([u1, u2, u3, u4, u5])
	ugen.append(ua)
