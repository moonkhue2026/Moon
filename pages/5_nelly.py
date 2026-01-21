import streamlit as st
import random
import datetime

st.set_page_config(page_title="Nelly's Viral Manager", page_icon="👠", layout="wide")

# =========================================================
# 1. CẤU HÌNH LỊCH TRÌNH CHI TIẾT (3 CA/NGÀY)
# =========================================================

weekly_schedule = {
    "Thứ 2": {
        "Sáng": "🥂 Lifestyle: Tư duy phụ nữ độc lập (Chào tuần mới)",
        "Chiều": "👗 Styling: Phối đồ đi làm thanh lịch",
        "Tối": "💃 Dancing: Biến hình đồ ngủ -> Đồ công sở",
        "Reason": "Đầu tuần cần năng lượng và sự chỉn chu."
    },
    "Thứ 3": {
        "Sáng": "💄 Beauty: Skincare nhanh gọn buổi sáng",
        "Chiều": "📸 Posing: 3 Dáng đứng chờ xe bus thần thái",
        "Tối": "💃 Dancing: Aerobic đốt mỡ bụng (Nhạc sôi động)",
        "Reason": "Giữa tuần tập trung vào kỹ năng & sức khỏe."
    },
    "Thứ 4": {
        "Sáng": "🥂 Lifestyle: Quản lý tài chính cá nhân",
        "Chiều": "👗 Styling: Tips chọn đồ che bụng mỡ",
        "Tối": "💃 Dancing: Bohemian Dance (Phong cách du mục phóng khoáng)",
        "Reason": "Thứ 4 đổi gió với style Bohemian hoang dã."
    },
    "Thứ 5": {
        "Sáng": "💄 Beauty: Review nước hoa mùi sang chảnh",
        "Chiều": "📸 Posing: Tạo dáng với ghế văn phòng",
        "Tối": "💃 Dancing: Sexy Dance (High Heels)",
        "Reason": "Chuẩn bị tinh thần cho cuối tuần rực rỡ."
    },
    "Thứ 6": {
        "Sáng": "🥂 Lifestyle: Vlog dọn tủ đồ tối giản",
        "Chiều": "👗 Styling: Phối đồ đi tiệc tối nay",
        "Tối": "💃 Dancing: Trend TikTok mới nhất",
        "Reason": "Thứ 6 máu chảy về tim, content ăn chơi/tiệc tùng."
    },
    "Thứ 7": {
        "Sáng": "🥂 Lifestyle: Đi cafe cuối tuần (Vlog)",
        "Chiều": "📸 Posing: Chụp ảnh sống ảo tại quán Cafe",
        "Tối": "💃 Dancing: Bohemian Dance (Quẩy bên đống lửa/Biển)",
        "Reason": "Cuối tuần Chill & Nghệ thuật."
    },
    "Chủ Nhật": {
        "Sáng": "💄 Beauty: Spa day tại nhà (Mask time)",
        "Chiều": "👗 Styling: Chuẩn bị outfit tuần sau",
        "Tối": "🥂 Lifestyle: Tâm sự mỏng/Q&A với Fan",
        "Reason": "Chủ nhật chữa lành và kết nối."
    }
}

# =========================================================
# 2. KHO TÀNG Ý TƯỞNG (ĐÃ THÊM BOHEMIAN)
# =========================================================

categories = {
    "💃 Dancing & Trends (Vũ đạo)": [
        "Bohemian Dance (Phong cách du mục/Hoang dã) 🌿", 
        "Nhảy Cover Trend TikTok mới nhất", 
        "Aerobic đốt mỡ bụng tại nhà", 
        "Sexy Dance thần thái (High Heels)", 
        "Shuffle Dance cực cuốn", 
        "Dance Sport sang trọng (Latin)", 
        "Biến hình: Đồ ngủ sang Đồ nhảy"
    ],
    "👗 Hack Dáng & Phối Đồ (Styling)": [
        "Hack chân dài cho nấm lùn 1m50", "Che bụng mỡ dưới thần thánh", "Phối đồ Gym đi chơi vẫn sang",
        "Biến đồ công sở thành Sang chảnh", "Tips chọn quần Jeans tôn vòng 3", "Phối màu đơn sắc tinh tế"
    ],
    "📸 Tạo Dáng & Thần Thái (Posing)": [
        "3 Dáng đứng chụp ảnh 'kéo chân'", "Tạo dáng với gương phòng tập", "Cách cười tự nhiên", 
        "Xử lý tay khi chụp ảnh", "Thần thái 'Chị Đại'"
    ],
    "💄 Làm Đẹp & Skincare (Beauty)": [
        "Makeup tone Tây đi quẩy", "Tips giữ nền không trôi khi tập Gym", "Quy trình Glass Skin", 
        "Chọn nước hoa 'Bad Girl'", "Buộc tóc đuôi ngựa hack tuổi"
    ],
    "🥂 Phong Cách Sống (Lifestyle)": [
        "Xây dựng sự tự tin", "Vlog: Một ngày đi tập & làm việc", "Chế độ ăn Eat Clean", "Tư duy phụ nữ độc lập"
    ]
}

