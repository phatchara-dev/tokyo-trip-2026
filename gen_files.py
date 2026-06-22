import os

# ข้อมูลแผนการเดินทาง 9 วัน ตัดเรื่องอาหารและส่องรถไฟซ้ำซาก เน้นที่เที่ยว + Mega Sento
trip_data = {
    1: {
        "date_th": "วันอังคารที่ 28 กรกฎาคม 2026", "date_en": "Tuesday, July 28, 2026", "date_ja": "2026年7月28日(火)",
        "title_th": "แลนดิ้งสู่โตเกียว ยิงรถไฟโลคอลเข้าชินจูกุ & ประเดิมสปายักษ์คึกคัก 🛬",
        "title_en": "Narita Landing, Budget Train Commute to Shinjuku & Mega Sento Launch 🛬",
        "title_ja": "成田空港到着、格安一般列車での新宿移動＆郊外型大型銭湯 🛬",
        "sento_th": "Mega Sento 1: Manten no Yu (天然温泉 満天の湯)", "sento_en": "Mega Sento 1: Manten no Yu", "sento_ja": "メガ銭湯 1：満天の湯",
        "sento_detail_th": "เดินทางด้วยรถไฟไปซูเปอร์เซ็นโตขนาดใหญ่ บ่อแช่น้ำเปิดโล่งและบ่อคาร์บอเนตขนาดยักษ์จำนวนมาก ล้างความล้าจากการเดินทาง บรรยากาศโลคอลคึกคักคนเยอะหนาตา",
        "sento_detail_en": "Commute via local train to a massive suburban super sento with spacious outdoor natural pools and huge carbonated baths. Vibrant local crowd attendance.",
        "sento_detail_ja": "広々とした人気スーパー銭湯へ。巨大な露天風呂や炭酸泉に浸かり、フライトの疲れを癒やす。地元客で大変賑わう。",
        "sento_cost": "¥1,000", "transit_cost": "¥1,250", "return_cost": "¥240", "total_cost": "¥2,490"
    },
    2: {
        "date_th": "วันพุธที่ 29 กรกฎาคม 2026", "date_en": "Wednesday, July 29, 2026", "date_ja": "2026年7月29日(水)",
        "title_th": "พักผ่อนตามอัธยาศัยย่านชินจูกุ & ลุยเมกะเซ็นโตอันดับหนึ่ง Spadium Japon 🚇",
        "title_en": "Free Time in Shinjuku & Spadium Japon Mega Sento 🚇",
        "title_ja": "新宿での自由行動＆東京最大級メガ銭湯スパジアムジャポン 🚇",
        "sento_th": "Mega Sento 2: Spadium Japon (スパジアムジャポン)", "sento_en": "Mega Sento 2: Spadium Japon", "sento_ja": "メガ銭湯 2：スパジアムジャポン",
        "sento_detail_th": "เดินทางด้วยรถไฟและต่อรถบัสท้องถิ่นลู่ตรงสู่เมกะเซ็นโตอันดับหนึ่งที่ใหญ่ที่สุดในโตเกียว บ่อแช่น้ำอลังการกว่า 15 รูปแบบ ทั้งบ่อกลางแจ้งและบ่อไฟฟ้า บรรยากาศคึกคักสูงสุด",
        "sento_detail_en": "Take a local train and free shuttle bus to Tokyo's largest mega sento complex, featuring over 15 dynamic hot spring pools with a lively local crowd.",
        "sento_detail_ja": "一般列車とシャトルバスを乗り継ぎ、東京最大級のメガ銭湯施設へ。15種類もの多彩な大浴場を誇り、非常に活気ある雰囲気。",
        "sento_cost": "¥850", "transit_cost": "ฟรี", "return_cost": "¥180", "total_cost": "¥1,030"
    },
    3: {
        "date_th": "วันพฤหัสบดีที่ 30 กรกฎาคม 2026", "date_en": "Thursday, July 30, 2026", "date_ja": "2026年7月30日(木)",
        "title_th": "ลุยเขตพระราชวังอิมพีเรียล & แช่น้ำแร่ Super Sento บ่อยักษ์ชานเมือง ⛩️",
        "title_en": "Tokyo Imperial Palace Walk & Suburban Yura no Sato Super Sento ⛩️",
        "title_ja": "皇居散策＆郊外型大型スーパー銭湯湯楽の里 ⛩️",
        "sento_th": "Mega Sento 3: Yura no Sato (天然温泉 湯楽の里)", "sento_en": "Mega Sento 3: Yura no Sato", "sento_ja": "メガ銭湯 3：湯楽の里",
        "sento_detail_th": "เดินทางด้วยรถไฟสายประหยัดสู่ซูเปอร์เซ็นโตขนาดใหญ่ ผ่อนคลายกับบ่อหินธรรมชาติกลางแจ้ง (Rotenburo) และบ่อเจ็ทนวดตัวที่มีผู้คนหนาแน่นคึกคักบ่อเพียบสะใจ",
        "sento_detail_en": "Commute via budget rail line to a spacious suburban super sento. Unwind in massive outdoor natural stone Rotenburo baths alongside local bathers.",
        "sento_detail_ja": "格安の一般列車で大型スーパー銭湯へ移動。広大な岩造り露天風呂や各種ジェットバスを誇り、地元客で大変賑わう。",
        "sento_cost": "¥1,050", "transit_cost": "ฟรี", "return_cost": "¥240", "total_cost": "¥1,290"
    },
    4: {
        "date_th": "วันศุกร์ที่ 31 กรกฎาคม 2026", "date_en": "Friday, July 31, 2026", "date_ja": "2026年7月31日(金)",
        "title_th": "เดินเล่นชิล ๆ ย่าน Akihabara & ตลาด Ameyoko + แช่เมกะเซ็นโต Spadium Japon ⚡",
        "title_en": "Strolling Akihabara & Ameyoko Open Market + Spadium Japon Mega Sento ⚡",
        "title_ja": "秋葉原＆アメ横散策＋メガ銭湯スパジアムジャポン ⚡",
        "sento_th": "Mega Sento 4: Spadium Japon (スパジアムジャポン)", "sento_en": "Mega Sento 4: Spadium Japon", "sento_ja": "メガ銭湯 4：スパジアムジャポン",
        "sento_detail_th": "กลับมาซ้ำเมกะเซ็นโตที่ใหญ่ที่สุดในโตเกียวเพื่อเก็บตกบ่อแช่น้ำอลังการกว่า 15 รูปแบบ ท่ามกลางบรรยากาศโลคอลคึกคักคนหนาแน่นสะใจ",
        "sento_detail_en": "Return to Tokyo's premier mega sento complex to fully enjoy its 15+ hot spring grids with a lively local crowd.",
        "sento_detail_ja": "再び東京最大級の有名メガ銭湯へ。15種類の多彩な大浴場を、非常に賑やかなローカルな雰囲気の中で満喫。",
        "sento_cost": "¥850", "transit_cost": "ฟรี", "return_cost": "¥180", "total_cost": "¥1,030"
    },
    5: {
        "date_th": "วันเสาร์ที่ 1 สิงหาคม 2026", "date_en": "Saturday, August 1, 2026", "date_ja": "2026年8月1日(土)",
        "title_th": "พักผ่อนตามอัธยาศัยในวันหยุด & แช่น้ำแร่สะใจที่เมกะเซ็นโต Ryusenji no Yu 🚄",
        "title_en": "Weekend Free Lounge & Ryusenji no Yu Gigantic Mega Sento 🚄",
        "title_ja": "週末の自由行動＆郊外型メガスーパー銭湯竜泉寺の湯 🚄",
        "sento_th": "Mega Sento 5: Ryusenji no Yu (竜泉寺の湯)", "sento_en": "Mega Sento 5: Ryusenji no Yu", "sento_ja": "メガ銭湯 5：竜泉寺の湯",
        "sento_detail_th": "เดินทางสู่เมกะเซ็นโตขนาดยักษ์ชื่อดัง เพลิดเพลินกับโซนน้ำแร่ธรรมชาติและบ่อคาร์บอเนตความเข้มข้นสูงยักษ์ บ่อเพียบ คนหนาแน่นคึกคักสะใจสายเซ็นโต",
        "sento_detail_en": "Unwind at a legendary mega sento complex famous for its enormous outdoor bath areas and highly dense carbonated spring grids packed with locals.",
        "sento_detail_ja": "有名メガ銭湯施設へ。広大な大露天風呂や、毎週末大変賑わう名物の高濃度炭酸泉大浴場を満喫。",
        "sento_cost": "¥950", "transit_cost": "ฟรี", "return_cost": "ตามจริง", "total_cost": "¥950"
    },
    6: {
        "date_th": "วันอาทิตย์ที่ 2 สิงหาคม 2026", "date_en": "Sunday, August 2, 2026", "date_ja": "2026年8月2日(日)",
        "title_th": "พักผ่อนสัมผัสย่านวัฒนธรรมเมืองเก่าศาลเจ้าเมจิ & ลุยสปาคาเฟ่ยักษ์โมเดิร์น 🌳",
        "title_en": "Historic Meiji Jingu Forest Walk & Ofuro Cafe Utatane Modern Sento Lounge 🌳",
        "title_ja": "明治神宮の杜散策＆超大型銭湯おふろcafe utatane 🌳",
        "sento_th": "Mega Sento 6: Ofuro Cafe Utatane (おふろcafe utatane)", "sento_en": "Mega Sento 6: Ofuro Cafe Utatane", "sento_ja": "メガ銭湯 6：おふろcafe utatane",
        "sento_detail_th": "เดินทางสู่ซูเปอร์เซ็นโตสไตล์โมเดิร์นขนาดยักษ์ มีบ่อแช่น้ำแร่ธรรมชาติหลากหลายรูปแบบและสิ่งอำนวยความสะดวกครบครัน คนหนาแน่นคึกคักเป็นที่นิยมสูงสุด",
        "sento_detail_en": "Visit a massive modern-concept super sento complex in Saitama. Features extensive natural hot spring baths and lounge facilities with a packed weekend youth attendance.",
        "sento_detail_ja": "埼玉の近代的な超大型温泉施設へ。多彩な浴槽や広々としたサウナを誇り、若い世代を中心に一日中大変活気がある。",
        "sento_cost": "¥1,260", "transit_cost": "ฟรี", "return_cost": "¥390", "total_cost": "¥1,650"
    },
    7: {
        "date_th": "วันจันทร์ที่ 3 สิงหาคม 2026", "date_en": "Monday, August 3, 2026", "date_ja": "2026年8月3日(月)",
        "title_th": "สโลว์ไลฟ์รับลมชมวิวสวนญี่ปุ่นศิลาแท้ & แช่น้ำออนเซ็นเขียวเข้ม Sayanoyudoko 🎋",
        "title_en": "Shinjuku Free Rest & Japanese Stone Garden Hot Spring Sayanoyudoko 🎋",
        "title_ja": "新宿での休息タイム＆日本庭園名湯さやの湯処 🎋",
        "sento_th": "Mega Sento 7: Sayanoyudoko (前野原温泉 さやの湯処)", "sento_en": "Mega Sento 7: Sayanoyudoko", "sento_ja": "メガ銭湯 7：さやの湯処",
        "sento_detail_th": "เดินทางด้วยรถไฟขบวนธรรมดาสู่ซูเปอร์เซ็นโตน้ำแร่ธรรมชาติแท้สีเขียวเข้มบ่อยักษ์ บ่อหินศิลา บ่อน้ำพุร้อนกลางแจ้งในบรรยากาศสวนญี่ปุ่นแบบดั้งเดิมที่ผู้คนหนาแน่นแน่นตลอดวัน",
        "sento_detail_en": "Commute via local lines to a top-tier authentic natural hot spring complex. Soothe your body in deep green mineral water and outdoor rock pools looking into traditional Japanese gardens. Highly packed with locals all day.",
        "sento_detail_ja": "都内屈指の超人気天然温泉へ。本格的な日本庭園を眺めながら、源泉かけ流しの濃い緑色の露天風呂や各種アトラクションバスを満喫。一日中非常に混雑する名店。",
        "sento_cost": "¥1,100", "transit_cost": "ฟรี", "return_cost": "¥220", "total_cost": "¥1,320"
    },
    8: {
        "date_th": "วันอังคารที่ 4 สิงหาคม 2026", "date_en": "Tuesday, August 4, 2026", "date_ja": "2026年8月4日(火)",
        "title_th": "ย้ายค่ายฐานที่มั่นสู่ฝั่งเมือง Narita & ส่งท้ายเมกะเซ็นโตบ่อยักษ์ Hana no Yu 🧳",
        "title_en": "Base Relocation to Narita & Grand Finale at Hana no Yu Mega Sento 🧳",
        "title_ja": "成田への拠点移動＆成田温泉華の湯で旅の締めくくり 🧳",
        "sento_th": "Mega Sento 8: Hana no Yu Narita (成田温泉 華の湯)", "sento_en": "Mega Sento 8: Hana no Yu Narita", "sento_ja": "メガ銭湯 8：華の湯 成田",
        "sento_detail_th": "ส่งท้ายค่ำคืนสุดท้ายด้วยการเดินเท้าไปเมกะเซ็นโตขนาดยักษ์ที่ใหญ่ที่สุดในนาริตะ เพลิดเพลินกับบ่อแช่น้ำกลางแจ้ง บ่อคาร์บอเนต บ่อสมุนไพรรวมกว่า 10 รูปแบบ บรรยากาศโลคอลแน่นคึกคักสุดฟิน",
        "sento_detail_en": "Walk to Narita's premier large-scale super sento complex. Experience over 10 varieties of outdoor, carbonated, and herb baths with a highly packed local attendance.",
        "sento_detail_ja": "徒歩で成田最大級の大型スーパー銭湯へ移動。10種類以上の広々とした露天風呂、大炭酸泉、ハーブ湯などを多数の地元客とともに存分に堪能。",
        "sento_cost": "¥900", "transit_cost": "¥1,140", "return_cost": "ฟรี", "total_cost": "¥2,040"
    }
}

