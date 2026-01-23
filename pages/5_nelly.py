import streamlit as st
import random
import datetime

st.set_page_config(page_title="Nelly Manager v9.4", page_icon="👠", layout="wide")

# =========================================================
# 1. KHO DỮ LIỆU (KHÔI PHỤC CHÍNH XÁC TỪ ẢNH CHỤP)
# =========================================================

# Lịch trình (Giữ nguyên cấu trúc Checklist bên trái)
weekly_schedule = {
    "Thứ 2": {"Sáng": "🥂 Lifestyle: Dọn tủ đồ", "Chiều": "👗 Styling: Đồ công sở", "Tối": "💃 Dancing: Cơ bản", "Reason": "Đầu tuần năng lượng"},
    "Thứ 3": {"Sáng": "💄 Beauty: Skincare", "Chiều": "📸 Posing: Tập dáng", "Tối": "💃 Dancing: Sexy Dance", "Reason": "Tập trung kỹ năng"},
    "Thứ 4": {"Sáng": "🥂 Lifestyle: Cafe sáng", "Chiều": "👗 Styling: Streetwear", "Tối": "💃 Dancing: Shuffle", "Reason": "Đổi gió Bohemian"},
    "Thứ 5": {"Sáng": "💄 Beauty: Makeup", "Chiều": "📸 Posing: Chụp ảnh", "Tối": "💃 Dancing: Choreography", "Reason": "Chuẩn bị cuối tuần"},
    "Thứ 6": {"Sáng": "🥂 Lifestyle: Dọn tủ đồ", "Chiều": "👗 Styling: Đồ đi tiệc", "Tối": "💃 Dancing: Trend TikTok", "Reason": "Thứ 6 máu chảy về tim"},
    "Thứ 7": {"Sáng": "🥂 Lifestyle: Du lịch", "Chiều": "📸 Posing: Ngoại cảnh", "Tối": "💃 Dancing: Free style", "Reason": "Cuối tuần Chill"},
    "Chủ Nhật": {"Sáng": "💄 Beauty: Spa", "Chiều": "👗 Styling: Sắp xếp", "Tối": "🥂 Lifestyle: Tổng kết", "Reason": "Chủ nhật chữa lành"}
}

# Danh sách chủ đề (Chuẩn hóa theo Screenshot 139 & Yêu cầu 5 mục lớn)
categories = {
    "💃 Dancing & Trends": [ # 6 mục chuẩn theo ảnh 139
        "Bohemian Dance (Du mục) 🌿", 
        "Nhảy Cover Trend TikTok", 
        "Aerobic đốt mỡ", 
        "Sexy Dance (High Heels)", 
        "Shuffle Dance", 
        "Biến hình: Đồ ngủ -> Đồ nhảy"
    ],
    "👗 Hack Dáng & Phối Đồ": [
        "Hack chân dài 1m70", 
        "Che bụng mỡ dưới", 
        "Phối đồ Gym/Sporty", 
        "Outfit công sở sang chảnh", 
        "Boho-Chic (Du mục)"
    ],
    "📸 Tạo Dáng (Posing)": [
        "Góc mặt thần thánh", 
        "Dáng đứng hack chân", 
        "Tạo dáng với ghế", 
        "Tạo dáng cafe", 
        "Thần thái sang chảnh"
    ],
    "💄 Làm Đẹp (Beauty)": [
        "Makeup Tone Tây", 
        "Skincare Glass Skin", 
        "Tóc hack tuổi", 
        "Nước hoa bad girl"
    ],
    "🥂 Lifestyle": [
        "Vlog 1 ngày của Nelly", 
        "Tư duy phụ nữ hiện đại", 
        "Eat Clean giữ dáng", 
        "Góc Chill tại nhà"
    ]
}

# Danh sách Góc độ (Chuẩn hóa theo Screenshot 140 - 4 mục)
angles_list = [
    "🔥 Biến hình (Transformation)", 
    "🎓 Hướng dẫn (Tutorial)", 
    "⚠️ Sai lầm (Mistakes)", 
    "❤️ Biểu diễn/Vlog"
]

# =========================================================
# 2. GIAO DIỆN APP (LAYOUT CHUẨN)
# =========================================================

