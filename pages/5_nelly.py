import streamlit as st
import random
import datetime

st.set_page_config(page_title="Nelly Manager v8.0", page_icon="👠", layout="wide")

# =========================================================
# 1. CẤU HÌNH LỊCH TRÌNH & DỮ LIỆU
# =========================================================

weekly_schedule = {
    "Thứ 2": {"Sáng": "🥂 Lifestyle: Tư duy độc lập", "Chiều": "👗 Styling: Phối đồ công sở", "Tối": "💃 Dancing: Biến hình", "Reason": "Đầu tuần chỉn chu & năng lượng."},
    "Thứ 3": {"Sáng": "💄 Beauty: Skincare nhanh", "Chiều": "📸 Posing: Dáng đứng chờ xe", "Tối": "💃 Dancing: Aerobic đốt mỡ", "Reason": "Giữa tuần tập trung kỹ năng."},
    "Thứ 4": {"Sáng": "🥂 Lifestyle: Quản lý tài chính", "Chiều": "👗 Styling: Che bụng mỡ", "Tối": "💃 Dancing: Bohemian Dance (Hoang dã)", "Reason": "Đổi gió với style Bohemian."},
    "Thứ 5": {"Sáng": "💄 Beauty: Review nước hoa", "Chiều": "📸 Posing: Dáng ghế văn phòng", "Tối": "💃 Dancing: Sexy Dance", "Reason": "Chuẩn bị cho cuối tuần."},
    "Thứ 6": {"Sáng": "🥂 Lifestyle: Dọn tủ đồ", "Chiều": "👗 Styling: Đồ đi tiệc", "Tối": "💃 Dancing: Trend TikTok", "Reason": "Thứ 6 máu chảy về tim."},
    "Thứ 7": {"Sáng": "🥂 Lifestyle: Cafe cuối tuần", "Chiều": "📸 Posing: Sống ảo quán Cafe", "Tối": "💃 Dancing: Bohemian Dance (Biển)", "Reason": "Cuối tuần Chill & Nghệ thuật."},
    "Chủ Nhật": {"Sáng": "💄 Beauty: Spa day", "Chiều": "👗 Styling: Outfit tuần sau", "Tối": "🥂 Lifestyle: Q&A Tâm sự", "Reason": "Chủ nhật chữa lành."}
}

categories = {
    "💃 Dancing & Trends": ["Bohemian Dance (Du mục) 🌿", "Nhảy Cover Trend TikTok", "Aerobic đốt mỡ", "Sexy Dance (High Heels)", "Shuffle Dance", "Biến hình: Đồ ngủ -> Đồ nhảy"],
    "👗 Hack Dáng & Phối Đồ": ["Hack chân dài 1m50", "Che bụng mỡ dưới", "Phối đồ Gym sang chảnh", "Biến đồ công sở", "Tips quần Jeans tôn vòng 3"],
    "📸 Tạo Dáng (Posing)": ["3 Dáng đứng 'kéo chân'", "Tạo dáng gương phòng tập", "Cách cười tự nhiên", "Xử lý tay đỡ đơ", "Thần thái 'Chị Đại'"],
    "💄 Làm Đẹp (Beauty)": ["Makeup tone Tây", "Giữ nền không trôi khi tập", "Quy trình Glass Skin", "Nước hoa 'Bad Girl'", "Tóc đuôi ngựa hack tuổi"],
    "🥂 Lifestyle": ["Xây dựng sự tự tin", "Vlog: Một ngày của Nelly", "Eat Clean giữ dáng", "Tư duy phụ nữ độc lập"]
}

caption_library = {
    "Dancing": ["Nhảy xấu không sao, quan trọng là thần thái! 💃", "Feel the beat, feel the heat! 🔥", "Bohemian vibe - Tự do như gió! 🌿"],
    "Styling": ["Quần áo làm nên thần thái! 😎", "Không có phụ nữ lùn, chỉ chưa biết hack dáng! 👠"],
    "Posing": ["Đứng im cũng đẹp, cười cái đổ luôn! 📸", "Thần thái không mua được bằng tiền! 💃"],
    "Beauty": ["Mồ hôi là lớp makeup đẹp nhất của Gymmer! 💦", "Makeup sương sương, sát thương cực lớn! 💋"],
    "Lifestyle": ["Sống sang là biết yêu bản thân. 🥂", "Body này tạo nên từ kỷ luật. 🔥"]
}

pillars = {
    "🔥 Biến hình (Transformation)": {"kw": "snapping fingers transition, spinning, glowing up", "tone": "Hào hứng, Nhạc Trend"},
    "🎓 Hướng dẫn (Tutorial)": {"kw": "pointing details, step-by-step demonstration", "tone": "Chuyên gia, Rõ ràng"},
    "⚠️ Sai lầm (Mistakes)": {"kw": "holding STOP sign, shaking head No", "tone": "Nghiêm túc, Cảnh báo"},
    "💖 Biểu diễn/Vlog": {"kw": "performing confidently, energetic movement", "tone": "Cuốn hút, Cảm xúc"}
}

# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("👠 NELLY MANAGER v8.0")
st.markdown("*Quy trình chuẩn: 1. Bài viết & Ảnh -> 2. Video (Sora/Grok)*")

