import streamlit as st

st.set_page_config(page_title="Nelly's Daily Routine", page_icon="👠", layout="wide")

# =========================================================
# 1. CẤU HÌNH PHONG CÁCH & LỊCH TRÌNH
# =========================================================

schedule_data = {
    "🌅 Buổi Sáng (Morning Routine)": {
        "activity": "Vận động & Lifestyle",
        "topics": ["Gym/Yoga tại nhà", "Bơi lội chào ngày mới", "Chạy bộ công viên", "Morning Skincare", "Pha cà phê/Matcha"],
        "vibe": "Energetic, fresh, bright morning light",
        "outfit": "Stylish gym wear (Alo Yoga/Lululemon) or Silk robe"
    },
    "🥗 Buổi Trưa (Healthy Lunch)": {
        "activity": "Ăn uống Healthy",
        "topics": ["Salad ức gà", "Sinh tố Green Detox", "Bữa trưa Eat Clean", "Review nhà hàng chay", "Uống đủ nước"],
        "vibe": "Cozy, clean, natural lighting, appetizing",
        "outfit": "Casual chic, comfortable home wear"
    },
    "☕ Buổi Chiều (Knowledge & Tips)": {
        "activity": "Chia sẻ kiến thức/Kỹ năng",
        "topics": ["Tips makeup nhanh", "Kỹ năng giao tiếp", "Truyền động lực (Quote)", "Học ngoại ngữ/Edit video", "Review sách hay"],
        "vibe": "Professional, smart, focus, warm tone",
        "outfit": "Smart casual, Blazer, Glasses"
    },
    "✨ Buổi Tối (Fashion & Glamour)": {
        "activity": "Biểu diễn Thời trang",
        "topics": ["Đi sự kiện (Event)", "Outfit of the Night (OOTD)", "Catwalk thần thái", "Biến hình (Transformation)", "Dạo phố đêm"],
        "vibe": "Luxury, glamour, city lights, flash photography",
        "outfit": "High-end Evening Gown, Designer Bag, Heels"
    }
}

# =========================================================
# GIAO DIỆN CHÍNH
# =========================================================

st.title("👠 NELLY'S DAILY ROUTINE")
st.markdown("*Lịch làm việc chuyên nghiệp của Fashion & Lifestyle KOL*")

# --- BƯỚC 1: CHỌN KHUNG GIỜ LÀM VIỆC ---
c1, c2 = st.columns([1, 2])

with c1:
    st.info("📅 **LỊCH TRÌNH HÔM NAY**")
    time_of_day = st.radio("Chọn buổi:", list(schedule_data.keys()))
    
    # Lấy dữ liệu theo buổi
    current_schedule = schedule_data[time_of_day]
    
    st.write("---")
    topic_select = st.selectbox("Chủ đề cụ thể:", current_schedule["topics"])
    st.caption(f"Trang phục: {current_schedule['outfit']}")

