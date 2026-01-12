import streamlit as st

# --- CẤU HÌNH DỮ LIỆU ---

# 1. LỊCH TRÌNH (Ma trận nội dung)
schedule = {
    "Thứ 2": {"text": "Nuôi dưỡng (Nurture)", "video": "Kể chuyện (Story-based)"},
    "Thứ 3": {"text": "Không có bài viết", "video": "Giải quyết vấn đề (Problem)"},
    "Thứ 4": {"text": "Giáo dục (Educate)", "video": "Cảnh báo sai lầm (Warning)"},
    "Thứ 5": {"text": "Không có bài viết", "video": "Phản biện (Counter-Intuitive)"},
    "Thứ 6": {"text": "Chuyển đổi (Convert)", "video": "Trước - Sau (Transformation)"},
    "Thứ 7": {"text": "Không có bài viết", "video": "Trải nghiệm/Review"},
    "Chủ Nhật": {"text": "Nghỉ ngơi/Story", "video": "Hài hước/Trend"}
}

# 2. TEMPLATE BÀI VIẾT (TEXT)
text_templates = {
    "Nuôi dưỡng (Nurture)": "Mục tiêu: Chia sẻ lối sống, kết nối cảm xúc.\nCấu trúc:\n1. Hook: Một khoảnh khắc đời thường/suy nghĩ cá nhân.\n2. Body: Kể chuyện liên quan đến sức khỏe/gia đình.\n3. Kết nối: Lồng ghép khéo léo vai trò của việc yêu bản thân.\n4. CTA: Tương tác nhẹ nhàng (Hỏi thăm).",
    "Giáo dục (Educate)": "Mục tiêu: Cung cấp kiến thức chuyên gia.\nCấu trúc:\n1. Hook: Myth vs Fact (Sự thật lầm tưởng).\n2. Body: Giải thích cơ chế khoa học (Curcumin, Nano...).\n3. Giải pháp: Tại sao Hera giải quyết được vấn đề này.\n4. CTA: Lưu lại kiến thức.",
    "Chuyển đổi (Convert)": "Mục tiêu: Bán hàng, Chốt đơn.\nCấu trúc:\n1. Hook: Feedback khách hàng hoặc Kết quả ấn tượng.\n2. Body: Nêu rõ nỗi đau -> Giải pháp Hera.\n3. Offer: Ưu đãi/Khan hiếm (Gom đơn, Freeship).\n4. CTA: Kêu gọi Inbox/Mua ngay.",
    "Nghỉ ngơi/Story": "Chia sẻ ảnh đi chơi, gia đình, không bán hàng."
}

# 3. TEMPLATE VIDEO (VIDEO)
video_templates = {
    "Kể chuyện (Story-based)": "Kịch bản: Từ mệt mỏi đến Hạnh phúc.\nPhân đoạn 1 (0-20s): Nỗi đau, sự mệt mỏi, bế tắc.\nPhân đoạn 2 (20-45s): Tìm thấy ánh sáng (Sản phẩm), cảm xúc thay đổi.",
    "Giải quyết vấn đề (Problem)": "Kịch bản: Đau đâu chữa đó.\nPhân đoạn 1 (0-15s): Cảnh báo cơn đau (Dạ dày, mất ngủ).\nPhân đoạn 2 (15-45s): Giải pháp ngay lập tức (Uống Hera) + Kết quả êm dịu.",
    "Cảnh báo sai lầm (Warning)": "Kịch bản: Stop Sign!\nPhân đoạn 1 (0-15s): Hành động sai (Pha nước sôi, uống sai cách).\nPhân đoạn 2 (15-45s): Hướng dẫn làm đúng + Lợi ích khi làm đúng.",
    "Phản biện (Counter-Intuitive)": "Kịch bản: Lật ngược vấn đề.\nPhân đoạn 1 (0-15s): Quan niệm cũ (Sữa béo, Nghệ nóng).\nPhân đoạn 2 (15-45s): Sự thật mới (Cỏ ngọt, Tách béo, Tách dầu).",
    "Trước - Sau (Transformation)": "Kịch bản: Split Screen.\nPhân đoạn 1 (0-20s): Hình ảnh cũ (Xấu, mệt, đau).\nPhân đoạn 2 (20-45s): Hình ảnh mới (Đẹp, khỏe, vui) nhờ Hera.",
    "Trải nghiệm/Review": "Kịch bản: Vlog 7 ngày.\nPhân đoạn 1 (0-20s): Quá trình trải nghiệm thực tế.\nPhân đoạn 2 (20-45s): Kết quả tổng kết chân thực.",
    "Hài hước/Trend": "Bắt trend nhạc hot, nội dung vui vẻ giải trí."
}

