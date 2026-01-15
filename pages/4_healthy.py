import streamlit as st

# Cài đặt trang web
st.set_page_config(page_title="Moon's Health Creator", page_icon="🥑", layout="wide")

# =========================================================
# 1. DỮ LIỆU DANH MỤC
# =========================================================

categories = {
    "🍎 Trái cây (Fruits)": [
        "Táo", "Cam", "Chuối", "Dưa hấu", "Nho", "Thanh long", "Bơ",
        "Sầu riêng", "Măng cụt", "Vải thiều", "Nhãn", "Xoài", "Dâu tây", 
        "Ổi", "Mận", "Đu đủ", "Vú sữa", "Mãng cầu"
    ],
    "🌿 Rau củ & Dược liệu (Veg & Herbs)": [
        "Cải thìa", "Cà rốt", "Súp lơ", "Khổ qua", "Rau má", "Cà chua", "Khoai tây",
        "Ngải cứu", "Lá mơ", "Tía tô", "Diếp cá", "Húng quế", "Sả", "Gừng", "Nghệ",
        "Hành tây", "Cần tây", "Rau ngót", "Bắp cải", "Bí đỏ"
    ],
    "🫀 Nội tạng & Cơ thể (Organs)": [
        "Tim", "Gan", "Dạ dày (Bao tử)", "Phổi", "Thận", "Ruột non", "Đại tràng",
        "Não", "Xương khớp", "Mắt", "Làn da"
    ]
}

themes = {
    "Sức khỏe (Cảnh báo)": {
        "tone": "Nghiêm túc, cảnh báo",
        "context": "Tác hại, Sai lầm khi ăn uống, Bệnh tật tiềm ẩn",
        "action": "đang đau đớn, ôm bụng/đầu, hoặc giơ dấu X đỏ cảnh báo"
    },
    "Mẹo dân gian (Chữa bệnh)": {
        "tone": "Thủ thỉ, chia sẻ bí quyết",
        "context": "Bài thuốc nam, Mẹo vặt chữa bệnh không dùng thuốc",
        "action": "đang pha chế, cầm thảo dược, hoặc giơ ngón cái (Like)"
    },
    "Ẩm thực & Dinh dưỡng": {
        "tone": "Vui vẻ, năng động",
        "context": "Công dụng tuyệt vời, Món ngon mỗi ngày",
        "action": "đang nhảy múa, nấu ăn, hoặc tận hưởng món ngon"
    }
}

# =========================================================
# GIAO DIỆN APP
# =========================================================

st.title("🥑 MOON'S HEALTH CREATOR (v4.1)")
st.markdown("*Kiến tạo Video triệu view: Rau củ - Trái cây - Sức khỏe*")

# --- BƯỚC 1: CẤU HÌNH (SIDEBAR HOẶC TOP) ---
c1, c2, c3 = st.columns(3)
with c1:
    cat_select = st.selectbox("Chọn nhóm:", list(categories.keys()))
    char_select = st.selectbox("Chọn nhân vật:", categories[cat_select])
with c2:
    theme_select = st.selectbox("Chủ đề:", list(themes.keys()))
    duration_option = st.select_slider("Thời lượng video:", options=["15s", "30s", "45s", "60s"], value="30s")
with c3:
    quality = st.selectbox("Chất lượng:", ["8K", "4K"])

# Xử lý Logic Data
current_theme = themes[theme_select]
ar_param = "--ar 9:16"

# Tạo dữ liệu phân đoạn (Segments) dựa trên thời lượng
t_total = int(duration_option.replace("s", ""))
segments = []

# Logic chia kịch bản
if t_total == 15:
    segments = [
        ("HOOK (0-5s)", "Gây tò mò/Sốc", f"Biết gì chưa? {char_select} không chỉ để ăn đâu nha!", f"Character looks shocked/surprised holding {char_select}."),
        ("BODY (5-10s)", "Giải thích nhanh", f"Nó giúp trị bệnh cực hay mà ít ai biết.", f"Character explains excitedly, pointing at {char_select}."),
        ("CTA (10-15s)", "Kêu gọi", f"Thử ngay đi nhé, hiệu quả lắm đó!", f"Character winks and gives thumbs up.")
    ]
elif t_total == 30:
    segments = [
        ("HOOK (0-5s)", "Vấn đề/Nỗi đau", f"Ai đang bị đau nhức/mệt mỏi thì bơi vào đây ngay!", f"Character looks in pain or worried."),
        ("BODY 1 (5-15s)", "Giới thiệu giải pháp", f"Chỉ cần dùng {char_select} theo cách này là êm ru.", f"Character shows {char_select} glowing with magic effect."),
        ("BODY 2 (15-25s)", "Hướng dẫn/Kết quả", f"Dùng liên tục 3 ngày là thấy khác biệt liền.", f"Character demonstrates usage happily."),
        ("CTA (25-30s)", "Kêu gọi", f"Lưu lại ngay kẻo trôi bài nha cả nhà!", f"Character waves goodbye.")
    ]
elif t_total == 45:
    segments = [
        ("HOOK (0-5s)", "Cảnh báo", f"Dừng lại! Đừng ăn {char_select} nếu chưa biết điều này.", f"Character makes a 'STOP' gesture."),
        ("BODY 1 (5-20s)", "Giải thích sai lầm", f"Nhiều người cứ tưởng tốt, nhưng dùng sai là hại người đó.", f"Character shakes head, showing a red X sign."),
        ("BODY 2 (20-35s)", "Hướng dẫn đúng", f"Cách đúng là phải làm như thế này nè...", f"Character showing the correct method carefully."),
        ("CTA (35-45s)", "Kết luận", f"Nhớ chia sẻ cho người thân cùng biết nhé.", f"Character blows a kiss.")
    ]
