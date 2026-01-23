import streamlit as st

# --- CẤU HÌNH TRANG (TÊN FILE: Zen.py) ---
st.set_page_config(page_title="Zen Master v4.6 (Fix CTA)", layout="wide", page_icon="🙏")

# --- CSS GIAO DIỆN ---
st.markdown("""
<style>
    .main-header {font-size: 32px; font-weight: bold; color: #4A4A4A; text-align: center; margin-bottom: 10px;}
    .sub-header {font-size: 16px; color: #666; text-align: center; font-style: italic; margin-bottom: 25px;}
    .stButton>button {width: 100%; border-radius: 5px; font-weight: bold;}
    .caption-box {background-color: #f0f2f6; padding: 10px; border-radius: 5px; border-left: 5px solid #ff4b4b;}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="main-header">🙏 ZEN MASTER: CONTENT VIRAL v4.6</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Quy trình: 1. Tạo Ảnh → 2. Viết Kịch bản & Caption → 3. App tự xuất Prompt Sora kỹ thuật</div>', unsafe_allow_html=True)

# --- SIDEBAR: CẤU HÌNH ---
with st.sidebar:
    st.header("⚙️ CẤU HÌNH ZEN")
    
    pham_options = ["1️⃣ Phẩm Song Yếu", "2️⃣ Phẩm Tâm", "3️⃣ Phẩm Hoa", "4️⃣ Phẩm Ngu", "5️⃣ Phẩm Hiền Trí"]
    selected_pham = st.selectbox("Chọn Phẩm:", pham_options)
    
    format_options = ["📖 Lời Nhắc (Quote)", "❓ Giải Mã (Q&A)", "🎬 Kể Chuyện (Story)", "🎶 Nhạc Thiền (Mantra)"]
    selected_format = st.selectbox("Định dạng:", format_options)
    
    duration = st.slider("Thời lượng (giây):", 10, 60, 15)
    
    camera_angles = [
        "Macro Extreme Close-up (Cận cảnh cực đại)", "God’s Eye View (Góc nhìn thượng đế)", 
        "Immersive POV (Góc nhìn nhập vai)", "Low Angle 'Hero Shot' (Góc thấp tôn vinh)", 
        "Dolly Zoom (Hiệu ứng Vertigo)", "Gimbal Stabilization (Mượt mà)", 
        "Crash Zoom (Zoom sốc)", "Whip Pan (Lia máy vút)", 
        "Dutch Angle (Góc nghiêng)", "SnorriCam (Gắn thân)"
    ]
    selected_angle = st.selectbox("Góc máy:", camera_angles)
    
    if "Quote" in selected_format:
        st.success("✅ Ảnh cũ (Quote)")
    else:
        st.info("ℹ️ Tạo Ảnh mới (Tab 1)")

# --- HÀM MAPPING DỮ LIỆU SORA (LOGIC NGẦM) ---
def get_technical_params(fmt, pham):
    # 1. Map Subject & Action theo Định dạng
    if "Quote" in fmt:
        subject = "Statue of Buddha, golden texture."
        action = "Stillness, subtle breathing motion, dust particles floating."
        lighting = "Soft, volumetric lighting, God rays (divine atmosphere)."
    elif "Mantra" in fmt:
        subject = "Abstract Zen Mandala, Lotus flower opening."
        action = "Infinite seamless loop, hypnotic rotation, fluid motion."
        lighting = "Pastel colors, bioluminescent glow, healing energy."
    elif "Story" in fmt:
        subject = "A Zen monk walking in ancient temple, cinematic character."
        action = "Slow walking meditation, storytelling flow, looking at the sky."
        lighting = "Cinematic drama lighting, deep shadows, morning sun."
    else: # Q&A
        subject = "Conceptual art, duality of light and darkness."
        action = "Morphing shapes, transition from chaos to order."
        lighting = "High contrast (Chiaroscuro), dramatic spotlight."

    # 2. Map Context (Phẩm) sang tiếng Anh
    context_map = {
        "1️⃣ Phẩm Song Yếu": "Twin Verses, mind creates reality, duality of life.",
        "2️⃣ Phẩm Tâm": "The Mind, control your thoughts, inner peace.",
        "3️⃣ Phẩm Hoa": "Flowers, beauty of impermanence, blooming wisdom.",
        "4️⃣ Phẩm Ngu": "The Fool, darkness and ignorance, awakening.",
        "5️⃣ Phẩm Hiền Trí": "The Wise, clarity, mountain of wisdom."
    }
    context_theme = context_map.get(pham, "Zen philosophy.")
    
    return subject, action, lighting, context_theme

# --- HÀM TẠO CAPTION STYLE ---
def get_caption_style(fmt):
    if "Quote" in fmt: return "Triết lý, Ngắn gọn, Thấm (1-2 câu trích dẫn)"
    if "Mantra" in fmt: return "Chữa lành, Nhẹ nhàng, Mời gọi thư giãn"
    if "Story" in fmt: return "Kể chuyện, Bài học nhân sinh, Sâu sắc"
    return "Gợi mở, Đặt câu hỏi tu từ, Khai sáng (Q&A)"

def get_hashtags(fmt):
    if "Quote" in fmt: return "#PhatPhap #LoiPhatDay #TinhTam #AnYen"
    if "Mantra" in fmt: return "#NhacThien #Healing #Meditation #GiacNguNgon"
    if "Story" in fmt: return "#BaiHocCuocSong #NhanQua #PhatGiao #ZenStory"
    return "#GiaiMa #TuTap #KienThuc #HoiDap"

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["🖼️ 1. PROMPT ẢNH", "📝 2. LẤY NỘI DUNG", "🎬 3. PROMPT VIDEO"])

# TAB 1: ẢNH
with tab1:
    if "Quote" in selected_format:
        st.image("https://r2.erweima.ai/imgcompressed/compressed_93452f4c478474246835150242250266.webp", caption="Ảnh Phật mẫu (Macro Style)", width=300)
    else:
        st.info("👇 Prompt Midjourney (Copy & Paste):")
        subject, action, lighting, _ = get_technical_params(selected_format, selected_pham)
        mj_prompt = f"/imagine prompt: {subject} {action} {lighting} {selected_angle.split('(')[0]} style, 8k, cinematic --ar 9:16"
        st.code(mj_prompt, language="text")

# TAB 2: NỘI DUNG (TÁCH BIỆT RÕ RÀNG)
with tab2:
    st.link_button("🧘 Mở 'Bác Giác Ngộ' (GPT)", "https://chatgpt.com/g/g-693137cfde808191b2a5f60c8a49c862-chia-khoa-tam-linh-bac-giac-ngo", type="primary")
    
    # Logic Style Caption động
    caption_style = get_caption_style(selected_format)
    suggested_tags = get_hashtags(selected_format)
    
    st.markdown("### 📋 Copy yêu cầu này gửi cho GPT:")
    gpt_request = f"""Chủ đề: **{selected_pham}**. Thời lượng: **{duration}s**.
Định dạng: **{selected_format}**.

HÃY VIẾT 2 PHẦN RIÊNG BIỆT:

--- PHẦN 1: KỊCH BẢN VIDEO (Chỉ lấy Hook - Body - CTA) ---
- Hook: (Câu mở đầu 3s)
- Body: (Nội dung chính)
- CTA: (Câu chốt)

--- PHẦN 2: CAPTION ĐĂNG BÀI (Short & Deep) ---
- Yêu cầu Style: **{caption_style}**.
- Caption: Viết ngắn gọn, chất, thấm.
- Hashtag: {suggested_tags} #ZenMaster"""
    
    st.code(gpt_request, language="markdown")
    st.divider()
    
    col_script, col_social = st.columns(2)
    
    with col_script:
        st.subheader("🎥 1. Dán Kịch bản (Làm Video)")
        user_script_input = st.text_area("Chỉ dán phần Hook-Body-CTA vào đây:", height=300, placeholder="Hook: ...\nBody: ...\nCTA: ...")
    
    with col_social:
        st.subheader("📱 2. Dán Caption (Để đăng bài)")
        st.text_area("Dán Caption & Hashtag vào đây để lưu trữ (Không ảnh hưởng Video):", height=300, placeholder="Caption deep...\n#Hashtag")

# TAB 3: VIDEO (OUTPUT KỸ THUẬT - FULL SCRIPT)
with tab3:
    if not user_script_input:
        st.warning("⚠️ Vui lòng dán Kịch bản vào Tab 2 (Cột bên trái).")
    else:
        # Lấy thông số kỹ thuật
        sub, act, light, ctx_theme = get_technical_params(selected_format, selected_pham)
        
        # Làm sạch kịch bản (Bỏ dòng Hook/Body/CTA thừa)
        clean_script = user_script_input.replace("Hook:", "").replace("Body:", "").replace("CTA:", "").replace("\n", " ").strip()
        
        # TẠO PROMPT KỸ THUẬT (KHÔNG CẮT BỚT KÝ TỰ NỮA)
        sora_technical_prompt = f"""[INPUT ẢNH]

Cinematic shot.
Subject: {sub}
CAMERA: {selected_angle.split('(')[0]}
Action: {act}
Lighting: {light}
Context: {ctx_theme} Script content: "{clean_script}"
AUDIO: Zen music + Warm Vietnamese voiceover.
CONSTRAINT: NO TEXT, NO LOGO.
--duration {duration}s"""
        
        st.success("✅ Đã tạo Prompt Kỹ thuật (Full Kịch bản bao gồm CTA):")
        st.text_area("Copy đoạn này dán vào Sora:", value=sora_technical_prompt, height=350)
