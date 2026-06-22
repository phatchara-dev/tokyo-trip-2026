import os

# ข้อมูลแผนการเดินทางแบบละเอียด ยิบ ชั่วโมงต่อชั่วโมง ครบ 3 ภาษา ไร้ขยะอาหารรถไฟวนลูป
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
        "sento_cost": "¥1,000", "transit_cost": "¥1,250", "return_cost": "¥240", "total_cost": "¥2,490",
        "rows_th": """
            <tr><td>07:35 - 09:30</td><td>🛬 Landing นาริตะ & จัดการเอกสาร</td><td>เครื่องแลนดิ้งสู่สนามบินนาริตะ ผ่านกองตรวจคนเข้าเมืองและรับสัมภาระ</td><td>ฟรี</td></tr>
            <tr><td>09:30 - 11:30</td><td>🚃 รถไฟขบวนธรรมดาสายประหยัดเข้าชินจูกุ</td><td>นั่งรถไฟสาย Keisei Main Line (ขบวน Limited Express ธรรมดา) ไปเปลี่ยนสาย JR Yamanote Line ที่สถานี Nippori มุ่งหน้าเข้าสู่ Shinjuku</td><td>¥1,250</td></tr>
            <tr><td>11:30 - 12:30</td><td>🧳 ฝากสัมภาระที่พัก Shinjuku</td><td>เดินทางเท้าเข้าเช็กอินและฝากกระเป๋าเดินทางที่ Hostel Capsule Kuyakushomae Shinjuku</td><td>ฟรี</td></tr>
            <tr><td>12:30 - 14:30</td><td>🏙️ เดินสำรวจผังเมืองย่าน Shinjuku East</td><td>เดินเท้าศึกษาโครงสร้างผังเมือง ทางเข้า-ออกสถานี และสตรีทวิวรอบเขตชินจูกุฝั่งตะวันออก</td><td>ฟรี</td></tr>
            <tr><td>14:30 - 16:30</td><td>⛩️ เยี่ยมชมศาลเจ้า Hanazono Shrine</td><td>เดินเท้าไปยังศาลเจ้าเก่าแก่ใจกลางชินจูกุ ชมสถาปัตยกรรมและพื้นที่สีเขียวที่ซ่อนอยู่กลางเมืองหลวง</td><td>ฟรี</td></tr>
        """,
        "rows_en": """
            <tr><td>07:35 - 09:30</td><td>🛬 Narita Landing & Customs</td><td>Touch down at Narita Airport, clear immigration checkpoints, and collect luggage.</td><td>Free</td></tr>
            <tr><td>09:30 - 11:30</td><td>🚃 Budget Local Rail Commute to Shinjuku</td><td>Take the Keisei Main Line (Local), transfer to the JR Yamanote Line at Nippori Station, heading directly to Shinjuku.</td><td>¥1,250</td></tr>
            <tr><td>11:30 - 12:30</td><td>🧳 Baggage Drop off in Shinjuku</td><td>Walk to Hostel Capsule Kuyakushomae Shinjuku to clear check-in and drop off heavy bags.</td><td>Free</td></tr>
            <tr><td>12:30 - 14:30</td><td>🏙️ Shinjuku East District Layout Walk</td><td>Explore the town layout, street structure, and sub-ways around Eastern Shinjuku grids.</td><td>Free</td></tr>
            <tr><td>14:30 - 16:30</td><td>⛩️ Visit Hanazono Shrine Complex</td><td>Observe the historic Shinto architecture and hidden green sanctuary located in Shinjuku city core.</td><td>Free</td></tr>
        """,
        "rows_ja": """
            <tr><td>07:35 - 09:30</td><td>🛬 成田到着＆入国手続き</td><td>成田空港に着陸し、入国審査の手続きをすませて荷物を受け取る。</td><td>無料</td></tr>
            <tr><td>09:30 - 11:30</td><td>🚃 格安一般列車での新宿移動</td><td>京成本線（一般特急）に乗り、日暮里駅でJR山手線に乗り換えて新宿へ移動。</td><td>¥1,250</td></tr>
            <tr><td>11:30 - 12:30</td><td>🧳 新宿の宿に荷物を預ける</td><td>「ホステルカプセル区役所前新宿」に徒歩で移動し、チェックイン手続きと荷物預け。</td><td>無料</td></tr>
            <tr><td>12:30 - 14:30</td><td>🏙️ 新宿東口エリアの都市構造散策</td><td>新宿駅東口周辺の街路構造、地下道への動線、および街並みを徒歩で偵察。</td><td>無料</td></tr>
            <tr><td>14:30 - 16:30</td><td>⛩️ 花園神社境内の見学</td><td>新宿の中心部に鎮座する歴史ある神社へ。都会の真ん中に隠れた建築と緑の空間を鑑賞。</td><td>無料</td></tr>
        """
    },
    2: {
        "date_th": "วันพุธที่ 29 กรกฎาคม 2026", "date_en": "Wednesday, July 29, 2026", "date_ja": "2026年7月29日(水)",
        "title_th": "จัดทริปยาวลุยเมืองเก่า Kamakura & นั่งขบวนคลาสสิก Enoden เลียบทะเล 🌊",
        "title_en": "Day Trip to Historic Kamakura & Scenic Enoden Coastal Train Ride 🌊",
        "title_ja": "古都鎌倉日帰り観光＆江ノ電ローカル線の海沿い車窓旅 🌊",
        "sento_th": "Mega Sento 2: Spadium Japon (スパジアムジャポン)", "sento_en": "Mega Sento 2: Spadium Japon", "sento_ja": "メガ銭湯 2：スパジアムジャポン",
        "sento_detail_th": "เดินทางด้วยรถไฟและต่อรถบัสท้องถิ่นลู่ตรงสู่เมกะเซ็นโตอันดับหนึ่งที่ใหญ่ที่สุดในโตเกียว บ่อแช่น้ำอลังการกว่า 15 รูปแบบ ทั้งบ่อกลางแจ้งและบ่อไฟฟ้า บรรยากาศคึกคักสูงสุด",
        "sento_detail_en": "Take a local train and free shuttle bus to Tokyo's largest mega sento complex, featuring over 15 dynamic hot spring pools with a lively local crowd.",
        "sento_detail_ja": "一般列車とシャトルバスを乗り継ぎ、東京最大級のメガ銭湯施設へ。15種類もの多彩な大浴場を誇り、非常に活気ある雰囲気。",
        "sento_cost": "¥850", "transit_cost": "ตามจริง", "return_cost": "¥180", "total_cost": "¥1,030",
        "rows_th": """
            <tr><td>08:00 - 09:30</td><td>🚃 นั่งรถไฟ JR Shonan-Shinjuku ลงใต้</td><td>นั่งรถไฟขบวนธรรมดาสาย JR Shonan-Shinjuku ยาวตรงจากสถานีชินจูกุมุ่งหน้าสู่สถานีคามากุระ</td><td>ตามจริง</td></tr>
            <tr><td>09:30 - 11:00</td><td>⛩️ ชมเมืองเก่าและศาลเจ้า Tsurugaoka Hachimangu</td><td>เดินเท้าผ่านถนน Dankazura สู่ศาลเจ้าหลักประจำเมืองเก่าคามากุระ ชมสถาปัตยกรรมดั้งเดิม</td><td>ฟรี</td></tr>
            <tr><td>11:00 - 12:30</td><td>🗿 ไหว้พระใหญ่ Daibutsu แห่งวัด Kotoku-in</td><td>เดินทางด้วยรถไฟ Enoden สายคลาสสิกขบวนสั้น เข้าวัดโกโตคุอินเพื่อชมโครงสร้างพระพุทธรูปทองสัมฤทธิ์ขนาดยักษ์กลางแจ้ง</td><td>ตามจริง</td></tr>
            <tr><td>12:30 - 14:30</td><td>🌊 นั่ง Enoden เลียบหาด & แวะมุมมหาชน Kamakura-Koko-Mae</td><td>นั่งรถไฟเลียบชายฝั่งมหาสมุทรแปซิฟิก แวะถ่ายภาพสตรีทคู่กับจุดตัดทางรถไฟเลียบทะเลชื่อดัง</td><td>ตามจริง</td></tr>
            <tr><td>14:30 - 16:00</td><td>🚃 นั่งรถไฟโลคอลกลับเข้าเขตโตเกียว</td><td>นั่งรถไฟธรรมดาย้อนเส้นทางเดิมกลับเข้าสู่พื้นที่กรุงโตเกียวเพื่อเตรียมมุ่งหน้าไปสปายักษ์</td><td>ตามจริง</td></tr>
        """,
        "rows_en": """
            <tr><td>08:00 - 09:30</td><td>🚃 Commute via JR Shonan-Shinjuku Line</td><td>Board a local commuter train directly from Shinjuku Station down south to Kamakura Station.</td><td>Actual cost</td></tr>
            <tr><td>09:30 - 11:00</td><td>⛩️ Explore Tsurugaoka Hachimangu Shrine</td><td>Walk through Dankazura avenue to reach the prominent Shinto shrine core of ancient Kamakura town.</td><td>Free</td></tr>
            <tr><td>11:00 - 12:30</td><td>🗿 Witness Kamakura Daibutsu (Great Buddha)</td><td>Take the vintage Enoden train grids to Kotoku-in Temple to observe the monumental open-air bronze Buddha structure.</td><td>Actual cost</td></tr>
            <tr><td>12:30 - 14:30</td><td>🌊 Enoden Coastal Ride & Kamakura-Koko-Mae Stop</td><td>Ride the historic rail lines hugging the Pacific oceanfront, stopping at the world-famous coastal crossing grid.</td><td>Actual cost</td></tr>
            <tr><td>14:30 - 16:00</td><td>🚃 Rail Commute Back to Tokyo Area</td><td>Take local rail lines back up to the Tokyo metropolitan boundaries.</td><td>Actual cost</td></tr>
        """,
        "rows_ja": """
            <tr><td>08:00 - 09:30</td><td>🚃 JR湘南新宿ラインで南下</td><td>新宿駅から湘南新宿ラインの一般列車に乗車し、鎌倉駅へ直行移動。</td><td>実費</td></tr>
            <tr><td>09:30 - 11:00</td><td>⛩️ 鶴岡八幡宮参道と境内の散策</td><td>段葛を通り、古都鎌倉を代表する歴史的な八幡宮へ。伝統建築の配置を鑑賞。</td><td>無料</td></tr>
            <tr><td>11:00 - 12:30</td><td>🗿 高徳院の鎌倉大仏を参拝</td><td>レトロな江ノ電車両に乗り換えて高徳院へ。巨大な露天の青銅製大仏造形を視察。</td><td>実費</td></tr>
            <tr><td>12:30 - 14:30</td><td>🌊 江ノ電沿線ロケ＆鎌倉高校前踏切</td><td>太平洋沿いを走るローカル線の車窓を楽しみ、有名な海沿いの鉄道踏切ポイントに立ち寄り。</td><td>実費</td></tr>
            <tr><td>14:30 - 16:00</td><td>🚃 各駅整車で都内へ帰還移動</td><td>一般各駅停車を乗り継ぎ、東京都市圏へ向けて復路移動。</td><td>実費</td></tr>
        """
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
        "sento_cost": "¥1,050", "transit_cost": "ฟรี", "return_cost": "¥240", "total_cost": "¥1,290",
        "rows_th": """
            <tr><td>09:30 - 10:30</td><td>🚃 นั่งรถไฟขบวนธรรมดาเข้าสู่สถานี Tokyo</td><td>นั่งรถไฟสาย JR Chuo Line (ขบวนธรรมดา) ยิงตรงจากที่พักชินจูกุเข้าสู่สถานีโตเกียว</td><td>ฟรี</td></tr>
            <tr><td>10:30 - 12:30</td><td>👑 เดินชมพื้นที่ชั้นนอกพระราชวังอิมพีเรียล</td><td>เดินชมสะพานแว่นตา Nijubashi และโครงสร้างคูเมืองรอบพระราชวังอิมพีเรียลตามเส้นทางผังเมือง</td><td>ฟรี</td></tr>
            <tr><td>12:30 - 14:00</td><td>🏙️ เดินศึกษาสถาปัตยกรรมสถานีรถไฟโตเกียว</td><td>เดินชมตัวอาคารก่ออิฐแดงทรงคลาสสิกฝั่ง Marunouchi และการออกแบบผังสถานีรถไฟขนาดใหญ่</td><td>ฟรี</td></tr>
            <tr><td>14:00 - 16:00</td><td>🌳 เดินเล่นรับลมสวนสาธารณะ Hibiya Park</td><td>เดินเท้าทะลุเข้าสวนสาธารณะสไตล์ตะวันตกแห่งแรกของญี่ปุ่น ชมการจัดสวนสีเขียวและสระน้ำกลางเมือง</td><td>ฟรี</td></tr>
        """,
        "rows_en": """
            <tr><td>09:30 - 10:30</td><td>🚃 Rail Transit to Tokyo Station Core</td><td>Take the JR Chuo Line (Local) straight from Shinjuku station directly to Tokyo Station.</td><td>Free</td></tr>
            <tr><td>10:30 - 12:30</td><td>👑 Walk Tokyo Imperial Palace Outer Grounds</td><td>Observe the landmark Nijubashi Bridge and the massive structural stone walls and moat system.</td><td>Free</td></tr>
            <tr><td>12:30 - 14:00</td><td>🏙️ Architectural Study of Tokyo Station Base</td><td>Examine the iconic red-brick classic station designs around Marunouchi exit grids.</td><td>Free</td></tr>
            <tr><td>14:00 - 16:00</td><td>🌳 Stroll through Hibiya Park Boundaries</td><td>Walk into Japan's first Western-style modern park layout to observe its city center landscape.</td><td>Free</td></tr>
        """,
        "rows_ja": """
            <tr><td>09:30 - 10:30</td><td>🚃 JR中央線快速で東京駅へ</td><td>新宿駅から中央線快速の一般列車に乗り、一気に東京駅エリアへ移動。</td><td>無料</td></tr>
            <tr><td>10:30 - 12:30</td><td>👑 皇居外苑と二重橋の徒歩視察</td><td>有名な二重橋や、広大な濠の石垣構造など、皇居外周の土木遺構を歩いて見学。</td><td>無料</td></tr>
            <tr><td>12:30 - 14:00</td><td>🏙️ 東京駅丸の内赤レンガ駅舎の建築鑑賞</td><td>復原された丸の内側の歴史的赤レンガ駅舎建築と、巨大駅ターミナルの動線設計を観察。</td><td>無料</td></tr>
            <tr><td>14:00 - 16:00</td><td>🌳 日比谷公園のウォーキング</td><td>日本初の近代洋風都市公園へ。噴水広場や都会のオアシスとして機能する景観レイアウトを見学。</td><td>無料</td></tr>
        """
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
        "sento_cost": "¥850", "transit_cost": "ฟรี", "return_cost": "¥180", "total_cost": "¥1,030",
        "rows_th": """
            <tr><td>10:30 - 12:30</td><td>⚡ เดินเล่นสำรวจย่านไอที Akihabara</td><td>นั่งรถไฟธรรมดาไปลงสถานีอากิฮาบาระ เดินสำรวจตึกวิทยุ Radio Kaikan และตรอกขายชิ้นส่วนอิเล็กทรอนิกส์ดั้งเดิม</td><td>ฟรี</td></tr>
            <tr><td>12:30 - 14:00</td><td>🏙️ เดินเท้าสำรวจทางรถไฟยกระดับกิ่ง Ueno</td><td>เดินเท้าจากอากิฮาบาระมุ่งหน้าไปทางอุเอโนะ เลาะตามแนวโครงสร้างเสาตอม่อทางรถไฟยกระดับสายประวัติศาสตร์</td><td>ฟรี</td></tr>
            <tr><td>14:00 - 16:00</td><td>🛍️ ลุยตลาดเปิดโล่ง Ameyoko Market</td><td>เดินรับบรรยากาศความคึกคักใต้ทางรถไฟยกระดับย่านตลาดอาเมโยโกะ ชมผังการค้าและทางเดินที่มีผู้คนหนาแน่น</td><td>ฟรี</td></tr>
        """,
        "rows_en": """
            <tr><td>10:30 - 12:30</td><td>⚡ Walk Akihabara Electronics District</td><td>Take local rail to Akihabara station. Explore Radio Kaikan and the historic electronic parts alleyways.</td><td>Free</td></tr>
            <tr><td>12:30 - 14:00</td><td>🏙️ Urban Track Walk towards Ueno Base</td><td>Walk alongside the historical elevated railway viaduct pillars heading north toward Ueno district.</td><td>Free</td></tr>
            <tr><td>14:00 - 16:00</td><td>🛍️ Experience Ameyoko Open-Air Street Market</td><td>Observe the dynamic open-market structure under the elevated rail tracks packed with shoppers.</td><td>Free</td></tr>
        """,
        "rows_ja": """
            <tr><td>10:30 - 12:30</td><td>⚡ 秋葉原電気街とラジオ会館の巡回</td><td>一般列車で秋葉原駅へ。電気街の電子部品露店街やラジオ会館内の立体店舗レイアウトを視察。</td><td>無料</td></tr>
            <tr><td>12:30 - 14:00</td><td>🏙️ 上野方面への高架橋沿い都市探訪</td><td>秋葉原から上野駅方面へ、歴史ある鉄道高架橋の煉瓦・コンクリート橋脚構造を見ながら徒歩移動。</td><td>無料</td></tr>
            <tr><td>14:00 - 16:00</td><td>🛍️ アメ横商店街の高密度マーケット体感</td><td>高架下に展開するアメ横独特の密集店舗配置と、多くの買い物客で賑わう街路空間を歩行見学。</td><td>無料</td></tr>
        """
    },
    5: {
        "date_th": "วันเสาร์ที่ 1 สิงหาคม 2026", "date_en": "Saturday, August 1, 2026", "date_ja": "2026年8月1日(土)",
        "title_th": "เปิดประสบการณ์นั่ง 'รถไฟห้อยหัว' Chiba Monorail & แช่บ่อคาร์บอเนต Ryusenji 🚄",
        "title_en": "Ride the Chiba Urban Hanging Monorail & Ryusenji no Yu Mega Sento 🚄",
        "title_ja": "千葉モノレール懸垂型車両体験＆郊外型メガスーパー銭湯竜泉寺の湯 🚄",
        "sento_th": "Mega Sento 5: Ryusenji no Yu (竜泉寺の湯)", "sento_en": "Mega Sento 5: Ryusenji no Yu", "sento_ja": "メガ銭湯 5：竜泉寺の湯",
        "sento_detail_th": "เดินทางสู่เมกะเซ็นโตขนาดยักษ์ชื่อดัง เพลิดเพลินกับโซนน้ำแร่ธรรมชาติและบ่อคาร์บอเนตความเข้มข้นสูงยักษ์ บ่อเพียบ คนหนาแน่นคึกคักสะใจสายเซ็นโต",
        "sento_detail_en": "Unwind at a legendary mega sento complex famous for its enormous outdoor bath areas and highly dense carbonated spring grids packed with locals.",
        "sento_detail_ja": "有名メガ銭湯施設へ。広大な大露天風呂や、毎週末大変賑わう名物の高濃度炭酸泉大浴場を満喫。",
        "sento_cost": "¥950", "transit_cost": "ตามจริง", "return_cost": "ตามจริง", "total_cost": "¥950",
        "rows_th": """
            <tr><td>10:00 - 11:30</td><td>🚃 เดินทางข้ามจังหวัดมุ่งหน้าสู่ Chiba</td><td>นั่งรถไฟขบวนธรรมดาโลคอลสายยาว ยิงตรงจากเขตโตเกียวข้ามฝั่งมุ่งสู่ตัวเมืองจังหวัดชิบะ</td><td>ตามจริง</td></tr>
            <tr><td>11:30 - 13:30</td><td>🚟 นั่งรถไฟห้อยหัว Chiba Urban Monorail</td><td>ทดลองนั่งรถไฟรางเดี่ยวแขวนย้อยกลับหัว (Suspended Monorail) ที่ยาวที่สุดในโลก สังเกตระบบสับรางกลางอากาศวิจิตรพิสดาร</td><td>ตามจริง</td></tr>
            <tr><td>13:30 - 14:30</td><td>🏙️ สำรวจโครงสร้างผังเมืองสถานี Chiba</td><td>เดินเท้าสำรวจพื้นที่ยกระดับรอบสถานีรถไฟชิบะ การเชื่อมต่อระบบทางเดินลอยฟ้าเข้าตัวอาคาร</td><td>ฟรี</td></tr>
            <tr><td>14:30 - 16:00</td><td>🚃 นั่งรถไฟย้อนกลับเข้าเขตเมืองโตเกียว</td><td>นั่งรถไฟโลคอลขบวนธรรมดาย้อนเส้นทางรางเพื่อเตรียมเข้าสู่พื้นที่ตั้งของเมกะเซ็นโตวันหยุด</td><td>ตามจริง</td></tr>
        """,
        "rows_en": """
            <tr><td>10:00 - 11:30</td><td>🚃 Commute via Local Rail to Chiba Station</td><td>Board a local commuter train line crossing the prefectural border directly into Chiba City area.</td><td>Actual cost</td></tr>
            <tr><td>11:30 - 13:30</td><td>🚟 Experience the Chiba Hanging Monorail</td><td>Ride the world's longest suspended inverted monorail system. Study its complex mid-air switching rail grid mechanics.</td><td>Actual cost</td></tr>
            <tr><td>13:30 - 14:30</td><td>🏙️ Explore Chiba Station Skywalk Layout</td><td>Walk around Chiba station's modern pedestrian deck layout and multi-level structural connections.</td><td>Free</td></tr>
            <tr><td>14:40 - 16:00</td><td>🚃 Return Rail Commute to Tokyo Bounds</td><td>Take a local rail commuter train back up into the Tokyo metropolitan grid lines.</td><td>Actual cost</td></tr>
        """,
        "rows_ja": """
            <tr><td>10:00 - 11:30</td><td>🚃 一般各駅列車で千葉駅へ移動</td><td>都心から総武線の一般列車などに乗り、県境を越えて千葉県千葉市エリアへ移動。</td><td>実費</td></tr>
            <tr><td>11:30 - 13:30</td><td>🚟 世界最長の懸垂式千葉都市モノレール乗車</td><td>サスペンデッド式モノレール車両に試乗。空中に浮かぶ複雑なポイント軌道切り替えシステムを車内から見学。</td><td>実費</td></tr>
            <tr><td>13:30 - 14:30</td><td>🏙️ 千葉駅周辺のペデストリアンデッキ構造構造散策</td><td>千葉駅ビルの立体的な歩行者用高架デッキ、都市交通網との接続デザインを徒歩観察。</td><td>無料</td></tr>
            <tr><td>14:30 - 16:00</td><td>🚃 各駅停車で東京都内へ帰還</td><td>往路の一般各駅停車を乗り継ぎ、週末の大型銭湯へ向けて東京都圏内へ復路移動。</td><td>実費</td></tr>
        """
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
        "sento_cost": "¥1,260", "transit_cost": "ฟรี", "return_cost": "¥390", "total_cost": "¥1,650",
        "rows_th": """
            <tr><td>10:00 - 11:30</td><td>🌳 ทะลุพื้นที่ป่าขนาดยักษ์ ศาลเจ้าเมจิ (Meiji Jingu)</td><td>นั่งรถไฟสายสั้นไป Harajuku เดินเท้าผ่านแนวประตูโทริอิยักษ์เข้าสู่เขตพื้นที่ป่าปลูกความหนาแน่นสูงอันเงียบสงบ</td><td>ฟรี</td></tr>
            <tr><td>11:30 - 13:00</td><td>🏙️ เดินศึกษาวิศวกรรมโครงสร้างสถานี Harajuku</td><td>เดินชมสถานีฮาราจูกุโฉมใหม่และการจัดการทางเดินเชื่อมลอยฟ้าเพื่อระบายคลื่นฝูงชนวันหยุด</td><td>ฟรี</td></tr>
            <tr><td>13:00 - 14:30</td><td>🏙️ เดินปล่อยใจรับสีสันถนน Takeshita Street</td><td>เดินสังเกตรูปแบบแฟชั่นและการหลั่งไหลของมวลชนบนถนนคนเดินชื่อดังในวันอาทิตย์</td><td>ฟรี</td></tr>
            <tr><td>14:30 - 16:00</td><td>🚃 นั่งรถไฟธรรมดาข้ามเขตมุ่งสู่จังหวัด Saitama</td><td>นั่งรถไฟสายท้องถิ่นขบวนธรรมดายิงยาวขึ้นเหนือข้ามเขตสู่ไซตามะเพื่อไปคาเฟ่สปายักษ์</td><td>ฟรี</td></tr>
        """,
        "rows_en": """
            <tr><td>10:00 - 11:30</td><td>🌳 Walk through Meiji Jingu Sacred Forest Grids</td><td>Take short rail to Harajuku. Pass through giant Torii gates into the high-density quiet man-made forest sanctuary.</td><td>Free</td></tr>
            <tr><td>11:30 - 13:00</td><td>🏙️ Technical Study of Harajuku Station Redesign</td><td>Examine the modern glass-layout architecture and crowd control flow management of Harajuku hub.</td><td>Free</td></tr>
            <tr><td>13:00 - 14:30</td><td>🏙️ Walk the Vivid Lanes of Takeshita Street</td><td>Observe the weekend youth fashion layout and high-density pedestrian flow on the street tracks.</td><td>Free</td></tr>
            <tr><td>14:30 - 16:00</td><td>🚃 Rail Commute Northbound into Saitama Prefecture</td><td>Take local rail commuter lines directly up north into Saitama region for the modern mega lounge.</td><td>Free</td></tr>
        """,
        "rows_ja": """
            <tr><td>10:00 - 11:30</td><td>🌳 明治神宮の広大な人工林と大鳥居の見学</td><td>格安列車で原宿駅へ。巨木が密集する深い社叢の参道を歩き、大鳥居や社殿の配置を視察。</td><td>無料</td></tr>
            <tr><td>11:30 - 13:00</td><td>🏙️ 新駅舎化された原宿駅の土木デザイン研究</td><td>リニューアルされたモダンなガラス張りの原宿駅舎の設計、および明治神宮側への歩行者流動制御を観察。</td><td>無料</td></tr>
            <tr><td>13:00 - 14:30</td><td>🏙️ 日曜日の竹下通り高密度流動の観察</td><td>週末の若者文化の発信地へ。密集するアパレル店舗配置と、歩行者天国における大混雑流動を体感。</td><td>無料</td></tr>
            <tr><td>14:30 - 16:00</td><td>🚃 一般各駅列車で北上、埼玉県エリアへ</td><td>一般ローカル各駅停車を乗り継ぎ、荒川を渡って埼玉県の温浴ラウンジ施設へ向けて北上移動。</td><td>無料</td></tr>
        """
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
        "sento_cost": "¥1,100", "transit_cost": "ฟรี", "return_cost": "¥220", "total_cost": "¥1,320",
        "rows_th": """
            <tr><td>10:00 - 12:00</td><td>🛌 พักผ่อนนอนหลับเต็มคราบในที่พัก Shinjuku</td><td>ตื่นสายนอนพักผ่อนชาร์จแบตร่างกายเต็มที่ในโฮสเทล เพื่อเคลียร์อาการล้าสะสมจากการเดินทริปยาว</td><td>ฟรี</td></tr>
            <tr><td>12:00 - 14:00</td><td>🏙️ เดินชิลชมผังเมืองฝั่ง Shinjuku West Skyscrapers</td><td>เดินออกกำลังกายย่อยอาหารรอบเขตตึกระฟ้าและอาคารราชการโตเกียว (TMG) ฝั่งตะวันตก</td><td>ฟรี</td></tr>
            <tr><td>14:00 - 15:30</td><td>🚃 นั่งรถไฟโลคอลมุ่งหน้าสู่เขตบ่อน้ำแร่ยอดฮิต</td><td>นั่งรถไฟสายท้องถิ่นขบวนธรรมดาเพื่อเคลื่อนตัวไปยังพื้นที่ออนเซ็นสวนญี่ปุ่นโบราณ</td><td>ฟรี</td></tr>
        """,
        "rows_en": """
            <tr><td>10:00 - 12:00</td><td>🛌 Slow Rest and Sleep Inside Shinjuku Bed</td><td>Sleep in and recharge fully inside the hostel capsules to dump out all accumulated physical fatigue.</td><td>Free</td></tr>
            <tr><td>12:00 - 14:00</td><td>🏙️ Stroll through Shinjuku West Skyscrapers</td><td>Observe the urban block structure and scale of the giant office towers and Tokyo Metropolitan Government buildings.</td><td>Free</td></tr>
            <tr><td>14:00 - 15:30</td><td>🚃 Local Rail Transit to Top Hot Spring Site</td><td>Board local commuter train lines toward the authentic traditional hot spring park coordinates.</td><td>Free</td></tr>
        """,
        "rows_ja": """
            <tr><td>10:00 - 12:00</td><td>🛌 新宿のカプセルベッドでのんびり朝寝坊</td><td>午前中はホステル内でゆっくり朝寝坊。連日の歩行による脳と身体の疲労を完全リセット。</td><td>無料</td></tr>
            <tr><td>12:00 - 14:00</td><td>🏙️ 新宿西口超高層ビル街の都市グリッド散策</td><td>東京都庁舎をはじめとする西口の巨大超高層オフィスビル群の配置レイアウト、二層構造の街路設計を徒歩視察。</td><td>無料</td></tr>
            <tr><td>14:00 - 15:30</td><td>🚃 一般各駅列車で超人気都内天然温泉へ移動</td><td>一般各駅停車に乗り、都内屈指の名湯と言われる本格日本庭園露天風呂に向けてゆったり移動。</td><td>無料</td></tr>
        """
    },
    8: {
        "date_th": "วันอังคารที่ 4 สิงหาคม 2026", "date_en": "Tuesday, August 4, 2026", "date_ja": "2026年8月4日(火)",
        "title_th": "ย้ายค่ายฐานที่มั่นสู่ฝั่งเมือง Narita & ส่งท้ายเมกะเซ็นโตบ่อยักษ์ Hana no Yu 🧳",
        "title_en": "Base Relocation to Narita & Grand Finale at Hana no Yu Mega Sento 🧳",
        "title_ja": "成田への拠点移動＆成田温泉華の湯で旅の締めくくり 🧳",
        "sento_th": "Mega Sento 8: Hana no Yu Narita (成田温泉 華ของ湯)", "sento_en": "Mega Sento 8: Hana no Yu Narita", "sento_ja": "メガ銭湯 8：華の湯 成田",
        "sento_detail_th": "ส่งท้ายค่ำคืนสุดท้ายด้วยการเดินเท้าไปเมกะเซ็นโตขนาดยักษ์ที่ใหญ่ที่สุดในนาริตะ เพลิดเพลินกับบ่อแช่น้ำกลางแจ้ง บ่อคาร์บอเนต บ่อสมุนไพรรวมกว่า 10 รูปแบบ บรรยากาศโลคอลแน่นคึกคักสุดฟิน",
        "sento_detail_en": "Walk to Narita's premier large-scale super sento complex. Experience over 10 varieties of outdoor, carbonated, and herb baths with a highly packed local attendance.",
        "sento_detail_ja": "徒歩で成田最大級の大型スーパー銭湯へ移動。10種類以上の広々とした露天風呂、大炭酸泉、ハーブ湯などを多数の地元客とともに存分に堪能。",
        "sento_cost": "¥900", "transit_cost": "¥1,140", "return_cost": "ฟรี", "total_cost": "¥2,040",
        "rows_th": """
            <tr><td>10:00 - 11:00</td><td>🧳 แพ็กสัมภาระ & เช็กเอาต์ Shinjuku</td><td>จัดการรวบรวมอุปกรณ์ไอทีและเสื้อผ้า เช็กเอาต์อำลาที่พักแคปซูลชินจูกุ</td><td>ฟรี</td></tr>
            <tr><td>11:00 - 13:00</td><td>🚃 นั่งรถไฟขบวนประหยัดข้ามเมืองยาวสู่ย่าน Narita</td><td>นั่งรถไฟธรรมดาสายประหยัดเลาะตามเส้นทางผังเมือง ย้ายฐานทัพจากใจกลางโตเกียวลู่ตรงสู่เขตเมืองนาริตะ</td><td>¥1,140</td></tr>
            <tr><td>13:00 - 14:00</td><td>🧳 เช็กอินฝากกระเป๋า Hotel Welco Narita</td><td>เดินเท้าเข้าเช็กอินฝากกระเป๋าเดินทางที่โรงแรมคืนสุดท้ายเพื่อเตรียมตัวสำหรับเที่ยวบินขากลับ</td><td>ฟรี</td></tr>
            <tr><td>14:00 - 16:00</td><td>🏙️ เดินศึกษาผังเมืองและบรรยากาศรอบพื้นที่ Narita</td><td>เดินปล่อยอารมณ์ชมผังการจราจรและความสงบเงียบเรียบง่ายรอบสถานีรถไฟนาริตะโลคอล</td><td>ฟรี</td></tr>
        """,
        "rows_en": """
            <tr><td>10:00 - 11:00</td><td>🧳 Pack Gear and Checkout from Shinjuku</td><td>Gather all tech gadgets and utilities, clearing out checkout protocols at Shinjuku capsule.</td><td>Free</td></tr>
            <tr><td>11:00 - 13:00</td><td>🚃 Budget Local Rail Commute Out to Narita</td><td>Take cheap local rail lines directly out of central Tokyo boundaries down to the quiet Narita city area.</td><td>¥1,140</td></tr>
            <tr><td>13:00 - 14:00</td><td>🧳 Hotel Welco Narita Baggage Drop</td><td>Check in and store heavy luggage inside the final night hotel base near Narita station tracks.</td><td>Free</td></tr>
            <tr><td>14:00 - 16:00</td><td>🏙️ Observe Narita Town Layout and Architecture</td><td>Walk through the calm local grids to study the quiet countryside transportation and infrastructure designs.</td><td>Free</td></tr>
        """,
        "rows_ja": """
            <tr><td>10:00 - 11:00</td><td>🧳 荷物整理＆新宿の宿をチェックアウト</td><td>ガジェット類や衣服をパッキングし、長年滞在した新宿のカプセルホテルを退出。</td><td>無料</td></tr>
            <tr><td>11:00 - 13:00</td><td>🚃 格安の一般列車を乗り継いで成田市内へ長距離移動</td><td>都心エリアに別れを告げ、経済的なローカル各駅停車を乗り継いで成田駅エリアへ移動。</td><td>¥1,140</td></tr>
            <tr><td>13:00 - 14:00</td><td>🧳 ホテルウェルコ成田に荷物預け・チェックイン</td><td>成田駅近くの最終泊ホテルへ徒歩移動。重い荷物を預けて帰国便前夜の防衛拠点を構築。</td><td>無料</td></tr>
            <tr><td>14:00 - 16:00</td><td>🏙️ 成田駅周辺の静かな地方都市構造の散策</td><td>都心の喧騒から離れた成田駅周辺の落ち着いた街路設計、地方のローカル都市交通網を歩行見学。</td><td>無料</td></tr>
        """
    }
}

