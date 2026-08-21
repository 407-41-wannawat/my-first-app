import time
import streamlit as st
st.title("เกมเติมคำศัพท์จับเวลา")
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = "'
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "start" not in st.session_state:
    st.session_state.start = None
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False
@st.dialog("สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    if u_ans1 == "apple":
        st.success("ข้อที่ 1 : ถูกต้อง")
        score += 1
    else:
        st.error(f"ข้อที่ 1 : ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")
    if u_ans2 == "fish":
        st.success("ข้อที่ 2 : ถูกต้อง")
        score += 1
    else:
        st.error(f"ข้อที่ 2 : ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")
    if u_ans3 == "motorcycle":
        st.success("ข้อที่ 3 : ถูกต้อง")
        score += 1
    else:
        st.error(f"ข้อที่ 3 : ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")
    if u_ans4 == "smartphone":
        st.success("ข้อที่ 4 : ถูกต้อง")
        score += 1
    else:
        st.error(f"ข้อที่ 4 ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")
    st.info(f"ได้คะแนนรวม: {score} / 2 คะแนน")
    if score == 4:
        st.success("You Win!!! 🎉")
    else:
        st.error("You Lose!!!! ❌")
st.button("เริ่มเล่นเกม / เริ่มต้นใหม่", on_click=reset_game)
if st.session_state.start is not None and not st.session_state.is_ended:
    time_left = int(30 - (time.time() - st.session_state.start))
    if time_left > 0:
        st.error(f"⏱️ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()
st.divider()
ans1 = st.text_input(
    "ข้อที่ 1 : An A__le a day keeps the doctor away.🍎",
    key="ans1_val"
)
ans2 = st.text_input(
    "ข้อที่ 2 : Cats love to eat f_sh.🐟",
    key="ans2_val"
)
ans3 = st.text_input(
    "ข้อที่ 3 : Two wheel vahicle with engine is ____rcycle",
    key="ans_val"
)
ans4 = st.text_input(
    "ข้อที่ 4 : The thing that can call play a game or watch movie is ____tphone",
    key="ans_val"
)
if st.session_state.start is not None and not st.session_state.is_ended:
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()
    time.sleep(1)
    st.rerun()
if st.session_state.is_ended and st.session_state.start is not None:
    show_result_dialog(st.session_state.ans1_val, st.session_state.ans2_val, st.session_state.ans3_val, st.session_state.ans4_val)
st.divider()
st.write("นายวรรณวัฒน์ โภชกรณ์ ม.4/7 เลขที่ 41")