def generate_html(day, lang):
    d = trip_data.get(day)
    header_title = "🚇 Tokyo Unseen & Mega Sento Speed Trip 2026 🏮"
    
    if lang == "th":
        title_tag = f"Day {day}: Tokyo Mega Sento Trip 2026"
        th_header, act_header, route_header, cost_header = "เวลา", "กิจกรรม", "การเดินทาง & รายละเอียด", "ค่าใช้จ่ายแยก"
        free_txt, total_lbl, back_lbl, home_lbl, next_lbl = "ฟรี", f"รวมค่าใช้จ่ายแยกของ Day {day}", "← ย้อนกลับ Day", "กลับหน้าเลือกวัน", "ไปยัง Day"
        
        if day == 1:
            rows = f"""
                <tr><td>07:35 - 09:30</td><td>🛬 Landing นาริตะ & จัดการเอกสาร</td><td>เครื่องแลนดิ้งสู่สนามบินนาริตะ ผ่านกองตรวจคนเข้าเมืองและรับสัมภาระ</td><td>{free_txt}</td></tr>
                <tr><td>09:30 - 11:30</td><td>🚃 นั่งรถไฟธรรมดาสายประหยัดเข้าสู่ Shinjuku</td><td>นั่งรถไฟสาย Keisei Main Line (ขบวนธรรมดา) ไปเปลี่ยนสาย JR Yamanote Line ที่สถานี Nippori ลู่ตรงเข้าสู่ Shinjuku เพื่อฝากกระเป๋าเดินทางที่ Hostel Capsule Kuyakushomae Shinjuku</td><td>{d['transit_cost']}</td></tr>
                <tr><td>11:30 - 17:00</td><td>🏙️ พักผ่อนเดินเล่นย่าน Shinjuku</td><td>เดินรับบรรยากาศเมืองโตเกียว ส่องตึก ศาลเจ้า และย่านมีชื่อเสียงรอบที่พักชินจูกุ</td><td>{free_txt}</td></tr>
            """
        elif day == 6:
            rows = f"""
                <tr><td>10:00 - 13:00</td><td>🌳 ชมป่าใจกลางเมือง ศาลเจ้าเมจิ (Meiji Jingu)</td><td>นั่งรถไฟสายประหยัดสั้น ๆ ไปยัง Harajuku เดินเข้าชมความเงียบสงบของพื้นที่ป่าขนาดยักษ์และศาลเจ้าเมจิอันศักดิ์สิทธิ์</td><td>{free_txt}</td></tr>
                <tr><td>13:00 - 15:30</td><td>🏙️ เดินปล่อยใจย่าน Harajuku / Takeshita</td><td>เดินรับชมสีสันและแฟชั่นบนถนนคนเดินย่านฮาราจูกุในวันหยุดสุดสัปดาห์ตามใจชอบ</td><td>{free_txt}</td></tr>
            """
        elif day == 8:
            rows = f"""
                <tr><td>10:00 - 12:30</td><td>🧳 เช็กเอาต์ชินจูกุ & ย้ายเมืองสู่ Narita</td><td>เช็กเอาต์จากชินจูกุ นั่งรถไฟขบวนธรรมดาสายประหยัดยาวลู่ตรงเข้าสู่ย่าน Narita และฝากสัมภาระเข้าเช็กอินที่ Hotel Welco Narita คืนสุดท้าย</td><td>{d['transit_cost']}</td></tr>
                <tr><td>12:30 - 16:00</td><td>🏙️ เดินชมบรรยากาศเมืองโลคอลรอบ Narita</td><td>ปล่อยฟรีไทม์เดินชมโครงสร้างผังเมืองและบรรยากาศความสงบเงียบเรียบง่ายรอบพื้นที่สถานีรถไฟ Narita</td><td>{free_txt}</td></tr>
            """
        else:
            rows = f"""
                <tr><td>09:30 - 13:00</td><td>🛌 สโลว์ไลฟ์ พักผ่อนเต็มพิกัดในที่พัก</td><td>นอนพักผ่อนยาว ๆ ชาร์จแบตเตอรี่ร่างกายและสมองในที่พักเพื่อลดความล้าสะสม</td><td>{free_txt}</td></tr>
                <tr><td>13:00 - 16:00</td><td>🏙️ เดินเล่นรับลมชมวิวในตัวเมือง</td><td>เดินเล่นพักผ่อน รับบรรยากาศชิล ๆ สบาย ๆ ในกรุงโตเกียวแบบไม่เร่งรีบ</td><td>{free_txt}</td></tr>
            """
            
        rows += f"""
            <tr class="highlight-pass"><td>16:30 - 19:30</td><td>♨️ {d['sento_th']}</td><td>{d['sento_detail_th']}</td><td>{d['sento_cost']}</td></tr>
            <tr><td>19:30 - 21:00</td><td>💤 กลับเข้าที่พัก</td><td>เดินทางด้วยรถไฟขบวนธรรมดาสายประหยัดกลับสู่ที่พักเพื่อพักผ่อนนอนหลับ</td><td>{d['return_cost']}</td></tr>
        """
        
    elif lang == "en":
        title_tag = f"Day {day}: Tokyo Mega Sento Trip 2026"
        th_header, act_header, route_header, cost_header = "Time", "Activity", "Route & Details", "Cost"
        free_txt, total_lbl, back_lbl, home_lbl, next_lbl = "Free", f"Total Cost for Day {day}", "← Back to Day", "Select Day", "Go to Day"
        
        if day == 1:
            rows = f"""
                <tr><td>07:35 - 09:30</td><td>🛬 Narita Landing & Customs</td><td>Touch down at Narita Airport, clear immigration procedures, and collect luggage.</td><td>{free_txt}</td></tr>
                <tr><td>09:30 - 11:30</td><td>🚃 Budget Local Train Commute to Shinjuku</td><td>Take the Keisei Main Line (Local), transfer to the JR Yamanote Line at Nippori Station, and head directly to Shinjuku. Drop off bags at Hostel Capsule Kuyakushomae Shinjuku.</td><td>{d['transit_cost']}</td></tr>
                <tr><td>11:30 - 17:00</td><td>🏙️ Relaxed Stroll around Shinjuku</td><td>Explore the streets and shrines near the Shinjuku accommodation at an easy pace.</td><td>{free_txt}</td></tr>
            """
        elif day == 6:
            rows = f"""
                <tr><td>10:00 - 13:00</td><td>🌳 Meiji Jingu Shrine Forest Layout</td><td>Take a cheap local train to Harajuku. Walk deep into the high-density quiet shrine forest grids of Meiji Jingu.</td><td>{free_txt}</td></tr>
                <tr><td>13:00 - 15:30</td><td>🏙️ Leisurely Walk around Harajuku Streets</td><td>Experience Sunday color layouts on Takeshita Street freely.</td><td>{free_txt}</td></tr>
            """
        elif day == 8:
            rows = f"""
                <tr><td>10:00 - 12:30</td><td>🧳 Shinjuku Checkout & Budget Rail to Narita</td><td>Check out from Shinjuku, catch a budget local train heading out directly to Narita City, and drop off bags at Hotel Welco Narita for the final night.</td><td>{d['transit_cost']}</td></tr>
                <tr><td>12:30 - 16:00</td><td>🏙️ Peaceful Walk around Narita Local Lines</td><td>Spend free time observing town layouts and enjoying a quiet walk near Narita rail grids.</td><td>{free_txt}</td></tr>
            """
        else:
            rows = f"""
                <tr><td>09:30 - 13:00</td><td>🛌 Slow Leisure Lounging in Hostel</td><td>Relax completely inside the hostel beds to clear off all cumulative exhaustion.</td><td>{free_txt}</td></tr>
                <tr><td>13:00 - 16:00</td><td>🏙️ Easy Outing Walk</td><td>Take a slow, unhurried walk to breathe in the calm atmosphere of Tokyo.</td><td>{free_txt}</td></tr>
            """
            
        rows += f"""
            <tr class="highlight-pass"><td>16:30 - 19:30</td><td>♨️ {d['sento_en']}</td><td>{d['sento_detail_en']}</td><td>{d['sento_cost']}</td></tr>
            <tr><td>19:30 - 21:00</td><td>💤 Return to Accommodation</td><td>Hop on a budget local train line back to your accommodation to sleep.</td><td>{d['return_cost']}</td></tr>
        """
        
    else: # ja
        title_tag = f"Day {day}: Tokyo Mega Sento Trip 2026"
        th_header, act_header, route_header, cost_header = "時間", "スケジュール", "ルート＆詳細", "個別費用"
        free_txt, total_lbl, back_lbl, home_lbl, next_lbl = "無料", f"Day {day} 個別費用合計", "← Day 前に戻る", "日付選択に戻る", "Day へ進む →"
        
        if day == 1:
            rows = f"""
                <tr><td>07:35 - 09:30</td><td>🛬 成田到着＆入国手続き</td><td>成田空港に着陸し、入国審査の手続きをすませて荷物を受け取る。</td><td>{free_txt}</td></tr>
                <tr><td>09:30 - 11:30</td><td>🚃 格安一般列車での新宿移動</td><td>京成本線（一般）に乗り、日暮里駅でJR山手線に乗り換えて新宿へ直行。「ホステルカプセル区役所前新宿」に荷物を預ける。</td><td>{d['transit_cost']}</td></tr>
                <tr><td>11:30 - 17:00</td><td>🏙️ 新宿エリアののんびり散策</td><td>新宿駅周辺や有名な神社、高層ビル街の周辺を各自のペースで自由に街歩き。</td><td>{free_txt}</td></tr>
            """
        elif day == 6:
            rows = f"""
                <tr><td>10:00 - 13:00</td><td>🌳 明治神宮の広大な杜の散策</td><td>格安列車で原宿へ。都会の中心に広がる広大な明治神宮の深い杜の参道をのんびり歩く。</td><td>{free_txt}</td></tr>
                <tr><td>13:00 - 15:30</td><td>🏙️ 原宿・竹下通りの街歩き</td><td>週末の活気あふれる原宿エリアや裏通りの風景をのんびり視察。</td><td>{free_txt}</td></tr>
            """
        elif day == 8:
            rows = f"""
                <tr><td>10:00 - 12:30</td><td>🧳 新宿チェックアウト＆成田移動</td><td>新宿をチェックアウト。最も経済的な一般列車を乗り継いで成田市内へ。「ホテルウェルコ成田」にチェックイン。</td><td>{d['transit_cost']}</td></tr>
                <tr><td>12:30 - 16:00</td><td>🏙️ 成田駅周辺ののんびり街歩き</td><td>成田駅の周辺エリアを静かに散策。のんびりとした街並みを眺めながら自由に行動。</td><td>{free_txt}</td></tr>
            """
        else:
            rows = f"""
                <tr><td>09:30 - 13:00</td><td>🛌 宿でののんびり朝寝坊</td><td>午前中はホステルでゆっくり朝寝坊。日頃の脳と体の疲れを完全にリセットする。</td><td>{free_txt}</td></tr>
                <tr><td>13:00 - 16:00</td><td>🏙️ 都内エリアの穏やかな散策</td><td>人混みから離れた街並みを各自のペースでのんびりお散歩。</td><td>{free_txt}</td></tr>
            """
            
        rows += f"""
            <tr class="highlight-pass"><td>16:30 - 19:30</td><td>♨️ {d['sento_ja']}</td><td>{d['sento_detail_ja']}</td><td>{d['sento_cost']}</td></tr>
            <tr><td>19:30 - 21:00</td><td>💤 ホテルへ帰還</td><td>格安の一般列車でホテルに帰り、ゆっくり休む。</td><td>{d['return_cost']}</td></tr>
        """

    btn_back = f'<a href="day{day-1}-{lang}.html" class="btn btn-back">{back_lbl} {day-1}</a>' if day > 1 else ''
    btn_next = f'<a href="day{day+1}-{lang}.html" class="btn btn-next">{next_lbl} {day+1} →</a>' if day < 9 else ''
    if day == 8: btn_next = f'<a href="day9-{lang}.html" class="btn btn-next">{next_lbl} 9 →</a>'

    date_str = d[f'date_{lang}']
    title_str = d[f'title_{lang}']

    html_content = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="UTF-8">
    <title>{title_tag}</title>
    <link rel="stylesheet" href="style.css?v=10">
