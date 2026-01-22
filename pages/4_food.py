import streamlit as st

st.set_page_config(page_title="Moon's Food Matrix v7.3", page_icon="🥗", layout="wide")

# =========================================================
# 1. CẤU HÌNH DỮ LIỆU (12 CÔNG THỨC & 4 GÓC ĐỘ)
# =========================================================

# Danh sách 12 Công thức Detox (Chuẩn theo ảnh Moon gửi)
detox_menu = [
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
]

# Danh sách 4 Góc độ Video (Chuẩn theo ảnh Moon gửi)
video_angles = {
    "🎥 1. Hướng dẫn (How-to/ASMR)": {
        "style": "Macro shots, focus on cutting/blending sounds. Bright lighting.",
        "desc": "Quay cận cảnh quy trình làm, âm thanh ASMR đã tai."
    },
    "🎓 2. Kiến thức (Education)": {
        "style": "Medium shot of Moon (or 3D Character) pointing to a hologram chart. Professional studio.",
        "desc": "Chuyên gia đứng phân tích thành phần hóa học/công dụng."
    },
    "⚠️ 3. Cảnh báo (Warning)": {
        "style": "Dramatic lighting, serious tone. Holding a 'STOP' sign or shaking head.",
        "desc": "Cảnh báo sai lầm khi uống (VD: Uống lúc đói hại dạ dày)."
    },
    "📖 4. Câu chuyện (Story/Vlog)": {
        "style": "Handheld POV, sunny garden background, relaxing vibe.",
        "desc": "Vlog tâm sự: 'Hôm nay Moon cảm thấy mệt, Moon uống ly này...'"
    }
}

# KHO KIẾN THỨC (Tự động tra cứu hoạt chất cho 12 món)
nutrition_db = {
    "Chanh + Tỏi": {"chat": "Allicin & Vitamin C", "loi": "Allicin trong tỏi là 'vua' diệt khuẩn, kết hợp Vitamin C giúp quét sạch mỡ máu cực mạnh!"},
    "Chanh + Gừng": {"chat": "Gingerol & Axit Citric", "loi": "Đầy bụng khó tiêu? Gingerol trong gừng sẽ làm ấm bụng và đẩy lùi cơn đau dạ dày ngay lập tức."},
    "Chanh + Nha đam": {"chat": "Polysaccharide & Collagen", "loi": "Muốn da căng mướt? Nha đam cấp nước, còn chanh kích thích sản sinh Collagen tự nhiên."},
    "Chanh + Nghệ": {"chat": "Curcumin hoạt tính", "loi": "Curcumin là chất kháng viêm tự nhiên mạnh nhất, giúp chữa lành mọi tổn thương bên trong."},
    "Chanh + Mật ong": {"chat": "Enzyme kháng khuẩn", "loi": "Bài thuốc dân gian nhưng hiệu quả gấp 10 lần thuốc tây trong việc tăng cường hệ miễn dịch."},
    "Trà chanh nóng": {"chat": "Theanine & Vitamin C", "loi": "Một ly ấm nóng giúp thanh lọc gan thận và xoa dịu tinh thần sau ngày dài."},
    "Củ dền + Táo + Cà rốt": {"chat": "Sắt & Beta-carotene", "loi": "Công thức 'ABC' huyền thoại! Bơm máu lên não và giúp đôi mắt sáng khỏe."},
    "Bơ + Dưa leo + Gừng": {"chat": "Omega-3 & Hydration", "loi": "Chất béo tốt từ bơ kết hợp dưa leo giúp giảm viêm khớp và cấp ẩm sâu cho da."},
    "Việt quất + Cà chua + Gừng": {"chat": "Lycopene & Anthocyanin", "loi": "Siêu phẩm chống lão hóa! Lycopene bảo vệ tế bào khỏi gốc tự do gây hại."},
    "Cam + Táo + Nghệ": {"chat": "Vitamin C & Curcumin", "loi": "Mệt mỏi tan biến! Cú hích năng lượng tự nhiên giúp bạn tỉnh táo không cần Cafein."},
    "Bưởi + Cà rốt + Gừng": {"chat": "Naringenin & Fiber", "loi": "Naringenin trong bưởi kích thích gan đốt cháy mỡ thừa ngay cả khi bạn đang ngủ."},
    "Kiwi + Xà lách + Gừng": {"chat": "Serotonin & Magie", "loi": "Mất ngủ kinh niên? Ly này chứa Serotonin tự nhiên giúp bạn chìm vào giấc ngủ êm ái."}
}

# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🥗 MOON'S FOOD MATRIX v7.3")
st.markdown("*Phiên bản chuẩn: 12 Công thức Detox & 4 Góc độ*")

# --- KHU VỰC CHỌN LỰA ---
with st.expander("⚙️ CẤU HÌNH VIDEO (Mở rộng)", expanded=True):
    c1, c2, c3 = st.columns([1, 2, 1])
    with c1: 
        # Mặc định chọn nhóm Detox vì Moon đang tập trung cái này
        group = st.selectbox("Chọn nhóm:", ["🥤 Smoothie & Detox (12 Công thức vàng)", "🥗 Healthy Food (Khác)"])
    
    with c2: 
        if "Detox" in group:
            recipe_full = st.selectbox("Nguyên liệu/Công thức:", detox_menu)
        else:
            recipe_full = st.text_input("Nhập tên món khác:", "Salad Ức gà")
            
    with c3:
        angle_full = st.selectbox("Góc độ Video:", list(video_angles.keys()))

# --- XỬ LÝ DỮ LIỆU ---
# Tách tên món để tra từ điển (VD: "1. Chanh + Tỏi..." -> "Chanh + Tỏi")
if "Detox" in group:
    key_name = recipe_full.split(". ")[1].split(" (")[0]
else:
    key_name = recipe_full

# Lấy thông tin từ kho
info = nutrition_db.get(key_name, {"chat": "Vitamin & Khoáng chất", "loi": "Công thức tuyệt vời cho sức khỏe của bạn!"})
angle_data = video_angles.get(angle_full, video_angles["🎥 1. Hướng dẫn (How-to/ASMR)"])

# =========================================================
# HIỂN THỊ KẾT QUẢ
# =========================================================

st.divider()

# 1. CAPTION & KỊCH BẢN NGẮN
c_left, c_right = st.columns(2)

with c_left:
    st.subheader("📝 Caption TikTok:")
    st.info(f"""
    {recipe_full} 🌿
    
    bí mật nằm ở **{info['chat']}** giúp {info['loi'].lower()}
    
    👉 {angle_data['desc']}
    #MoonDetox #{key_name.replace(' + ','').replace(' ','')} #SốngKhỏe
    """)

with c_right:
    st.subheader("🗣️ Lời thoại (Voiceover):")
    st.success(f"\"{info['loi']}\"")
    st.caption(f"💡 Hoạt chất chính: {info['chat']}")

# 2. PROMPT SORA (TỰ ĐỘNG ĐIỀN)
st.subheader(f"🎥 Prompt Sora (15s) - {angle_full}")
st.write("Copy đoạn code bên dưới:")

sora_prompt = f"""
8k, Food Cinematography.
Subject: Fresh ingredients (**{key_name}**) transforming into a delicious smoothie.
Style: {angle_data['style']}
Action: {angle_data['desc']} showing the health benefits.
Speaking Line (Vietnamese): "{info['loi']}"
Overlay Text: Floating label showing "{info['chat']}".
Constraint: NO TEXT OVERLAYS (except the label). --duration 15s
"""
st.code(sora_prompt, language='text')
