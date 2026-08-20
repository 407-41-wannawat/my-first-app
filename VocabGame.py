import time
import streamlit as st

# หัวข้อ
st.title("เกมเติมคำศัพท์จับเวลา")

# 1. Default Session State
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "start" not in st.session_state:
    st.session_state.start = None
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False

# 2. ฟังก์ชันเริ่มใหม่/รีเซ็ตเกม
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False

# 3. Dialog แสดงผลการเล่นเกม (ปรับให้รับพารามิเตอร์ครบ 4 ข้อ)
@st.dialog("สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ตรวจข้อที่ 1
    if u_ans1 == "apple":
        st.success("ข้อที่ 1 : ถูกต้อง")
        score += 1
    else:
        st.error(f"ข้อที่ 1 : ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อที่ 2
    if u_ans2 == "fish":
        st.success("ข้อที่ 2 : ถูกต้อง")
        score += 1
    else:
        st.error(f"ข้อที่ 2 : ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ตรวจข้อที่ 3
    if u_ans3 == "rcycle" or u_ans3 == "motorcycle":
        st.success("ข้อที่ 3 : ถูกต้อง")
        score += 1
    else:
        st.error(f"ข้อที่ 3 : ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ตรวจข้อที่ 4 (สมาร์ตโฟน: smar)
    if u_ans4 == "smar" or u_ans4 == "smartphone":
        st.success("ข้อที่ 4 : ถูกต้อง")
        score += 1
    else:
        st.error(f"ข้อที่ 4 : ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    # สรุปคะแนน
    st.info(f"ได้คะแนนรวม: {score} / 4 คะแนน")
    if score >= 3:
        st.success("You Win!!! 🎉")
    else:
        st.error("You Lose!!!! ❌")

# ปุ่มเริ่มเล่น
st.button("เริ่มเล่นเกม / รีเซ็ต", on_click=reset_game)

# 4. ระบบนับถอยหลัง
time_left = 0
if st.session_state.start is not None and not st.session_state.is_ended:
    time_left = int(30 - (time.time() - st.session_state.start))
    if time_left > 0:
        st.error(f"⏱️ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 5. ช่องกรอกคำตอบ (เชื่อมกับ value ใน Session State)
ans1 = st.text_input(
    "ข้อที่ 1 : An A__le a day keeps the doctor away.🍎",
    value=st.session_state.ans1_val,
    disabled=st.session_state.is_ended or st.session_state.start is None
)
ans2 = st.text_input(
    "ข้อที่ 2 : Cats love to eat f_sh.🐟",
    value=st.session_state.ans2_val,
    disabled=st.session_state.is_ended or st.session_state.start is None
)
ans3 = st.text_input(
    "ข้อที่ 3 : The two wheel vehicle with engine is moto___le 🏍️",
    value=st.session_state.ans3_val,
    disabled=st.session_state.is_ended or st.session_state.start is None
)
ans4 = st.text_input(
    "ข้อที่ 4 : Thing that you can call to some people/play a game/watch a video is ____tphone 📱",
    value=st.session_state.ans4_val,
    disabled=st.session_state.is_ended or st.session_state.start is None
)

# อัปเดตค่าใน State
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

# ปุ่มส่งคำตอบ
if st.session_state.start is not None and not st.session_state.is_ended:
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    # รีเฟรชหน้าเพื่ออัปเดตตัวนับเวลาถอยหลัง
    time.sleep(1)
    st.rerun()

# แสดง Dialog สรุปผล
if st.session_state.is_ended and st.session_state.start is not None:
    show_result_dialog(ans1, ans2, ans3, ans4)

st.divider()
