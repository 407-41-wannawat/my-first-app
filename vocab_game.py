import time
import streamlit as st
# ส่วนหัวข้อ
st.title("เกมเติมคำศัพท์จับเวลา")
# Default Session State
if "ans1_val" not in st.session_state:
   st.session_state.ans1_val=""
if "ans2_val" not in st.session_state:
   st.session_state.ans2_val=""
if "ans3_val" not in st.session_state:
   st.session_state.ans3_val=""
if "ans4_val" not in st.session_state:
   st.session_state.ans4_val=""
# Clear Value Button
def reset_game():
   st.session_state.ans1_val = "" # Box 1
   st.session_state.ans2_val = "" # Box 2
   st.session_state.ans3_val = "" # Box 3
   st.session_state.ans4_val = "" # Box 4
   st.session_state.start = time.time() # Restart Clock
   st.session_state.is_ended = False # Close Dialog
# Message Box
st.dialog("สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):
   st.balloons()
   score = 0
   u_ans1 = ans1.strip().lower()
   u_ans2 = ans2.strip().lower()
   u_ans3 = ans3.strip().lower()
   u_ans4 = ans4.strip().lower()
# Check 1st Ans.
if u_ans1 == "apple":
   st.success("ข้อที่ 1 : ถูกต้อง")
   score += 1
else:
   st.error(f"ข้อที่ 1 : ยังไม่ถูกต้อง(คุณตอบ '{u_ans1}')")
# Check 2nd Ans.
if u_ans2 == "fish":
   st.success("ข้อที่ 2 ถูกต้อง")
   score += 1
else:
   st.error(f"ข้อที่ 2 : ยังไม่ถูกต้อง(คุณตอบ '{u_ans1}')")
# Check 3rd Ans.
if u_ans3 == "motocycle":
   st.success("ข้อที่ 3 ถูกต้อง")
   score += 1
else:
   st.error (f"ข้อที่ 3 : ยังไม่ถูกต้อง(คุณตอบ '{u_ans1}')")
# Check 4th Ans.
if u_ans4 == "":
   st.success("ข้อที่ 4 ถูกต้อง")
   score += 1
else:
   st.error (f"ข้อที่ 4 : ยังไม่ถูกต้อง(คุณตอบ '{u_ans1}')")
# Score
st.info(f"ได้คะแนนรวม: {score} คะแนน")
if score == 2
  st.success(" You Win!!! ")
else:
  st.error(" You Lose!!!! ")
# Game Button
st.button("เริ่มเล่นเกม", on_click=reset_game)
# Countdown Bar
if "start" in st.session_state and not st.session_state.get("is_ended",False):
   time_left = int(30 - (time.time() - st.session_state.start))
if time_left > 0:
   st.error(f"เหลือเวลา: {time_left} วินาที")
else:
   st.session_state:is_ended = True
   st.rerun
st.divider()
# Input
ans1 = st.text.input(
   "ข้อที่ 1 : An A__le a day keeps the doctor away.🍎",
)
ans2 = st.text.input(
   "ข้อที่ 2 : Cats love to eat f_sh.🐟",
)
ans3 = st.text.input(
   "ข้อที่ 3 : The two wheel vehicle with engine is moto___le",
)
ans4 = st.text.input(
   "ข้อที่ 2 : Thing that you can call to some people/play a game/watch a video is ____tphone",
)
# Update Latest Value
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
# Send Button
if "start" in st.session_state and not st.session_state.get("is_ended", False):
if st.button("📥 ส่งคำตอบ"):
   st.session_state.is_ended = True
   st.rerun()
time.sleep(1)
st.rerun
# Show the Dialog
if st.session_state.get("is_ended", False):
  show_result_dialog(ans1, ans2)
st.divider()
st.write("นายวรรณวัฒน์ โภชกรณ์ ม.4/7 เลขที่ 41")