def generate_html(day, lang):
    d = trip_data.get(day)
    header_title = "🚇 Tokyo Unseen & Mega Sento Speed Trip 2026 🏮"
    
    if lang == "th":
        title_tag = f"Day {day}: Tokyo Mega Sento Trip 2026"
        th_header, act_header, route_header, cost_header = "เวลา", "กิจกรรม", "การเดินทาง & รายละเอียด", "ค่าใช้จ่ายแยก"
        total_lbl, back_lbl, home_lbl, next_lbl = f"รวมค่าใช้จ่ายแยกของ Day {day}", "← ย้อนกลับ Day", "กลับหน้าเลือกวัน", "ไปยัง Day"
        ret_txt = d['return_cost'] if isinstance(d['return_cost'], str) else f"¥{d['return_cost']}"
        sento_title, sento_desc, sento_c = d['sento_th'], d['sento_detail_th'], d['sento_cost']
        date_str, title_str = d['date_th'], d['title_th']
        ret_title = "กลับเข้าที่พัก"
        ret_desc = "เดินทางด้วยรถไฟขบวนธรรมดาสายประหยัดกลับสู่ที่พักเพื่อพักผ่อนนอนหลับ"
    elif lang == "en":
        title_tag = f"Day {day}: Tokyo Mega Sento Trip 2026"
        th_header, act_header, route_header, cost_header = "Time", "Activity", "Route & Details", "Cost"
        total_lbl, back_lbl, home_lbl, next_lbl = f"Total Cost for Day {day}", "← Back to Day", "Select Day", "Go to Day"
        ret_txt = d['return_cost'] if isinstance(d['return_cost'], str) else f"¥{d['return_cost']}"
        sento_title, sento_desc, sento_c = d['sento_en'], d['sento_detail_en'], d['sento_cost']
        date_str, title_str = d['date_en'], d['title_en']
        ret_title = "Return to Accommodation"
        ret_desc = "Hop on a budget local train line back to your accommodation to sleep."
    else: # ja
        title_tag = f"Day {day}: Tokyo Mega Sento Trip 2026"
        th_header, act_header, route_header, cost_header = "時間", "スケジュール", "ルート＆詳細", "個別費用"
        total_lbl, back_lbl, home_lbl, next_lbl = f"Day {day} 個別費用合計", "← Day 前に戻る", "日付選択に戻る", "Day へ進む →"
        ret_txt = "実費" if d['return_cost'] == "ตามจริง" else "無料" if d['return_cost'] == "ฟรี" else d['return_cost']
        sento_title, sento_desc, sento_c = d['sento_ja'], d['sento_detail_ja'], d['sento_cost']
        date_str, title_str = d['date_ja'], d['title_ja']
        ret_title = "ホテルへ帰還"
        ret_desc = "格安の一般列車でホテルに帰り、ゆっくり休む。"

    rows = d[f'rows_{lang}']
    full_rows = rows + f"""
        <tr class="highlight-pass"><td>16:30 - 19:30</td><td>♨️ {sento_title}</td><td>{sento_desc}</td><td>{sento_c}</td></tr>
        <tr><td>19:30 - 21:00</td><td>💤 {ret_title}</td><td>{ret_desc}</td><td>{ret_txt}</td></tr>
    """

    btn_back = f'<a href="day{day-1}-{lang}.html" class="btn btn-back">{back_lbl} {day-1}</a>' if day > 1 else ''
    btn_next = f'<a href="day{day+1}-{lang}.html" class="btn btn-next">{next_lbl} {day+1} →</a>' if day < 8 else f'<a href="day9-{lang}.html" class="btn btn-next">{next_lbl} 9 →</a>'

    return f"""<!DOCTYPE html>
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
                    {full_rows}
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

def generate_day9(lang):
    if lang == "th":
        return """<!DOCTYPE html>
