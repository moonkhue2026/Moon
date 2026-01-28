import streamlit as st

# 1. CẤU HÌNH TRANG
st.set_page_config(page_title="Moon's 3D Anatomy V4", page_icon="🧬", layout="wide")

# 2. STYLE CỐ ĐỊNH (LOCK STYLE) - XƯƠNG SỐNG CỦA VISUAL
MOON_STYLE = "medical X-Ray cross-section view, dark blue background, glowing highlights, hyper-realistic texture, cinematic lighting, 8k resolution, unreal engine 5 render --no text, labels, words, watermark --ar 9:16"
# 3. TỪ ĐIỂN LOGIC (CORE DATA)

# --- A. LOGIC GIẢI PHẪU (FOOD) ---
FOOD_LOGIC = {
    "🔥 VIÊM / NHIỆT (Mì cay, Rượu, Ớt)": {
        "visual": "glowing red inflamed tissue, pulsating violently, extreme swelling, heat waves",
        "desc": "Sưng tấy đỏ rực, rung động mạnh và tỏa nhiệt."
    },
    "❄️ LẠNH / CO THẮT (Nước đá, Kem)": {
        "visual": "frozen blue texture, ice crystals, veins shrinking and constricting, pale tissue",
        "desc": "Tím tái, đóng băng, mạch máu co lại."
    },
    "☠️ ĐỘC TỐ / HƯ HẠI (Thuốc lá, Khói bụi)": {
        "visual": "blackened tissue, tar accumulation, dark smoke, decaying texture, grey spots",
        "desc": "Đen xám xịt, ám khói, mục nát và hư hại."
    },
    "⛔ TẮC NGHẼN / VẬT THỂ (Trân châu, Mỡ)": {
        "visual": "thick yellow fat layers, solid blockage, sticky texture, compressing organs",
        "desc": "Lớp mỡ/vật thể vàng chèn ép, gây tắc nghẽn dòng chảy."
    },
    "🌿 CHỮA LÀNH / BẢO VỆ (Yogurt, Vitamin)": {
        "visual": "glowing green aura, cleaning effect, smooth healthy tissue, regeneration light",
        "desc": "Phát sáng màu xanh dịu, lớp màng bảo vệ, chữa lành."
    }
}

# --- B. LOGIC LÀM ĐẸP (BEAUTY) ---
BEAUTY_MECHANISMS = {
    "1. BƠM / LÀM ĐẦY (Filler, Má baby)": "injecting transparent gel, tissue expanding, volume increasing, plump texture",
    "2. LẤY RA / LÀM SẠCH (Mụn, Hút mỡ)": "extracting impurities, suction tube removing yellow fat, pores clearing, unclogging",
    "3. DI CHUYỂN / SẮP XẾP (Niềng răng, Nâng mũi)": "bone structure shifting, teeth alignment time-lapse, straightening, correction",
    "4. TÁI TẠO / BẮN LASER (Peel da, Xóa xăm)": "laser beam scanning, burning old skin layer, revealing fresh pink skin, regeneration",
    "5. CĂNG KÉO / NÂNG CƠ (Botox, Căng chỉ)": "threads pulling skin up, muscles relaxing, wrinkles smoothing out, firming texture"
}

# 4. GIAO DIỆN CHÍNH
st.title("Moon's 3D Studio: Cơ Thể & Làm Đẹp (V4 Final) 🧬")
st.markdown("---")

main_tab1, main_tab2 = st.tabs(["🍔 Giải phẫu (Food/Organ)", "💄 Làm đẹp (Beauty/Skin)"])