# Caption Thư viện
caption_library = {
    "Dancing": ["Nhảy xấu không sao, quan trọng là thần thái! 💃", "Feel the beat, feel the heat! 🔥", "Bohemian vibe - Tự do như gió! 🌿"],
    "Styling": ["Quần áo làm nên thần thái! 😎", "Không có phụ nữ lùn, chỉ chưa biết hack dáng! 👠"],
    "Posing": ["Đứng im cũng đẹp, cười cái đổ luôn! 📸", "Thần thái không mua được bằng tiền! 💃"],
    "Beauty": ["Mồ hôi là lớp makeup đẹp nhất của Gymmer! 💦", "Makeup sương sương, sát thương cực lớn! 💋"],
    "Lifestyle": ["Sống sang là biết yêu bản thân. 🥂", "Body này tạo nên từ kỷ luật. 🔥"]
}

# Góc độ Video
pillars = {
    "🔥 Biến hình (Transformation)": {"kw": "snapping fingers transition, spinning, glowing up"},
    "🎓 Hướng dẫn (Tutorial)": {"kw": "pointing details, step-by-step demonstration"},
    "⚠️ Sai lầm (Mistakes)": {"kw": "holding STOP sign, shaking head No"},
    "💖 Biểu diễn/Vlog": {"kw": "performing confidently, energetic movement, cinematic shots"}
}

# =========================================================
# GIAO DIỆN APP
# =========================================================

st.title("👠 NELLY MANAGER v7.0")
st.markdown("*Kế hoạch Viral: 3 Bài/Ngày - Không lo sót việc!*")

# --- SIDEBAR: CHECKLIST CÔNG VIỆC ---
with st.sidebar:
    st.header("📅 CHECKLIST HÔM NAY")
    
    # Lấy thứ tự động
    days = list(weekly_schedule.keys())
    today_index = datetime.datetime.today().weekday()
    selected_day = st.selectbox("Chọn ngày làm việc:", days, index=today_index)
    
    schedule = weekly_schedule[selected_day]
    
    st.info(f"🎯 **Mục tiêu:** {schedule['Reason']}")
    
    st.markdown("### 📋 Nhiệm vụ cần làm:")
    task1 = st.checkbox(f"🌅 SÁNG: {schedule['Sáng'].split(':')[0]}")
    st.caption(f"Suggestion: {schedule['Sáng']}")
    
    task2 = st.checkbox(f"☀️ CHIỀU: {schedule['Chiều'].split(':')[0]}")
    st.caption(f"Suggestion: {schedule['Chiều']}")
    
    task3 = st.checkbox(f"🌙 TỐI: {schedule['Tối'].split(':')[0]}")
    st.caption(f"Suggestion: {schedule['Tối']}")
    
    if task1 and task2 and task3:
        st.balloons()
        st.success("Tuyệt vời! Moon đã hoàn thành KPI hôm nay! 💯")

    st.divider()
    st.write("⚙️ Cấu hình Video:")
    style_select = st.radio("Style:", ["KOL (Người thật)", "3D Animation"])
    duration_option = st.select_slider("Thời lượng:", ["15s", "30s", "45s", "60s"])

# --- MAIN: SẢN XUẤT NỘI DUNG ---
st.header(f"🎬 SẢN XUẤT NỘI DUNG: {selected_day}")

c1, c2 = st.columns([1, 2])
with c1:
    st.write("👉 **Chọn nhiệm vụ để làm ngay:**")
    # Tự động gợi ý task chưa làm
    suggested_task = schedule['Tối'] # Mặc định là Tối (Viral)
    if not task1: suggested_task = schedule['Sáng']
    elif not task2: suggested_task = schedule['Chiều']
    
    # Parse chủ đề từ lịch
    cat_hint = suggested_task.split(':')[0].strip() # Vd: Dancing
    topic_hint = suggested_task.split(':')[1].strip() # Vd: Bohemian Dance
    
    # Tìm index trong list categories
    cat_keys = list(categories.keys())
    cat_ix = 0
    for i, k in enumerate(cat_keys):
        if cat_hint in k: cat_ix = i; break
        
    group_select = st.selectbox("1. Nhóm chủ đề:", cat_keys, index=cat_ix)
    topic_select = st.selectbox("2. Chủ đề cụ thể:", categories[group_select]) # Moon có thể chọn Bohemian ở đây
    pillar_select = st.selectbox("3. Góc độ:", list(pillars.keys()))

