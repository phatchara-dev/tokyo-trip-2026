import requests
from fastapi import FastAPI
from datetime import datetime
import zoneinfo  # 🎌 ไลบรารีสำหรับล็อคโซนเวลา
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1518569159636553869/DK5HwszET1DjeoKKULYyKvVRNexnLrU9svPhyfjbg3ZHRs1wE-2Us5GfxY3uo8h2iodW"

def send_discord_alert(time_slot, activity, details, expense):
    payload = {
        "embeds": [
            {
                "title": f"⏰ กำหนดการ (เวลาญี่ปุ่น): {time_slot} น.",
                "description": f"**{activity}**",
                "color": 13938487, 
                "fields": [
                    {"name": "📍 รายละเอียด/เส้นทาง", "value": details, "inline": False},
                    {"name": "💰 ค่าใช้จ่าย", "value": expense, "inline": True}
                ],
                "footer": {"text": "Tokyo Smart Assistant Live Engine (JST Zone) 🌌"}
            }
        ]
    }
    requests.post(DISCORD_WEBHOOK_URL, json=payload)

def check_trip_schedule():
    """ฟังก์ชันทำงานเบื้องหลัง ล็อคเวลาประเทศญี่ปุ่นเป๊ะ ๆ 100%"""
    tokyo_tz = zoneinfo.ZoneInfo("Asia/Tokyo")
    now_tokyo = datetime.now(tokyo_tz).strftime("%H:%M")
    
    print(f"🎌 ระบบกำลังเฝ้าเวลา... เวลาปัจจุบันที่ญี่ปุ่นคือ: {now_tokyo}")
    
    # 🕒 ทดสอบลอจิกเวลา: ตอนนี้เวลาญี่ปุ่นคือเท่าไหร่ ให้เปลี่ยนเลขด้านล่างนี้ให้ตรง (หรือบวกไป 1 นาที) เพื่อทดสอบยิงอัตโนมัติครับ
    if now_tokyo == "20:38":  
        send_discord_alert(
            time_slot="21:40", 
            activity="♨️ แช่น้ำแร่ธรรมชาติ Jindaiji Onsen", 
            details="ทดสอบระบบดักเวลาโซนญี่ปุ่นสำเร็จแล้วครับคุณ Kaito!", 
            expense="¥1,000"
        )

# ⚙️ สั่งให้นาฬิกาปลุกทำงานเบื้องหลัง รันเช็กเวลาทุก 1 นาที
scheduler = BackgroundScheduler()
scheduler.add_job(check_trip_schedule, 'interval', minutes=1)
scheduler.start()

@app.get("/")
def home():
    return {"status": "Online", "zone": "Asia/Tokyo"}

# 🚀 3 บรรทัดสุดท้ายที่เติมเพื่อสั่งสตาร์ทเครื่องยนต์ห้ามดับ
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)