<html lang="th"><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="UTF-8"><title>Day 9: Tokyo Mega Sento Trip 2026</title><link rel="stylesheet" href="style.css?v=10"></head><body><div class="container"><div class="lang-switcher"><a href="day9-th.html" style="background: #d4af37; color: #252a36 !important;">TH</a> | <a href="day9-en.html">EN</a> | <a href="day9-ja.html">JP</a></div><div class="header">🚇 Tokyo Unseen & Mega Sento Speed Trip 2026 🏮</div><div class="day-section"><div class="day-title">🗓️ Day 9: วันพุธที่ 5 สิงหาคม 2026 | เดินทางจากที่พักนาริตะ เข้าสนามบิน บอร์ดดิ้งกลับบ้านโดยสวัสดิภาพ ✈️</div><div class="table-wrapper"><table class="activity-table"><thead><tr><th>เวลา</th><th>กิจกรรม</th><th>การเดินทาง & รายละเอียด</th><th>ค่าใช้จ่ายแยก</th></tr></thead><tbody><tr><td>06:30 - 07:15</td><td>🧳 เช็กเอาต์ที่พัก & เดินทางเข้าสนามบินนาริตะ</td><td>เช็กเอาต์จาก Hotel Welco Narita นั่งรถไฟขบวนธรรมดาสายสั้นลู่ตรงจากสถานี Narita มุ่งหน้าสู่สถานี Airport Terminal สนามบินนาริตะ</td><td>¥270</td></tr><tr><td>07:15 - 09:30</td><td>✈️ ผ่านด่านตรวจคนเข้าเมือง & บอร์ดดิ้งไฟลท์ 09:30 น.</td><td>จัดการเช็กอินโหลดสัมภาระ ผ่านกองตรวจคนเข้าเมือง และเตรียมตัวขึ้นเครื่องบินเดินทางกลับโดยสวัสดิภาพ</td><td>ฟรี</td></tr><tr style="font-weight: bold;"><td colspan="3">รวมค่าใช้จ่ายแยกของ Day 9</td><td style="text-align: right;">¥270</td></tr></tbody></table></div></div><div class="btn-wrapper"><a href="day8-th.html" class="btn btn-back">← ย้อนกลับ Day 8</a><a href="index.html" class="btn btn-home">กลับหน้าเลือกวัน</a></div></div></body></html>"""
    elif lang == "en":
        return """<!DOCTYPE html>
