import streamlit as st
import random

st.set_page_config(page_title="Moon's Fresh Food", page_icon="🥗", layout="wide")

# =========================================================
# 1. DỮ LIỆU & LOGIC CAPTION HÀI HƯỚC
# =========================================================

categories = {
    "🥤 Smoothie & Detox (12 Công thức vàng)": [
        "1. Chanh + Tỏi (Sạch mạch máu)",
        "2. Chanh + Gừng (Tiêu hóa tốt)",
        "3. Chanh + Nha đam (Đẹp da)",
        "4. Chanh + Nghệ (Kháng viêm)",
        "5. Chanh + Mật ong (Tăng đề kháng)",
        "6. Trà chanh nóng (Thanh lọc)",
        "7. Củ dền + Táo + Cà rốt (Bổ máu)",
        "8. Bơ + Dưa leo + Gừng (Giảm viêm)",
        "9. Việt quất + Cà chua + Gừng (Tăng miễn dịch)",
        "10. Cam + Táo + Nghệ (Giảm mệt mỏi)",
        "11. Bưởi + Cà rốt + Gừng (Giảm mỡ máu)",
        "12. Kiwi + Xà lách + Gừng (Trị mất ngủ)"
    ],
    "🍎 Trái cây (Fruits)": [
        "Táo", "Cam", "Chuối", "Dưa hấu", "Nho", "Thanh long", "Bơ",
        "Sầu riêng", "Măng cụt", "Vải thiều", "Nhãn", "Xoài", "Dâu tây", "Chanh"
    ],
    "🥦 Rau xanh (Vegetables)": [
        "Cải thìa", "Cà rốt", "Súp lơ", "Khổ qua", "Rau má", "Cà chua", "Khoai tây",
        "Rau ngót", "Bắp cải", "Bí đỏ", "Dưa leo", "Cần tây"
    ]
}

# Dịch & Data phụ trợ
smoothie_map = {
    "Chanh + Tỏi": {"en": "Lemon and Garlic", "cap": "Uống xong người yêu chạy mất dép nhưng tim mạch thì khỏe re! 🤣"},
    "Chanh + Gừng": {"en": "Lemon and Ginger", "cap": "Ấm bụng hơn cả người yêu cũ nhắn tin quay lại! 🔥"},
    "Chanh + Nha đam": {"en": "Lemon and Aloe Vera", "cap": "Da đẹp thế này thì ai chơi lại? 💅"},
    "Chanh + Nghệ": {"en": "Lemon and Turmeric", "cap": "Vàng da là do nghệ, chứ không phải do 'nghệ' sĩ đâu nha! 😜"},
    "Chanh + Mật ong": {"en": "Lemon and Honey", "cap": "Ngọt ngào đến mấy cũng tan thành... ly nước này thôi! 🍯"},
    "Trà chanh nóng": {"en": "Hot Tea with Lemon", "cap": "Chill một chút thì có sao, miễn là khỏe! ☕"},
    "Củ dền + Táo + Cà rốt": {"en": "Beetroot, Apple, Carrot", "cap": "Máu lên não nhanh hơn cả tốc độ lương về! 🚀"},
    "Bơ + Dưa leo + Gừng": {"en": "Avocado, Cucumber, Ginger", "cap": "Xanh mượt mà như tình yêu đầu đời! 💚"},
    "Việt quất + Cà chua + Gừng": {"en": "Blueberries, Tomato, Ginger", "cap": "Tăng đề kháng để còn 'chiến' với deadline! 💪"},
    "Cam + Táo + Nghệ": {"en": "Orange, Apple, Turmeric", "cap": "Hết mệt mỏi, chỉ còn 'mệt' vì quá xinh! 😎"},
    "Bưởi + Cà rốt + Gừng": {"en": "Grapefruit, Carrot, Ginger", "cap": "Mỡ đi nhé, đừng quay lại nữa! 👋"},
    "Kiwi + Xà lách + Gừng": {"en": "Kiwi, Lettuce, Ginger", "cap": "Uống xong ngủ ngon hơn cả lúc họp! 😴"}
}

# Ma trận 4 góc độ
pillars = {
    "🥣 1. Hướng dẫn (How-to/ASMR)": {"focus": "Tập trung vào âm thanh, hình ảnh ngon mắt, quy trình làm.", "tone": "Thư giãn, ngon miệng", "action_kw": "chopping, blending, pouring, ASMR style"},
    "🎓 2. Kiến thức (Education)": {"focus": "Giải thích tại sao công thức này tốt (Phân tích thành phần).", "tone": "Chuyên gia, tin cậy", "action_kw": "pointing to ingredients, showing health chart, nodding"},
    "⚠️ 3. Cảnh báo (Warning)": {"focus": "Những
