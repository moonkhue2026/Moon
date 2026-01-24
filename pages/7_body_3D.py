import streamlit as st
import pandas as pd

# 1. CẤU HÌNH TRANG (Bắt buộc dòng đầu)
st.set_page_config(page_title="Moon's 3D Anatomy V2", page_icon="🧬", layout="wide")

# 2. TIÊU ĐỀ
st.title("Moon's 3D Studio: Cơ Thể & Làm Đẹp (V2.0) 🧬")
st.markdown("---")

# 3. CHIA TAB LỚN
main_tab1, main_tab2 = st.tabs(["🍔 Giải phẫu (Food & Organ)", "💄 Làm đẹp (Beauty & Skincare)"])

# ==================================================
# KHU VỰC 1: GIẢI PHẪU (FOOD)
# ==================================================
with main_tab1:
    st.header("Anatomy Viral Station 🩺")
    
    col_a, col_b = st.columns([1.2, 1.5]) # Chia cột lệch chút để phần nhập liệu rộng hơn

    # --- CỘT TRÁI: NHẬP LIỆU & XUẤT PROMPT ---
    with col_a:
        st.subheader("🛠️ Bộ điều khiển")
        with st.form("food_form"):
            topic = st.text_input("Món ăn/Vật thể", "Mì cay cấp 7")
            body_part = st.selectbox("Bộ phận tác động", ["Dạ dày", "Phổi", "Gan", "Ruột", "Não", "Tim"])
            effect = st.text_input("Hiệu ứng Visual", "Dạ dày đỏ rực, co thắt mạnh, sủi bọt")
            
            # THANH CHỌN THỜI LƯỢNG VIDEO (QUAN TRỌNG)
            duration = st.select_slider("Thời lượng Video (Sora 2)", options=["15s", "30s", "60s", "120s"], value="15s")
            
            submit_food = st.form_submit_button("🚀 Xuất Kịch Bản & Prompt")
            
            if submit_food:
                st.success(f"Đã xuất bộ tài liệu cho video {duration}!")
                
                # --- A. KỊCH BẢN 3 PHẦN (HOOK - BODY - CTA) ---
                st.markdown("### 1. Kịch bản Nội Dung (Script)")
                
                # Logic tạo nội dung theo thời lượng
                body_script = ""
                if duration == "15s":
                    body_script = f"Cắt nhanh: {topic} rơi vào {body_part}. Zoom cực cận cảnh {body_part} đang {effect}. Hiệu ứng âm thanh dồn dập."
                elif duration == "30s":
                    body_script = f"0-5s: Cận cảnh ăn {topic}. 5-15s: Thức ăn trôi qua thực quản (X-Ray view). 15-25s: Tại {body_part}, phản ứng {effect} xảy ra dữ dội. 25-30s: {body_part} đổi màu báo động."
                else: # 60s, 120s
                    body_script = f"Giải thích chi tiết quy trình: Bắt đầu từ khoang miệng -> Thực quản -> {body_part}. Phân tích kỹ phản ứng hóa học của {topic} làm {effect}. So sánh tình trạng trước và sau khi ăn."

                st.info(f"""
                **📌 Phần 1: HOOK (3s đầu - Giữ chân người xem)**
                "ĐỪNG ăn {topic} nếu bạn chưa thấy cảnh tượng này bên trong {body_part}!" 😱
                
                **📌 Phần 2: BODY (Nội dung chính)**
                {body_script}
                
                **📌 Phần 3: CTA (Kêu gọi hành động)**
                "Bạn có hay ăn món này không? Comment ngay bên dưới nhé! 👇 #Anatomy #Health"
                """)

                # --- B. PROMPT ẢNH (MIDJOURNEY) ---
                st.markdown("### 2. Prompt Ảnh Thumbnail (Midjourney)")
                mj_prompt = f"/imagine prompt: 3d medical animation cross-section of human {body_part}, inside is {topic}, visual effect is {effect}, hyper-realistic, detailed texture, cinematic lighting, 8k resolution, bright colors, --ar 9:16"
                st.code(mj_prompt, language="bash")

                # --- C. PROMPT VIDEO (SORA 2) - THEO THỜI LƯỢNG ---
                st.markdown(f"### 3. Prompt Video Sora 2 ({duration})")
                
                sora_prompt = ""
                base_style = "Photorealistic 3D medical animation, high quality, 8k, unreal engine 5 render style."
                
                if duration == "15s":
                    sora_prompt = f"{base_style} Duration 15s. Continuous shot. Close up macro view of {topic} entering human {body_part}. Immediate reaction: {effect}. Fast paced, dramatic lighting."
                elif duration == "30s":
                    sora_prompt = f"{base_style} Duration 30s. Sequence. Shot 1: Person eating {topic}. Shot 2: X-Ray view of chest showing food traveling down. Shot 3: Inside {body_part}, showing intense {effect}, tissues turning red. Smooth camera movement."
                elif duration == "60s":
                    sora_prompt = f"{base_style} Duration 60s. Educational storytelling. Detailed journey of {topic} through the digestive system. Focus on {body_part}. Slow motion visualization of {effect}. Comparison view of healthy {body_part} vs damaged {body_part}. Clear visibility of texture and fluids."
                else:
                    sora_prompt = f"{base_style} Duration 120s. Full documentary style. Comprehensive anatomy tour of {body_part}. Interaction of {topic} at cellular level. Detailed simulation of {effect} over time. Multiple angles: wide shot of organs, macro shot of cells."

                st.code(sora_prompt, language="bash")

    # --- CỘT PHẢI: QUẢN LÝ ---
    with col_b:
        st.subheader("📅 Quản lý sản xuất")
        df_food = pd.DataFrame({
            "Chủ đề": ["Mì cay", "Trân châu", "Nước đá"],
            "Thời lượng": ["15s", "60s", "30s"],
            "Trạng thái": ["Render", "Idea", "Done"]
        })
        st.data_editor(df_food, use_container_width=True, num_rows="dynamic", key="food_editor")

        st.divider()
        st.subheader("👀 Góc nhìn tham khảo")
        st.caption("(Đây là ảnh demo từ thư viện, Moon thay link ảnh thật của Moon sau nhé)")
        
        # Dùng từ khóa chung chung để đảm bảo luôn hiện ảnh
        c1, c2 = st.columns(2)
        with c1:
            st.image("https://source.unsplash.com/400x600/?anatomy", caption="Style giải phẫu")
            st.image("https://source.unsplash.com/400x600/?stomach", caption="Dạ dày")
        with c2:
            st.image("https://source.unsplash.com/400x600/?medical", caption="Góc nhìn X-Ray")
            st.image("https://source.unsplash.com/400x600/?microscope", caption="Zoom tế bào")

