import streamlit as st

# Cài đặt trang web
st.set_page_config(page_title="Moon's Health Creator", page_icon="🥑", layout="wide")

# =========================================================
# 1. DỮ LIỆU DANH MỤC (ĐÃ BỔ SUNG KHỦNG)
# =========================================================

categories = {
    "🍎 Trái cây (Fruits)": [
        "Táo", "Cam", "Chuối", "Dưa hấu", "Nho", "Thanh long", "Bơ",
        "Sầu riêng", "Măng cụt", "Vải thiều", "Nhãn", "Xoài", "Dâu tây", 
        "Ổi", "Mận (Hà Nội)", "Đu đủ", "Vú sữa", "Mãng cầu"
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
        "tone": "Nghiêm túc nhưng hình ảnh dễ thương, cảnh báo thói quen xấu.",
        "action": "đang đau đớn, ôm bụng/đầu, hoặc giơ biển báo cấm (dấu X).",
        "setting": "Phòng khám hiện đại hoặc Bên trong cơ thể (trừu tượng)."
    },
    "Mẹo dân gian": {
        "tone": "Thủ thỉ, chia sẻ bí quyết, gần gũi.",
        "action": "đang pha chế, cầm thảo dược, hoặc thì thầm bí mật.",
        "setting": "Gian bếp ấm cúng hoặc Vườn thuốc nam."
    },
    "Ẩm thực & Đời sống": {
        "tone": "Dí dỏm, vui nhộn, tận hưởng cuộc sống.",
        "action": "đang nhảy múa, nấu ăn, hoặc tắm nắng (chill).",
        "setting": "Gian bếp sang trọng hoặc Bàn tiệc ngoài trời."
    }
}

# =========================================================
# GIAO DIỆN APP
# =========================================================

st.title("🥑 MOON'S HEALTH CREATOR (Pro Version)")
st.markdown("*Kiến tạo Video triệu view: Đa dạng Rau củ - Tùy biến Thời lượng*")

# --- BƯỚC 1: CHỌN CHỦ ĐỀ & NHÂN VẬT ---
st.header("1️⃣ CHỦ ĐỀ & NHÂN VẬT")
c1, c2, c3 = st.columns(3)

with c1:
    cat_select = st.selectbox("Chọn nhóm:", list(categories.keys()))

with c2:
    char_select = st.selectbox("Chọn nhân vật chính:", categories[cat_select])

with c3:
    theme_select = st.selectbox("Chủ đề nội dung:", list(themes.keys()))

# --- BƯỚC 2: CÀI ĐẶT SẢN XUẤT ---
st.header("2️⃣ CÀI ĐẶT SẢN XUẤT")
col_s1, col_s2, col_s3 = st.columns(3)

with col_s1:
    style_select = st.radio("Phong cách Visual:", ["3D Animation (Pixar/Disney)", "KOL (Chuyên gia thật)"], horizontal=True)

with col_s2:
    # THANH TRƯỢT THỜI LƯỢNG (LINH HOẠT)
    duration_option = st.select_slider("Thời lượng video:", options=["15s (Shorts)", "30s (Tiêu chuẩn)", "60s (Video dài)"], value="30s (Tiêu chuẩn)")

with col_s3:
    quality = st.selectbox("Chất lượng:", ["8K", "4K"])

# --- XỬ LÝ LOGIC ---
current_theme = themes[theme_select]
ar_param = "--ar 9:16" # Mặc định dọc cho Shorts/Reels

# Tách chuỗi thời lượng để lấy số giây
total_seconds = int(duration_option.split("s")[0]) 

# Tính toán thời lượng từng phân cảnh (Tỷ lệ vàng: Hook ngắn - Body dài - CTA ngắn)
if total_seconds == 15:
    t_hook, t_body, t_cta = "5s", "5s", "5s"
elif total_seconds == 30:
    t_hook, t_body, t_cta = "5s", "20s", "5s"
else: # 60s
    t_hook, t_body, t_cta = "10s", "40s", "10s"

# Mô tả nhân vật dựa trên Style
if style_select == "3D Animation (Pixar/Disney)":
    subject_prompt = f"a cute anthropomorphic {char_select.split('(')[0]} character, big expressive eyes, Pixar style 3D render"
    style_keywords = "3D animation, Disney Pixar style, vibrant colors, soft studio lighting, high fidelity, octane render, 8k"
    movement_desc = "movements are bouncy, squash and stretch animation style"
else:
    subject_prompt = f"a professional Vietnamese health expert (KOL), friendly face, holding a fresh {char_select.split('(')[0]}"
    style_keywords = "Cinematic lighting, photorealistic, shot on Arri Alexa, 8k, sharp focus, professional commercial look"
    movement_desc = "movements are natural, professional and engaging"

# =========================================================
# TABS HIỂN THỊ
# =========================================================