</head>
<body>
<div class="container">
    <div class="lang-switcher">
        <a href="day{day}-th.html" {'style="background: #d4af37; color: #252a36 !important;"' if lang=='th' else ''}>TH</a> | 
        <a href="day{day}-en.html" {'style="background: #d4af37; color: #252a36 !important;"' if lang=='en' else ''}>EN</a> | 
        <a href="day{day}-ja.html" {'style="background: #d4af37; color: #252a36 !important;"' if lang=='ja' else ''}>JP</a>
    </div>
    <div class="header">{header_title}</div>
    <div class="day-section">
        <div class="day-title">🗓️ Day {day}: {date_str} | {title_str}</div>
        <div class="table-wrapper">
            <table class="activity-table">
                <thead>
                    <tr><th>{th_header}</th><th>{act_header}</th><th>{route_header}</th><th>{cost_header}</th></tr>
                </thead>
                <tbody>
                    {rows}
                    <tr style="font-weight: bold;"><td colspan="3" style="text-align: left;">{total_lbl}</td><td style="text-align: right;">{d['total_cost']}</td></tr>
                </tbody>
            </table>
        </div>
    </div>
    <div class="btn-wrapper">
        {btn_back}
        <a href="index.html" class="btn btn-home">{home_lbl}</a>
        {btn_next}
    </div>
