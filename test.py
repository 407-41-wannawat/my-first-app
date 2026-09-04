import streamlit as st
import time

st.title("🌌 Galaxy Explorer")

# --- 1. คลังคำถามและตัวเลือก (15 ข้อ) ---
# คุณสามารถเข้ามาแก้ไขโจทย์ ตัวเลือก หรือดัชนีเฉลย (0=ก, 1=ข, 2=ค, 3=ง) ตรงนี้ได้เลยครับ
quiz_data = [
    {"q": "ดาวเคราะห์ดวงใดอยู่ใกล้ดวงอาทิตย์มากที่สุด?", "choices": ["ก. ดาวศุกร์", "ข. ดาวพุธ", "ค. ดาวอังคาร", "ง. โลก"], "correct_idx": 1},
    {"q": "ดาวเคราะห์ดวงใดได้ชื่อว่าเป็นฝาแฝดของโลก?", "choices": ["ก. ดาวศุกร์", "ข. ดาวพุธ", "ค. ดาวอังคาร", "ง. ดาวพฤหัสบดี"], "correct_idx": 0},
    {"q": "ดาวเคราะห์ดวงใดมีขนาดใหญ่ที่สุดในระบบสุริยะ?", "choices": ["ก. ดาวเสาร์", "ข. ดาวยูเรนัส", "ค. ดาวพฤหัสบดี", "ง. ดาวเนปจูน"], "correct_idx": 2},
    {"q": "ดาวเคราะห์แดง หมายถึงดาวดวงใด?", "choices": ["ก. ดาวพุธ", "ข. ดาวอังคาร", "ค. ดาวศุกร์", "ง. ดาวเสาร์"], "correct_idx": 1},
    {"q": "ดาวเคราะห์ดวงใดที่มีวงแหวนขนาดใหญ่และมองเห็นชัดเจนที่สุด?", "choices": ["ก. ดาวเสาร์", "ข. ดาวพฤหัสบดี", "ค. ดาวยูเรนัส", "ง. ดาวเนปจูน"], "correct_idx": 0},
    {"q": "กาแล็กซีที่ระบบสุริยะของเราอาศัยอยู่มีชื่อว่าอะไร?", "choices": ["ก. กาแล็กซีแอนโดรเมดา", "ข. กาแล็กซีทางช้างเผือก", "ค. กาแล็กซีแมกเจลแลน", "ง. กาแล็กซีน้ำวน"], "correct_idx": 1},
    {"q": "ดาวฤกษ์ที่อยู่ใกล้โลกมากที่สุดคือดาวดวงใด?", "choices": ["ก. ดาวเหนือ", "ข. ดาวซิริอุส", "ค. ดวงอาทิตย์", "ง. ดาวโปรซิออน"], "correct_idx": 2},
    {"q": "เทหวัตถุในอวกาศที่มีแรงดึงดูดมหาศาลจนแม้กระทั่งแสงก็ไม่สามารถหนีออกมาได้เรียกว่าอะไร?", "choices": ["ก. เนบิวลา", "ข. ดาวนิวตรอน", "ค. หลุมดำ", "ง. ดาวหาง"], "correct_idx": 2},
    {"q": "แสงเหนือ-แสงใต้ เกิดจากปรากฏการณ์ใด?", "choices": ["ก. ลมสุริยะปะทะกับชั้นบรรยากาศโลก", "ข. แสงอาทิตย์สะท้อนกับน้ำแข็งขั้วโลก", "ค. การระเบิดของดาวหาง", "ง. อุกกาบาตเสียดสีกับบรรยากาศ"], "correct_idx": 0},
    {"q": "กลุ่มแก๊สและฝุ่นผงในอวกาศที่เป็นแหล่งกำเนิดของดาวฤกษ์เรียกว่าอะไร?", "choices": ["ก. หลุมดำ", "ข. ซูเปอร์โนวา", "ค. เนบิวลา", "ง. ดาวเคราะห์น้อย"], "correct_idx": 2},
    {"q": "ดาวเคราะห์ดวงใดหมุนรอบตัวเองในทิศทางตรงกันข้ามกับดาวเคราะห์ดวงอื่นส่วนใหญ่?", "choices": ["ก. ดาวศุกร์", "ข. ดาวพุธ", "ค. ดาวอังคาร", "ง. ดาวพฤหัสบดี"], "correct_idx": 0},
    {"q": "ดาวดวงใดที่เรามักใช้ในการหาทิศเหนือในเวลากลางคืน?", "choices": ["ก. ดาวศุกร์", "ข. ดาวเหนือ", "ค. ดาวลูกไก่", "ง. ดาวโจร"], "correct_idx": 1},
    {"q": "ยานอวกาศลำแรกที่พามนุษย์ไปเหยียบดวงจันทร์คือยานลำใด?", "choices": ["ก. วอยเอเจอร์ 1", "ข. อพอลโล 11", "ค. สปุตนิก 1", "ง. คิวริออซิตี"], "correct_idx": 1},
    {"q": "ดาวเคราะห์น้อยส่วนใหญ่ในระบบสุริยะโคจรอยู่ระหว่างดาวดวงใด?", "choices": ["ก. โลก กับ ดาวอังคาร", "ข. ดาวพุธ กับ ดาวศุกร์", "ค. ดาวอังคาร กับ ดาวพฤหัสบดี", "ง. ดาวพฤหัสบดี กับ ดาวเสาร์"], "correct_idx": 2},
    {"q": "ปรากฏการณ์ที่ดวงจันทร์บังดวงอาทิตย์เรียกว่าอะไร?", "choices": ["ก. สุริยุปราคา", "ข. จันทรุปราคา", "ค. พระจันทร์ยิ้ม", "ง. ฝนดาวตก"], "correct_idx": 0}
]