tab1, tab2 = st.tabs(["📝 KỊCH BẢN (AI WRITER)", "🎬 PROMPT VIDEO (VEO & SORA)"])

with tab1:
    st.subheader("Copy lệnh này cho ChatGPT/Claude để viết kịch bản chi tiết:")
    
    # Tạo prompt cho AI Writer
    ai_writer_prompt = f"""
    Bạn là chuyên gia sáng tạo nội dung TikTok triệu view. Hãy viết kịch bản video ({duration_option}) về:
    - Nhân vật chính: {char_select} (Được nhân hóa).
    - Chủ đề: {theme_select}.
    - Phong cách: {current_theme['tone']}
    
    YÊU CẦU CẤU TRÚC:
    1. HOOK (0-{t_hook.replace('s','')}s): Tình huống gây tò mò hoặc giật gân (Ví dụ: {char_select} {current_theme['action']}).
    2. BODY ({t_hook.replace('s','')}s-{int(t_hook.replace('s',''))+int(t_body.replace('s',''))}s): 
       - Giải thích vấn đề hoặc kể chuyện.
       - Thoại: Ngắn gọn, bắt trend, hài hước.
    3. CTA (Cuối): Kêu gọi hành động (Follow, Tim, Share).
    
    Định dạng đầu ra: Bảng phân cảnh (Thời lượng - Hình ảnh mô tả - Lời thoại tiếng Việt).
    """
    st.code(ai_writer_prompt, language='text')

with tab2:
    st.subheader(f"🎥 Prompt tạo video (Chủ đề: {char_select} | {duration_option})")
    st.caption(f"💡 Hệ thống tự động chia thời lượng: Hook ({t_hook}) - Body ({t_body}) - CTA ({t_cta})")

    # PHÂN ĐOẠN 1: HOOK
    st.markdown("### 🎞️ PHÂN CẢNH 1: HOOK (Gây chú ý)")
    c_hook_1, c_hook_2 = st.columns(2)
    
    with c_hook_1:
        st.info("🤖 **VEO 3 Prompt**")
        veo_hook = f"""
        Cinematic shot, {subject_prompt}. 
        Action: The character is {current_theme['action']} looking straight at the camera with a shocked or funny expression. {movement_desc}.
        Background: {current_theme['setting']}, blurred background.
        Style: {style_keywords}.
        """
        st.code(veo_hook, language='text')
        
    with c_hook_2:
        st.error("🦅 **SORA Prompt**")
        sora_hook = f"""
        {style_keywords}.
        Subject: {subject_prompt}.
        Scene: Close-up shot. The character {current_theme['action']}.
        Atmosphere: Energetic and engaging. High texture quality on the {char_select}.
        Constraint: NO TEXT OVERLAYS.
        {ar_param} --duration {t_hook}
        """
        st.code(sora_hook, language='text')

    st.divider()

    # PHÂN ĐOẠN 2: BODY
    st.markdown("### 🎞️ PHÂN CẢNH 2: BODY (Nội dung chính)")
    c_body_1, c_body_2 = st.columns(2)
    
    with c_body_1:
        st.info("🤖 **VEO 3 Prompt**")
        veo_body = f"""
        Medium shot, {subject_prompt}.
        Action: The character is explaining/dancing/interacting with props about {theme_select}. {movement_desc}.
        Lighting: Warm, cozy lighting emphasizing the freshness/health aspect.
        Style: {style_keywords}.
        """
        st.code(veo_body, language='text')
        
    with c_body_2:
        st.error("🦅 **SORA Prompt**")
        sora_body = f"""
        {style_keywords}.
        Subject: {subject_prompt}.
        Scene: Wide shot showing the character in {current_theme['setting']}.
        Action: The character is actively demonstrating the tip or warning. Dynamic camera movement.
        Constraint: NO TEXT OVERLAYS.
        {ar_param} --duration {t_body}
        """
        st.code(sora_body, language='text')

    st.divider()

    # PHÂN ĐOẠN 3: CTA
    st.markdown("### 🎞️ PHÂN CẢNH 3: CTA (Kêu gọi)")
    c_cta_1, c_cta_2 = st.columns(2)
    
    with c_cta_1:
        st.info("🤖 **VEO 3 Prompt**")
        veo_cta = f"""
        Close-up, {subject_prompt}.
        Action: The character winks, gives a thumbs up, or points to the 'Subscribe' button area. Smiling happily.
        Style: {style_keywords}.
        """
        st.code(veo_cta, language='text')
        
    with c_cta_2:
        st.error("🦅 **SORA Prompt**")
        sora_cta = f"""
        {style_keywords}.
        Subject: {subject_prompt}.
        Action: Friendly gesture, waving goodbye or blowing a kiss.
        Atmosphere: Positive and inviting.
        Constraint: NO TEXT OVERLAYS.
        {ar_param} --duration {t_cta}
        """
        st.code(sora_cta, language='text')
