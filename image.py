import os

# ลิงก์ที่ต้องการเปิด (ควรเป็นลิงก์ไฟล์รูปภาพโดยตรงที่ลงท้ายด้วย .jpg, .png ฯลฯ)
url = "https://pin.it/5o2UhR2t4"

# ใช้ termux-open เพื่อสั่งให้ Android เปิด URL นี้ด้วยแอปเริ่มต้น (เช่น Chrome)
os.system(f"termux-open '{url}'")
