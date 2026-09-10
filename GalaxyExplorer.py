import streamlit as st
import time
st.title("Galaxy Explorer 👾🚀")
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
def show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10, ans11, ans12, ans13, ans14, ans15):
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
  if u_ans1 == "c. mercury":
     st.success("ข้อที่ 1 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 1: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans1}')")
  if u_ans2 == "b. jupiter":
     st.success("ข้อที่ 2 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 2: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans2}')")
  if u_ans3 == "c. gravity":
     st.success("ข้อที่ 3 ถูกต้องนะคร้าบบบบบบ")
     score += 1
  else:
     st.error(f"ข้อที่ 3: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans3}')")
  if u_ans4 == "c. we see different portions of the moon’s sunlit side.":
     st.success("ข้อที่ 4 ถูกต้องนะคร้าบบบบบบ")
     score += 2
  else:
     st.error(f"ข้อที่ 4: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans4}')")
  if u_ans5 == "b. earth’s axis is tilted as it orbits the sun.":
     st.success("ข้อที่ 5 ถูกต้องนะคร้าบบบบบบ")
     score += 2
  else:
     st.error(f"ข้อที่ 5: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans5}')")
  if u_ans6 == "d. distance":
     st.success("ข้อที่ 6 ถูกต้องนะคร้าบบบบบบ")
     score += 2
  else:
     st.error(f"ข้อที่ 6: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans6}')")
  if u_ans7 == "b. it is cooler.":
     st.success("ข้อที่ 7 ถูกต้องนะคร้าบบบบบบ")
     score += 3
  else:
     st.error(f"ข้อที่ 7: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans7}')")
  if u_ans8 == "c. the moon’s rotation period equals its orbital period.":
     st.success("ข้อที่ 8 ถูกต้องนะคร้าบบบบบบ")
     score += 3
  else:
     st.error(f"ข้อที่ 8: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans8}')")
  if u_ans9 == "b. it decreases.":
     st.success("ข้อที่ 9 ถูกต้องนะคร้าบบบบบบ")
     score += 3
  else:
     st.error(f"ข้อที่ 9: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans9}')")
  if u_ans10 == "c. its orbital period is longer than one earth year.":
     st.success("ข้อที่ 10 ถูกต้องนะคร้าบบบบบบ")
     score += 5
  else:
     st.error(f"ข้อที่ 10: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans10}')")
  if u_ans11 == "b. 4 au":
     st.success("ข้อที่ 11 ถูกต้องนะคร้าบบบบบบ")
     score += 5
  else:
     st.error(f"ข้อที่ 11: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans11}')")
  if u_ans12 == "a. star a is intrinsically brighter than star b.":
     st.success("ข้อที่ 12 ถูกต้องนะคร้าบบบบบบ")
     score += 5
  else:
     st.error(f"ข้อที่ 12: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans12}')")
  if u_ans13 == "b. the star is moving away from earth.":
     st.success("ข้อที่ 13 ถูกต้องนะคร้าบบบบบบ")
     score += 5
  else:
     st.error(f"ข้อที่ 13: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans13}')")
  if u_ans14 == "b. earth overtaking mars in their respective orbits.":
     st.success("ข้อที่ 14 ถูกต้องนะคร้าบบบบบบ")
     score += 5
  else:
     st.error(f"ข้อที่ 14: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans14}')")
  if u_ans15 == "c. the thermonuclear runaway of a carbon–oxygen white dwarf.":
     st.success("ข้อที่ 15 ถูกต้องนะคร้าบบบบบบ")
     score += 5
  else:
     st.error(f"ข้อที่ 15: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans15}')")
  st.info(f"ได้คะแนนรวม: {score} / 48 คะแนน")
  if score == 48:
     st.success("You are the master of Earth Science 👍❤️")
  if score < 48:
    st.success("You Win 😁")
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
st.write("ข้อที่ 1 : Which planet is closest to the Sun?")
ans1 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. Earth", "B. Venus", "C. Mercury", "D. Mars"],
    key="ans1_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 2 : What is the largest planet in our Solar System?")
