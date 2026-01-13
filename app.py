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

# 4. KỊCH BẢN VIDEO (SCRIPT)
video_scripts = {
    "Kể chuyện (Story-based)": "🎬 KỊCH BẢN: TỪ MỆT MỎI ĐẾN HẠNH PHÚC\n🔸 HOOK (0-5s): Cảnh thở dài, gục xuống bàn. Text: 'Đuối sức...'\n🔸 BODY (5-25s): Uống Hera, mắt sáng lên, mỉm cười.\n🔸 CTA (25-30s): Giơ ly sữa mời. Text: 'Nạp lại năng lượng ngay!'",
    "Giải quyết vấn đề (Problem)": "🎬 KỊCH BẢN: ĐAU DẠ DÀY\n🔸 HOOK (0-5s): Ôm bụng nhăn nhó, tia sét đỏ. Text: 'Đau bao tử lại hành!'\n🔸 BODY (5-25s): Uống Hera, hiệu ứng dịu mát, bụng êm.\n🔸 CTA (25-30s): Giơ ngón tay Like. Text: 'Êm ru sau 1 ly. Thử ngay!'",
    "Cảnh báo sai lầm (Warning)": "🎬 KỊCH BẢN: CẢNH BÁO PHA SAI\n🔸 HOOK (0-5s): Dấu X ĐỎ to đùng trước ấm nước sôi. Text: 'Dừng lại! Đừng pha nước sôi!'\n🔸 BODY (5-25s): Pha nước ấm 40 độ, ly sữa vàng mịn.\n🔸 CTA (25-30s): Text: 'Pha đúng mới giữ được chất!'",
    "Phản biện (Counter-Intuitive)": "🎬 KỊCH BẢN: SỢ BÉO?\n🔸 HOOK (0-5s): Lắc đầu xua tay với đường trắng. Text: 'Sợ béo? Xưa rồi!'\n🔸 BODY (5-25s): Ôm lá cỏ ngọt Stevia, show eo thon.\n🔸 CTA (25-30s): Nháy mắt. Text: 'Đường cỏ ngọt 0 Calo. Uống đi chờ chi!'",
    "Trước - Sau (Transformation)": "🎬 KỊCH BẢN: LỘT XÁC (SPLIT SCREEN)\n🔸 HOOK (0-5s): Mặt buồn, da sạm (Bên trái). Text: 'Trước khi gặp Hera...'\n🔸 BODY (5-25s): Biến hình sang da hồng, tươi cười (Bên phải).\n🔸 CTA (25-30s): Tạo dáng tự tin. Text: 'Khỏe đẹp từ bên trong. Inbox Moon!'",
    "Trải nghiệm/Review": "🎬 KỊCH BẢN: NHẬT KÝ 7 NGÀY\n🔸 HOOK (0-5s): Show lịch 7 ngày. Text: 'Thử thách 7 ngày uống Hera'.\n🔸 BODY (5-25s): Cắt nhanh cảnh uống ngon lành các ngày.\n🔸 CTA (25-30s): Hôn gió/Bắn tim. Text: 'Duyệt nha! Chị em thử ngay.'",
    "Hài hước/Trend": "🎬 KỊCH BẢN: BẮT TREND\n🔸 HOOK: Nhạc nổi lên, nhân vật vào thế chuẩn bị.\n🔸 BODY: Nhảy theo nhạc hot hoặc diễn cảnh hài hước về ăn uống healthy.\n🔸 CTA: Chỉ tay vào sản phẩm. Text: 'Muốn khỏe thì về đội Moon!'"
}

# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🌙 MOON'S CREATOR v2.8 (Split Prompt)")
st.write("👉 **Mẹo:** Sora chỉ tạo được tối đa 15s/lần. App sẽ tự động chia nhỏ video dài thành các đoạn 15s để bạn ghép lại.")

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
YÊU CẦU: Caption hấp dẫn, thoại tự nhiên, có CTA cuối bài. Hashtag: #SuaNgheHera #HaPhanMinhNguyet"""
        st.code(full_prompt, language='text')