# ==================================================
# KHU VỰC 2: LÀM ĐẸP (BEAUTY)
# ==================================================
with main_tab2:
    st.header("Beauty 3D Studio 💉👄")
    
    b_col1, b_col2 = st.columns([1.2, 1.5])

    # --- CỘT TRÁI: BEAUTY PROMPT ---
    with b_col1:
        st.subheader("✨ Tùy chỉnh Beauty")
        
        with st.form("beauty_form"):
            # 1. Chọn nhóm
            category = st.selectbox("Nhóm chủ đề", ["Tiêm Filler/Botox", "Phẫu thuật thẩm mỹ", "Nha khoa", "Skincare/Mụn"])
            
            # 2. Nhập chi tiết (Để Moon tự nhập cho linh hoạt)
            beauty_topic = st.text_input("Tên video (VD: Nặn mụn đầu đen)", "Tiêm Filler Môi")
            beauty_action = st.text_input("Hành động chính", "Kim tiêm bơm gel vào môi")
            beauty_result = st.text_input("Kết quả/Hiệu ứng", "Môi phồng lên, căng mọng")
            
            # 3. Chọn thời lượng
            beauty_duration = st.select_slider("Thời lượng Sora", options=["15s", "30s", "60s"], value="30s")
            
            submit_beauty = st.form_submit_button("🚀 Xuất Prompt Beauty")
            
            if submit_beauty:
                st.success(f"Đã xuất bộ Beauty {beauty_duration}!")
                
                # A. KỊCH BẢN
                st.markdown("### 1. Kịch bản (Script)")
                st.info(f"""
                **HOOK:** Xem cận cảnh {beauty_topic} dưới kính hiển vi 3D! Bạn có dám xem không?
                **BODY:** {beauty_action}. Zoom 1000x vào lớp da. Thấy rõ {beauty_result}.
                **CTA:** Bạn muốn soi da món nào tiếp theo? Comment nhé!
                """)
                
                # B. MIDJOURNEY
                st.markdown("### 2. Prompt Ảnh (Midjourney)")
                st.code(f"/imagine prompt: 3d medical animation of {beauty_topic}, {beauty_action}, cross-section view of skin layers, hyper-realistic, 8k --ar 9:16", language="bash")
                
                # C. SORA VIDEO
                st.markdown(f"### 3. Prompt Video Sora ({beauty_duration})")
                sora_beauty = ""
                if beauty_duration == "15s":
                     sora_beauty = f"Photorealistic 3D animation, 15s. Macro shot of {beauty_topic}. Action: {beauty_action}. Immediate visual satisfaction: {beauty_result}. Bright lighting."
                else:
                     sora_beauty = f"Photorealistic 3D animation, {beauty_duration}. Process visualization. Step 1: Show {beauty_topic} condition. Step 2: {beauty_action} in slow motion. Step 3: Transformation to {beauty_result}. Smooth texture, medical aesthetic."
                
                st.code(sora_beauty, language="bash")

    # --- CỘT PHẢI: QUẢN LÝ BEAUTY ---
    with b_col2:
        st.subheader("📅 Quản lý Beauty")
        df_beauty = pd.DataFrame({
            "Chủ đề": ["Filler Môi", "Niềng răng", "Nặn mụn"],
            "Phân loại": ["Nội khoa", "Nha khoa", "Da liễu"],
            "Trạng thái": ["Done", "Render", "Idea"]
        })
        st.data_editor(df_beauty, use_container_width=True, num_rows="dynamic", key="beauty_editor")
        
        st.divider()
        st.subheader("👀 Beauty Demo")
        c3, c4 = st.columns(2)
        with c3:
            st.image("https://source.unsplash.com/400x600/?skincare", caption="Skincare")
        with c4:
            st.image("https://source.unsplash.com/400x600/?dentist", caption="Nha khoa")
