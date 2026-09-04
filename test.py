import streamlit as st
import time

st.title("🌌 Galaxy Explorer")

# --- 1. ประกาศ Session State ---
for i in range(1, 16):
    if f"ans{i}_val" not in st.session_state:
        st.session_state[f"ans{i}_val"] = ""

if "start" not in st.session_state:
    st.session_state.start = None
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False

def reset_game():
    for i in range(1, 16):
        st.session_state[f"ans{i}_val"] = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False

# --- 2. ฟังก์ชันแสดง Dialog สรุปผล ---
@st.dialog("สรุปผลการเล่นเกม")
def show_result_dialog(answers):
    st.balloons()
    score = 0
    
    # กำหนดเฉลย (สมมติตัวอย่างคำตอบที่ถูกต้อง เปลี่ยนข้อความในเครื่องหมายคำพูดได้เลยครับ)
    # ในโค้ดเดิมของคุณ u_ans == "" หมายถึง ถ้าไม่พิมพ์อะไรเลยจะได้คะแนนเต็ม 
    # ตรงนี้ผมใส่คำตอบสมมติไว้ หากต้องการให้เว้นว่างแล้วได้คะแนนเหมือนเดิม ให้แก้เป็น "" ครับ
    solutions = {
        1: "ดวงอาทิตย์", 2: "ดาวพุธ", 3: "ดาวศุกร์", 4: "โลก", 5: "ดาวอังคาร",
        6: "ดาวพฤหัส", 7: "ดาวเสาร์", 8: "ดาวยูเรนัส", 9: "ดาวเนปจูน", 10: "ทางช้างเผือก",
        11: "หลุมดำ", 12: "ดาวหาง", 13: "อุกกาบาต", 14: "เนบิวลา", 15: "แสงเหนือ"
    }

    for i in range(1, 16):
        u_ans = answers[i-1].strip().lower()
        sol = solutions[i].strip().lower()
        
        if u_ans == sol:
            st.success(f"ข้อที่ {i} ถูกต้องนะคร้าบบบบบบ")
            score += 1
        else:
            st.error(f"ข้อที่ {i}: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{u_ans}')")

    st.info(f"ได้คะแนนรวม: {score} / 15 คะแนน")
    
    # แก้ไข Syntax Error (ใส่ :) และเปลี่ยนคะแนนเต็มเป็น 15
    if score == 15:
        st.success("🏆 You are the master of Earth Science")
    elif score > 0:
        st.success("🎉 You Win")
    elif score == 0:
        st.error("❌ พยายามใหม่อีกครั้งน้าาา ไม่ผ่านสักข้อเลย")

# --- 3. ส่วนการแสดงผลบนหน้าจอหลัก ---
st.button("🔄 เริ่มเล่นเกม / เริ่มต้นใหม่", on_click=reset_game)

if st.session_state.start is not None and not st.session_state.is_ended:
    # คำนวณเวลาถอยหลัง
    time_left = int(240 - (time.time() - st.session_state.start))
    
    if time_left > 0:
        st.metric(label="⏳ เวลาที่เหลือ", value=f"{time_left} วินาที")
        
        # --- เพิ่มส่วนช่องกรอกคำถาม 15 ข้อ ---
        st.subheader("📝 จงตอบคำถามต่อไปนี้:")
        
        # ใช้สร้างช่อง Input ครบ 15 ข้ออัตโนมัติเพื่อประหยัดบรรทัดโค้ด
        answers_list = []
        for i in range(1, 16):
            # ดึงคำตอบมาเก็บไว้ใน session_state เพื่อไม่ให้หายเวลารีเฟรช
            ans = st.text_input(f"คำถามข้อที่ {i}:", key=f"ans{i}_val")
            answers_list.append(ans)
            
        # ปุ่มส่งคำตอบ
        if st.button("📤 ส่งคำตอบ"):
            st.session_state.is_ended = True
            show_result_dialog(answers_list)
            
        # สั่งให้รีเฟรชหน้าจอทุกๆ 1 วินาที เพื่อให้นาฬิกานับถอยหลังทำงาน
        time.sleep(1)
        st.rerun()
    else:
        st.session_state.is_ended = True
        st.error("⏰ หมดเวลาแล้วววว!")
        st.button("ลองใหม่อีกครั้ง", on_click=reset_game)