# ==================================================
# TAB 1: GIẢI PHẪU (FOOD)
# ==================================================
with main_tab1:
    st.header("Anatomy Viral Station 🩺")
    st.info("🛠️ **Bước 1: Nhập thông tin video**")
    
    with st.form("food_form"):
        col1, col2 = st.columns(2)
        with col1:
            topic = st.text_input("Món ăn / Vật thể", "Mì cay cấp 7")
            body_part = st.selectbox("Bộ phận cơ thể", ["Dạ dày", "Phổi", "Gan", "Ruột non", "Não", "Tim", "Thận", "Mạch máu"])
        with col2:
            reaction_key = st.selectbox("Loại phản ứng:", list(FOOD_LOGIC.keys()))
            selected_logic = FOOD_LOGIC[reaction_key]
            effect_preview = st.text_input("Chi tiết hiệu ứng:", value=selected_logic["desc"])
        
        duration = st.select_slider("Thời lượng Video (Sora 2)", options=["15s", "30s", "60s"], value="15s")
        submit_food = st.form_submit_button("🚀 XUẤT KỊCH BẢN & PROMPT (FOOD)")

    # --- KẾT QUẢ FOOD ---
    if submit_food:
        st.divider()
        st.success(f"✅ Đã xong bộ tài liệu cho: {topic}")
        visual_keywords = selected_logic["visual"]

        # 1. Kịch bản & Caption
        st.subheader("1. Kịch bản & Caption")
        caption_hook = f"😱 Điều gì xảy ra khi {topic} đi vào {body_part}?"
        caption_visual = f"Zoom cận cảnh {body_part} đang {effect_preview.lower()} Đừng chủ quan!"
        caption_cta = f"👇 Tag ngay người cần xem video này nhé!"
        
        st.info(f"**HOOK (3s):** {caption_hook}\n\n**BODY:** Mô tả hành trình {topic} đi vào. Zoom vào tế bào thấy {effect_preview}. \n\n**CTA:** {caption_cta}")
        st.code(f"{caption_hook}\n{caption_visual}\n{caption_cta}\n\n#Anatomy3D #Suckhoe #{topic.replace(' ', '')} #Kienthuc", language="text")

        # 2. Prompt Ảnh
        st.subheader("2. Prompt Thumbnail (Midjourney)")
        mj_prompt = f"/imagine prompt: 3d medical animation of human {body_part}, inside containing {topic}, visual effect is {visual_keywords}, {MOON_STYLE}"
        st.code(mj_prompt, language="bash")

        # 3. Prompt Video
        st.subheader(f"3. Prompt Video Sora 2 ({duration})")
        sora_prompt = ""
        base_sora = "Photorealistic 3D medical animation, high quality, 8k. Dark blue background aesthetic."
        if duration == "15s":
            sora_prompt = f"{base_sora} Duration 15s. Continuous shot. Macro view inside {body_part}. {topic} enters. Immediate reaction: {visual_keywords}. Fast paced action."
        elif duration == "30s":
            sora_prompt = f"{base_sora} Duration 30s. Sequence. Shot 1: Consumption of {topic}. Shot 2: X-Ray view of {body_part}. Shot 3: Detailed simulation of {visual_keywords}. Text labels explaining the mechanism."
        else:
            sora_prompt = f"{base_sora} Duration 60s. Educational storytelling. Journey of {topic} affecting {body_part}. Progressive damage showing {visual_keywords}. Comparison: Healthy vs Affected tissue."
        st.code(sora_prompt, language="bash")


