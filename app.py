import streamlit as st

# Cài đặt trang web
st.set_page_config(page_title="Moon's Content Creator", page_icon="🌙", layout="centered")

# =========================================================
# DỮ LIỆU HỆ THỐNG
# =========================================================

# 1. CONTEXT SẢN PHẨM
product_context = """
Sản phẩm: Sữa nghệ Hera.
Thành phần: Tinh chất Curcumin cao cấp, Sữa tách béo New Zealand, Đường cỏ ngọt Stevia.
Công dụng: Hỗ trợ đau dạ dày, trào ngược, lành vết thương, đẹp da, ngủ ngon.
Ưu điểm: Không hăng, không đắng, không nóng, không béo.
Đối tượng: Người đau dạ dày, mẹ bỉm sữa, người sợ béo.
Thương hiệu cá nhân: Moon - Chân thành, thủ thỉ, chuyên gia gần gũi.
"""

# 2. LỊCH TRÌNH
schedule = {
    "Thứ 2": {"text": "Nuôi dưỡng (Nurture)", "video": "Kể chuyện (Story-based)"},
    "Thứ 3": {"text": "Không có bài viết", "video": "Giải quyết vấn đề (Problem)"},
    "Thứ 4": {"text": "Giáo dục (Educate)", "video": "Cảnh báo sai lầm (Warning)"},
    "Thứ 5": {"text": "Không có bài viết", "video": "Phản biện (Counter-Intuitive)"},
    "Thứ 6": {"text": "Chuyển đổi (Convert)", "video": "Trước - Sau (Transformation)"},
    "Thứ 7": {"text": "Không có bài viết", "video": "Trải nghiệm/Review"},
    "Chủ Nhật": {"text": "Nghỉ ngơi/Story", "video": "Hài hước/Trend"}
}

# 3. PROMPT TEXT (CHATGPT)
text_prompts = {
    "Nuôi dưỡng (Nurture)": "Viết bài Facebook Storytelling.\nChủ đề: Sự bận rộn và nhu cầu chăm sóc bản thân.\nCấu trúc: Hook (Than thở nhẹ) -> Body (Bình yên bên ly sữa Hera) -> Kết (Hỏi thăm).\nTone: Ấm áp, thủ thỉ.",
    "Giáo dục (Educate)": "Viết bài Kiến thức (Myth vs Fact).\nChủ đề: So sánh Nghệ tươi/Bột nghệ thường VS Tinh chất Curcumin Hera.\nCấu trúc: Hook (Giật tít sai lầm) -> Body (Khoa học đơn giản: Tách dầu, Cỏ ngọt) -> Kết (Khuyên dùng tinh chế).\nTone: Chuyên gia.",
    "Chuyển đổi (Convert)": "Viết bài Bán hàng (Sales).\nChủ đề: Feedback khách hoặc Kết quả bản thân.\nCấu trúc: Hook (Lời khen/Kết quả) -> Body (Nỗi đau cũ -> Thay đổi nhờ Hera) -> CTA (Mua ngay, ưu đãi).\nTone: Hào hứng, tự tin.",
    "Nghỉ ngơi/Story": "Viết Caption ngắn kèm ảnh đi chơi.\nNội dung: Chúc cuối tuần, nhắc giữ sức khỏe.\nTone: Vui vẻ."
}

# 4. KỊCH BẢN VIDEO (SCRIPT) - Đã tối ưu Hook/CTA
video_scripts = {
    "Kể chuyện (Story-based)": "🎬 KỊCH BẢN: TỪ MỆT MỎI ĐẾN HẠNH PHÚC\n🔸 HOOK (3s): Cảnh thở dài, gục xuống bàn. Text: 'Đuối sức...'\n🔸 BODY (15s-40s): Uống Hera, mắt sáng lên, mỉm cười.\n🔸 CTA (Cuối): Giơ ly sữa mời. Text: 'Nạp lại năng lượng ngay!'",
    
    "Giải quyết vấn đề (Problem)": "🎬 KỊCH BẢN: ĐAU DẠ DÀY\n🔸 HOOK (3s): Ôm bụng nhăn nhó, tia sét đỏ. Text: 'Đau bao tử lại hành!'\n🔸 BODY (15s-40s): Uống Hera, hiệu ứng dịu mát, bụng êm.\n🔸 CTA (Cuối): Giơ ngón tay Like. Text: 'Êm ru sau 1 ly. Thử ngay!'",
    
    "Cảnh báo sai lầm (Warning)": "🎬 KỊCH BẢN: CẢNH BÁO PHA SAI\n🔸 HOOK (3s): Dấu X ĐỎ to đùng trước ấm nước sôi. Text: 'Dừng lại! Đừng pha nước sôi!'\n🔸 BODY (15s-25s): Pha nước ấm 40 độ, ly sữa vàng mịn.\n🔸 CTA (Cuối): Text: 'Pha đúng mới giữ được chất!'",
    
    "Phản biện (Counter-Intuitive)": "🎬 KỊCH BẢN: SỢ BÉO?\n🔸 HOOK (3s): Lắc đầu xua tay với đường trắng. Text: 'Sợ béo? Xưa rồi!'\n🔸 BODY (15s-25s): Ôm lá cỏ ngọt Stevia, show eo thon.\n🔸 CTA (Cuối): Nháy mắt. Text: 'Đường cỏ ngọt 0 Calo. Uống đi chờ chi!'",
    
    "Trước - Sau (Transformation)": "🎬 KỊCH BẢN: LỘT XÁC (SPLIT SCREEN)\n🔸 HOOK (3s): Mặt buồn, da sạm (Bên trái). Text: 'Trước khi gặp Hera...'\n🔸 BODY (20s-40s): Biến hình sang da hồng, tươi cười (Bên phải).\n🔸 CTA (Cuối): Tạo dáng tự tin. Text: 'Khỏe đẹp từ bên trong. Inbox Moon!'",
    
    "Trải nghiệm/Review": "🎬 KỊCH BẢN: NHẬT KÝ 7 NGÀY\n🔸 HOOK (3s): Show lịch 7 ngày. Text: 'Thử thách 7 ngày uống Hera'.\n🔸 BODY (15s-40s): Cắt nhanh cảnh uống ngon lành các ngày.\n🔸 CTA (Cuối): Hôn gió/Bắn tim. Text: 'Duyệt nha! Chị em thử ngay.'",
    
    "Hài hước/Trend": "🎬 KỊCH BẢN: BẮT TREND\n🔸 HOOK (3s): Nhạc nổi lên, nhân vật vào thế chuẩn bị.\n🔸 BODY: Nhảy theo nhạc hot hoặc diễn cảnh hài hước về ăn uống healthy.\n🔸 CTA: Chỉ tay vào sản phẩm. Text: 'Muốn khỏe thì về đội Moon!'"
}

# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🌙 MOON'S CREATOR v2.7 (Pro)")
st.write("👉 **Mẹo:** Rê chuột vào góc phải khung đen để thấy nút **Copy** 📄")

# Sidebar
selected_day = st.selectbox("📅 Hôm nay là thứ mấy?", list(schedule.keys()))
today_task = schedule[selected_day]
video_topic = today_task['video']

st.info(f"Nhiệm vụ: {selected_day} | Video: {video_topic}")

# TABS
tab1, tab2 = st.tabs(["📝 BÀI VIẾT (CHATGPT)", "🎬 VIDEO (SORA & MIDJOURNEY)"])

with tab1:
    if today_task['text'] == "Không có bài viết":
        st.caption("Hôm nay nghỉ viết bài dài.")
    else:
        st.subheader("Copy lệnh này cho ChatGPT:")
        full_prompt = f"""Đóng vai Moon (Thương hiệu cá nhân sức khỏe).
{product_context}
NHIỆM VỤ: {text_prompts[today_task['text']]}
YÊU CẦU: 
- Viết caption hấp dẫn, gợi sự tò mò.
- Văn phong tiếng Việt tự nhiên, thủ thỉ, chân thành.
- Thêm Call To Action (CTA) cuối bài.
- Hashtag: #SuaNgheHera #HaPhanMinhNguyet #SucKhoe"""
        st.code(full_prompt, language='text')

with tab2:
    st.subheader(f"Chủ đề: {video_topic}")
    
    # 1. KỊCH BẢN TEXT
    st.write("📜 **Kịch bản quay/dựng (Có Hook & CTA):**")
    st.code(video_scripts.get(video_topic, ""), language='text')
    
    st.divider()
    
    # 2. CHỌN PHONG CÁCH
    video_style = st.radio("Chọn phong cách video:", ["3D Animation (Bé Nghệ)", "KOL (Người thật)"], horizontal=True)
    
    # Biến đổi Prompt dựa trên phong cách
    if video_style == "3D Animation (Bé Nghệ)":
        style_desc = "Pixar 3D animation style, cute anthropomorphic turmeric root character"
        char_desc = "The character is cute, round, with big expressive eyes"
        mj_prompt_start = "/imagine prompt: A cute anthropomorphic turmeric root character"
    else:
        style_desc = "High-quality realistic cinematic video, photorealistic, 8k, shot on Arri Alexa"
        char_desc = "A friendly Vietnamese female health expert (Moon), natural beauty, warm smile, professional yet approachable, wearing comfortable elegant clothes"
        mj_prompt_start = "/imagine prompt: A beautiful Vietnamese female health expert holding a glass of turmeric milk"

    # HIỂN THỊ PROMPT MIDJOURNEY (Ảnh bìa/Thumbnail)
    st.write("🎨 **Prompt tạo ảnh Thumbnail (Midjourney):**")
    prompt_mj = f"{mj_prompt_start} acting in a scene about: {video_topic}. Holding a glass of warm, creamy golden-yellow turmeric milk. {style_desc}, warm lighting, expressive face, 8k --ar 9:16"
    st.code(prompt_mj, language='text')
    
    st.divider()
    
    # HIỂN THỊ PROMPT SORA 2 (Video)
    st.subheader("🎥 Prompt tạo video Sora 2 (Cho cả 2 styles)")
    
    # Slider chọn thời lượng
    duration_option = st.select_slider("Chọn độ dài video:", options=["15s", "30s", "60s"], value="15s")
    
    # Prompt Sora tối ưu
    sora_prompt = f"""
    {style_desc}.
    Subject: {char_desc}.
    Scene: The character is performing an action about '{video_topic}'.
    Details: The character is holding/drinking a glass of warm, creamy golden-yellow turmeric milk.
    Atmosphere: Warm, inviting, energetic, high quality.
    Action: The video starts with an impressive hook (expressive emotion or surprising action). The character talks naturally (Vietnamese context implied). Ends with a welcoming gesture (Call to action).
    --duration {duration_option}
    """
    st.code(sora_prompt, language='text')
    st.caption("💡 Copy prompt trên dán vào Sora. Prompt đã bao gồm mô tả Hook và CTA bằng hành động.")