with tab2:
    st.subheader(f"Chủ đề: {video_topic}")
    st.write("📜 **Kịch bản gốc:**")
    st.code(video_scripts.get(video_topic, ""), language='text')
    
    st.divider()
    
    # 1. CHỌN PHONG CÁCH
    video_style = st.radio("Chọn phong cách video:", ["3D Animation (Bé Nghệ)", "KOL (Người thật)"], horizontal=True)
    
    # Thiết lập biến Style
    if video_style == "3D Animation (Bé Nghệ)":
        style_desc = "Pixar 3D animation style, cute anthropomorphic turmeric root character"
        char_desc = "The character is cute, round, with big expressive eyes"
        action_verb = "animating"
    else:
        style_desc = "High-quality realistic cinematic video, photorealistic, 8k, shot on Arri Alexa"
        char_desc = "A beautiful Vietnamese female health expert (Moon), natural beauty, warm smile, wearing elegant comfortable clothes"
        action_verb = "acting"

    # 2. MIDJOURNEY PROMPT (THUMBNAIL)
    st.write("🎨 **Prompt Ảnh Thumbnail (Midjourney):**")
    prompt_mj = f"/imagine prompt: {char_desc} holding a glass of warm golden turmeric milk, {action_verb} in a scene about {video_topic}. {style_desc}, warm lighting, 8k --ar 9:16"
    st.code(prompt_mj, language='text')
    
    st.divider()
    
    # 3. SORA PROMPT (CHIA NHỎ THEO THỜI LƯỢNG)
    st.subheader("🎥 Prompt tạo video Sora 2 (Đã chia đoạn)")
    
    # Slider chọn tổng thời lượng
    total_duration = st.select_slider("Chọn TỔNG thời lượng video mong muốn:", options=["15s", "30s", "45s", "60s"], value="30s")
    
    # Logic chia đoạn
    segments = []
    if total_duration == "15s":
        segments = [("Full Video", "Start with a strong Hook, show the main action, and end with a clear Call to Action gesture.")]
    elif total_duration == "30s":
        segments = [
            ("Phần 1 (0-15s): Hook & Mở đầu", "Start with an impressive Hook (surprising emotion/action). Introduce the problem/situation."),
            ("Phần 2 (15-30s): Giải pháp & CTA", "Show the solution (drinking Hera Milk). The character looks happy/relieved. End with a welcoming gesture (CTA).")
        ]
    elif total_duration == "45s":
        segments = [
            ("Phần 1 (0-15s): Hook & Vấn đề", "Start with a strong Hook. Focus on the pain point or problem vividly."),
            ("Phần 2 (15-30s): Giải pháp", "Show the transformation/solution. Drinking the golden milk, feeling better."),
            ("Phần 3 (30-45s): Kết quả & CTA", "Show the final happy result (glowing skin/no pain). End with a strong Call to Action.")
        ]
    else: # 60s
        segments = [
            ("Phần 1 (0-15s): Hook", "Start with a strong Hook. Introduce the context/problem."),
            ("Phần 2 (15-30s): Diễn biến 1", "Develop the story. Show the struggle or the 'Before' state clearly."),
            ("Phần 3 (30-45s): Diễn biến 2 (Giải pháp)", "Transition to the solution. Drinking Hera Milk, enjoying the taste."),
            ("Phần 4 (45-60s): Kết & CTA", "Show the 'After' effect. Happy, energetic. End with a strong Call to Action.")
        ]

    # Vòng lặp hiển thị từng Prompt
    for name, focus in segments:
        st.markdown(f"**🎞️ {name}**")
        sora_prompt = f"""
        {style_desc}.
        Subject: {char_desc}.
        Scene Context: Segment of a video about '{video_topic}'.
        ACTION FOCUS: {focus}
        Details: Holding/interacting with a glass of warm, creamy golden-yellow turmeric milk.
        Atmosphere: Warm, inviting, high quality.
        --duration 15s
        """
        st.code(sora_prompt, language='text')
