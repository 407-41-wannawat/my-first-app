import time
import streamlit as st

# Title
st.title("เกมเติมคำศัพท์จับเวลา")

# Default Session State
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "start" not in st.session_state:
    st.session_state.start = None
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False
# Clear Value Button
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False
# Message Box
@st.dialog("สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):
    st.balloons()
    score = 0
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
# Check 1st Ans.
    if u_ans1 == "apple":
        st.success("ข้อที่ 1 : ถูกต้อง")
        score += 1
    else:
        st.error(f"ข้อที่ 1 : ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")
# Check 2nd Ans.
    if u_ans2 == "fish":
        st.success("ข้อที่ 2 : ถูกต้อง")
        score += 1
    else:
        st.error(f"ข้อที่ 2 : ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")
# Summarize
    st.info(f"ได้คะแนนรวม: {score} / 2 คะแนน")
    if score == 2:
        st.success("You Win!!! 🎉")
    else:
        st.error("You Lose!!!! ❌")
# Play Button
st.button("เริ่มเล่นเกม / เริ่มต้นใหม่", on_click=reset_game)
# Countdown Bar
time_left = 0
if st.session_state.start is not None and not st.session_state.is_ended:
    time_left = int(30 - (time.time() - st.session_state.start))
    if time_left > 0:
        st.error(f"⏱️ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()
st.divider()
# Answer Box
ans1 = st.text_input(
    "ข้อที่ 1 : An A__le a day keeps the doctor away.🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อที่ 2 : Cats love to eat f_sh.🐟",
    value=st.session_state.ans2_val,
)
# Update Latest State
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
# Send Button
if st.session_state.start is not None and not st.session_state.is_ended:
    if st.button("📥 ส่งคำตอบ"):
       st.session_state.is_ended = True
       st.rerun()
# Page Refresh
    time.sleep(1)
    st.rerun()
# Show the dialog
if st.session_state.is_ended and st.session_state.start is not None:
   show_result_dialog(ans1, ans2)
st.divider()
st.write("นายวรรณวัฒน์ โภชกรณ์")
