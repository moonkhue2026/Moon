import streamlit as st

# --- CẤU HÌNH TRANG (ĐÚNG TÊN APP ZEN) ---
st.set_page_config(page_title="Zen Master v3.5", layout="wide", page_icon="🙏")

# --- CSS GIAO DIỆN ---
st.markdown("""
<style>
    .main-header {font-size: 32px; font-weight: bold; color: #4A4A4A; text-align: center; margin-bottom: 10px;}
    .sub-header {font-size: 16px; color: #666; text-align: center; font-style: italic; margin-bottom: 25px;}
    .stButton>button {width: 100%; border-radius: 5px; font-weight: bold;}
    .highlight-box {background-color: #f8f9fa; padding: 15px; border-radius: 8px; border: 1px solid #ddd;}
</style>
""", unsafe_allow_html=True)

# --- HEADER APP ZEN ---
st.markdown('<div class="main-header">🙏 ZEN MASTER: CONTENT VIRAL v3.5</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Quy trình: 1. Tạo Ảnh → 2. Viết Kịch bản (Có Hook/CTA) → 3. Tạo Video</div>', unsafe_allow_html=True)

# --- SIDEBAR: CẤU HÌNH ---
with st.sidebar:
    st.header("⚙️ CẤU HÌNH ZEN")
    
    # 1. Chọn Phẩm
    pham_options = ["1️⃣ Phẩm Song Yếu", "2️⃣ Phẩm Tâm", "3️⃣ Phẩm Hoa", "4️⃣ Phẩm Ngu", "5️⃣ Phẩm Hiền Trí"]
    selected_pham = st.selectbox("Chọn Phẩm:", pham_options)
    
    # 2. Chọn Định dạng
    format_options = [
        "📖 Lời Nhắc (Quote)", 
        "❓ Giải Mã (Q&A)", 
        "🎬 Kể Chuyện (Story)", 
        "🎶 Nhạc Thiền (Mantra)"
    ]
    selected_format = st.selectbox("Định dạng:", format_options)
    
    # 3. Chọn Thời lượng
    duration = st.slider("Thời lượng (giây):", 10, 60, 15)
    
    # 4. Chọn Góc máy (10 Loại xịn)
    camera_angles = [
        "🔍 Macro Extreme Close-up (Cận cảnh cực đại)",
        "🦅 God’s Eye View (Góc nhìn thượng đế)",
        "🧘 Immersive POV (Góc nhìn nhập vai)",
        "🛡️ Low Angle 'Hero Shot' (Góc thấp tôn vinh)",
        "🎥 Dolly Zoom (Hiệu ứng Vertigo)",
        "⚖️ Gimbal Stabilization (Mượt mà)",
        "⚡ Crash Zoom (Zoom sốc)",
        "😵 Whip Pan (Lia máy vút)",
        "📏 Dutch Angle (Góc nghiêng)",
        "🌪️ SnorriCam (Gắn thân)"
    ]
    selected_angle = st.selectbox("Góc máy:", camera_angles)
    
    # Thông báo trạng thái ảnh
    if "Quote" in selected_format:
        st.success("✅ Đã có Ảnh cũ (Mặc định cho Quote)")
    else:
        st.info("ℹ️ Cần tạo Ảnh mới (Prompt MJ ở Tab 1)")

# --- TABS CHỨC NĂNG ---
tab1, tab2, tab3 = st.tabs(["🖼️ 1. PROMPT ẢNH (MJ)", "📝 2. LẤY NỘI DUNG (GPT)", "🎬 3. PROMPT VIDEO (Sora)"])

# ==============================================================================
# TAB 1: ẢNH (QUOTE CỐ ĐỊNH / CÒN LẠI TẠO MỚI)
# ==============================================================================
with tab1:
    if "Quote" in selected_format:
        st.subheader("🖼️ Visual Tĩnh (Quote)")
        col_img, col_info = st.columns([1, 2])
        with col_img:
            # Ảnh Phật mẫu
            st.image("https://r2.erweima.ai/imgcompressed/compressed_93452f4c478474246835150242250266.webp", caption="Ảnh Phật mẫu (Macro Style)", use_container_width=True)
        with col_info:
            st.warning("🔒 Định dạng 'Lời Nhắc' dùng ảnh Phật cố định.")
            
    else:
        st.subheader(f"🖼️ Gợi ý Prompt Midjourney cho: {selected_format}")
        
        # Tạo Prompt MJ tự động
        mj_subject = ""
        if "Mantra" in selected_format:
            mj_subject = "Abstract mandala art, spiritual flow, healing energy, seamless loop texture"
        elif "Story" in selected_format:
            mj_subject = "Cinematic character shot, a monk walking in ancient temple, dramatic lighting"
        elif "Q&A" in selected_format:
            mj_subject = "Conceptual art, duality of light and shadow, contrast between confusion and clarity"
        
        # Ghép chuỗi Prompt MJ
        mj_prompt_text = f"/imagine prompt: {mj_subject}. Context: {selected_pham}. Style: {selected_angle.split('(')[0]}, 8k resolution, photorealistic, cinematic lighting --ar 9:16"
        
        st.info("👇 Copy dòng này dán vào Midjourney:")
        st.code(mj_prompt_text, language="text")

