import streamlit as st

# --- CẤU HÌNH DỮ LIỆU ---

# THÔNG TIN SẢN PHẨM (Context để ChatGPT hiểu)
product_context = """
Sản phẩm: Sữa nghệ Hera.
Thành phần: Tinh chất Curcumin cao cấp (loại bỏ dầu/nhựa), Sữa tách béo New Zealand, Đường cỏ ngọt Stevia.
Công dụng: Hỗ trợ đau dạ dày, trào ngược, làm lành vết thương cho người mới mổ/mẹ sau sinh, đẹp da, ngủ ngon.
Ưu điểm: Không hăng, không đắng, không nóng trong, không gây béo.
Đối tượng: Người đau dạ dày, mẹ bỉm sữa, người già, người sợ béo.
Phong cách thương hiệu: Chân thành, thủ thỉ, chuyên gia nhưng gần gũi (Moon).
"""

schedule = {
    "Thứ 2": {"text": "Nuôi dưỡng (Nurture)", "video": "Kể chuyện (Story-based)"},
    "Thứ 3": {"text": "Không có bài viết", "video": "Giải quyết vấn đề (Problem)"},
    "Thứ 4": {"text": "Giáo dục (Educate)", "video": "Cảnh báo sai lầm (Warning)"},
    "Thứ 5": {"text": "Không có bài viết", "video": "Phản biện (Counter-Intuitive)"},
    "Thứ 6": {"text": "Chuyển đổi (Convert)", "video": "Trước - Sau (Transformation)"},
    "Thứ 7": {"text": "Không có bài viết", "video": "Trải nghiệm/Review"},
    "Chủ Nhật": {"text": "Nghỉ ngơi/Story", "video": "Hài hước/Trend"}
}

# PROMPT TEMPLATES (Lệnh cho ChatGPT)
text_prompts = {
    "Nuôi dưỡng (Nurture)": """
    Viết một bài đăng Facebook cá nhân (Personal Story).
    Mục tiêu: Kết nối cảm xúc, chưa bán hàng vội.
    Chủ đề: Sự bận rộn và nhu cầu được chăm sóc bản thân của phụ nữ/mẹ bỉm.
    Cấu trúc bài viết:
    1. Hook: Một câu than thở nhẹ hoặc khoảnh khắc mệt mỏi cuối ngày.
    2. Body: Kể về việc tìm thấy sự bình yên bên ly sữa nghệ ấm nóng. Lồng ghép khéo léo việc yêu bản thân.
    3. Kết: Câu hỏi thăm nhẹ nhàng với bạn bè.
    Tone mood: Ấm áp, thủ thỉ, sâu sắc.
    """,
    
    "Giáo dục (Educate)": """
    Viết một bài đăng chia sẻ kiến thức (Educational Post).
    Mục tiêu: Giải quyết định kiến sai lầm (Myth vs Fact).
    Chủ đề: So sánh Nghệ tươi/Bột nghệ thường VS Tinh chất Curcumin trong Sữa nghệ Hera.
    Cấu trúc bài viết:
    1. Hook: Giật tít về sai lầm (Ví dụ: Uống nghệ bị nóng? Bị vàng răng?).
    2. Body: Giải thích khoa học đơn giản. Tại sao Hera loại bỏ được dầu nghệ gây nóng? Tại sao đường cỏ ngọt không gây béo?
    3. Kết: Lời khuyên nên chọn sản phẩm tinh chế.
    Tone mood: Chuyên gia, tin cậy, khách quan.
    """,
    
    "Chuyển đổi (Convert)": """
    Viết một bài đăng bán hàng (Sales Post).
    Mục tiêu: Chốt đơn hàng.
    Chủ đề: Kể câu chuyện khách hàng (Feedback) hoặc Kết quả của bản thân.
    Cấu trúc bài viết:
    1. Hook: Một lời khen/tin nhắn của khách hàng về việc hết đau dạ dày/ngủ ngon.
    2. Body: Nêu rõ nỗi đau trước kia -> Sự thay đổi sau khi dùng Hera. Nhấn mạnh ưu điểm: Ngon, Dễ uống, Hiệu quả nhanh.
    3. Call to Action: Kêu gọi mua hàng, ưu đãi gom đơn hoặc freeship.
    Tone mood: Hào hứng, tự tin, thôi thúc.
    """,
    
    "Nghỉ ngơi/Story": """
    Viết một caption ngắn (Short Caption) kèm ảnh đi chơi hoặc gia đình.
    Nội dung: Chúc cuối tuần vui vẻ, nhắc nhở mọi người giữ gìn sức khỏe. Không bán hàng.
    Tone mood: Vui vẻ, năng lượng tích cực.
    """
}

# --- GIAO DIỆN APP ---
st.title("🌙 MOON'S CONTENT CREATOR")
st.caption("Công cụ tạo Prompt tự động cho Sữa Nghệ Hera")

# Sidebar
selected_day = st.selectbox("📅 Hôm nay là thứ mấy?", list(schedule.keys()))
today_task = schedule[selected_day]

# Hiển thị nhiệm vụ
col1, col2 = st.columns(2)
with col1:
    st.info(f"📝 **Bài viết:** {today_task['text']}")
with col2:
    st.warning(f"🎬 **Video:** {today_task['video']}")

st.divider()

# XỬ LÝ BÀI VIẾT (TEXT)
if today_task['text'] != "Không có bài viết":
    st.subheader(f"📝 TẠO BÀI VIẾT: {today_task['text']}")
    st.write("Copy đoạn lệnh bên dưới và dán vào ChatGPT:")
    
    # Ghép thông tin sản phẩm vào prompt cụ thể
    full_prompt = f"""
    Đóng vai là Moon - một người xây dựng thương hiệu cá nhân về sức khỏe và lối sống lành mạnh.
    
    {product_context}
    
    NHIỆM VỤ:
    {text_prompts[today_task['text']]}
    
    YÊU CẦU:
    - Viết tiếng Việt tự nhiên, ngắt dòng dễ đọc.
    - Dùng icon hợp lý.
    - Thêm hashtag: #SuaNgheHera #HaPhanMinhNguyet #SucKhoe
    """
    st.code(full_prompt, language="text")

# XỬ LÝ VIDEO
st.subheader(f"🎬 TẠO VIDEO: {today_task['video']}")
video_style = st.radio("Chọn phong cách video:", ["3D Animation (Bé Nghệ)", "KOL (Người thật)"], horizontal=True)

if video_style == "3D Animation (Bé Nghệ)":
    st.write("**Copy Prompt này dán vào Midjourney để tạo ảnh:**")
    prompt_3d = f"/imagine prompt: A cute anthropomorphic turmeric root character acting in a scene about: {today_task['video']}. Pixar 3D animation style, warm lighting, expressive face, high detail, 8k --ar 9:16"
    st.code(prompt_3d, language="text")
    st.write("**Gợi ý kịch bản:** Dùng các phân cảnh vui nhộn, không thoại, nhạc nền trend.")
else:
    st.write("**Gợi ý kịch bản KOL:**")
    st.info("Quay trực diện, ánh sáng tốt. Tập trung vào biểu cảm khuôn mặt và sản phẩm trên tay.")

st.markdown("---")
st.caption("Updated Version 1.5 - Auto Prompt Generation")
