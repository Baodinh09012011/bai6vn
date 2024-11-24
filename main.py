import streamlit as s

s.title("Dang nhap tai khoan")
mybar = s.progress(0)
buoc = ["tai khoan","mat khau","nhap lai mat khau","ten nguoi dung","email"]
userinfor = []

for i in range(len(buoc)):
  infor = s.text_input(buoc[i], "")
  if infor != '':
    userinfor.append(infor)
if s.button("Confirm"):
    if len(userinfor) == len(buoc):
      mybar.progress(100)
    else:
      mybar.progress(len(userinfor) / len(buoc))

  
  
