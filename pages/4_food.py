import streamlit as st

st.set_page_config(page_title="Moon's Food Matrix v8.0", page_icon="🥗", layout="wide")

# =========================================================
# 1. CẤU HÌNH DỮ LIỆU
# =========================================================

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

video_angles = {
    "🎥 1. Hướng dẫn (How-to/ASMR)": {"style": "Macro shots, extreme close-up on textures", "desc": "Quay cận cảnh quy trình sơ chế"},
    "🎓 2. Kiến thức (Education)": {"style": "Medium shot pointing to hologram chart", "desc": "Chuyên gia phân tích thành phần"},
    "⚠️ 3. Cảnh báo (Warning)": {"style": "Dramatic lighting, serious tone", "desc": "Cảnh báo sai lầm thường gặp"},
    "📖 4. Câu chuyện (Story/Vlog)": {"style": "Handheld POV, sunny garden background", "desc": "Vlog tâm sự trải nghiệm"}
}

nutrition_db = {
    "Chanh + Tỏi": {"chat": "Allicin & Vitamin C", "hook": "Uống xong người yêu chạy mất dép nhưng tim mạch thì khỏe re!", "body": "Vì Allicin trong tỏi kết hợp Vitamin C của chanh sẽ quét sạch mỡ máu cứng đầu.", "cta": "Thử ngay công thức này nhé!"},
    "Chanh + Gừng": {"chat": "Gingerol & Axit Citric", "hook": "Vừa ăn xong mà bụng căng tức khó chịu?", "body": "Hoạt chất Gingerol trong gừng sẽ làm ấm bụng và đẩy lùi cơn đau dạ dày ngay lập tức.", "cta": "Lưu lại công thức để dùng khi cần."},
    "Chanh + Nha đam": {"chat": "Polysaccharide & Collagen", "hook": "Da khô mốc meo dù đã dưỡng đủ thứ?", "body": "Nha đam cấp nước tầng sâu, còn chanh kích thích sản sinh Collagen tự nhiên cho da căng mướt.", "cta": "Uống đi chờ chi!"},
    "Chanh + Nghệ": {"chat": "Curcumin hoạt tính", "hook": "Đau dạ dày uống thuốc mãi không khỏi?", "body": "Curcumin trong nghệ là kháng sinh tự nhiên mạnh nhất, giúp chữa lành mọi vết loét.", "cta": "Kiên trì mỗi sáng nhé."},
    "Chanh + Mật ong": {"chat": "Enzyme kháng khuẩn", "hook": "Mùa này ai cũng sụt sịt, trừ mình!", "body": "Nhờ Enzyme trong mật ong giúp tăng cường hệ miễn dịch gấp 10 lần thuốc bổ.", "cta": "Tăng đề kháng ngay hôm nay."},
    "Trà chanh nóng": {"chat": "Theanine & Vitamin C", "hook": "Stress công việc muốn nổ tung đầu óc?", "body": "Theanine trong trà kết hợp hương chanh sẽ xoa dịu thần kinh và thanh lọc gan thận.", "cta": "Thư giãn cùng Moon nhé."},
    "Củ dền + Táo + Cà rốt": {"chat": "Sắt & Beta-carotene", "hook": "Đứng lên ngồi xuống là hoa mắt chóng mặt?", "body": "Công thức ABC huyền thoại này chứa đầy Sắt hữu cơ giúp bơm máu lên não tức thì.", "cta": "Bổ máu cực tốt, thử nha."},
    "Bơ + Dưa leo + Gừng": {"chat": "Omega-3 & Hydration", "hook": "Xương khớp cứ kêu rắc rắc khi trở trời?", "body": "Chất béo tốt Omega-3 từ bơ kết hợp gừng ấm giúp bôi trơn khớp và giảm viêm hiệu quả.", "cta": "Xay uống liền đi nè."},
    "Việt quất + Cà chua + Gừng": {"chat": "Lycopene & Anthocyanin", "hook": "Sợ già trước tuổi thì đừng bỏ qua ly này!", "body": "Lycopene và Anthocyanin là bộ đôi chống lão hóa, bảo vệ tế bào khỏi gốc tự do.", "cta": "Bí quyết trẻ mãi không già đó."},
    "Cam + Táo + Nghệ": {"chat": "Vitamin C & Curcumin", "hook": "Sáng ngủ dậy mà người cứ lờ đờ uể oải?", "body": "Cú hích Vitamin C và Nghệ này sẽ nạp năng lượng tỉnh táo mà không cần Cafein.", "cta": "Tỉnh táo ngay tức thì."},
    "Bưởi + Cà rốt + Gừng": {"chat": "Naringenin & Fiber", "hook": "Bụng dưới núng nính làm bạn mất tự tin?", "body": "Naringenin trong bưởi kích thích gan đốt cháy mỡ thừa ngay cả khi bạn đang ngủ.", "cta": "Eo thon đón tết nào."},
    "Kiwi + Xà lách + Gừng": {"chat": "Serotonin & Magie", "hook": "Đếm cừu tới sáng mà vẫn không ngủ được?", "body": "Ly nước xanh này chứa Serotonin tự nhiên giúp vỗ về giấc ngủ êm ái.", "cta": "Chúc bạn ngủ ngon nhé."}
}

# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🥗 MOON'S FOOD MATRIX v8.0")
st.markdown("*Chế độ: 3D Animation (Pixar) & KOL (Cinematic)*")

# CẤU HÌNH
with st.expander("⚙️ CẤU HÌNH VIDEO (Bấm để mở rộng)", expanded=True):
    c1, c2 = st.columns(2)
    with c1: 
        # NÚT CHỌN STYLE QUAN TRỌNG
        style_select = st.radio("🎭 Chọn Phong cách Hình ảnh:", ["3D Animation (Pixar Cute)", "Người thật (Cinematic)"], horizontal=True)
    with c2:
        angle_full = st.selectbox("Góc quay:", list(video_angles.keys()))

    c3, c4 = st.columns(2)
    with c3: group = st.selectbox("Nhóm:", ["🥤 Smoothie (12 Món Vàng)", "🥗 Khác"])
    with c4: 
        if "Smoothie" in group: recipe_full = st.selectbox("Công thức:", detox_menu)
        else: recipe_full = st.text_input("Tên món:", "Salad Ức gà")

# XỬ LÝ DỮ LIỆU
if "Smoothie" in group: key_name = recipe_full.split(". ")[1].split(" (")[0]
else: key_name = recipe_full

# Xử lý Style Prompt (QUAN TRỌNG)
if "3D Animation" in style_select:
    subject_prompt = f"Cute 3D Pixar-style character representing {key_name}, vibrant colors, friendly expression"
    mj_style = "Disney Pixar style 3D render, cute, vibrant"
    angle_subject = "Character"
else:
    subject_prompt = f"High-end Food Cinematography, Real fresh ingredients ({key_name})"
    mj_style = "Professional food photography, 8k, photorealistic"
    angle_subject = "Moon (KOL)"

# Lấy data dinh dưỡng
default_data = {"chat": "Dưỡng chất", "hook": "Món này ngon lắm!", "body": "Nó tốt cho sức khỏe.", "cta": "Thử nhé!"}
info = nutrition_db.get(key_name, default_data)
angle_data = video_angles[angle_full]
full_speaking_line = f"{info['hook']} {info['body']} {info['cta']}"

# =========================================================
# HIỂN THỊ KẾT QUẢ
# =========================================================

tab_content, tab_video = st.tabs(["📝 BÀI VIẾT & ẢNH", "🎥 VIDEO SORA"])

# --- TAB 1: NỘI DUNG ---
with tab_content:
    c_left, c_right = st.columns(2)
    with c_left:
        st.subheader("1. Caption TikTok")
        st.info(f"""
        {info['hook']} 🌿
        Bí mật nằm ở **{info['chat']}**...
        👉 {info['cta']}
        #MoonFood #{key_name.replace(' + ','')} #Healthy
        """)
        st.divider()
        st.subheader("2. Prompt Ảnh Bìa (Midjourney)")
        # Prompt MJ thay đổi theo Style đã chọn
        st.code(f"/imagine prompt: {mj_style}. Subject: {subject_prompt}. Context: {recipe_full}. --ar 3:4", language='text')

    with c_right:
        st.subheader("3. Prompt Viết Bài (Blog)")
        st.code(f"Viết bài Facebook về {recipe_full}. Hook: '{info['hook']}'. Body: '{info['body']}'. Tone: Chuyên gia.", language='text')

# --- TAB 2: VIDEO ---
with tab_video:
    st.subheader(f"🎬 Sản xuất Video: {recipe_full}")
    st.caption(f"🎨 Style đang chọn: **{style_select}**")
    
    st.markdown("#### 🅰️ Kịch bản Voiceover (3 Phần)")
    c_v1, c_v2, c_v3 = st.columns(3)
    with c_v1: st.success(f"HOOK: \"{info['hook']}\"")
    with c_v2: st.info(f"BODY: \"{info['body']}\"")
    with c_v3: st.error(f"CTA: \"{info['cta']}\"")

    st.divider()
    
    st.markdown("#### 🅱️ Prompt Sora 2 (15s)")
    # Prompt Sora đã tích hợp Style (3D hoặc Người thật)
    sora_prompt = f"""
    8k, {mj_style}.
    Subject: {subject_prompt}.
    Style: {angle_data['style']}.
    Action: {angle_data['desc'].replace('Moon', angle_subject)} demonstrating health benefits.
    
    Speaking Line (Vietnamese): "{full_speaking_line}"
    Lip-sync instruction: Match naturally with Vietnamese dialogue.
    
    Constraint: ABSOLUTELY NO TEXT OVERLAYS, NO LOGOS, CLEAN BACKGROUND. --duration 15s
    """
    st.code(sora_prompt, language='text')