# --- 2. ประกาศ Session State ---
for i in range(1, 16):
    if f"ans{i}_val" not in st.session_state:
        st.session_state[f"ans{i}_val"] = None  # None แปลว่ายังไม่ได้เลือกข้อไหนเลยตอนเริ่ม

if "start" not in st.session_state:
    st.session_state.start = None
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False

def reset_game():
    for i in range(1, 16):
        st.session_state[f"ans{i}_val"] = None
    st.session_state.start = time.time()
    st.session_state.is_ended = False

# --- 3. ฟังก์ชันแสดง Dialog สรุปผล ---
@st.dialog("สรุปผลการเล่นเกม")
def show_result_dialog():
    st.balloons()
    score = 0
    
    st.write("### 📊 ตรวจคำตอบอย่างละเอียด:")
    for i in range(1, 16):
        user_choice = st.session_state[f"ans{i}_val"]
        correct_answer = quiz_data[i-1]["choices"][quiz_data[i-1]["correct_idx"]]
        
        if user_choice == correct_answer:
            st.success(f"ข้อที่ {i} ถูกต้องนะคร้าบบบบบบ")
            score += 1
        else:
            ans_display = user_choice if user_choice is not None else "ไม่ได้ตอบ"
            st.error(f"ข้อที่ {i}: ยังไม่ถูกต้องน้าาาาาา (คุณตอบ '{ans_display}' ➡️ เฉลยคือ: {correct_answer})")

    st.info(f"ได้คะแนนรวม: {score} / 15 คะแนน")
    
    if score == 15:
        st.success("🏆 You are the master of Earth Science")
    elif score > 0:
        st.success("🎉 You Win")
    elif score == 0:
        st.error("❌ พยายามใหม่อีกครั้งน้าาา ไม่ผ่านสักข้อเลย")

# --- 4. ส่วนการแสดงผลบนหน้าจอหลัก ---
st.button("🔄 เริ่มเล่นเกม / เริ่มต้นใหม่", on_click=reset_game)

if st.session_state.start is not None and not st.session_state.is_ended:
    time_left = int(240 - (time.time() - st.session_state.start))
    
    if time_left > 0:
        st.metric(label="⏳ เวลาที่เหลือ", value=f"{time_left} วินาที")
        st.divider()
        
        # --- แสดงคำถามรูปแบบ ปุ่มตัวเลือก (Radio) ---
        st.subheader("🪐 จงเลือกคำตอบที่ถูกต้องที่สุด:")
        
        for i in range(1, 16):
            q_info = quiz_data[i-1]
            
            # ใช้ st.radio สำหรับเลือกตอบแบบปรนัย
            st.radio(
                f"**ข้อที่ {i}: {q_info['q']}**",
                options=q_info["choices"],
                index=None,  # ไม่มีค่าเริ่มต้น เพื่อบังคับให้ผู้ใช้กดเลือกเอง
                key=f"ans{i}_val"
            )
            st.write("") # เว้นบรรทัดให้อ่านง่าย
            
        st.divider()
        # ปุ่มส่งคำตอบ
        if st.button("📤 ส่งคำตอบ", type="primary"):
            st.session_state.is_ended = True
            show_result_dialog()
            
        # สั่งรีเฟรชหน้าจอทุกๆ 1 วินาที เพื่อให้นาฬิกานับถอยหลังขยับ
        time.sleep(1)
        st.rerun()
    else:
        st.session_state.is_ended = True
        st.error("⏰ หมดเวลาแล้วววว!")
        st.button("ลองใหม่อีกครั้ง", on_click=reset_game)
