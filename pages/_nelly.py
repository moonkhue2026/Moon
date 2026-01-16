import streamlit as st

st.set_page_config(page_title="KOL Nelly Manager", page_icon="👠", layout="wide")

# =========================================================
# 1. CẤU HÌNH PHONG CÁCH NELLY
# =========================================================

styles = {
    "Sang trọng (Luxury)": {
        "kw": "High-end commercial, Vogue style, luxury apartment background, golden hour, 8k",
        "outfit": "high-end designer suit or evening gown",
        "vibe": "confident, powerful, sophisticated"
    },
    "Thân thiện (Daily)": {
        "kw": "Vlog style, cinematic daily life, cozy modern home, soft natural light, 4k",
        "outfit": "casual chic, silk pajamas or sportswear",
        "vibe": "warm, engaging, authentic"
    },
    "Chuyên gia (Expert)": {
        "kw": "Studio lighting, clean background, sharp focus, professional look, 8k",
        "outfit": "modern blazer, smart glasses",
        "vibe": "trustworthy, intelligent, focused"
    }
}

# =========================================================
# GIAO DIỆN CHÍNH
# =========================================================

st.title("👠 NELLY'S WORKSPACE MANAGER")
st.markdown("*Quản lý 4 Trụ cột công việc: Sáng tạo - Cộng đồng - Booking - Nghiên cứu*")

# SIDEBAR: GIAO NHIỆM VỤ CỤ THỂ
with st.sidebar:
    st.header("📅 LÊN KẾ HOẠCH LÀM VIỆC")
    
    # 1. Chọn nhóm công việc (4 Trụ cột Moon yêu cầu)
    task_type = st.radio("Chọn loại nhiệm vụ:", [
        "1. Sáng tạo nội dung (Content Creation)", 
        "2. Tương tác cộng đồng (Community)",
        "3. Hợp tác Marketing (Booking/Review)",
        "4. Nghiên cứu & Cập nhật (R&D)"
    ])
    
    st.divider()
    
    # Form nhập liệu thay đổi theo từng loại nhiệm vụ
    task_input = {}
    
    if "Sáng tạo" in task_type:
        task_input['niche'] = st.selectbox("Lĩnh vực:", ["Làm đẹp (Beauty)", "Công nghệ (Tech)", "Ẩm thực (Food)", "Tài chính (Finance)", "Lifestyle"])
        task_input['topic'] = st.text_input("Chủ đề cụ thể:", "Ví dụ: 5 sai lầm khi quản lý tài chính cá nhân")
        task_input['style'] = st.selectbox("Style Nelly:", ["Chuyên gia (Expert)", "Sang trọng (Luxury)"])
        
    elif "Cộng đồng" in task_type:
        task_input['topic'] = st.text_input("Câu chuyện muốn chia sẻ:", "Ví dụ: Hành trình vượt qua sự tự ti của Nelly")
        task_input['style'] = "Thân thiện (Daily)"
        
    elif "Hợp tác" in task_type:
        task_input['brand'] = st.text_input("Tên Thương hiệu/Sàn:", "Ví dụ: Shopee, Dyson, Chanel")
        task_input['product'] = st.text_input("Sản phẩm:", "Ví dụ: Máy sấy tóc, Son môi")
        task_input['type'] = st.selectbox("Loại content:", ["Review chân thực", "Unboxing", "Livestream/Sale"])
        task_input['style'] = "Sang trọng (Luxury)" if "Unboxing" in task_input['type'] else "Chuyên gia (Expert)"
        
    elif "Nghiên cứu" in task_type:
        task_input['trend'] = st.text_input("Xu hướng cần học:", "Ví dụ: Cách edit video kiểu Douyin, Trend biến hình mới")
        
    st.divider()
    
    # Cấu hình Video chung
    duration = st.select_slider("Thời lượng:", options=["15s", "30s", "60s"], value="30s")
    model_ai = st.radio("AI Model:", ["Sora (15s)", "Veo 3 (8s)"], horizontal=True)

# =========================================================
# XỬ LÝ LOGIC & HIỂN THỊ (MAIN CONTENT)
# =========================================================

if "Nghiên cứu" in task_type:
    # --- GIAO DIỆN RIÊNG CHO R&D ---
    st.info(f"📚 **NHIỆM VỤ R&D:** {task_input['trend']}")
    st.markdown("""
    **Checklist cho Nelly:**
    - [ ] Lướt Douyin/TikTok 30 phút để tìm video gốc.
    - [ ] Phân tích âm nhạc, góc quay, transition.
    - [ ] Ghi chú lại 3 điểm cốt lõi để áp dụng cho kênh.
    - [ ] Tìm đọc tài liệu chuyên sâu nếu là kiến thức sản phẩm mới.
    """)
    st.warning("👉 Nhiệm vụ này tập trung vào việc HỌC, chưa cần sản xuất video ngay.")