# ==================================================
# TAB 2: LÀM ĐẸP (BEAUTY) - GIAO DIỆN ĐỒNG BỘ
# ==================================================
with main_tab2:
    st.header("Beauty 3D Studio 💉👄")
    st.info("🛠️ **Bước 1: Nhập thông tin dịch vụ**")
    
    with st.form("beauty_form"):
        c1, c2 = st.columns(2)
        with c1:
            beauty_topic = st.text_input("Tên dịch vụ / Vấn đề", "Tiêm Filler Môi")
            # 5 CƠ CHẾ LÀM ĐẸP
            mech_key = st.selectbox("Cơ chế tác động:", list(BEAUTY_MECHANISMS.keys()))
            
        with c2:
            # 3 GÓC NHÌN (PERSPECTIVE)
            perspective = st.selectbox("Góc nhìn (Perspective):", 
                                       ["🔬 Khoa học / Giải phẫu (Khuyên dùng)", 
                                        "✨ Thẩm mỹ / Satisfying", 
                                        "⚠️ Cảnh báo / Rủi ro"])
            
            # Visual tự động điền từ cơ chế
            mech_visual = BEAUTY_MECHANISMS[mech_key]
            beauty_visual_desc = st.text_input("Mô tả Visual (Tự động):", value=mech_visual)

        beauty_duration = st.select_slider("Thời lượng Video", options=["15s", "30s", "60s"], value="30s")
        submit_beauty = st.form_submit_button("🚀 XUẤT KỊCH BẢN & PROMPT (BEAUTY)")

    # --- KẾT QUẢ BEAUTY ---
    if submit_beauty:
        st.divider()
        st.success(f"✅ Đã xong bộ tài liệu Beauty: {beauty_topic}")
        
        # LOGIC XỬ LÝ THEO GÓC NHÌN (PERSPECTIVE)
        p_hook, p_body, p_tone = "", "", ""
        
        if "Khoa học" in perspective:
            p_hook = f"🔍 Giải phẫu học: Điều gì thực sự diễn ra dưới lớp da khi {beauty_topic}?"
            p_body = f"Mô phỏng mặt cắt lớp (Cross-section). Thấy rõ cấu trúc da/xương. Cơ chế {beauty_topic} tác động vào lớp trung bì/hạ bì. Hiển thị khoa học, trung lập."
            p_tone = "Educational, Neutral, Anatomically correct"
        elif "Thẩm mỹ" in perspective:
            p_hook = f"✨ Visual cực đã mắt: Quá trình {beauty_topic} biến hình trong 1 nốt nhạc!"
            p_body = f"Tập trung vào sự thay đổi mượt mà. Hiệu ứng {beauty_visual_desc} diễn ra trơn tru. Kết quả hoàn hảo, căng bóng."
            p_tone = "Satisfying, Beautiful, Smooth, Glowing"
        else: # Cảnh báo
            p_hook = f"⚠️ Cảnh báo: Đừng {beauty_topic} nếu chưa hiểu rõ cấu trúc giải phẫu này!"
            p_body = f"Mô phỏng rủi ro nếu làm sai kỹ thuật. Hiển thị mạch máu bị chèn ép hoặc vật liệu bị vón cục. Nhắc nhở an toàn."
            p_tone = "Warning, Detailed, Medical Risk"

        # 1. Kịch bản 3 Phần
        st.subheader("1. Kịch bản & Caption")
        st.info(f"""
        **🎬 KỊCH BẢN ({perspective})**
        * **HOOK:** {p_hook}
        * **BODY:** {p_body}
        * **VISUAL:** {beauty_visual_desc}
        * **CTA:** 👇 Bạn nghĩ sao về phương pháp này? Comment nhé!
        """)
        
        # Caption ngắn
        st.code(f"{p_hook}\nXem cận cảnh: {beauty_visual_desc}\n👇 Góc nhìn 3D chân thực nhất!\n\n#Beauty3D #{beauty_topic.replace(' ','')} #Giaiphau #Kienthuc", language="text")

        # 2. Prompt Thumbnail (Midjourney)
        st.subheader("2. Prompt Thumbnail (Style Đồng bộ)")
        mj_beauty = f"/imagine prompt: 3d medical animation cross-section of {beauty_topic}, showing {beauty_visual_desc}, perspective is {p_tone}, {MOON_STYLE}"
        st.code(mj_beauty, language="bash")

        # 3. Prompt Video Sora
        st.subheader(f"3. Prompt Video Sora ({beauty_duration})")
        sora_b = ""
        base_beauty = "Photorealistic 3D medical animation, 8k, dark blue background."
        
        if beauty_duration == "15s":
             sora_b = f"{base_beauty} Duration 15s. Macro shot. Focus on {beauty_topic}. Action: {beauty_visual_desc}. Tone: {p_tone}. Fast and clear."
        else:
             sora_b = f"{base_beauty} Duration {beauty_duration}. Process visualization. Step 1: Anatomy layers before procedure. Step 2: {beauty_visual_desc} in detail. Step 3: Result. Tone: {p_tone}. Text labels explaining anatomy."
             
        st.code(sora_b, language="bash")