# 4. STYLE VIDEO
styles = {
    "KOL (Người thật)": "Quay trực diện, ánh sáng tự nhiên, cầm sản phẩm thật. Giọng nói thủ thỉ hoặc chuyên gia.",
    "3D Animation (Bé Nghệ)": "Nhân vật: Bé Nghệ (Mr. Turmeric) dễ thương, Pixar Style.\nMàu sắc: Vàng nghệ ấm áp.\nPrompt tạo ảnh: 'A cute anthropomorphic turmeric root character... Pixar style'"
}

# --- GIAO DIỆN APP ---
st.title("🌙 MOON'S CONTENT GENERATOR")
st.subheader("Hệ thống quản lý nội dung Sữa Nghệ Hera")

# Sidebar chọn ngày
selected_day = st.selectbox("📅 Hôm nay là thứ mấy?", list(schedule.keys()))

# Hiển thị nhiệm vụ hôm nay
today_task = schedule[selected_day]
st.info(f"**Nhiệm vụ {selected_day}:**\n- 📝 Bài viết: {today_task['text']}\n- 🎬 Video: {today_task['video']}")

# Chọn loại nội dung muốn làm
content_type = st.radio("Bạn muốn sản xuất nội dung nào?", ["📝 Bài Viết (Text)", "🎬 Video Ngắn"])

if content_type == "📝 Bài Viết (Text)":
    topic = today_task['text']
    if topic == "Không có bài viết":
        st.warning("Hôm nay lịch không yêu cầu viết bài dài. Hãy tập trung làm Video hoặc nghỉ ngơi!")
    else:
        st.success(f"Đang tạo dàn ý cho chủ đề: **{topic}**")
        st.text_area("Cấu trúc bài viết gợi ý:", text_templates.get(topic, ""), height=200)
        st.markdown("---")
        st.write("**👉 Gợi ý hành động:** Copy cấu trúc trên và yêu cầu ChatGPT viết chi tiết.")

elif content_type == "🎬 Video Ngắn":
    topic = today_task['video']
    st.success(f"Đang lên kịch bản Video: **{topic}**")
    
    # Chọn Style
    video_style = st.selectbox("Chọn phong cách video:", list(styles.keys()))
    
    st.markdown(f"### 🎥 KỊCH BẢN CHI TIẾT ({video_style})")
    st.write(f"**Thời lượng:** 45 giây")
    
    # Hiển thị cấu trúc kịch bản
    script_structure = video_templates.get(topic, "")
    st.code(script_structure, language="text")
    
    # Hiển thị hướng dẫn style
    st.info(f"💡 **Lưu ý phong cách:** {styles[video_style]}")
    
    # Nếu là 3D thì hiện thêm Prompt
    if video_style == "3D Animation (Bé Nghệ)":
        st.markdown("#### 🎨 Prompt tạo ảnh 3D (Copy vào Midjourney):")
        st.code(f"PROMPT CHO {topic.upper()}:\n/imagine prompt: A cute anthropomorphic turmeric root character [Doing action related to: {topic}]. Pixar 3D animation style, warm lighting, expressive face, high detail, 8k --ar 9:16", language="text")

st.markdown("---")
st.caption("Developed for Moon - Hera Milk Project")
