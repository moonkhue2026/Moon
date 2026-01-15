import streamlit as st

st.set_page_config(page_title="Moon's Fresh Food", page_icon="🥗", layout="wide")

# =========================================================
# DỮ LIỆU
# =========================================================

categories = {
    "🍎 Trái cây (Fruits)": [
        "Táo", "Cam", "Chuối", "Dưa hấu", "Nho", "Thanh long", "Bơ",
        "Sầu riêng", "Măng cụt", "Vải thiều", "Nhãn", "Xoài", "Dâu tây"
    ],
    "🥦 Rau xanh (Vegetables)": [
        "Cải thìa", "Cà rốt", "Súp lơ", "Khổ qua", "Rau má", "Cà chua", "Khoai tây",
        "Rau ngót", "Bắp cải", "Bí đỏ", "Dưa leo"
    ],
    "🌶️ Gia vị & Thảo mộc (Spices)": [
        "Gừng", "Nghệ", "Sả", "Tỏi", "Hành tây", "Tiêu", "Ớt",
        "Ngải cứu", "Tía tô", "Lá mơ", "Diếp cá", "Húng quế"
    ]
}

themes = {
    "Dinh dưỡng & Vitamin": {
        "tone": "Tươi vui, năng động",
        "context": "Cung cấp vitamin, khoáng chất, năng lượng cho ngày mới",
        "action": "đang tỏa sáng, nhảy múa vui vẻ, hoặc cầm bảng vitamin"
    },
    "Mẹo vặt nhà bếp": {
        "tone": "Thủ thỉ, mách nhỏ",
        "context": "Cách chọn lựa ngon, cách bảo quản, sơ chế đúng cách",
        "action": "đang đeo tạp dề, thực hiện sơ chế hoặc chọn lựa kỹ càng"
    },
    "Món ngon bài thuốc": {
        "tone": "Ấm áp, chăm sóc",
        "context": "Món ăn giúp giải cảm, ấm bụng, tăng đề kháng",
        "action": "đang nấu ăn trong nồi súp/trà bốc khói nghi ngút"
    }
}

# =========================================================
# GIAO DIỆN CHÍNH
# =========================================================

st.title("🥗 MOON'S FOOD CREATOR (v5.0)")

# Cấu hình chung
c1, c2 = st.columns(2)
with c1:
    cat_select = st.selectbox("Chọn nhóm:", list(categories.keys()))
with c2:
    char_select = st.selectbox("Chọn nhân vật:", categories[cat_select])
    
theme_select = st.selectbox("Chủ đề:", list(themes.keys()))
current_theme = themes[theme_select]

# =========================================================
# TABS
# =========================================================

tab1, tab2 = st.tabs(["📝 BÀI VIẾT (CHATGPT)", "🎬 VIDEO (SORA/VEO)"])

with tab1:
    st.subheader("Copy lệnh cho ChatGPT:")
    st.code(f"Viết bài Facebook về lợi ích của {char_select}. Tone: {current_theme['tone']}. Hashtag: #DinhDuong #SongKhoe", language='text')

with tab2:
    st.markdown("### 🛠️ CẤU HÌNH VIDEO")
    
    # 3 CỘT TÙY CHỌN: STYLE - AI MODEL - DURATION
    col_v1, col_v2, col_v3 = st.columns(3)
    
    with col_v1:
        style_select = st.radio("1. Chọn Style:", ["3D Animation (Pixar)", "KOL (Người thật)"])
    
    with col_v2:
        model_select = st.radio("2. Chọn AI Model:", ["Sora (15s/cảnh + Lip-sync)", "Veo 3 (8s/cảnh)"])
    
    with col_v3:
        duration_option = st.radio("3. Thời lượng Video:", ["15s", "30s", "60s"], horizontal=True)

    st.divider()

    # --- XỬ LÝ LOGIC ---
    # 1. Định nghĩa Style
    if style_select == "3D Animation (Pixar)":
        subject_prompt = f"a cute anthropomorphic {char_select.split('(')[0]} character, Pixar style 3D"
        style_kw = "Disney Pixar style, vibrant colors, soft lighting, 8k"
        move = "bouncy animation"
    else:
        subject_prompt = f"a professional Vietnamese nutritionist (KOL), holding fresh {char_select.split('(')[0]}"
        style_kw = "Cinematic lighting, photorealistic, Arri Alexa, 8k"
        move = "professional gestures"

    # 2. Định nghĩa Kịch bản theo Thời lượng
    t_total = int(duration_option.replace("s", ""))
    segments = []

    if t_total == 15:
        segments = [
            ("HOOK", "Gây tò mò", f"Bạn có biết {char_select} là vua vitamin không?", "Character looks surprised holding item."),
            ("BODY", "Lợi ích", f"Ăn mỗi ngày giúp da đẹp, dáng xinh.", "Character eating happily and glowing."),
            ("CTA", "Kêu gọi", f"Thử ngay hôm nay nhé!", "Character thumbs up.")
        ]
    elif t_total == 30:
        segments = [
            ("HOOK", "Vấn đề", f"Sáng dậy uể oải, da dẻ sạm màu?", "Character looking tired in mirror."),
            ("BODY 1", "Giải pháp", f"Nạp ngay {char_select} vào thực đơn đi.", "Character presenting the fresh item."),
            ("BODY 2", "Kết quả", f"Vitamin C tự nhiên giúp bừng tỉnh sức sống.", "Character dancing energetically."),
            ("CTA", "Kêu gọi", f"Follow Moon để bỏ túi mẹo hay nha.", "Character wink.")
        ]
    else: # 60s
        segments = [
            ("HOOK", "Kể chuyện", f"Hồi xưa Moon không thích ăn {char_select} đâu.", "Character shaking head at item."),
            ("BODY 1", "Khám phá", f"Nhưng từ khi biết mẹo chế biến này, mê luôn.", "Character cooking/preparing item."),
            ("BODY 2", "Lợi ích", f"Không chỉ ngon mà còn thải độc cực tốt.", "Character showing strong muscles/shield."),
            ("CTA", "Thông điệp", f"Đừng bỏ qua siêu thực phẩm này nha.", "Character hugging item.")
        ]

    # 3. HIỂN THỊ KỊCH BẢN TÓM TẮT
    st.markdown("#### 📜 Kịch bản tóm tắt:")
    script_text = ""
    for name, role, vn, en in segments:
        script_text += f"- {name}: {vn}\n"
    st.info(script_text)
    
    # 4. TRẢ PROMPT (CHỈ HIỆN LOẠI ĐÃ CHỌN)
    st.subheader(f"🎥 Prompt tạo video ({model_select})")
    
    for name, role, vn, en in segments:
        st.markdown(f"**🎞️ {name}: {role}**")
        
        if "Sora" in model_select:
            # Code cho Sora
            prompt = f"""
            {style_kw}.
            Subject: {subject_prompt}.
            Action: {en} {move}.
            Speaking Line (Vietnamese): "{vn}"
            Lip-sync instruction: Match Vietnamese dialogue naturally.
            Context: {current_theme['context']}.
            Constraint: NO TEXT OVERLAYS.
            --duration 15s
            """
            st.code(prompt, language='text')
            
        else:
            # Code cho Veo 3
            prompt = f"""
            Cinematic shot, {subject_prompt}.
            Action: {en} {move}. Character is speaking.
            Atmosphere: {current_theme['tone']}.
            Style: {style_kw}.
            --duration 8s
            """
            st.code(prompt, language='text')