with c2:
    st.success(f"🎬 **SẢN XUẤT VIDEO: {topic_select}**")
    
    # Cấu hình Video
    col_set1, col_set2 = st.columns(2)
    with col_set1:
        duration_option = st.select_slider("Thời lượng Video:", options=["15s", "30s", "45s", "60s"], value="15s")
    with col_set2:
        style_select = st.radio("Phong cách:", ["KOL (Người thật)", "3D Animation (Mascot)"], horizontal=True)

    # Logic Style
    if style_select == "KOL (Người thật)":
        subject_prompt = "A stunning Vietnamese fashion KOL (Nelly), beautiful face, confident aura"
        visual_style = "High-end commercial, Arri Alexa, 8k, photorealistic"
    else:
        subject_prompt = "A cute 3D fashion doll character (Nelly)"
        visual_style = "Pixar style, vibrant colors, 8k"

    # =========================================================
    # XỬ LÝ LOGIC PROMPT (GỘP HOẶC TÁCH)
    # =========================================================
    
    t_num = int(duration_option.replace("s", ""))
    prompts_list = []
    
    # Nội dung chung dựa trên chủ đề
    outfit = current_schedule['outfit']
    vibe = current_schedule['vibe']
    topic = topic_select

    # --- TRƯỜNG HỢP 1: 15S (GỘP 1 PROMPT) ---
    if t_num == 15:
        # Kịch bản tóm tắt
        script_summary = f"""
        - HOOK (0-3s): Nelly xuất hiện ấn tượng/gây tò mò với {topic}.
        - BODY (3-12s): Thực hiện hành động chính ({current_schedule['activity']}) đầy năng lượng.
        - CTA (12-15s): Kêu gọi tương tác/thả tim.
        """
        
        # Prompt gộp
        action_desc = f"Start with a close up of Nelly looking at camera excitedly regarding {topic}. Then cut to wide shot of her {current_schedule['activity']}, wearing {outfit}. Ends with her winking and gesturing to follow."
        vn_line = f"Chào cả nhà! Hôm nay cùng Nelly {topic} nha. Bí quyết là đây nè! Nhớ thả tim cho Nelly đó."
        
        prompts_list.append({
            "title": "🎞️ FULL VIDEO (15s)",
            "action": action_desc,
            "dialogue": vn_line
        })

    # --- TRƯỜNG HỢP 2: 30S (TÁCH 2 PROMPTS) ---
    elif t_num == 30:
        script_summary = f"""
        - PHẦN 1 (0-15s): Hook + Dẫn dắt vấn đề.
        - PHẦN 2 (15-30s): Giải quyết/Show kết quả + CTA.
        """
        # P1
        prompts_list.append({
            "title": "🎞️ PHẦN 1 (0-15s): Mở đầu",
            "action": f"Nelly starts facing camera, talking about {topic} with {vibe} atmosphere. She looks slightly worried or curious, then presents the solution/item.",
            "dialogue": f"Mọi người hay hỏi Nelly bí quyết về {topic} đúng không? Hôm nay Nelly bật mí nha."
        })
        # P2
        prompts_list.append({
            "title": "🎞️ PHẦN 2 (15-30s): Kết quả & CTA",
            "action": f"Nelly confidently demonstrates {topic}, showing the result/final look. She looks happy, spins around or smiles brightly. Waving goodbye.",
            "dialogue": f"Đó, đơn giản vậy thôi mà hiệu quả lắm. Áp dụng ngay và khoe kết quả với Nelly nhé!"
        })

    # --- TRƯỜNG HỢP 3: 45S (TÁCH 3 PROMPTS) ---
    elif t_num == 45:
        script_summary = "Video 3 phần: Mở đầu -> Chi tiết -> Kết thúc."
        prompts_list.append({"title": "🎞️ PHẦN 1 (0-15s)", "action": f"Intro to {topic}, outfit {outfit}", "dialogue": "Hello cả nhà, lại là Nelly đây..."})
        prompts_list.append({"title": "🎞️ PHẦN 2 (15-30s)", "action": f"Deep dive into {topic}, showing details", "dialogue": "Bước quan trọng nhất là..."})
        prompts_list.append({"title": "🎞️ PHẦN 3 (30-45s)", "action": "Final result and Call to action", "dialogue": "Tuyệt vời chưa? Thử ngay nhé!"})

    # --- TRƯỜNG HỢP 4: 60S (TÁCH 4 PROMPTS) ---
    else:
        script_summary = "Video 4 phần: Vlog hoàn chỉnh."
        prompts_list.append({"title": "🎞️ PHẦN 1 (0-15s)", "action": "Vlog intro walking/talking", "dialogue": "Hôm nay là một ngày bận rộn của Nelly..."})
        prompts_list.append({"title": "🎞️ PHẦN 2 (15-30s)", "action": "Main activity highlights", "dialogue": "Đầu tiên là phải..."})
        prompts_list.append({"title": "🎞️ PHẦN 3 (30-45s)", "action": "Sharing tip/secret", "dialogue": "Lưu ý nhỏ cho mấy bà là..."})
        prompts_list.append({"title": "🎞️ PHẦN 4 (45-60s)", "action": "Outro and goodbye", "dialogue": "Hẹn gặp lại các tình yêu nha!"})

    # --- HIỂN THỊ KẾT QUẢ ---
    
    # 1. Kịch bản ngắn gọn (Nằm trong giao diện Video)
    with st.expander("📜 KỊCH BẢN TÓM TẮT (Tiếng Việt)", expanded=True):
        st.info(script_summary)

    # 2. Hiển thị Prompt
    st.divider()
    st.subheader("🎥 VIDEO PROMPT (SORA & VEO)")
    
    for p in prompts_list:
        st.markdown(f"**{p['title']}**")
        
        # Code Sora
        sora_prompt = f"""
        {visual_style}.
        Subject: {subject_prompt}, wearing {outfit}.
        Action: {p['action']}.
        Speaking Line (Vietnamese): "{p['dialogue']}"
        Lip-sync instruction: Match Vietnamese dialogue naturally.
        Atmosphere: {vibe}. Constraint: NO TEXT OVERLAYS.
        --duration 15s
        """
        st.code(sora_prompt, language='text')
        st.caption(f"💡 Thoại: {p['dialogue']}")
        st.divider()
