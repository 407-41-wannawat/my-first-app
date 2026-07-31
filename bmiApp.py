import streamlit as st

st.markdown("# :red[✅ แอปพลิเคชั่นคำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลนํ้าหนักส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น 🏋️ 🏃 ⚖️ 🩺 ❤️ 🍎 🥗 📏 💧 💪 ️‍🔥")

weight = st.number_input("กรอกนํ้าหนักของคุณ (กิโลกรัม):")
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):")

if st.button("คำนวณค่า BMI"):
   height_m = height_cm / 100
   bmi = weight / (height_m ** 2)

   st.write("---")
   st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")
if bmi < 18.5:
   st.warning("คุณมีนํ้าหนักน้อยกว่าเกณฑ์ (กินข้าวเยอะๆ) ⚠️")
elif 18.5 <= bmi < 23.0:
   st.success("คุณมีนํ้าหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี) 🎉")
elif 23.0 <=bmi < 25.0:
   st.info("คุณเริ่มมีนํ้าหนักเกินเกณฑ์ (เริ่มบวมแล้วนะ) 🚨")
else:
   st.error("คุณอยู่ในเกณฑ์อ้วน ควรเริ่มดูแลสุขภาพ 💪")

st.divider()
st.write("นายวรรณวัฒน์ โภชกรณ์ ม.4/7 เลขที่ 41")
