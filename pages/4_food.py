import streamlit as st
import random

st.set_page_config(page_title="Moon's Food Matrix v8.2", page_icon="🥗", layout="wide")

# =========================================================
# 1. KHO DỮ LIỆU & CAPTION
# =========================================================

# Menu 12 món cố định
detox_menu = [
    "1. Chanh + Tỏi (Sạch mạch máu)", "2. Chanh + Gừng (Tiêu hóa tốt)", "3. Chanh + Nha đam (Đẹp da)",
    "4. Chanh + Nghệ (Kháng viêm)", "5. Chanh + Mật ong (Tăng đề kháng)", "6. Trà chanh nóng (Thanh lọc)",
    "7. Củ dền + Táo + Cà rốt (Bổ máu)", "8. Bơ + Dưa leo + Gừng (Giảm viêm)", "9. Việt quất + Cà chua + Gừng (Tăng miễn dịch)",
    "10. Cam + Táo + Nghệ (Giảm mệt mỏi)", "11. Bưởi + Cà rốt + Gừng (Giảm mỡ máu)", "12. Kiwi + Xà lách + Gừng (Trị mất ngủ)"
]

# Góc quay Video
video_angles = {
    "🎥 1. Hướng dẫn (How-to/ASMR)": {"style": "Macro shots, extreme close-up", "desc": "Quay cận cảnh sơ chế"},
    "🎓 2. Kiến thức (Education)": {"style": "Medium shot pointing to hologram chart", "desc": "Chuyên gia phân tích thành phần"},
    "⚠️ 3. Cảnh báo (Warning)": {"style": "Dramatic lighting, serious tone", "desc": "Cảnh báo sai lầm thường gặp"},
    "📖 4. Câu chuyện (Story/Vlog)": {"style": "Handheld POV, sunny garden", "desc": "Vlog tâm sự trải nghiệm"}
}

# Kho Caption theo Mood (MỚI)
caption_moods = {
    "😂 Hài hước (Funny)": [
        "Ăn healthy không phải là hành xác, mà là cách yêu bản thân 'ngon' nhất! 😜",
        "Đừng để cái miệng làm hại cái thân, uống ly này đi cho đời bớt 'nghiệp'! 😂",
        "Người yêu có thể không có, nhưng {item} thì nhất định phải có một ly! 🥤"
    ],
    "😘 Thả thính (Flirty)": [
        "Em không thích trà sữa, em chỉ thích trà... trộn vào tim anh bằng ly {item} này thôi! 💘",
        "Muốn da đẹp dáng xinh để 'cưa' crush? Bí mật nằm ở đây nè 👇",
        "Ngọt ngào như {item}, liệu anh có muốn thử? 😉"
    ],
    "🧐 Chuyên gia (Expert)": [
        "⚠️ Cảnh báo: 90% mọi người đang bỏ qua 'thần dược' {item} này!",
        "Phân tích sâu: Tại sao {item} lại là khắc tinh của mỡ thừa?",
        "Góc kiến thức: Đừng uống thuốc bổ nếu chưa thử công thức tự nhiên này."
    ],
    "🌿 Chữa lành (Inspiring)": [
        "Hãy yêu thương cơ thể bạn từ những điều nhỏ nhất. 🌿",
        "Mỗi sáng một ly {item}, nạp năng lượng tích cực cho ngày dài.",
        "Sống xanh không khó, chỉ cần bắt đầu từ ly nước hôm nay."
    ]
}

# Database Dinh dưỡng (Giữ nguyên)
nutrition_db = {
    "Chanh + Tỏi": {"chat": "Allicin & Vitamin C", "hook": "Uống xong người yêu chạy mất dép nhưng tim mạch thì khỏe re!", "body": "Allicin trong tỏi quét sạch mỡ máu cứng đầu.", "cta": "Thử ngay nhé!"},
    "Chanh + Gừng": {"chat": "Gingerol", "hook": "Bụng căng tức khó chịu?", "body": "Gingerol làm ấm bụng, đẩy lùi cơn đau dạ dày.", "cta": "Lưu lại ngay."},
    # ... (Các món khác dùng Default logic nếu không tìm thấy để code gọn)
}

# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🥗 MOON'S FOOD MATRIX v8.2")
st.markdown("*Caption Chất Lừ - Hashtag Tách Riêng - Video Sạch*")

