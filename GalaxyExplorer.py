import streamlit as st
import time
st.title("Galaxy Explorer")
if "ans1_val" not in st.session_state:
   st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
   st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
   st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
   st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
   st.session_state.ans5_val = ""
if "ans6_val" not in st.session_state:
   st.session_state.ans6_val = ""
if "ans7_val" not in st.session_state:
   st.session_state.ans7_val = ""
if "ans8_val" not in st.session_state:
   st.session_state.ans8_val = ""
if "ans9_val" not in st.session_state:
  st.session_state.ans9_val = ""
if "ans10_val" not in st.session_state:
  st.session_state.ans10_val = ""
if "ans11_val" not in st.session_state:
   st.session_state.ans11_val = ""
if "ans12_val" not in st.session_state:
   st.session_state.ans12_val = ""
if "ans13_val" not in st.session_state:
   st.session_state.ans13_val = ""
if "ans14_val" not in st.session_state:
   st.session_state.ans14_val = ""
if "ans15_val" not in st.session_state:
   st.session_state.ans15_val = ""
if "start" not in st.session_state:
  st.session_state.start = None
if "is_ended" not in st.session_state:
  st.session_state.is_ended = False
def reset_game():
  st.session_state.ans1_val = ""
  st.session_state.ans2_val = ""
  st.session_state.ans3_val = ""
  st.session_state.ans4_val = ""
  st.session_state.ans5_val = ""
  st.session_state.ans6_val = ""
  st.session_state.ans7_val = ""
  st.session_state.ans8_val = ""
  st.session_state.ans9_val = ""
  st.session_state.ans10_val = ""
  st.session_state.ans11_val = ""
  st.session_state.ans12_val = ""
  st.session_state.ans13_val = ""
  st.session_state.ans14_val = ""
  st.session_state.ans15_val = ""
  st.session_state.start = time.time()
  st.session_state.is_ended = False
@st.dialog("สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10):
  st.balloons()
  score = 0
  u_ans1 = ans1.strip().lower()
  u_ans2 = ans2.strip().lower()
  u_ans3 = ans3.strip().lower()
  u_ans4 = ans4.strip().lower()
  u_ans5 = ans5.strip().lower()
  u_ans6 = ans6.strip().lower()
  u_ans7 = ans7.strip().lower()
  u_ans8 = ans8.strip().lower()
  u_ans9 = ans9.strip().lower()
  u_ans10 = ans10.strip().lower()
  u_ans11 = ans11.strip().lower()
  u_ans12 = ans12.strip().lower()
  u_ans13 = ans13.strip().lower()
  u_ans14 = ans14.strip().lower()
  u_ans15 = ans15.strip().lower()
  if u_ans1 == "":
     st.success("ข้อที่ 1 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 1: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans1}')")
  if u_ans2 == "":
     st.success("ข้อที่ 2 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 2: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans2}')")
  if u_ans3 == "":
     st.success("ข้อที่ 3 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 3: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans3}')")
  if u_ans4 == "":
     st.success("ข้อที่ 4 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 4: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans4}')")
  if u_ans5 == "":
     st.success("ข้อที่ 5 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 5: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans5}')")
  if u_ans6 == "":
     st.success("ข้อที่ 6 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 6: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans6}')")
  if u_ans7 == "":
     st.success("ข้อที่ 7 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 7: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans7}')")
  if u_ans8 == "":
     st.success("ข้อที่ 8 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 8: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans8}')")
  if u_ans9 == "":
     st.success("ข้อที่ 9 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 9: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans9}')")
  if u_ans10 == "":
     st.success("ข้อที่ 10 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 10: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans10}')")
  if u_ans11 == "":
     st.success("ข้อที่ 11 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 1: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans11}')")
  if u_ans12 == "":
     st.success("ข้อที่ 12 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 12: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans12}')")
  if u_ans13 == "":
     st.success("ข้อที่ 13 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 13: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans13}')")
  if u_ans14 == "":
     st.success("ข้อที่ 14 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 4: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans14}')")
  if u_ans15 == "":
     st.success("ข้อที่ 15 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 15: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans15}')")
  st.info(f"ได้คะแนนรวม: {score} / คะแนน")
  if score == 45:
     st.success("You are the master of Earth Science")
  if score < 45:
    st.success("ํYou Win")
  if score == 0:
   st.error("Kwai I Ngao Tam Mai Tam Mai Dai Suck Kor KUY")
st.button("เริ่มเล่นเกม / เริ่มต้นใหม่", on_click=reset_game)
if st.session_state.start is not None and not st.session_state.is_ended:
    time_left = int(240 - (time.time() - st.session_state.start))
    if time_left > 0:
        st.error(f"⏱️ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()
st.divider()
ans1 = st.text_input(
    "ข้อที่ 1 :",
    key="ans1_val"
)
ans2 = st.text_input(
    "ข้อที่ 2 :",
    key="ans2_val"
)
ans3 = st.text_input(
    "ข้อที่ 3 :",
    key="ans3_val"
)
ans4 = st.text_input(
    "ข้อที่ 4 :",
    key="ans4_val"
)
ans5 = st.text_input(
    "ข้อที่ 5 :",
    key="ans5_val"
)
ans6 = st.text_input(
    "ข้อที่ 6 :",
    key="ans6_val"
)
ans7 = st.text_input(
    "ข้อที่ 7 :",
    key="ans7_val"
)
ans8 = st.text_input(
    "ข้อที่ 8 :",
    key="ans8_val"
)
ans9 = st.text_input(
    "ข้อที่ 9 :",
    key="ans9_val"
)
ans10 = st.text_input(
    "ข้อที่ 10 :",
    key="ans10_val"
)
ans11 = st.text_input(
    "ข้อที่ 11 :",
    key="ans11_val"
)
ans12 = st.text_input(
    "ข้อที่ 12 :",
    key="ans12_val"
)
ans13 = st.text_input(
    "ข้อที่ 13 :",
    key="ans13_val"
)
ans14 = st.text_input(
    "ข้อที่ 14 :",
    key="ans14_val"
)
ans15 = st.text_input(
    "ข้อที่ 15 :",
    key="ans15_val"
)
if st.session_state.start is not None and not st.session_state.is_ended:
   if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()
   time.sleep(1)
   st.rerun()
if st.session_state.is_ended and st.session_state.start is not None:
   show_result_dialog(st.session_state.ans1_val, st.session_state.ans2_val, st.session_state.ans3_val, st.session_state.ans4_val, st.session_state.ans5_val, st.session_state.ans6_val, st.session_state.ans7_val, st.session_state.ans8_val, st.session_state.ans9_val, st.session_state.ans10_val, st.session_state.ans11_val, st.session_state.ans12_val, st.session_state.ans13_val, st.session_state.ans14_val, st.session_state.ans15_val)
st.divider()
st.write("สมาชิกภายในกลุ่ม นางสาวเดือนนคร สิทธิเมา 18 นายปณิธาน แก้วอาจ 25 นายชวิน ไชยศรี 29 นายวรรณวัฒน์ โภชกรณ์ 41 ม.4/7")