ans2 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. Saturn", "B. Jupiter", "C. Mercury", "D. Mars"],
    key="ans2_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 3 : What force keeps planets in orbit around the Sun?")
ans3 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. Friction", "B. Magnetism", "C. Gravity", "D. Elctricity"],
    key="ans3_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 4 : Why does the Moon appear to change during a month?")
ans4 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. The moon changes its shape.", "B. Earth’s shadow always covers part of the moon", "C. We see different portions of the Moon’s sunlit side.", "D. Clouds cover different parts of the moon."],
    key="ans4_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 5 : Which statement about seasons on Earth is correct?")
ans5 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. Earth is much closer to the Sun in summer.", "B. Earth’s axis is tilted as it orbits the Sun.", "C. The Sun becomes hotter in summer.", "D. Earth rotates faster in summer."],
    key="ans5_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 6 : A light-year is a unit used to measure what?")
ans6 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. Time", "B. Brightness", "C. Temperature", "D. Distance"],
    key="ans6_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 7 : If a star appears red, what does this generally indicate its surface temperature?")
ans7 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. It is hotter.", "B. It is cooler.", "C. They have the same temperature.", "D. Cooler cannot indicate temperature."],
    key="ans7_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 8 : Why do we always see nearly the same side of the Moon from Earth?")
ans8 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. The Moon does not rotate.", "B. Earth blocks the other side.", "C. The Moon’s rotation period equals its orbital period.", "D. The Moon is smaller than Earth."],
    key="ans8_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 9 : If the distance between two objects increases, what happens to the gravitational force between them?")
ans9 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. It increases.", "B. It decreases.", "C. It stays the same.", "D. It becomes zero immediately."],
    key="ans9_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 10 : A planet takes longer to orbit the Sun than Earth. Which of the following is most likely true?")
ans10 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. It is always smaller than Earth.", "B. It is always closer to the Sun than Earth.", "C. Its orbital period is longer than one Earth year.", "D. It rotates more slowly than Earth."],
    key="ans10_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 11 : A planet has an orbital period of 8 Earth years. Approximately how many times farther from the Sun is it than Earth?")
ans11 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. 2 AU", "B. 4 AU", "C. 8 AU", "D. 16 AU"],
    key="ans11_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 12 : Two stars have the same apparent brightness, but Star A. is twice as far from Earth as Star B. Which statement is correct?")
ans12 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. Star A is intrinsically brighter than Star B.", "B. Star B is intrinsically brighter than Star A.", "C. Both stars have the same intrinsic brightness.", "D. Distance does not affect apparent brightness."],
    key="ans12_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 13 : A star’s spectrum shows that its spectral lines are shifted toward longer wavelengths. what does this most likely indicate?")
ans13 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. The star is moving to ward Earth.", "B. The star is moving away from Earth.", "C. The star is becoming hotter.", "D. The star has stopped moving."],
    key="ans13_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 14 : Which phenomenon is primarily responsible for the apparent retrograde motion of Mars as observed from Earth?")
ans14 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. Mars temporarily reversing its orbital direction.", "B. Earth overtaking Mars in their respective orbits.", "C. The gravitational influence of Jupiter.", "D. The precession of Earth's rotational axis."],
    key="ans14_val",
    label_visibility="collapsed",
)
st.write("ข้อที่ 15 : What is the primary physical mechanism that causes a Type Ia supernova?")
ans15 = st.radio(
    label="เลือกคำตอบ:",
    options=["A. The core collapse of a massive star.", "B. The merger of two neutron stars.", "C. The thermonuclear runaway of a carbon–oxygen white dwarf.", "D. The gravitational collapse of a molecular cloud."],
    key="ans15_val",
    label_visibility="collapsed",
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
st.write("""สมาชิกภายในกลุ่ม นางสาวเดือนนคร สิทธิเมา 18 
นายปณิธาน แก้วอาจ 25 
นายชวิน ไชยศรี 29 
นายวรรณวัฒน์ โภชกรณ์ 41 ม.4/7""")
