import streamlit as st
import random
import datetime

# =========================================================
# CẤU HÌNH APP & VERSION
# =========================================================
APP_VERSION = "v9.8"
st.set_page_config(page_title=f"Nelly Manager {APP_VERSION}", page_icon="👠", layout="wide")

# =========================================================
# 1. KHO DỮ LIỆU KHỔNG LỒ (ĐÃ CẬP NHẬT THÊM DU LỊCH)
# =========================================================

# 1.1. Danh sách chủ đề chi tiết
categories = {
    "💃 Dancing & Trends (Vũ đạo Viral)": [
        "Nhảy Cover Trend TikTok mới nhất",
        "Aerobic đốt mỡ bụng tại nhà",
        "Sexy Dance thần thái (High Heels)",
        "Shuffle Dance cực cuốn",
        "Dance Sport sang trọng (Cha Cha Cha/Rumba)",
        "Biến hình: Từ đồ ngủ sang Đồ nhảy (Transformation)",
        "Nhảy Free-style ngẫu hứng trên phố"
    ],
    "👗 Hack Dáng & Phối Đồ (Styling)": [
        "Hack chân dài cho nấm lùn 1m50",
        "Che bụng mỡ dưới thần thánh",
        "Phối đồ Gym/Sporty đi chơi vẫn sang",
        "Biến đồ công sở nhàm chán thành Sang chảnh",
        "Tips chọn quần Jeans tôn vòng 3",
        "Phối màu đơn sắc (Monochrome) tinh tế"
    ],
    "📸 Tạo Dáng & Thần Thái (Posing)": [
        "3 Dáng đứng chụp ảnh 'kéo chân' ảo diệu",
        "Tạo dáng với gương phòng tập (Gym Mirror)",
        "Cách cười tự nhiên không bị gượng gạo",
        "Xử lý tay khi chụp ảnh (đỡ bị đơ)",
        "Thần thái 'Chị Đại' (Boss Girl Energy)",
        "Tạo dáng ngoại cảnh / Check-in du lịch (Outdoor)" # <-- MỚI THÊM
    ],
    "💄 Làm Đẹp & Skincare (Beauty)": [
        "Makeup tone Tây đi tiệc/đi quẩy",
        "Tips giữ lớp nền không trôi khi tập Gym",
        "Quy trình dưỡng da Glass Skin buổi tối",
        "Chọn mùi nước hoa 'Bad Girl' quyến rũ",
        "Cách buộc tóc đuôi ngựa (Ponytail) hack tuổi"
    ],
    "🥂 Phong Cách Sống (Lifestyle)": [
        "Xây dựng sự tự tin từ bên trong",
        "Vlog: Một ngày đi tập & làm việc của Nelly",
        "Chế độ ăn Eat Clean giữ dáng",
        "Tư duy phụ nữ hiện đại: Độc lập & Hạnh phúc",
        "Vlog Du lịch & Trải nghiệm (Travel Vlog)" # <-- MỚI THÊM
    ]
}

# 1.2. Kho Caption phong phú
caption_library = {
    "Dancing": [
        "Nhảy xấu không sao, quan trọng là thần thái! 💃🔥",
        "Đốt cháy sàn diễn (và cả mỡ bụng) cùng Nelly! 💦",
        "Nhạc lên là em lên! Ai đu trend này chưa? 🎶",
        "Tập luyện là cách yêu bản thân tốt nhất. Go hard or go home! 💪"
    ],
    "Styling": [
        "Quần áo không làm nên con người, nhưng làm nên thần thái! 😎",
        "Không có phụ nữ lùn, chỉ có phụ nữ chưa biết hack dáng! 👠",
        "Mặc đẹp không phải để ai ngắm, mà là để mình vui! ✨"
    ],
    "Posing": [
        "Đứng im cũng đẹp, mà cười cái là 'đổ' luôn! 📸",
        "Thần thái là thứ không mua được bằng tiền, nhưng luyện tập thì được! 💃",
        "Lưu ngay bí kíp tạo dáng này kẻo xóa video nha mấy bà! 🤫"
    ],
    "Beauty": [
        "Đẹp tự nhiên nhưng không phải tự nhiên mà đẹp! 💄",
        "Mồ hôi là lớp makeup đẹp nhất của cô gái phòng Gym! 💦",
        "Makeup sương sương nhưng sát thương cực lớn! 💋"
    ],
    "Lifestyle": [
        "Sống sang không phải là khoe tiền, mà là biết yêu bản thân. 🥂",
        "Phụ nữ hiện đại: Kiếm tiền giỏi, Sống chất chơi! 👑",
        "Body này được tạo nên từ kỷ luật, không phải may mắn. 🔥",
        "Đi đâu không quan trọng, quan trọng là đi cùng ai (và có ảnh đẹp mang về)! ✈️🌊" # <-- MỚI THÊM
    ]
}

