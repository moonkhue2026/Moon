import streamlit as st

# --- CẤU HÌNH TRANG (TÊN FILE: Zen.py) ---
st.set_page_config(page_title="Zen Master v5.0 (Final)", layout="wide", page_icon="🙏")

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
st.markdown('<div class="main-header">🙏 ZEN MASTER: CONTENT VIRAL v5.0</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Quy trình: 1. Tạo Ảnh → 2. Viết Kịch bản (Lưu trữ) → 3. App tự xuất Prompt Visual (Sạch & Chuẩn)</div>', unsafe_allow_html=True)

# --- SIDEBAR: CẤU HÌNH ---
with st.sidebar:
    st.header("⚙️ CẤU HÌNH ZEN")
    
    # DANH SÁCH ĐỦ 26 PHẨM KINH PHÁP CÚ
    pham_options = [
        "1. Phẩm Song Yếu (Twin Verses)", "2. Phẩm Không Phóng Dật (Vigilance)", "3. Phẩm Tâm (The Mind)", 
        "4. Phẩm Hoa (Flowers)", "5. Phẩm Ngu (The Fool)", "6. Phẩm Hiền Trí (The Wise)", 
        "7. Phẩm A-la-hán (The Arhat)", "8. Phẩm Ngàn (Thousands)", "9. Phẩm Ác (Evil)", 
        "10. Phẩm Hình Phạt (Punishment)", "11. Phẩm Già (Old Age)", "12. Phẩm Tự Ngã (Self)", 
        "13. Phẩm Thế Gian (The World)", "14. Phẩm Phật Đà (The Buddha)", "15. Phẩm Hạnh Phúc (Happiness)", 
        "16. Phẩm Hỷ Ái (Pleasure)", "17. Phẩm Phẫn Nộ (Anger)", "18. Phẩm Cấu Uế (Impurity)", 
        "19. Phẩm Pháp Trụ (The Just)", "20. Phẩm Đạo (The Path)", "21. Phẩm Tạp Lục (Miscellaneous)", 
        "22. Phẩm Địa Ngục (Hell)", "23. Phẩm Voi (The Elephant)", "24. Phẩm Tham Ái (Craving)", 
        "25. Phẩm Tỳ Kheo (The Monk)", "26. Phẩm Bà-la-môn (The Brahmin)"
    ]
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

# --- HÀM MAPPING DỮ LIỆU SORA (VISUAL ONLY) ---
def get_technical_params(fmt, pham_full_name):
    # 1. Map Subject & Action & Audio theo Định dạng (KHÔNG CÓ VOICE)
    if "Quote" in fmt:
        subject = "Statue of Buddha, golden texture."
        action = "Stillness, subtle breathing motion, dust particles floating."
        lighting = "Soft, volumetric lighting, God rays (divine atmosphere)."
        audio_style = "Silence, temple bell sound, peace."
    elif "Mantra" in fmt:
        subject = "Abstract Zen Mandala, Lotus flower opening."
        action = "Infinite seamless loop, hypnotic rotation, fluid motion."
        lighting = "Pastel colors, bioluminescent glow, healing energy."
        audio_style = "Deep meditation music, theta waves, nature sounds."
    elif "Story" in fmt:
        subject = "A Zen monk walking in ancient temple, cinematic character."
        action = "Slow walking meditation, storytelling flow, looking at the sky."
        lighting = "Cinematic drama lighting, deep shadows, morning sun."
        audio_style = "Cinematic score, emotional ambient."
    else: # Q&A
        subject = "Conceptual art, duality of light and darkness."
        action = "Morphing shapes, transition from chaos to order."
        lighting = "High contrast (Chiaroscuro), dramatic spotlight."
        audio_style = "Mystery ambient, revealing sound effect."

    # 2. Lấy tên tiếng Anh của Phẩm làm Context (Tách từ chuỗi input)
    # Ví dụ: "1. Phẩm Song Yếu (Twin Verses)" -> Lấy "Twin Verses"
    try:
        context_theme = pham_full_name.split("(")[1].replace(")", "") + ", Zen philosophy, Buddhism."
    except:
        context_theme = "Zen philosophy, Buddhism, Inner peace."
    
    return subject, action, lighting, context_theme, audio_style

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
        subject, action, lighting, _, _ = get_technical_params(selected_format, selected_pham)
        mj_prompt = f"/imagine prompt: {subject} {action} {lighting} {selected_angle.split('(')[0]} style, 8k, cinematic --ar 9:16"
        st.code(mj_prompt, language="text")

# TAB 2: NỘI DUNG (GIỮ NGUYÊN ĐỂ USER LƯU TRỮ/LẤY IDEA)
with tab2:
    st.link_button("🧘 Mở 'Bác Giác Ngộ' (GPT)", "https://chatgpt.com/g/g-693137cfde808191b2a5f60c8a49c862-chia-khoa-tam-linh-bac-giac-ngo", type="primary")
    
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
        st.subheader("🎥 1. Dán Kịch bản (Lưu trữ)")
        user_script_input = st.text_area("Dán Kịch bản vào đây (Chỉ để bạn xem, KHÔNG đưa vào Video):", height=300)
    
    with col_social:
        st.subheader("📱 2. Dán Caption (Đăng bài)")
        st.text_area("Dán Caption & Hashtag vào đây:", height=300)

# TAB 3: VIDEO (OUTPUT VISUAL THUẦN TÚY - KHÔNG TEXT KỊCH BẢN)
with tab3:
    # Lấy thông số kỹ thuật thuần túy
    sub, act, light, ctx_theme, audio_st = get_technical_params(selected_format, selected_pham)
    
    # TẠO PROMPT KỸ THUẬT (SẠCH - CLEAN)
    # Lưu ý: Phần Context chỉ lấy Theme tiếng Anh, không lấy user_script_input
    sora_technical_prompt = f"""[INPUT ẢNH]

Cinematic shot.
Subject: {sub}
CAMERA: {selected_angle.split('(')[0]}
Action: {act}
Lighting: {light}
Context: {ctx_theme}
AUDIO: {audio_st}
CONSTRAINT: NO TEXT, NO LOGO, NO WATERMARK.
--duration {duration}s"""
    
    st.success(f"✅ Đã tạo Prompt Visual (Sạch & Không dính Text). Phẩm: {selected_pham}")
    st.text_area("Copy đoạn này dán vào Sora:", value=sora_technical_prompt, height=350)