<html lang="en"><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="UTF-8"><title>Day 9: Tokyo Mega Sento Trip 2026</title><link rel="stylesheet" href="style.css?v=10"></head><body><div class="container"><div class="lang-switcher"><a href="day9-th.html">TH</a> | <a href="day9-en.html" style="background: #d4af37; color: #252a36 !important;">EN</a> | <a href="day9-ja.html">JP</a></div><div class="header">🚇 Tokyo Unseen & Mega Sento Speed Trip 2026 🏮</div><div class="day-section"><div class="day-title">🗓️ Day 9: Wednesday, August 5, 2026 | Narita Check-out, Terminal Commute & Safe Flight Home ✈️</div><div class="table-wrapper"><table class="activity-table"><thead><tr><th>Time</th><th>Activity</th><th>Route & Details</th><th>Cost</th></tr></thead><tbody><tr><td>06:30 - 07:15</td><td>🧳 Hotel Checkout & Airport Transit</td><td>Check out from Hotel Welco Narita. Take a cheap short local rail ride from Narita Station to Narita Airport Terminal Station.</td><td>¥270</td></tr><tr><td>07:15 - 09:30</td><td>✈️ Customs Clearance & 09:30 AM Boarding</td><td>Complete baggage drop, clear immigration checkpoints, and proceed to the gate for departure flight back home.</td><td>Free</td></tr><tr style="font-weight: bold;"><td colspan="3">Total Cost for Day 9</td><td style="text-align: right;">¥270</td></tr></tbody></table></div></div><div class="btn-wrapper"><a href="day8-en.html" class="btn btn-back">← Back to Day 8</a><a href="index.html" class="btn btn-home">Select Day</a></div></div></body></html>"""
    else:
        return """<!DOCTYPE html>