# --- CẤU HÌNH ---
with st.expander("⚙️ CẤU HÌNH NỘI DUNG (Bấm mở rộng)", expanded=True):
    c1, c2 = st.columns(2)
    with c1: 
        style_select = st.radio("🎭 Style:", ["3D Animation (Pixar)", "Người thật (Cinematic)"], horizontal=True)
    with c2:
        angle_full = st.selectbox("🎥 Góc quay:", list(video_angles.keys()))

    st.divider()
    
    c3, c4 = st.columns([1, 2])
    with c3:
        group = st.selectbox("📂 Chọn Nhóm:", ["🥤 Smoothie & Detox", "🍎 Trái cây", "🥦 Rau xanh", "🥗 Healthy Food"])
    with c4:
        if "Smoothie" in group:
            recipe_full = st.selectbox("Món:", detox_menu)
            custom_ing = ""
        else:
            recipe_full = st.text_input("Tên món:", "Salad Ức gà")
            custom_ing = st.text_input("Thành phần (để AI viết đúng):", "Ức gà, xà lách, sốt mè")

    # CHỌN MOOD CAPTION
    st.divider()
    selected_mood = st.selectbox("📝 Chọn Mood Caption:", list(caption_moods.keys()))

# =========================================================
# XỬ LÝ LOGIC
# =========================================================

# 1. Tên & Kịch bản
if "Smoothie" in group:
    key_name = recipe_full.split(". ")[1].split(" (")[0]
    info = nutrition_db.get(key_name, {"chat": "Dưỡng chất tự nhiên", "hook": f"Bí mật của {key_name}!", "body": "Tốt cho sức khỏe.", "cta": "Thử ngay!"})
else:
    key_name = recipe_full if recipe_full else "Món ngon"
    info = {"chat": custom_ing, "hook": f"Ai mê {key_name} bơi vào đây!", "body": f"Sự kết hợp của {custom_ing} cực tốt.", "cta": "Lưu công thức nha!"}

# 2. Tạo Caption & Hashtag
raw_cap = random.choice(caption_moods[selected_mood]).format(item=key_name)
full_caption = f"""{raw_cap}

Công thức: {custom_ing if custom_ing else key_name}
👉 Bí mật: **{info['chat']}** giúp {info['body'].lower()}

{info['cta']} 👇"""

hashtag_block = f"#MoonFood #{key_name.replace(' + ','').replace(' ','')} #EatClean #HealthyLifestyle #DinhDuong"

# 3. Visual Style
if "3D" in style_select:
    subject = f"Cute 3D Pixar-style character representing {key_name}, vibrant"
    mj_style = "Disney Pixar style 3D render, cute"
    actor = "Character"
else:
    subject = f"High-end Food Cinematography, Real {key_name}"
    mj_style = "Professional food photography, 8k"
    actor = "Moon (KOL)"

angle_data = video_angles[angle_full]

# =========================================================
# HIỂN THỊ KẾT QUẢ
# =========================================================

tab_content, tab_video = st.tabs(["📝 BÀI VIẾT (Copy)", "🎥 VIDEO SORA"])

# --- TAB 1 ---
with tab_content:
    c_cap, c_tag = st.columns(2)
    
    with c_cap:
        st.subheader("1. NỘI DUNG CAPTION (Copy dán)")
        st.code(full_caption, language='text')
        st.caption("☝️ Bấm nút nhỏ bên phải để Copy nội dung.")
        
    with c_tag:
        st.subheader("2. HASHTAG (Copy riêng)")
        st.code(hashtag_block, language='text')
        st.caption("☝️ Bấm nút nhỏ bên phải để Copy Hashtag.")

    st.divider()
    st.subheader("3. Prompt Ảnh Bìa (Midjourney)")
    st.code(f"/imagine prompt: {mj_style}. Subject: {subject}. Context: {recipe_full}. --ar 3:4", language='text')
    
    st.subheader("4. Lệnh Viết Bài Blog (ChatGPT)")
    st.code(f"Viết bài FB về {key_name}. Mood: {selected_mood}. Hook: '{info['hook']}'. Body: '{info['body']}'.", language='text')

# --- TAB 2 ---
with tab_video:
    st.subheader(f"🎬 Sản xuất Video: {key_name}")
    st.info(f"Style: {style_select} | Góc: {angle_full}")
    
    # Kịch bản 3 phần
    c1, c2, c3 = st.columns(3)
    c1.success(f"HOOK: \"{info['hook']}\"")
    c2.info(f"BODY: \"{info['body']}\"")
    c3.error(f"CTA: \"{info['cta']}\"")
    
    st.divider()
    
    # Prompt Sora
    details = f"Ingredients visible: {custom_ing}" if custom_ing else "Fresh ingredients visible"
    sora_prompt = f"""
    8k, {mj_style}.
    Subject: {subject}. {details}.
    Style: {angle_data['style']}.
    Action: {angle_data['desc'].replace('Moon', actor)} demonstrating benefits.
    
    Speaking Line (Vietnamese): "{info['hook']} {info['body']} {info['cta']}"
    Lip-sync instruction: Match naturally with Vietnamese dialogue.
    
    Constraint: ABSOLUTELY NO TEXT OVERLAYS, NO LOGOS. --duration 15s
    """
    st.code(sora_prompt, language='text')
