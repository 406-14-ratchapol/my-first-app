import time
import streamlit as st

st.title("เกมเติมศัพท์สถานที่สำคัญของโลก🌏")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
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




# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.session_state.ans6_val = ""
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()
    u_ans5 = ans6.strip().lower()


    # ตรวจข้อ 1
    if u_ans1 == "ทัชมาฮาล":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "หอไอเฟล":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มตรวจข้อ 3, 4 ตรงนี้
    if u_ans3 == "หอเอนปิซา":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")
    if u_ans4 == "กำแพงเมืองจีน":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")
    if u_ans5 == "มาชูปิชู":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")
    if u_ans6 == "โคลอสเซียม":
        st.success("✅ ข้อ 6: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 6: ยังไม่ถูกต้อง (คุณตอบ '{u_ans6}')")





    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 6:
        st.success("🎉 สุดยอดไปเลย คุณโหดระเบิดจัด!")
    elif score >= 3 and score <= 5:
        st.info("คุณก็เก่งเหมือนกันนี่หว่า!")
    else:
      st.error("เศร้าจังเลย ไปเรียนมาใหม่นะ 😭")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1: สิ่งที่เป็นอนุสรณ์สถานในประเทศอินเดียที่มีอาบังขายโรตีคือที่ใด",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: สถานที่ท่องเที่ยวที่โด่งดังในเมืองปารีส ประเทศฝรั่งเศส",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: สิ่งก่อสร้างที่มีชื่อเสียงมาจากการทรุดตัวของรากฐาน ",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: สถานที่ที่เป็นปราการโบราณยาวกว่า21000กิโลเมตรตั้งอยู่ในจีน ",
    value=st.session_state.ans4_val,
)
ans5 = st.text_input(
    "ข้อ 5: นครโบราณชาวอินคาที่ตั้งอยู่บนเทือกเขาสูง ",
    value=st.session_state.ans5_val,
)
ans6 = st.text_input(
    "ข้อ 6: ลานประลองโบราณที่กรุงโรมประเทศอิตาลี ",
    value=st.session_state.ans6_val,
)

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
st.session_state.ans6_val = ans6

# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มข้อ 3, 4 ตรงนี้


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6)

st.divider()
st.write("ผลงานโดยกลุ่มที่ 6")
