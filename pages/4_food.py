import streamlit as st

st.set_page_config(page_title="Moon's Food Matrix v7.3", page_icon="🥗", layout="wide")

# =========================================================
# 1. CẤU HÌNH DỮ LIỆU (12 CÔNG THỨC & 4 GÓC ĐỘ)
# =========================================================

# Danh sách 12 Công thức Detox (Chuẩn theo ảnh Moon gửi)
detox_menu = [
    "1. Chanh + Tỏi (Sạch mạch máu)"import streamlit as st

st.set_page_config(page_title="Moon's Food Matrix v7.5", page_icon="🥗", layout="wide")

# =========================================================
# 1. KHO DỮ LIỆU THÔNG MINH (12 MÓN - 3 PHẦN KỊCH BẢN)
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
    "🎥 1. Hướng dẫn (How-to/ASMR)": {"style": "Macro shots, extreme close-up on textures, cutting sounds", "desc": "Quay cận cảnh quy trình sơ chế"},
    "🎓 2. Kiến thức (Education)": {"style": "Medium shot of Moon (or 3D Character) pointing to hologram chart", "desc": "Chuyên gia phân tích thành phần"},
    "⚠️ 3. Cảnh báo (Warning)": {"style": "Dramatic lighting, darker tone, serious expression", "desc": "Cảnh báo sai lầm thường gặp"},
    "📖 4. Câu chuyện (Story/Vlog)": {"style": "Handheld POV, sunny garden background, relaxing vibe", "desc": "Vlog tâm sự trải nghiệm cá nhân"}
}

# Database chưa Kịch bản chi tiết (Hook - Body - CTA) & Hoạt chất
nutrition_db = {
    "Chanh + Tỏi": {
        "chat": "Allicin & Vitamin C",
        "hook": "Uống xong người yêu chạy mất dép nhưng tim mạch thì khỏe re!",
        "body": "Vì Allicin trong tỏi kết hợp Vitamin C của chanh sẽ quét sạch mỡ máu cứng đầu.",
        "cta": "Thử ngay công thức này nhé!"
    },
    "Chanh + Gừng": {
        "chat": "Gingerol & Axit Citric",
        "hook": "Vừa ăn xong mà bụng căng tức khó chịu?",
        "body": "Hoạt chất Gingerol trong gừng sẽ làm ấm bụng và đẩy lùi cơn đau dạ dày ngay lập tức.",
        "cta": "Lưu lại công thức để dùng khi cần."
    },
    "Chanh + Nha đam": {
        "chat": "Polysaccharide & Collagen",
        "hook": "Da khô mốc meo dù đã dưỡng đủ thứ?",
        "body": "Nha đam cấp nước tầng sâu, còn chanh kích thích sản sinh Collagen tự nhiên cho da căng mướt.",
        "cta": "Uống đi chờ chi!"
    },
    "Chanh + Nghệ": {
        "chat": "Curcumin hoạt tính",
        "hook": "Đau dạ dày uống thuốc mãi không khỏi?",
        "body": "Curcumin trong nghệ là kháng sinh tự nhiên mạnh nhất, giúp chữa lành mọi vết loét.",
        "cta": "Kiên trì mỗi sáng nhé."
    },
    "Chanh + Mật ong": {
        "chat": "Enzyme kháng khuẩn",
        "hook": "Mùa này ai cũng sụt sịt, trừ mình!",
        "body": "Nhờ Enzyme trong mật ong giúp tăng cường hệ miễn dịch gấp 10 lần thuốc bổ.",
        "cta": "Tăng đề kháng ngay hôm nay."
    },
    "Trà chanh nóng": {
        "chat": "Theanine & Vitamin C",
        "hook": "Stress công việc muốn nổ tung đầu óc?",
        "body": "Theanine trong trà kết hợp hương chanh sẽ xoa dịu thần kinh và thanh lọc gan thận.",
        "cta": "Thư giãn cùng Moon nhé."
    },
    "Củ dền + Táo + Cà rốt": {
        "chat": "Sắt & Beta-carotene",
        "hook": "Đứng lên ngồi xuống là hoa mắt chóng mặt?",
        "body": "Công thức ABC huyền thoại này chứa đầy Sắt hữu cơ giúp bơm máu lên não tức thì.",
        "cta": "Bổ máu cực tốt, thử nha."
    },
    "Bơ + Dưa leo + Gừng": {
        "chat": "Omega-3 & Hydration",
        "hook": "Xương khớp cứ kêu rắc rắc khi trở trời?",
        "body": "Chất béo tốt Omega-3 từ bơ kết hợp gừng ấm giúp bôi trơn khớp và giảm viêm hiệu quả.",
        "cta": "Xay uống liền đi nè."
    },
    "Việt quất + Cà chua + Gừng": {
        "chat": "Lycopene & Anthocyanin",
        "hook": "Sợ già trước tuổi thì đừng bỏ qua ly này!",
        "body": "Lycopene và Anthocyanin là bộ đôi chống lão hóa, bảo vệ tế bào khỏi gốc tự do.",
        "cta": "Bí quyết trẻ mãi không già đó."
    },
    "Cam + Táo + Nghệ": {
        "chat": "Vitamin C & Curcumin",
        "hook": "Sáng ngủ dậy mà người cứ lờ đờ uể oải?",
        "body": "Cú hích Vitamin C và Nghệ này sẽ nạp năng lượng tỉnh táo mà không cần Cafein.",
        "cta": "Tỉnh táo ngay tức thì."
    },
    "Bưởi + Cà rốt + Gừng": {
        "chat": "Naringenin & Fiber",
        "hook": "Bụng dưới núng nính làm bạn mất tự tin?",
        "body": "Naringenin trong bưởi kích thích gan đốt cháy mỡ thừa ngay cả khi bạn đang ngủ.",
        "cta": "Eo thon đón tết nào."
    },
    "Kiwi + Xà lách + Gừng": {
        "chat": "Serotonin & Magie",
        "hook": "Đếm cừu tới sáng mà vẫn không ngủ được?",
        "body": "Ly nước xanh này chứa Serotonin tự nhiên giúp vỗ về giấc ngủ êm ái.",
        "cta": "Chúc bạn ngủ ngon nhé."
    }
}

# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🥗 MOON'S FOOD MATRIX v7.5")
st.markdown("*Phiên bản chuẩn: Hook/Body/CTA - Clean Video*")

# CẤU HÌNH
with st.expander("⚙️ CHỌN CÔNG THỨC & GÓC QUAY", expanded=True):
    c1, c2, c3 = st.columns([1, 2, 1])
    with c1: group = st.selectbox("Nhóm:", ["🥤 Smoothie (12 Món Vàng)", "🥗 Khác"])
    with c2: 
        if "Smoothie" in group: recipe_full = st.selectbox("Công thức:", detox_menu)
        else: recipe_full = st.text_input("Tên món:", "Salad Ức gà")
    with c3: angle_full = st.selectbox("Góc quay:", list(video_angles.keys()))

# XỬ LÝ DỮ LIỆU
if "Smoothie" in group: key_name = recipe_full.split(". ")[1].split(" (")[0]
else: key_name = recipe_full

# Lấy data mặc định nếu không tìm thấy
default_data = {"chat": "Dưỡng chất", "hook": "Món này ngon lắm!", "body": "Nó tốt cho sức khỏe.", "cta": "Thử nhé!"}
info = nutrition_db.get(key_name, default_data)
angle_data = video_angles[angle_full]

# Ghép câu thoại full (để đưa vào Prompt Sora)
full_speaking_line = f"{info['hook']} {info['body']} {info['cta']}"

# =========================================================
# HIỂN THỊ KẾT QUẢ (2 TAB)
# =========================================================

tab_content, tab_video = st.tabs(["📝 BÀI VIẾT & ẢNH (Làm trước)", "🎥 VIDEO SORA (Làm sau)"])

# --- TAB 1: NỘI DUNG ---
with tab_content:
    c_left, c_right = st.columns(2)
    
    with c_left:
        st.subheader("1. Caption TikTok/Reels")
        st.info(f"""
        {info['hook']} 🌿
        
        Bí mật nằm ở **{info['chat']}** giúp {key_name} hiệu quả bất ngờ!
        {info['body']}
        
        👉 {info['cta']}
        #MoonDetox #{key_name.replace(' + ','').replace(' ','')} #HealthyLifestyle
        """)
        
        st.divider()
        st.subheader("2. Prompt Ảnh Bìa (Midjourney)")
        mj_prompt = f"/imagine prompt: Professional food photography of **{key_name}** smoothie. Fresh ingredients ({key_name.replace(' + ',', ')}), cinematic lighting, 8k, bokeh background --ar 3:4"
        st.code(mj_prompt, language='text')

    with c_right:
        st.subheader("3. Prompt Viết Bài (Blog/Fanpage)")
        gpt_prompt = f"""
        Viết bài chia sẻ Facebook chi tiết về: **{recipe_full}**.
        - Hook mở đầu: "{info['hook']}"
        - Góc độ tiếp cận: {angle_full} ({angle_data['desc']}).
        - Phân tích hoạt chất: {info['chat']}.
        - Giải thích cơ chế: {info['body']}.
        - Kết bài (CTA): "{info['cta']}"
        - Văn phong: Chuyên gia dinh dưỡng, gần gũi, tin cậy.
        """
        st.code(gpt_prompt, language='text')

# --- TAB 2: VIDEO ---
with tab_video:
    st.subheader(f"🎬 Sản xuất Video: {recipe_full}")
    
    # KỊCH BẢN THU ÂM (Tách rõ 3 phần cho Moon đọc)
    st.markdown("#### 🅰️ Kịch bản Voiceover (Thu âm trên CapCut)")
    st.warning("🎙️ Moon đọc diễn cảm theo 3 phần dưới đây:")
    col_v1, col_v2, col_v3 = st.columns(3)
    with col_v1: 
        st.markdown("**1. HOOK (3s)**")
        st.success(f"\"{info['hook']}\"")
    with col_v2:
        st.markdown("**2. BODY (Main)**")
        st.info(f"\"{info['body']}\"")
    with col_v3:
        st.markdown("**3. CTA (End)**")
        st.error(f"\"{info['cta']}\"")

    st.divider()
    
    # PROMPT SORA (SẠCH SẼ - KHÔNG TEXT)
    st.markdown("#### 🅱️ Prompt Sora 2 (15s)")
    st.caption("✅ Đã bao gồm lệnh 'Speaking Line' đầy đủ 3 phần & Chặn Text/Logo.")
    
    sora_prompt = f"""
    8k, High-end Food Cinematography.
    Subject: Fresh ingredients (**{key_name}**) transforming into a delicious smoothie.
    Style: {angle_data['style']}.
    Action: {angle_data['desc']} showing the health benefits.
    
    Speaking Line (Vietnamese): "{full_speaking_line}"
    Lip-sync instruction: Match naturally with Vietnamese dialogue.
    
    Constraint: ABSOLUTELY NO TEXT OVERLAYS, NO LOGOS, NO SUBTITLES, CLEAN BACKGROUND. --duration 15s
    """
    st.code(sora_prompt, language='text')
