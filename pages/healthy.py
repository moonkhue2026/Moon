import streamlit as st

# Cài đặt trang web
st.set_page_config(page_title="Moon's Health Creator", page_icon="🥑", layout="wide")

# =========================================================
# DỮ LIỆU DANH MỤC
# =========================================================

categories = {
    "🍎 Trái cây (Fruits)": ["Táo", "Cam", "Chuối", "Dưa hấu", "Nho", "Thanh long", "Bơ"],
    "🥦 Rau củ (Vegetables)": ["Cải thìa", "Cà rốt", "Súp lơ", "Khổ qua", "Rau má", "Cà chua", "Khoai tây"],
    "🫀 Nội tạng & Cơ thể (Organs)": ["Tim", "Gan", "Dạ dày (Bao tử)", "Phổi", "Thận", "Ruột non", "Não"]
}

themes = {
    "Sức khỏe (Cảnh báo)": {
        "tone": "Nghiêm túc nhưng hình ảnh dễ thương, cảnh báo thói quen xấu.",
        "action": "đang đau đớn, ôm bụng/đầu, hoặc giơ biển báo cấm.",
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

st.title("🥑 MOON'S HEALTH CREATOR (3D & KOL)")
st.markdown("*Kiến tạo kịch bản & Video triệu view: Rau củ - Trái cây - Sức khỏe*")

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
    ratio = st.selectbox("Tỷ lệ khung hình:", ["9:16 (TikTok/Reels)", "16:9 (Youtube)"])

with col_s3:
    quality = st.selectbox("Chất lượng:", ["8K", "4K"])

# --- XỬ LÝ DỮ LIỆU ---
current_theme = themes[theme_select]
ar_param = "--ar 9:16" if ratio == "9:16 (TikTok/Reels)" else "--ar 16:9"

# Mô tả nhân vật dựa trên Style
if style_select == "3D Animation (Pixar/Disney)":
    subject_prompt = f"a cute anthropomorphic {char_select.split('(')[0]} character, big expressive eyes, Pixar style 3D render"
    style_keywords = "3D animation, Disney Pixar style, vibrant colors, soft studio lighting, high fidelity, octane render, 8k"
else:
    subject_prompt = f"a professional Vietnamese health expert (KOL), friendly face, holding a fresh {char_select.split('(')[0]}"
    style_keywords = "Cinematic lighting, photorealistic, shot on Arri Alexa, 8k, sharp focus, professional commercial look"

# =========================================================
# TABS HIỂN THỊ
# =========================================================

tab1, tab2 = st.tabs(["📝 KỊCH BẢN (AI WRITER)", "🎬 PROMPT VIDEO (VEO & SORA)"])

with tab1:
    st.subheader("Copy lệnh này cho ChatGPT/Claude để viết kịch bản:")
    
    # Tạo prompt cho AI Writer
    ai_writer_prompt = f"""
    Bạn là chuyên gia sáng tạo nội dung TikTok triệu view. Hãy viết kịch bản video ngắn (30-45s) về:
    - Nhân vật chính: {char_select} (Được nhân hóa).
    - Chủ đề: {theme_select}.
    - Phong cách: {current_theme['tone']}
    
    YÊU CẦU CẤU TRÚC:
    1. HOOK (0-5s): Tình huống gây tò mò hoặc giật gân (Ví dụ: {char_select} {current_theme['action']}).
    2. BODY (5-30s): 
       - Nếu là Cảnh báo: Nêu hậu quả và cách phòng tránh.
       - Nếu là Vui vẻ: Kể câu chuyện dí dỏm hoặc nhảy múa.
       - Thoại: Ngắn gọn, bắt trend.
    3. CTA (30-45s): Kêu gọi hành động (Follow, Tim, Share).
    
    Định dạng đầu ra: Bảng phân cảnh (Thời lượng - Hình ảnh mô tả - Lời thoại).
    """
    st.code(ai_writer_prompt, language='text')

with tab2:
    st.subheader(f"🎥 Prompt tạo video (Chủ đề: {char_select})")
    
    # PHÂN ĐOẠN 1: HOOK
    st.markdown("### 🎞️ PHÂN CẢNH 1: HOOK (Gây chú ý)")
    c_hook_1, c_hook_2 = st.columns(2)
    
    with c_hook_1:
        st.info("🤖 **VEO 3 Prompt**")
        veo_hook = f"""
        Cinematic shot, {subject_prompt}. 
        Action: The character is {current_theme['action']} looking straight at the camera with a shocked or funny expression.
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
        Atmosphere: Energetic and engaging.
        Details: High texture quality on the {char_select}.
        {ar_param} --duration 5s
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
        Action: The character is explaining/dancing/interacting with props. Movements are fluid and bouncy (if 3D).
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
        Action: The character is actively demonstrating the tip or warning.
        Constraint: NO TEXT OVERLAYS.
        {ar_param} --duration 15s
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
        {ar_param} --duration 5s
        """
        st.code(sora_cta, language='text')

# =========================================================
# GHI CHÚ
# =========================================================
st.sidebar.markdown("---")
st.sidebar.caption("🌙 **Moon's Tips:**")
st.sidebar.info("""
* **Sức khỏe:** Chọn tone màu hơi trầm hoặc xanh dương (Uy tín).
* **Rau củ/Ẩm thực:** Chọn tone màu vàng ấm, cam (Kích thích vị giác).
* **3D Mascot:** Nhớ copy prompt Veo 3 để tạo chuyển động 'bouncy' dễ thương.
""")