<html lang="ja"><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="UTF-8"><title>Day 9: Tokyo Mega Sento Trip 2026</title><link rel="stylesheet" href="style.css?v=10"></head><body><div class="container"><div class="lang-switcher"><a href="day9-th.html">TH</a> | <a href="day9-en.html">EN</a> | <a href="day9-ja.html" style="background: #d4af37; color: #252a36 !important;">JP</a></div><div class="header">🚇 Tokyo Unseen & Mega Sento Speed Trip 2026 🏮</div><div class="day-section"><div class="day-title">🗓️ Day 9: 2026年8月5日(水) | 成田の宿出発、成田空港への移動＆安全帰国 ✈️</div><div class="table-wrapper"><table class="activity-table"><thead><tr><th>時間</th><th>スケジュール</th><th>ルート＆詳細</th><th>個別費用</th></tr></thead><tbody><tr><td>06:30 - 07:15</td><td>🧳 チェックアウト＆空港への格安移動</td><td>「ホテルウェルコ成田」をチェックアウト。成田駅から格安の一般各駅停車で成田空港各ターミナル駅へ直行。</td><td>¥270</td></tr><tr><td>07:15 - 09:30</td><td>✈️ 搭乗手続き＆安全帰国（09:30発フライト）</td><td>航空会社カウンターでの手荷物預け、出国審査をすませて搭乗ゲートへ。日本を出発し安全に帰国。</td><td>無料</td></tr><tr style="font-weight: bold;"><td colspan="3">Day 9 個別費用合計</td><td style="text-align: right;">¥270</td></tr></tbody></table></div></div><div class="btn-wrapper"><a href="day8-ja.html" class="btn btn-back">← Day 8 へ戻る</a><a href="index.html" class="btn btn-home">日付選択に戻る</a></div></div></body></html>"""

langs = ["th", "en", "ja"]
for day in range(1, 9):
    for lang in langs:
        filename = f"day{day}-{lang if lang!='ja' else 'ja'}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(generate_html(day, lang))
        print(f"Generated: {filename}")

for lang in langs:
    filename = f"day9-{lang if lang!='ja' else 'ja'}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(generate_day9(lang))
    print(f"Generated: {filename}")

print("\n🚀 [SUCCESS] ครบถ้วน 27 ไฟล์ โครงสร้างละเอียดชั่วโมงต่อชั่วโมง ไร้บั๊กคีย์ตัวแปร ผูกงานเนี๊ยบแล้วมึง!")