# --- SIDEBAR: CHECKLIST (Chuẩn ảnh 135) ---
with st.sidebar:
    st.header("🗓️ CHECKLIST HÔM NAY")
    
    # Xác định ngày
    days = list(weekly_schedule.keys())
    today = datetime.datetime.today().strftime("%A")
    d_map = {"Monday": "Thứ 2", "Tuesday": "Thứ 3", "Wednesday": "Thứ 4", "Thursday": "Thứ 5", "Friday": "Thứ 6", "Saturday": "Thứ 7", "Sunday": "Chủ Nhật"}
    today_vi = d_map.get(today, "Thứ 2")
    
    selected_day = st.selectbox("Ngày làm việc:", days, index=days.index(today_vi) if today_vi in days else 0)
    schedule = weekly_schedule[selected_day]
    
    # Box mục tiêu (Màu xanh dương như ảnh)
    st.info(f"🎯 Mục tiêu: {schedule['Reason']}")
    
    st.write("---")
    # Checkbox công việc
    st.checkbox(f"🌅 SÁNG: {schedule['Sáng']}")
    st.checkbox(f"🌞 CHIỀU: {schedule['Chiều']}")
    st.checkbox(f"🌙 TỐI: {schedule['Tối']}")

# --- MAIN: CẤU HÌNH (Chuẩn ảnh 138, 139, 140) ---
# Dùng st.expander để tạo khung "CẤU HÌNH NỘI DUNG" có thể đóng mở
with st.expander("⚙️ CẤU HÌNH NỘI DUNG", expanded=True):
    c1, c2, c3 = st.columns([1.5, 2, 1.5])
    
    with c1: 
        # Nhóm chủ đề (5 mục)
        group_select = st.selectbox("Nhóm chủ đề:", list(categories.keys()))
    
    with c2: 
        # Chủ đề cụ thể (6 mục nếu chọn Dancing)
        topic_select = st.selectbox("Chủ đề cụ thể:", categories[group_select])
    
    with c3:
        # Góc độ (4 mục chuẩn)
        angle_select = st.selectbox("Góc độ:", angles_list)

    st.write("---")
    
    # Dòng Style và Outfit (Layout 2 cột)
    c_style, c_outfit = st.columns([1.5, 3])
    with c_style:
        style_select = st.radio("Style:", ["🔴 KOL (Người thật)", "⚪ 3D Animation"], horizontal=True)
    
    with c_outfit:
        # LOGIC TỰ ĐỘNG MAP OUTFIT & NHẠC (Dựa trên Topic đã chọn)
        # 1. Bohemian
        if "Bohemian" in topic_select or "Du mục" in topic_select:
            outfit_text = "Boho-chic maxi dress, headband, vintage accessories 🌿"
            music_text = "🌿 Acoustic Guitar, Indie Folk, Chill, Dreamy, Travel Vibe, Nomadic"
            caption_style = "Bohemian"
            
        # 2. Sexy Dance / High Heels
        elif "Sexy" in topic_select or "High Heels" in topic_select:
            outfit_text = "Sexy Cut-out Bodysuit & High Heels 👠"
            music_text = "🔥 Upbeat, EDM, Vinahouse, TikTok Trend Remix, High Tempo"
            caption_style = "Sexy"
            
        # 3. Gym / Aerobic
        elif "Aerobic" in topic_select or "Gym" in topic_select or "đốt mỡ" in topic_select:
            outfit_text = "Trendy gym set (crop top & leggings) 👟"
            music_text = "⚡ Workout Remix, High BPM, Aerobic Beat"
            caption_style = "Gym"
            
        # 4. Biến hình Đồ ngủ
        elif "Biến hình" in topic_select and "Đồ ngủ" in topic_select:
            outfit_text = "Pajamas (Before) -> Glitter Dress (After) ✨"
            music_text = "🎵 Transition Sound, Magic Chime, Drop Beat"
            caption_style = "Transition"
            
        # 5. Mặc định
        else:
            outfit_text = "High-fashion elegant dress ✨"
            music_text = "🎵 Trending TikTok Sound, Pop, R&B"
            caption_style = "General"
            
        st.caption(f"👕 Outfit: {outfit_text}")