# --- SIDEBAR: CHECKLIST ---
with st.sidebar:
    st.header("📅 CHECKLIST HÔM NAY")
    days = list(weekly_schedule.keys())
    today_index = datetime.datetime.today().weekday()
    selected_day = st.selectbox("Ngày làm việc:", days, index=today_index)
    schedule = weekly_schedule[selected_day]
    
    st.info(f"🎯 **Mục tiêu:** {schedule['Reason']}")
    st.checkbox(f"🌅 SÁNG: {schedule['Sáng']}")
    st.checkbox(f"☀️ CHIỀU: {schedule['Chiều']}")
    st.checkbox(f"🌙 TỐI: {schedule['Tối']}")

# --- MAIN: CẤU HÌNH ---
with st.expander("⚙️ CẤU HÌNH NỘI DUNG (Bấm mở rộng)", expanded=True):
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1: 
        # Logic gợi ý chủ đề từ lịch
        suggested = schedule['Tối']
        cat_hint = suggested.split(':')[0].strip()
        cat_ix = next((i for i, k in enumerate(categories.keys()) if cat_hint in k), 0)
        group_select = st.selectbox("1. Nhóm chủ đề:", list(categories.keys()), index=cat_ix)
    
    with c2: topic_select = st.selectbox("2. Chủ đề cụ thể:", categories[group_select])
    with c3: pillar_select = st.selectbox("3. Góc độ:", list(pillars.keys()))
    
    st.write("---")
    c4, c5 = st.columns(2)
    with c4: style_select = st.radio("Style:", ["KOL (Người thật)", "3D Animation"], horizontal=True)
    with c5: 
        is_dancing = "Dancing" in group_select
        is_bohemian = "Bohemian" in topic_select
        if is_bohemian: outfit_desc = "Boho-chic maxi dress, accessories"
        elif is_dancing: outfit_desc = "Trendy gym set (crop top & leggings)"
        else: outfit_desc = "High-fashion trendy outfit"
        st.caption(f"👕 Outfit: {outfit_desc}")

# =========================================================
# XỬ LÝ LOGIC (PROMPT GENERATOR)
# =========================================================

# 1. Setup Visual Style
if style_select == "KOL (Người thật)":
    subject = f"A stunning Vietnamese fashion KOL (Nelly), wearing {outfit_desc}"
    if is_bohemian:
        vis_style = "Cinematic outdoor, beach sunset/forest, warm lighting, 4k"
        grok_style = "Hyper-realistic, 8k, golden hour, festival vibes"
    elif is_dancing:
        vis_style = "High-energy dance studio, neon lights, 4k"
        grok_style = "Hyper-realistic, 4k, neon atmosphere, energetic"
    else:
        vis_style = "High-end fashion commercial, Vogue style, 8k"
        grok_style = "Cinematic photography, soft lighting, luxury background"
else:
    subject = "Cute 3D fashion doll (Nelly), Pixar style"
    vis_style = "Disney Pixar 3D, vibrant colors"
    grok_style = "3D render, Pixar style, cute"

current_pillar = pillars[pillar_select]

# 2. Logic Caption
cap_key = "Lifestyle"
if "Dancing" in group_select: cap_key = "Dancing"
elif "Styling" in group_select: cap_key = "Styling"
elif "Beauty" in group_select: cap_key = "Beauty"
elif "Posing" in group_select: cap_key = "Posing"
selected_cap = random.choice(caption_library[cap_key])

# =========================================================
# HIỂN THỊ KẾT QUẢ (TAB CHUẨN)
# =========================================================

tab_content, tab_video = st.tabs(["📝 BÀI VIẾT & ẢNH", "🎥 VIDEO (Sora & Grok)"])

# --- TAB 1: NỘI DUNG & ẢNH (LÀM TRƯỚC) ---
with tab_content:
    col_cap, col_blog = st.columns(2)
    
    with col_cap:
        st.subheader("1. Caption (TikTok/FB)")
        st.code(f"{selected_cap}\n\n#Nelly #{topic_select.replace(' ','')} #Trending", language="text")
        
        st.divider()
        st.subheader("2. Prompt Ảnh (Midjourney) - ĐÃ BỔ SUNG ✅")
        mj_prompt = f"/imagine prompt: A stunning photography shot of Nelly, {outfit_desc}, posing confidently. Context: {topic_select}. {vis_style.split(',')[0]}, vogue style, 8k --ar 3:4"
        st.code(mj_prompt, language='text')

    with col_blog:
        st.subheader("3. Prompt Viết Bài (ChatGPT)")
        st.code(f"""
        Viết bài Facebook/Blog về: {topic_select}.
        - Phong cách: {outfit_desc}.
        - Góc độ: {pillar_select}.
        - Tone giọng: {current_pillar['tone']}.
        - Kêu gọi hành động: Tương tác mạnh.
        """, language='text')

# --- TAB 2: VIDEO (LÀM SAU) ---
with tab_video:
    st.subheader(f"🎬 Sản xuất Video: {topic_select}")
    
    st.markdown("#### 🅰️ Prompt Sora 2 (15s - Kể chuyện/Full bài)")
    sora_prompt = f"""
    {vis_style}. Subject: {subject}.
    Action: {topic_select}, {current_pillar['kw']}.
    Camera: Dynamic movement.
    Lighting: Cinematic.
    Constraint: NO TEXT. --duration 15s
    """
    st.code(sora_prompt, language='text')
    
    st.divider()
    
    st.markdown("#### 🅱️ Prompt Grok 2 (6s - Intro/Highlight)")
    grok_prompt = f"""
    Video of {subject}, performing {topic_select}. {grok_style}, highly detailed, fluid motion, trending on artstation.
    --duration 6s
    """
    st.code(grok_prompt, language='text')
    st.caption("💡 Mẹo: Dùng Grok làm Intro hoặc đoạn Highlight ngắn cực đẹp.")'text')