# ==============================================================================
# TAB 2: LẤY NỘI DUNG (LINK SANG BÁC GIÁC NGỘ)
# ==============================================================================
with tab2:
    st.subheader("📝 Bước 1: Lấy 'Combo Viral' từ Bác Giác Ngộ")
    
    gpt_link = "https://chatgpt.com/g/g-693137cfde808191b2a5f60c8a49c862-chia-khoa-tam-linh-bac-giac-ngo"
    
    col_btn, col_prompt = st.columns([1, 3])
    with col_btn:
        st.link_button("🧘 Mở 'Bác Giác Ngộ' (GPT)", gpt_link, type="primary")
    
    with col_prompt:
        st.write("Copy đoạn yêu cầu này gửi cho GPT:")
        
        # Prompt xin đủ 3 món: Script + Caption + Hashtag
        gpt_request = f"""Chủ đề: **{selected_pham}**. Thời lượng: **{duration}s**.
Định dạng: **{selected_format}**.

HÃY VIẾT 2 PHẦN:
1. KỊCH BẢN VIDEO (Hook - Body - CTA):
- Hook: Giật gân/Tò mò (0-3s).
- Body: Sâu sắc ({duration-6}s).
- CTA: Kêu gọi hành động (3s).

2. BÀI ĐĂNG MXH:
- Caption: Deep, cuốn hút.
- Hashtag: 7-10 thẻ viral."""
        
        st.code(gpt_request, language="markdown")

    st.divider()
    
    st.subheader("📝 Bước 2: Dán kết quả vào đây")
    st.caption("Dán cả Kịch bản + Caption + Hashtag vào đây để App xử lý.")
    
    # Ô nhập liệu quan trọng
    user_script_input = st.text_area("👇 Dán kết quả từ ChatGPT:", height=250)

# ==============================================================================
# TAB 3: PROMPT VIDEO (SORA) - LỌC CAPTION THÔNG MINH
# ==============================================================================
with tab3:
    st.subheader(f"🎬 Tạo Video: {selected_pham}")
    
    if not user_script_input:
        st.warning("⚠️ Vui lòng dán nội dung vào Tab 2 trước.")
    else:
        # 1. Visual Style
        visual_desc = ""
        if "Quote" in selected_format:
            visual_desc = "Tĩnh tại (Minimalist). Macro shot chi tiết, ánh sáng tâm linh. Chuyển động cực chậm (Slow motion)."
        elif "Mantra" in selected_format:
            visual_desc = "Vòng lặp (Seamless Loop). Trừu tượng, Fractal art, thiên nhiên tuần hoàn. Không nhân vật cụ thể."
        elif "Story" in selected_format:
            visual_desc = "Điện ảnh (Cinematic). Có nhân vật, cốt truyện, diễn tiến theo thời gian."
        elif "Q&A" in selected_format:
            visual_desc = "Đối lập (Contrast). Hook tối/rối (vấn đề) -> Body/CTA sáng (giác ngộ)."
            
        # 2. System Prompt (Dạy Sora lọc Caption)
        sora_prompt = f"""
# SYSTEM PROMPT: SORA VIDEO GENERATOR (VIETNAMESE OUTPUT)

ROLE: Bạn là Đạo diễn hình ảnh AI.
INPUT DATA (Gồm Kịch bản & Caption):
---
{user_script_input}
---
Định dạng: {selected_format} | Góc máy: {selected_angle}

NHIỆM VỤ QUAN TRỌNG:
1. LỌC THÔNG TIN: Chỉ lấy phần "Kịch bản Video (Hook-Body-CTA)" để làm video. BỎ QUA Caption/Hashtag.
2. Viết Visual Prompt tiếng Việt mô tả video {duration}s.

YÊU CẦU VISUAL:
- Style: {visual_desc}
- Camera: {selected_angle}. Hãy mô tả chuyển động camera đúng kỹ thuật này.

OUTPUT FORMAT (BẮT BUỘC):
"Video chất lượng cao {duration}s.
[00s-03s] (Hook - {selected_angle.split('(')[0]}): {{Mô tả hình ảnh mở đầu ấn tượng}}.
[03s-{(duration-3)//2 + 3}s] (Body): {{Mô tả diễn biến chính}}.
[{(duration-3)//2 + 3}s-{duration}s] (CTA): {{Hình ảnh kết thúc/Text overlay}}.
Style: Cinematic, 8k, {selected_angle.split('(')[0]}."
"""
        st.success("✅ Đã tách Kịch bản (đã lọc bỏ Caption/Hashtag để Sora không bị nhiễu).")
        st.text_area("Copy đoạn này ném vào Sora:", value=sora_prompt, height=450)
        st.button("🔄 Tạo lại Prompt")
