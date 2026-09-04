import tkinter as tk

# 1. สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("ตัวอย่างปุ่มตัวเลือก")
root.geometry("300x200")

# 2. สร้างตัวแปรสำหรับเก็บค่าที่ผู้ใช้เลือก (กำหนดเป็นแบบ String)
selected_flavor = tk.StringVar()
selected_flavor.set("ช็อกโกแลต")  # ตั้งค่าเริ่มต้นให้เลือกเมนูนี้ไว้ก่อน

# ฟังก์ชันแสดงผลเมื่อคลิกปุ่มตรวจคำตอบ
def show_choice():
    label_result.config(text=f"คุณเลือกรส: {selected_flavor.get()}")

# 3. สร้าง Radiobutton (ปุ่มตัวเลือก)
# เชื่อมปุ่มทั้งหมดเข้าด้วยกันโดยใช้ variable=selected_flavor
radio1 = tk.Radiobutton(root, text="รสช็อกโกแลต", variable=selected_flavor, value="ช็อกโกแลต")
radio1.pack(anchor=tk.W, padx=20, pady=5)

radio2 = tk.Radiobutton(root, text="รสวานิลลา", variable=selected_flavor, value="วานิลลา")
radio2.pack(anchor=tk.W, padx=20, pady=5)

radio3 = tk.Radiobutton(root, text="รสสตรอว์เบอร์รี", variable=selected_flavor, value="สตรอว์เบอร์รี")
radio3.pack(anchor=tk.W, padx=20, pady=5)

# 4. ปุ่มกดเพื่อยืนยันการเลือก
btn = tk.Button(root, text="ยืนยัน", command=show_choice)
btn.pack(pady=10)

# 5. ป้ายกำกับแสดงผลลัพธ์
label_result = tk.Label(root, text="โปรดเลือกรสชาติที่ต้องการ")
label_result.pack(pady=10)

# เริ่มต้นทำงานโปรแกรม
root.mainloop()
