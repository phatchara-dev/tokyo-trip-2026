import flet as ft

def main(page: ft.Page):
    # วางองค์ประกอบหน้าเว็บในคอมคุณ Kaito เองเลย
    page.title = "Tokyo Trip Web APP"
    page.bgcolor = "#121212"
    
    # หน้าเว็บดิบ ๆ โชว์เวลานับถอยหลังด่วน
    page.add(
        ft.Text("🇯🇵 TOKYO TRIP 2026", size=30, weight="bold", color="amber"),
        ft.Text("ยินดีต้อนรับสู่หน้าเว็บแอปในเครื่องคุณ Kaito!", size=16),
        ft.Container(
            content=ft.Text("🚀 ส่งข้อมูลเข้า Discord ด่วน", color="white"),
            bgcolor="#5865F2",
            padding=15,
            border_radius=10
        )
    )

# 🌐 ทริคเด็ด: สั่งให้รันเปิดเป็น "หน้าเว็บ" บนบราวเซอร์ ไม่ใช่หน้าต่างโปรแกรม!
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)