# Box xanh lá gợi ý nhạc (Chuẩn ảnh 135)
st.success(f"🎵 Gợi ý Nhạc cho chủ đề này (Tìm trên CapCut): {music_text}")

# =========================================================
# 3. KẾT QUẢ (TAB LAYOUT)
# =========================================================

tab1, tab2, tab3 = st.tabs(["📝 BÀI VIẾT & ẢNH", "🎥 VIDEO (Sora & Grok)", "🎬 KỊCH BẢN (Script)"])

with tab1:
    col_cap, col_prompt = st.columns(2)
    with col_cap:
        st.subheader("1. Caption (TikTok/FB)")
        # Logic Caption
        if caption_style == "Bohemian":
            cap_content = f"Bohemian vibe - Tự do như gió! 🌿\n\n#Nelly #BohemianDance #DuMục #Trending"
        elif caption_style == "Sexy":
            cap_content = f"Đốt cháy sàn diễn hôm nay! 🔥\nAi bảo tập nhảy là mệt? Vừa đẹp dáng vừa thần thái.\n\n#Nelly #SexyDance #HighHeels #Trending"
        elif caption_style == "Gym":
            cap_content = f"Đốt mỡ cùng Nelly nào! 💦\nKhỏe đẹp mỗi ngày.\n\n#Nelly #Aerobic #GymMotivation"
        else:
            cap_content = f"{topic_select} cùng Nelly nhé! ✨\n\n#Nelly #Fashion #Trending"
            
        st.info(cap_content)
        
    with col_prompt:
        st.subheader("2. Prompt Ảnh (Midjourney)")
        st.code(f"/imagine prompt: A stunning photography shot of Nelly, {outfit_text}, performing {topic_select}, cinematic lighting --ar 3:4", language="text")

with tab2:
    st.subheader(f"🎬 Sản xuất Video: {topic_select}")
    
    # Logic Prompt Sora dựa trên Góc độ (Angle)
    action_desc = f"performing {topic_select}"
    
    if "Biến hình" in angle_select:
        action_desc = "TRANSFORMATION EFFECT: Starts with messy look/pajamas, then magic transition to stunning look in " + outfit_text
    elif "Sai lầm" in angle_select:
        action_desc = "holding a STOP sign initially, shaking head 'No', then smiling and showing the correct way"
    elif "Hướng dẫn" in angle_select:
        action_desc = "slowly demonstrating step-by-step movements, educational vibe"
        
    st.markdown("#### 🅰️ Prompt Sora 2 (15s)")
    st.code(f"""
    Cinematic outdoor/studio, 4k. Subject: A stunning Vietnamese fashion KOL (Nelly).
    Outfit: {outfit_text}.
    Action: {action_desc}. Energetic movements matching the beat.
    Camera: Dynamic zoom/pan. Constraint: NO TEXT. --duration 15s
    """, language="text")

with tab3:
    st.warning(f"💡 Kịch bản quay chi tiết: {angle_select}")
    if "Biến hình" in angle_select:
        st.markdown(f"""
        - **0-3s:** Mặc đồ thường/đồ ngủ. Mặt buồn chán. Nhạc intro nhẹ.
        - **3-5s:** Búng tay cái "Tách"! (Hiệu ứng chuyển cảnh).
        - **5-15s:** BÙM! {outfit_text} xuất hiện. Nhạc {music_text} nổi lên cực mạnh. Nelly diễn thần thái.
        """)
    elif "Sai lầm" in angle_select:
        st.markdown("""
        - **0-3s:** Làm động tác sai (ví dụ: gù lưng, phối đồ lỗi). Nhạc 'Èo uột'.
        - **3-5s:** Hiệu ứng dấu X đỏ to đùng ❌.
        - **5-15s:** Nelly bước ra đẩy cái bóng cũ đi, thị phạm dáng chuẩn. Nhạc sang chảnh.
        """)
    else:
        st.markdown(f"- **Toàn bộ:** Quay các góc cận/trung/toàn của {topic_select}. Chú ý bắt trọn khoảnh khắc thần thái nhất.")
