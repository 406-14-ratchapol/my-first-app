import streamlit as st
st.markdown("# :red[🫃แอปพลิเคชั่นคำนวณค่าดัชนีมวลกายหรือ BMI🩺]")
st.write("่กรอกข้อมูลน้ำหนักส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม) : ")
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร) : ")

if st.button("คำนวณค่า BMI") :
  height_m = height_cm / 100
  bmi = weight  / (height_m ** 2)

  st.write("___")
  st.header(f"ค่า BMI ของคุณคือ : **{bmi:.2f}**")

if bmi < 18.5:
  st.warning("คุณมีน้ำหนักต่ำกว่าเกณฑ์ (ผอม)")
elif 18.5 <= bmi <23.0:
  st.success("คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขถาพดี)")
elif 23.0 <= bmi < 25.0:
  st.info("คุณเริ่มมีน้ำหนักเกินเกณฑ์ (ท้วม)")
else:
  st.error("คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย")

st.divider()
st.write("นายรัชพล กองชุมพล เลขที่ 14 ม.4/6")