</div>
</body>
</html>"""
    return html_content

def generate_day9(lang):
    if lang == "th":
        return """<!DOCTYPE html>
<html lang="th">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="UTF-8">
    <title>Day 9: Tokyo Mega Sento Trip 2026</title><link rel="stylesheet" href="style.css?v=10">
</head>
<body>
<div class="container">
    <div class="lang-switcher"><a href="day9-th.html" style="background: #d4af37; color: #252a36 !important;">TH</a> | <a href="day9-en.html">EN</a> | <a href="day9-ja.html">JP</a></div>
    <div class="header">🚇 Tokyo Unseen & Mega Sento Speed Trip 2026 🏮</div>
    <div class="day-section">
        <div class="day-title">🗓️ Day 9: วันพุธที่ 5 สิงหาคม 2026 | เดินทางจากที่พักนาริตะ เข้าสนามบิน บอร์ดดิ้งกลับบ้านโดยสวัสดิภาพ ✈️</div>
        <div class="table-wrapper">
            <table class="activity-table">
                <thead><tr><th>เวลา</th><th>กิจกรรม</th><th>การเดินทาง & รายละเอียด</th><th>ค่าใช้จ่ายแยก</th></tr></thead>
                <tbody>
                    <tr><td>06:30 - 07:15</td><td>🧳 เช็กเอาต์ที่พัก & เดินทางเข้าสนามบินนาริตะ</td><td>เช็กเอาต์จาก Hotel Welco Narita นั่งรถไฟขบวนธรรมดาสายสั้นลู่ตรงจากสถานี Narita มุ่งหน้าสู่สถานี Airport Terminal สนามบินนาริตะ</td><td>¥270</td></tr>
                    <tr><td>07:15 - 09:30</td><td>✈️ ผ่านด่านตรวจคนเข้าเมือง & บอร์ดดิ้งไฟลท์ 09:30 น.</td><td>จัดการเช็กอินโหลดสัมภาระ ผ่านกองตรวจคนเข้าเมือง และเตรียมตัวขึ้นเครื่องบินเดินทางกลับโดยสวัสดิภาพ</td><td>ฟรี</td></tr>
                    <tr style="font-weight: bold;"><td colspan="3" style="text-align: left;">รวมค่าใช้จ่ายแยกของ Day 9</td><td style="text-align: right;">¥270</td></tr>
                </tbody>
            </table>
        </div>
    </div>
    <div class="btn-wrapper"><a href="day8-th.html" class="btn btn-back">← ย้อนกลับ Day 8</a><a href="index.html" class="btn btn-home">กลับหน้าเลือกวัน</a></div>