# 1.3. Lịch trình tuần
weekly_schedule = {
    "Thứ 2": {"Sáng": "🥂 Lifestyle: Dọn tủ đồ", "Chiều": "👗 Styling: Đồ công sở", "Tối": "💃 Dancing: Cơ bản", "Reason": "Đầu tuần năng lượng"},
    "Thứ 3": {"Sáng": "💄 Beauty: Skincare", "Chiều": "📸 Posing: Tập dáng", "Tối": "💃 Dancing: Sexy Dance", "Reason": "Tập trung kỹ năng"},
    "Thứ 4": {"Sáng": "🥂 Lifestyle: Cafe sáng", "Chiều": "👗 Styling: Streetwear", "Tối": "💃 Dancing: Shuffle", "Reason": "Đổi gió Bohemian"},
    "Thứ 5": {"Sáng": "💄 Beauty: Makeup", "Chiều": "📸 Posing: Chụp ảnh", "Tối": "💃 Dancing: Choreography", "Reason": "Chuẩn bị cuối tuần"},
    "Thứ 6": {"Sáng": "🥂 Lifestyle: Dọn tủ đồ", "Chiều": "👗 Styling: Đồ đi tiệc", "Tối": "💃 Dancing: Trend TikTok", "Reason": "Thứ 6 máu chảy về tim"},
    "Thứ 7": {"Sáng": "🥂 Lifestyle: Du lịch", "Chiều": "📸 Posing: Ngoại cảnh", "Tối": "💃 Dancing: Free style", "Reason": "Cuối tuần Chill"},
    "Chủ Nhật": {"Sáng": "💄 Beauty: Spa", "Chiều": "👗 Styling: Sắp xếp", "Tối": "🥂 Lifestyle: Tổng kết", "Reason": "Chủ nhật chữa lành"}
}

# 1.4. Góc độ (Angles)
angles_list = ["🔥 Biến hình (Transformation)", "🎓 Hướng dẫn (Tutorial)", "⚠️ Sai lầm (Mistakes)", "❤️ Biểu diễn/Vlog"]

# =========================================================
# 2. GIAO DIỆN APP
# =========================================================

# --- SIDEBAR ---
with st.sidebar:
    st.markdown(f"## 🚀 {APP_VERSION}") 
    st.header("🗓️ CHECKLIST HÔM NAY")
    
    days = list(weekly_schedule.keys())
    today = datetime.datetime.today().strftime("%A")
    d_map = {"Monday": "Thứ 2", "Tuesday": "Thứ 3", "Wednesday": "Thứ 4", "Thursday": "Thứ 5", "Friday": "Thứ 6", "Saturday": "Thứ 7", "Sunday": "Chủ Nhật"}
    today_vi = d_map.get(today, "Thứ 2")
    
    selected_day = st.selectbox("Ngày làm việc:", days, index=days.index(today_vi) if today_vi in days else 0)
    schedule = weekly_schedule[selected_day]
    
    st.info(f"🎯 Mục tiêu: {schedule['Reason']}")
    st.write("---")
    st.checkbox(f"🌅 SÁNG: {schedule['Sáng']}")
    st.checkbox(f"🌞 CHIỀU: {schedule['Chiều']}")
    st.checkbox(f"🌙 TỐI: {schedule['Tối']}")

# --- MAIN CONFIG ---
st.title(f"👠 NELLY MANAGER {APP_VERSION}")

with st.expander("⚙️ CẤU HÌNH NỘI DUNG", expanded=True):
    c1, c2, c3 = st.columns([1.5, 2, 1.5])
    with c1: 
        group_select = st.selectbox("Nhóm chủ đề:", list(categories.keys()))
    with c2: 
        topic_select = st.selectbox("Chủ đề cụ thể:", categories[group_select])
    with c3: 
        angle_select = st.selectbox("Góc độ:", angles_list)

    st.write("---")
    
    c_style, c_outfit = st.columns([1.5, 3])
    with c_style: 
        style_select = st.radio("Style:", ["🔴 KOL (Người thật)", "⚪ 3D Animation"], horizontal=True)
    
    with c_outfit:
        # LOGIC XỬ LÝ THÔNG MINH (MAPPING DATA)
        # 1. Xác định Style cơ bản
        if "Dancing" in group_select:
            key_style = "Dancing"
            music_text = "🔥 Upbeat, EDM, Vinahouse, TikTok Trend Remix"
            outfit_text = "Sexy Cut-out Bodysuit & High Heels 👠" if "Sexy" in topic_select else "Trendy gym set 👟"
        elif "Styling" in group_select:
            key_style = "Styling"
            music_text = "👠 Fashion Show BGM, Luxury Beat, Chic"
            outfit_text = "High-fashion blazer & jeans, heels ✨"
        elif "Posing" in group_select:
            key_style = "Posing"
            music_text = "📸 R&B, Trap Soul, Confident Vibe"
            outfit_text = "Elegant Dress or Streetwear 👗"
        elif "Beauty" in group_select:
            key_style = "Beauty"
            music_text = "✨ Soft Pop, Fresh, Lo-fi Chill, Spa"
            outfit_text = "Bathrobe / Clean Girl Outfit 🧖‍♀️"
        else: # Lifestyle
            key_style = "Lifestyle"
            music_text = "🥂 Vlog Music, Jazz Hop, Morning Coffee"
            outfit_text = "Casual Chic / Yoga wear 🧘‍♀️"

        # 2. Xử lý NGOẠI LỆ (Ghi đè - Override)
        if "Biến hình" in topic_select:
             outfit_text = "Pajamas (Before) -> Glitter Dress (After) ✨"
             music_text = "🎵 Transition Sound, Magic Chime, Drop Beat"
             
        # NEW: Xử lý Du lịch / Ngoại cảnh (v9.8)
        if "Du lịch" in topic_select or "Outdoor" in topic_select or "Ngoại cảnh" in topic_select:
             outfit_text = "Maxi Dress đi biển 🌊 / Streetwear năng động & Kính râm 😎"
             music_text = "🌊 Tropical House, Travel Vibe, Summer Chill"
             key_style = "Lifestyle" # Đưa về lifestyle để chọn caption hợp lý

        st.caption(f"👕 Outfit: {outfit_text}")

