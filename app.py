import requests
from fastapi import FastAPI
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()

# 🔑 ใส่ลิงก์ Webhook URL ของคุณ Kaito ตรงนี้ครับ
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1518569159636553869/DK5HwszET1DjeoKKULYyKvVRNexnLrU9svPhyfjbg3ZHRs1wE-2Us5GfxY3uo8h2iodW"

def send_discord_alert(time_slot, activity, details, expense):
    payload = {
        "embeds": [
            {
                "title": f"⏰ กำหนดการ: {time_slot} น.",
                "description": f"**{activity}**",
                "color": 13938487, 
                "fields": [
                    {"name": "📍 รายละเอียด/เส้นทาง", "value": details, "inline": False},
                    {"name": "💰 ค่าใช้จ่าย", "value": expense, "inline": True}
                ],
                "footer": {"text": "Tokyo Smart Assistant Cloud Engine 🌌"}
            }
        ]
    }
    requests.post(DISCORD_WEBHOOK_URL, json=payload)

def check_trip_schedule():
    """ฟังก์ชันเช็กเวลาที่จะทำงานอัตโนมัติบน Cloud ทุก ๆ 1 นาที"""
    now = datetime.now().strftime("%H:%M")
    print(f"🕒 Cloud Server กำลังตรวจเวลา... เวลาปัจจุบัน: {now}")
    
    # 🕒 ใส่ตารางเวลาทริปโตเกียวของคุณ Kaito ได้ยาว ๆ ตรงนี้เลยครับ
    if now == "09:00":
        send_discord_alert("09:00 - 11:00", "🌲 Meguro Sky Park", "สวนลอยฟ้าไฮเวย์ความสูง 35 เมตร", "¥200")
    elif now == "17:30":
        send_discord_alert("17:30 - 19:30", "♨️ Jindaiji Onsen Yumorino-sato", "แช่น้ำแร่ธรรมชาติบ่อน้ำดำชื่อดัง", "¥1,000")

# ⚙️ สั่งให้อาจารย์นาฬิกาปลุกทำงานเบื้องหลัง รันเช็กเวลาทุก 1 นาที
scheduler = BackgroundScheduler()
scheduler.add_job(check_trip_schedule, 'interval', minutes=1)
scheduler.start()

@app.get("/")
def home():
    return {"status": "Online", "message": "ระบบแจ้งเตือนทริปโตเกียว 2026 ของคุณ Kaito บน Cloud พร้อมทำงาน 24 ชม. แล้วครับ!"}