# =========================================================
# XỬ LÝ LOGIC PROMPT
# =========================================================

# 1. Setup Style & Outfit (Update Bohemian Style)
is_dancing = "Dancing" in group_select
is_bohemian = "Bohemian" in topic_select

if style_select == "KOL (Người thật)":
    if is_bohemian:
        subject_prompt = "A stunning Vietnamese fashion KOL (Nelly), wearing Boho-chic outfit (maxi dress with patterns, accessories), free-spirited aura"
        visual_style = "Cinematic outdoor shot, beach sunset or forest background, warm golden lighting, dreamy vibe, 4k"
        grok_style = "Hyper-realistic, 8k, golden hour, festival vibes, flowing fabric"
    elif is_dancing:
        subject_prompt = "A fit Vietnamese fashion KOL (Nelly), trendy gym set (crop top & leggings)"
        visual_style = "High-energy dance video, TikTok viral style, neon lights studio, 4k"
        grok_style = "Hyper-realistic, 4k, neon atmosphere, energetic motion"
    else:
        subject_prompt = "A stunning Vietnamese fashion KOL (Nelly), trendy high-fashion outfit"
        visual_style = "High-end fashion commercial, Vogue style, cinematic lighting, 8k"
        grok_style = "Cinematic photography, soft lighting, luxury background, 8k"
else:
    subject_prompt = "Cute 3D fashion doll (Nelly), Pixar style"
    visual_style = "Disney Pixar 3D, vibrant colors"
    grok_style = "3D render, Pixar style, cute, vibrant"

# 2. Nội dung Prompt
current_pillar = pillars[pillar_select]
action_kw = current_pillar['kw']

if is_dancing:
    act_desc = f"dancing {topic_select} energetically. Dynamic camera movement focusing on rhythm."
    if is_bohemian:
        act_desc = "dancing Bohemian style, spinning freely, dress flowing in the wind, feeling the nature."
else:
    act_desc = f"demonstrating {topic_select}. Confident and elegant poses."

# Caption
cap_key = "Lifestyle"
if "Dancing" in group_select: cap_key = "Dancing"
elif "Styling" in group_select: cap_key = "Styling"
elif "Posing" in group_select: cap_key = "Posing"
elif "Beauty" in group_select: cap_key = "Beauty"
selected_cap = random.choice(caption_library[cap_key])

# =========================================================
# HIỂN THỊ KẾT QUẢ
# =========================================================

with c2:
    st.success(f"✨ **Đang làm: {topic_select}**")
    
    # TAB VIDEO PROMPTS
    t1, t2, t3, t4 = st.tabs(["🎥 SORA (15s)", "🤖 GROK 2 (6s)", "📝 CAPTION", "📰 BÀI VIẾT"])
    
    with t1:
        st.markdown("**Prompt Sora (Kể chuyện/Viral):**")
        sora_prompt = f"""
        {visual_style}. Subject: {subject_prompt}.
        Action: {act_desc}. {action_kw}.
        Speaking Line (Vietnamese): "Cùng Nelly {topic_select} nhé!"
        Lip-sync instruction: Match naturally. Context: {topic_select}. Constraint: NO TEXT. --duration 15s
        """
        st.code(sora_prompt, language='text')

    with t2:
        st.markdown("**Prompt Grok 2 (Visual cực phẩm - 6s):**")
        grok_prompt = f"""
        Video of {subject_prompt}, {act_desc}. {grok_style}, highly detailed, fluid motion, trending on artstation.
        --duration 6s
        """
        st.code(grok_prompt, language='text')
        st.caption("💡 Dùng làm Intro hoặc video ngắn đăng Story.")

    with t3:
        st.code(f"{selected_cap}\n\n#Nelly #{topic_select.replace(' ','')} #Viral", language="text")
        
    with t4:
        st.subheader("Prompt viết bài (Copy cho ChatGPT):")
        st.code(f"""
        Viết bài Facebook/TikTok về: {topic_select}.
        - Phong cách: {visual_style}
        - Góc độ: {pillar_select}
        - Mục tiêu: Viral và tương tác.
        - Hashtag: #NellyViral
        """, language='text')
