import os
import requests

# 1. URL ของรูปภาพที่ต้องการ
image_url = "https://www.google.com/search?client=ms-android-samsung-ss&hs=bULV&sca_esv=a82350b6429375af&sxsrf=ANbL-n652MMjKbDXJHsoXZlxsZFoRR6_ZQ:1780539126158&udm=2&fbs=ADc_l-Zeyn16Si0Z162u24RYqfSJjJMNM6H_rRJHezH8H4yuHrLHXWM9R0GcvzxUqqy04rDuGOTwjvMAh9bIaCjpCGWwpRipS7s0GtuGwHKidx7pRa1p34Neh2n29dm0l9m1MQ7I9aQlh69UJ4wYrWFBONo0ReCjNO9486iUUtijEETC-zg5mbsAy3s65FucTkJkxADF6YE7hTHbqclURpMh3OM8OeiwY79WqmVPhcW6XxKao6v-0R0qb396Qb0SqAVNKCpX8DcMo9cDFrKrDjcYliG_UmVISQ&q=%E0%B8%A3%E0%B8%B9%E0%B8%9B+%E0%B8%A5%E0%B8%B4%E0%B8%87+%E0%B8%99%E0%B8%B4%E0%B9%89%E0%B8%A7+%E0%B8%81%E0%B8%A5%E0%B8%B2%E0%B8%87&sa=X&sqi=2&ved=2ahUKEwiM_P2QweyUAxVkRWcHHRz0CRwQtKgLegQIDxAB&biw=384&bih=726&dpr=1.88#sv=CAMSVxoyKhBlLWJCZUIwUVV0cV9GQ0dNMg5iQmVCMFFVdHFfRkNHTToOMkdxanpwS0E4MTRiZU0gBCoXCgFzEhBlLWJCZUIwUVV0cV9GQ0dNGAEwAUoECAEQAhgHIInO6bADSggQAhgBIAIoAQ"
# 2. ชื่อไฟล์ที่จะเซฟลงเครื่อง
file_name = "downloaded_image.jpg"

print("กำลังดาวน์โหลดรูปภาพ...")

# ดาวน์โหลดไฟล์
response = requests.get(image_url)

if response.status_code == 200:
    # บันทึกไฟล์ลงเครื่อง
    with open(file_name, 'wb') as f:
        f.write(response.content)
    
    print(f"ดาวน์โหลดสำเร็จ! กำลังเปิด: {file_name}")
    
    # เปิดรูปด้วย termux-open
    os.system(f"termux-open {file_name}")
else:
    print(f"ดาวน์โหลดไม่สำเร็จ! Error code: {response.status_code}")