st.success(f"🎵 Gợi ý Nhạc (CapCut): {music_text}")

# =========================================================
# 3. KẾT QUẢ OUTPUT
# =========================================================

tab1, tab2, tab3 = st.tabs(["📝 BÀI VIẾT & ẢNH", "🎥 VIDEO (Sora & Grok)", "🎬 KỊCH BẢN (Script)"])

# --- TAB 1: CAPTION & MIDJOURNEY ---
with tab1:
    col_cap, col_prompt = st.columns(2)
    with col_cap:
        st.subheader("1. Caption (TikTok/FB)")
        # Lấy random caption
        if key_style in caption_library:
            base_cap = random.choice(caption_library[key_style])
        else:
            base_cap = "Cùng Nelly tỏa sáng nhé! ✨"
            
        final_cap = f"{topic_select}\n\n{base_cap}\n\n#Nelly #{key_style} #Trending #Viral"
        st.info(final_cap)
        if st.button("🔄 Đổi Caption khác"): 
            pass 
        
    with col_prompt:
        st.subheader("2. Prompt Ảnh (Midjourney)")
        st.code(f"/imagine prompt: A stunning photography shot of Nelly, {outfit_text}, performing {topic_select}, cinematic lighting, natural sunlight, travel photography style --ar 3:4", language="text")

# --- TAB 2: SORA & GROK ---
with tab2:
    st.subheader(f"🎬 Sản xuất Video: {topic_select}")
    
    # Sora Logic
    action_desc = f"performing {topic_select}"
    if "Biến hình" in angle_select:
        action_desc = "TRANSFORMATION EFFECT: Starts with messy look/pajamas, then magic transition to stunning look in " + outfit_text
    elif "Sai lầm" in angle_select:
        action_desc = "holding a STOP sign initially, shaking head 'No', then smiling and showing the correct way"
    # NEW logic cho Du lịch
    elif "Du lịch" in topic_select or "Outdoor" in topic_select:
        action_desc = "walking confidently on the beach/street, enjoying the view, hair blowing in the wind, smiling at camera"
        
    st.markdown("#### 🅰️ Prompt Sora 2 (15s)")
    st.code(f"""
    Cinematic outdoor, 4k, sunny day. Subject: A stunning Vietnamese fashion KOL (Nelly).
    Outfit: {outfit_text}.
    Action: {action_desc}. Relaxed and happy vibe.
    Camera: Dynamic zoom/pan, tracking shot. Constraint: NO TEXT. --duration 15s
    """, language="text")

    st.markdown("#### 🅱️ Prompt Grok 2 (6s - Intro)")
    st.code(f"Video of A stunning Vietnamese fashion KOL (Nelly), wearing {outfit_text}, {topic_select}, travel vlog style, trending artstation. --duration 6s", language="text")

# --- TAB 3: SCRIPT KỊCH BẢN ---
with tab3:
    st.warning(f"💡 Kịch bản quay chi tiết cho Editor ({angle_select})")
    
    if "Biến hình" in angle_select:
        st.markdown(f"""
        * **0-3s (Hook):** Mặc đồ thường. Gương mặt buồn chán. Nhạc intro nhẹ.
        * **3-5s (Transition):** Búng tay cái "Tách"!
        * **5-15s (Result):** BÙM! {outfit_text} xuất hiện. Nhạc {music_text} nổi lên cực mạnh. Nelly diễn thần thái.
        """)
    elif "Du lịch" in topic_select or "Outdoor" in topic_select: # Kịch bản Du lịch
         st.markdown(f"""
        * **0-3s (Hook):** Quay lưng về phía camera, view đẹp (biển/phố). Nelly quay lại cười tươi.
        * **3-10s (Montage):** Cắt ghép các đoạn ngắn: đi dạo, uống nước, check-in góc đẹp. Nhạc chill.
        * **10-15s (Outro):** Tạo dáng "thần thánh" chốt video. Vẫy tay chào.
        """)
    else:
        st.markdown(f"""
        * **Toàn bộ video:** Quay các góc cận (chi tiết outfit/makeup) -> trung (nửa người) -> toàn (dáng đi).
        * **Lưu ý:** Chú ý bắt trọn khoảnh khắc thần thái nhất (Eye contact).
        * **Nhạc:** {music_text}
        """)
