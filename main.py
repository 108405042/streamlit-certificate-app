import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import datetime

# UI：標題與輸入框
st.title("🏅 陽明交大研究感謝狀")
name = st.text_input("請輸入您的名字：", "")

if name:
    # 載入底圖與字型
    bg = Image.open("2.png").convert("RGBA")
    font = ImageFont.truetype("NotoSerifTC-VariableFont_wght.ttf", size=80)
    draw = ImageDraw.Draw(bg)

    # 將名字置中寫上
    bbox = draw.textbbox((0, 0), name, font=font)
    text_width = bbox[2] - bbox[0]
    x = (bg.width - text_width) / 2
    y = 580  # 視你的圖設計，調整 Y 軸
    draw.text((x, y), name, fill="black", font=font)

    # 顯示預覽
    st.image(bg, caption="🎉 研究有您參與真好，恭喜您獲得獎狀！", use_container_width=True)

    # 提供下載按鈕
    buf = io.BytesIO()
    bg.save(buf, format="PNG")
    st.download_button(
        label="📥 下載我的獎狀",
        data=buf.getvalue(),
        file_name=f"第二週感謝狀_{name}.png",
        mime="image/png"
    )