</div>
</body>
</html>"""
    elif lang == "en":
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="UTF-8">
    <title>Day 9: Tokyo Mega Sento Trip 2026</title><link rel="stylesheet" href="style.css?v=10">
</head>
<body>
<div class="container">
    <div class="lang-switcher"><a href="day9-th.html">TH</a> | <a href="day9-en.html" style="background: #d4af37; color: #252a36 !important;">EN</a> | <a href="day9-ja.html">JP</a></div>
    <div class="header">🚇 Tokyo Unseen & Mega Sento Speed Trip 2026 🏮</div>
    <div class="day-section">
        <div class="day-title">🗓️ Day 9: Wednesday, August 5, 2026 | Narita Check-out, Terminal Commute & Safe Flight Home ✈️</div>
        <div class="table-wrapper">
            <table class="activity-table">
                <thead><tr><th>Time</th><th>Activity</th><th>Route & Details</th><th>Cost</th></tr></thead>
                <tbody>
                    <tr><td>06:30 - 07:15</td><td>🧳 Hotel Checkout & Airport Transit</td><td>Check out from Hotel Welco Narita. Take a cheap short local rail ride from Narita Station to Narita Airport Terminal Station.</td><td>¥270</td></tr>
                    <tr><td>07:15 - 09:30</td><td>✈️ Customs Clearance & 09:30 AM Boarding</td><td>Complete baggage drop, clear immigration checkpoints, and proceed to the gate for departure flight back home.</td><td>Free</td></tr>
                    <tr style="font-weight: bold;"><td colspan="3" style="text-align: left;">Total Cost for Day 9</td><td style="text-align: right;">¥270</td></tr>
                </tbody>
            </table>
        </div>
    </div>
    <div class="btn-wrapper"><a href="day8-en.html" class="btn btn-back">← Back to Day 8</a><a href="index.html" class="btn btn-home">Select Day</a></div>
</div>
</body>
</html>"""
    else:
        return """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="UTF-8">
    <title>Day 9: Tokyo Mega Sento Trip 2026</title><link rel="stylesheet" href="style.css?v=10">
</head>
<body>
<div class="container">
    <div class="lang-switcher"><a href="day9-th.html">TH</a> | <a href="day9-en.html">EN</a> | <a href="day9-ja.html" style="background: #d4af37; color: #252a36 !important;">JP</a></div>
    <div class="header">🚇 Tokyo Unseen & Mega Sento Speed Trip 2026 🏮</div>
    <div class="day-section">
        <div class="day-title">🗓️ Day 9: 2026年8月5日(水) | 成田の宿出発、成田空港への移動＆安全帰国 ✈️</div>
        <div class="table-wrapper">
            <table class="activity-table">
                <thead><tr><th>時間</th><th>スケジュール</th><th>ルート＆詳細</th><th>個別費用</th></tr></thead>
                <tbody>
                    <tr><td>06:30 - 07:15</td><td>🧳 チェックアウト＆空港への格安移動</td><td>「ホテルウェルコ成田」をチェックアウト。成田駅から格安の一般各駅停車で成田空港各ターミナル駅へ直行。</td><td>¥270</td></tr>
                    <tr><td>07:15 - 09:30</td><td>✈️ 搭乗手続き＆安全帰国（09:30発フライト）</td><td>航空会社カウンターでの手荷物預け、出国審査をすませて搭乗ゲートへ。日本を出発し安全に帰国。</td><td>無料</td></tr>
                    <tr style="font-weight: bold;"><td colspan="3" style="text-align: left;">Day 9 個別費用合計</td><td style="text-align: right;">¥270</td></tr>
                </tbody>
            </table>
        </div>
    </div>
    <div class="btn-wrapper"><a href="day8-ja.html" class="btn btn-back">← Day 8 へ戻る</a><a href="index.html" class="btn btn-home">日付選択に戻る</a></div>
</div>
</body>
</html>"""

langs = ["th", "en", "ja"]
for day in range(1, 9):
    for lang in langs:
        filename = f"day{day}-{lang}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(generate_html(day, lang))
        print(f"Generated: {filename}")

for lang in langs:
    filename = f"day9-{lang}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(generate_day9(lang))
    print(f"Generated: {filename}")

print("\n🚀 [SUCCESS] ครบถ้วน 27 ไฟล์ โครงสร้างเป๊ะ ไร้ขยะอาหารรถไฟ จบงานเรียบร้อยครับ!")