else: # 60s
    segments = [
        ("HOOK (0-10s)", "Kể chuyện/Drama", f"Hồi xưa Moon hay bị ốm vặt lắm, khổ sở vô cùng.", f"Character looking sad/sick in bed."),
        ("BODY 1 (10-25s)", "Khám phá", f"Tình cờ được bà hàng xóm mách cho mẹo dùng {char_select}.", f"Character discovering {char_select} in the garden."),
        ("BODY 2 (25-45s)", "Trải nghiệm & Kết quả", f"Kiên trì áp dụng, giờ khỏe re, da dẻ hồng hào.", f"Character transformation from sick to strong/happy."),
        ("CTA (45-60s)", "Thông điệp", f"Sức khỏe là vàng. Hãy chăm sóc bản thân từ những thứ tự nhiên nhất nha.", f"Character hugging {char_select} affectionately.")
    ]

# Tổng hợp kịch bản tóm tắt để hiển thị
full_script_text = f"CHỦ ĐỀ: {char_select} - {theme_select} ({duration_option})\n\n"
for name, role, script_vn, _ in segments:
    full_script_text += f"🔸 {name} - {role}: \"{script_vn}\"\n"

# =========================================================
# TABS HIỂN THỊ (GIAO DIỆN CŨ)
# =========================================================

tab1, tab2 = st.tabs(["📝 BÀI VIẾT (CHATGPT)", "🎬 VIDEO (SORA & MIDJOURNEY)"])

# --- TAB 1: BÀI VIẾT ---
with tab1:
    st.subheader("Copy lệnh này cho ChatGPT để viết bài chia sẻ:")
    blog_prompt = f"""
    Đóng vai chuyên gia sức khỏe (Moon). Hãy viết một bài đăng Facebook chia sẻ kiến thức về: **{char_select}**.
    - Chủ đề: {current_theme['context']}.
    - Đối tượng: Những người quan tâm sức khỏe, nội trợ.
    - Nội dung:
      1. Nêu rõ Công dụng chính (hoặc Tác hại nếu dùng sai).
      2. Dẫn chứng khoa học hoặc mẹo dân gian.
      3. Lời khuyên của Moon.
    - Tone giọng: {current_theme['tone']}, gần gũi, tin cậy.
    - Hashtag: #{char_select.replace(' ','')} #SongKhoeCungMoon #MeoDanGian
    """
    st.code(blog_prompt, language='text')

# --- TAB 2: VIDEO ---
with tab2:
    # 1. KỊCH BẢN TÓM TẮT
    st.subheader("📜 Kịch bản tóm tắt:")
    st.code(full_script_text, language='text')
    
    st.divider()

    # 2. CHỌN STYLE & THUMBNAIL
    video_style = st.radio("Chọn phong cách video:", ["3D Animation (Pixar/Disney)", "KOL (Người thật)"], horizontal=True)
    
    # Logic Style Prompt
    if video_style == "3D Animation (Pixar/Disney)":
        subject_prompt = f"a cute anthropomorphic {char_select.split('(')[0]} character, big expressive eyes, Pixar style 3D render"
        style_keywords = "3D animation, Disney Pixar style, vibrant colors, soft studio lighting, high fidelity, 8k"
        movement_desc = "bouncy, squash and stretch animation"
        action_verb = "animating"
    else:
        subject_prompt = f"a professional Vietnamese health expert (KOL), friendly face, holding fresh {char_select.split('(')[0]}"
        style_keywords = "Cinematic lighting, photorealistic, shot on Arri Alexa, 8k, professional commercial look"
        movement_desc = "natural, professional gestures"
        action_verb = "acting"

    st.subheader("🎨 Prompt Ảnh Thumbnail (Midjourney):")
    prompt_mj = f"/imagine prompt: {subject_prompt}, {action_verb} in a scene about {theme_select}. {style_keywords}, 8k --ar 9:16"
    st.code(prompt_mj, language='text')

    st.divider()

    # 3. PROMPT VIDEO (SORA & VEO)
    st.subheader(f"🎥 Tạo Video (Sora & Veo)")
    
    # Vòng lặp hiển thị từng phân cảnh
    for name, role, script_vn, action_en in segments:
        st.markdown(f"#### 🎞️ {name}: {role}")
        st.caption(f"💡 Nội dung: {script_vn}")
        
        c_veo, c_sora = st.columns(2)
        
        # VEO 3 PROMPT (8s)
        with c_veo:
            st.info("🤖 **VEO 3 (8s)**")
            veo_prompt = f"""
            Cinematic shot, {subject_prompt}.
            Action: {action_en} {movement_desc}. Character is speaking.
            Atmosphere: {current_theme['tone']}.
            Style: {style_keywords}.
            --duration 8s
            """
            st.code(veo_prompt, language='text')
            with st.expander("Dịch Veo"):
                st.write(f"Hành động: {action_en}")
                st.write("Thời lượng: 8 giây (Chuẩn Veo).")

        # SORA PROMPT (15s)
        with c_sora:
            st.error("🦅 **SORA (15s)**")
            sora_prompt = f"""
            {style_keywords}.
            Subject: {subject_prompt}.
            Action: {action_en} {movement_desc}.
            Speaking Line (Vietnamese): "{script_vn}"
            Lip-sync instruction: Mouth moves naturally matching Vietnamese dialogue.
            Scene Context: {current_theme['context']}.
            Constraint: NO TEXT OVERLAYS.
            {ar_param} --duration 15s
            """
            st.code(sora_prompt, language='text')
            with st.expander("Dịch Sora"):
                st.write(f"Hành động: {action_en}")
                st.write(f"Thoại nhép: '{script_vn}'")
                st.write("Thời lượng: 15 giây.")
        
        st.divider()
