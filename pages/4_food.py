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
        "tone": "Thủ thỉ, mách nhỏ (Life Hacks)",
        "context": "Cách chọn lựa ngon, cách bảo quản, sơ chế đúng cách",
        "action": "đang đeo tạp dề, thực hiện sơ chế hoặc chọn lựa kỹ càng"
    },
    "Món ngon bài thuốc": {
        "tone": "Ấm áp, chăm sóc (Healing)",
        "context": "Món ăn giúp giải cảm, ấm bụng, tăng đề kháng",
        "action": "đang nấu ăn trong nồi súp/trà bốc khói nghi ngút"
    }
}

# =========================================================
# GIAO DIỆN CHÍNH
# =========================================================

st.title("🥗 MOON'S FOOD CREATOR (v5.1)")

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
    st.code(f"Viết bài Facebook về {theme_select} của {char_select}. Tone: {current_theme['tone']}. Hashtag: #DinhDuong #SongKhoe", language='text')

with tab2:
    st.markdown("### 🛠️ CẤU HÌNH VIDEO")
    
    # 3 CỘT TÙY CHỌN
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

    # 2. ĐỊNH NGHĨA KỊCH BẢN CHI TIẾT (THEO CHỦ ĐỀ RIÊNG BIỆT)
    t_total = int(duration_option.replace("s", ""))
    segments = []

    # === CHỦ ĐỀ 1: DINH DƯỠNG (Năng lượng, Đẹp da) ===
    if "Dinh dưỡng" in theme_select:
        if t_total == 15:
            segments = [
                ("HOOK", "Gây tò mò", f"Bạn có biết {char_select} là vua vitamin không?", "Character looks surprised holding item."),
                ("BODY", "Lợi ích", f"Ăn mỗi ngày giúp da đẹp, dáng xinh.", "Character eating happily and glowing."),
                ("CTA", "Kêu gọi", f"Thử ngay hôm nay nhé!", "Character thumbs up.")
            ]
        elif t_total == 30:
            segments = [
                ("HOOK", "Vấn đề", f"Sáng dậy uể oải, da dẻ sạm màu? Thiếu vitamin rồi đó!", "Character looking tired in mirror."),
                ("BODY 1", "Giải pháp", f"Nạp ngay {char_select} vào thực đơn đi.", "Character presenting the fresh item."),
                ("BODY 2", "Kết quả", f"Vitamin tự nhiên giúp bừng tỉnh sức sống tức thì.", "Character dancing energetically."),
                ("CTA", "Kêu gọi", f"Follow Moon để bỏ túi mẹo hay nha.", "Character wink.")
            ]
        else: # 60s
            segments = [
                ("HOOK", "Kể chuyện", f"Hồi xưa Moon hay bị ốm vặt lắm, sức đề kháng kém cực kỳ.", "Character looking weak/sad."),
                ("BODY 1", "Khám phá", f"Tìm hiểu mới biết mình bỏ quên siêu thực phẩm {char_select}.", "Character studying nutrition book."),
                ("BODY 2", "Phân tích", f"Nó chứa hàm lượng khoáng chất gấp đôi các loại thường.", "Character pointing to chart/graph."),
                ("CTA", "Thông điệp", f"Đừng uống thuốc bổ vội, hãy ăn {char_select} trước đã nha.", "Character hugging item.")
            ]

    # === CHỦ ĐỀ 2: MẸO VẶT (Cách chọn, Cách gọt, Bảo quản) ===
    elif "Mẹo vặt" in theme_select:
        if t_total == 15:
            segments = [
                ("HOOK", "Sai lầm", f"Đừng vứt vỏ {char_select} đi! Sai lầm to đó!", "Character stopping someone from throwing away peel."),
                ("BODY", "Mẹo hay", f"Vỏ của nó dùng để khử mùi tủ lạnh cực đỉnh.", "Character putting peel in fridge."),
                ("CTA", "Kêu gọi", f"Lưu lại mẹo này ngay!", "Character nodding.")
            ]
        elif t_total == 30:
            segments = [
                ("HOOK", "Thách thức", f"Làm sao chọn được quả {char_select} ngon trăm quả như một?", "Character looking confused at market."),
                ("BODY 1", "Bí kíp", f"Nhìn vào cuống này nè. Cuống tươi là quả mới hái.", "Character using magnifying glass on item."),
                ("BODY 2", "Kết quả", f"Áp dụng cách này đảm bảo không bao giờ mua phải quả hỏng.", "Character picking perfect fruits."),
                ("CTA", "Kêu gọi", f"Bà nội trợ nào chưa biết thì share liền nha.", "Character blowing kiss.")
            ]
        else: # 60s
            segments = [
                ("HOOK", "Nỗi đau", f"Mua {char_select} về để tủ lạnh 2 ngày là héo queo, tiếc đứt ruột.", "Character holding withered item crying."),
                ("BODY 1", "Hướng dẫn", f"Để Moon chỉ cách bảo quản tươi cả tuần nha. Đầu tiên cần giấy báo...", "Character wrapping item in paper."),
                ("BODY 2", "Thực hành", f"Sau đó cho vào hộp kín, nhớ đừng rửa nước trước nhé.", "Character putting box in fridge."),
                ("CTA", "Kết quả", f"Giờ thì ăn dần cả tuần vẫn giòn ngọt. Thử đi các bà!", "Character eating fresh item happily.")
            ]

    # === CHỦ ĐỀ 3: MÓN NGON (Nấu ăn, Chế biến) ===
    else: 
        if t_total == 15:
            segments = [
                ("HOOK", "Thèm thuồng", f"Trời lạnh thế này mà có bát canh {char_select} thì hết sảy!", "Character shivering then thinking of food."),
                ("BODY", "Chế biến", f"Nấu cùng thịt băm, thêm xíu hành ngò thơm nức mũi.", "Character stirring pot."),
                ("CTA", "Kêu gọi", f"Vào bếp triển ngay thôi!", "Character holding spoon.")
            ]
        elif t_total == 30:
            segments = [
                ("HOOK", "Câu hỏi", f"Mọi người thường ăn {char_select} như thế nào? Luộc hay xào?", "Character holding item asking."),
                ("BODY 1", "Biến tấu", f"Hôm nay Moon làm món gỏi {char_select} chua ngọt siêu bắt cơm.", "Character chopping fast like chef."),
                ("BODY 2", "Thưởng thức", f"Vị giòn sần sật, thấm đẫm gia vị, ăn là ghiền.", "Character tasting and eye widening."),
                ("CTA", "Kêu gọi", f"Ai muốn xin công thức thì comment 'Mlem' nha.", "Character showing finished dish.")
            ]
        else: # 60s
            segments = [
                ("HOOK", "Tâm sự", f"Có những ngày mệt mỏi chỉ muốn ăn món gì đó thanh đạm chữa lành.", "Character sighing."),
                ("BODY 1", "Vào bếp", f"Và {char_select} hấp cách thủy là lựa chọn số 1 của Moon.", "Character steaming item gently."),
                ("BODY 2", "Cảm nhận", f"Giữ nguyên độ ngọt, không dầu mỡ, tốt cho dạ dày cực kỳ.", "Character smelling aroma."),
                ("CTA", "Kết luận", f"Hạnh phúc đôi khi chỉ là một bữa ăn ngon. Chúc cả nhà ngon miệng!", "Character smiling peacefully.")
            ]

    # 3. HIỂN THỊ KỊCH BẢN TÓM TẮT
    st.markdown("#### 📜 Kịch bản tóm tắt:")
    script_text = ""
    for name, role, vn, en in segments:
        script_text += f"- {name}: {vn}\n"
    st.info(script_text)
    
    # 4. TRẢ PROMPT
    st.subheader(f"🎥 Prompt tạo video ({model_select})")
    
    for name, role, vn, en in segments:
        st.markdown(f"**🎞️ {name}: {role}**")
        
        if "Sora" in model_select:
            # Code Sora
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
            # Code Veo 3
            prompt = f"""
            Cinematic shot, {subject_prompt}.
            Action: {en} {move}. Character is speaking.
            Atmosphere: {current_theme['tone']}.
            Style: {style_kw}.
            --duration 8s
            """
            st.code(prompt, language='text')