else:
    # --- GIAO DIỆN SẢN XUẤT CONTENT (3 LOẠI CÒN LẠI) ---
    
    # 1. Xác định Style & Context
    current_style = styles[task_input.get('style', 'Sang trọng (Luxury)')]
    
    # Tiêu đề nhiệm vụ
    if "Sáng tạo" in task_type:
        title = f"{task_input['niche']}: {task_input['topic']}"
        context_prompt = f"Sharing expert knowledge about {task_input['topic']}"
    elif "Cộng đồng" in task_type:
        title = f"Tâm sự: {task_input['topic']}"
        context_prompt = "Sharing personal story, emotional connection"
    else: # Booking
        title = f"{task_input['type']} x {task_input['brand']}: {task_input['product']}"
        context_prompt = f"Promoting {task_input['product']} for {task_input['brand']}"

    st.subheader(f"🎬 KỊCH BẢN: {title}")
    
    # 2. Logic Kịch bản (3 Trụ cột)
    t_num = int(duration.replace("s",""))
    segments = []

    # === LOGIC SÁNG TẠO (CHUYÊN MÔN) ===
    if "Sáng tạo" in task_type:
        segments = [
            ("HOOK", "Gây tò mò", f"3 điều Nelly ước mình biết sớm hơn về {task_input['topic']}.", "Holding a notebook/tablet, looking smart."),
            ("BODY", "Kiến thức", f"Thứ nhất... Thứ hai... (Chia sẻ kiến thức sâu).", "Pointing to text/graphics floating in air."),
            ("CTA", "Tương tác", f"Bạn thấy sao? Comment ý kiến bên dưới nhé.", "Smiling and waiting for response.")
        ]
        
    # === LOGIC CỘNG ĐỒNG (TÂM SỰ) ===
    elif "Cộng đồng" in task_type:
        segments = [
            ("HOOK", "Cảm xúc", f"Hôm nay cho phép Nelly yếu đuối một chút nhé...", "Sitting on sofa, holding a cup of tea."),
            ("BODY", "Trải nghiệm", f"Kể về hành trình/khó khăn đã qua...", "Looking out the window then back to camera."),
            ("CTA", "Kết nối", f"Cảm ơn mọi người đã luôn ở bên Nelly.", "Hand on heart gesture.")
        ]
        
    # === LOGIC BOOKING (QUẢNG CÁO) ===
    else: # Hợp tác
        if "Unboxing" in task_input['type']:
            action_body = f"Opening the {task_input['brand']} box, showing {task_input['product']} details."
            hook_text = "Cùng Nelly đập hộp siêu phẩm mới nhất này nha!"
        else:
            action_body = f"Using {task_input['product']} on face/hand, showing satisfaction."
            hook_text = f"Tại sao {task_input['product']} lại hot đến vậy?"
            
        segments = [
            ("HOOK", "Show hàng", hook_text, f"Holding {task_input['product']} box excitedly."),
            ("BODY", "Trải nghiệm", f"Thiết kế sang trọng, chất lượng đỉnh cao...", action_body),
            ("CTA", "Chốt đơn", f"Săn ngay deal hời tại giỏ hàng nhé!", "Showing phone screen/Sale sign.")
        ]

    # Điều chỉnh thời lượng 60s
    if t_num == 60:
        segments.insert(1, ("BODY 2", "Chi tiết sâu", "Đi sâu vào phân tích/kể chuyện chi tiết hơn.", "Change angle/Close up shot."))

    # 3. HIỂN THỊ TAB LÀM VIỆC
    tab1, tab2, tab3 = st.tabs(["📜 KỊCH BẢN CHI TIẾT", "🎥 PROMPT VIDEO", "📝 BÀI VIẾT BLOG"])
    
    with tab1:
        script_text = ""
        for name, role, vn, en in segments:
            script_text += f"🔸 {name} ({role}): \"{vn}\"\n"
        st.info(script_text)
        
    with tab2:
        st.markdown(f"**Prompt ({model_ai}):**")
        for name, role, vn, en in segments:
            st.markdown(f"🎞️ **{name}**")
            
            # Tinh chỉnh Prompt theo Niche (Công nghệ vs Làm đẹp)
            props = ""
            if "Công nghệ" in str(task_input): props = ", holding smartphone/laptop"
            if "Ẩm thực" in str(task_input): props = ", in luxury kitchen with food"
            
            if "Sora" in model_ai:
                prompt = f"""
                {current_style['kw']}.
                Subject: A stunning Vietnamese fashion KOL (Nelly), {current_style['vibe']} expression{props}.
                Outfit: {current_style['outfit']}.
                Action: {en}.
                Speaking Line (Vietnamese): "{vn}"
                Lip-sync: Match Vietnamese dialogue.
                Context: {context_prompt}. Constraint: NO TEXT.
                --duration 15s
                """
            else:
                prompt = f"""
                Cinematic shot, Nelly (Vietnamese KOL){props}.
                Outfit: {current_style['outfit']}.
                Action: {en}. Speaking.
                Style: {current_style['kw']}.
                --duration 8s
                """
            st.code(prompt, language='text')

    with tab3:
        st.subheader("Copy lệnh cho ChatGPT:")
        st.code(f"""
        Đóng vai KOL Nelly. Viết bài Facebook/Blog về: **{title}**.
        - Mục tiêu: {task_type}.
        - Nội dung chính: {context_prompt}.
        - Tone giọng: {current_style['vibe']}.
        - Kêu gọi hành động: {segments[-1][2]}.
        - Hashtag: #NellyKOL #{title.split(':')[0].replace(' ','')}
        """, language='text')
