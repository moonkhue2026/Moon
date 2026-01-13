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
    "Kể chuyện (Story-based)": "🎬 KỊCH BẢN: TỪ MỆT MỎI ĐẾN HẠNH PHÚC\n🔸 HOOK: Cảnh thở dài, gục xuống bàn.\n🔸 BODY: Uống Hera, mắt sáng lên, mỉm cười.\n🔸 CTA: Giơ ly sữa mời mọi người.",
    "Giải quyết vấn đề (Problem)": "🎬 KỊCH BẢN: ĐAU DẠ DÀY\n🔸 HOOK: Ôm bụng nhăn nhó, đau đớn.\n🔸 BODY: Uống Hera, hiệu ứng dịu mát, bụng êm.\n🔸 CTA: Giơ ngón tay Like, cười tươi.",
    "Cảnh báo sai lầm (Warning)": "🎬 KỊCH BẢN: CẢNH BÁO PHA SAI\n🔸 HOOK: Định chế nước sôi sùng sục vào ly.\n🔸 BODY: Pha nước ấm 40 độ chuẩn, ly sữa vàng mịn.\n🔸 CTA: Mời uống và gật đầu hài lòng.",
    "Phản biện (Counter-Intuitive)": "🎬 KỊCH BẢN: SỢ BÉO?\n🔸 HOOK: Lắc đầu xua tay với hũ đường trắng.\n🔸 BODY: Ôm lá cỏ ngọt Stevia, show eo thon.\n🔸 CTA: Nháy mắt, uống ngon lành.",
    "Trước - Sau (Transformation)": "🎬 KỊCH BẢN: LỘT XÁC\n🔸 HOOK: Mặt buồn, da sạm, thiếu sức sống.\n🔸 BODY: Biến hình sang da hồng hào, tươi cười rạng rỡ.\n🔸 CTA: Tạo dáng tự tin bên sản phẩm.",
    "Trải nghiệm/Review": "🎬 KỊCH BẢN: NHẬT KÝ 7 NGÀY\n🔸 HOOK: Show tờ lịch hoặc giơ 7 ngón tay.\n🔸 BODY: Cảnh uống ngon lành vui vẻ.\n🔸 CTA: Hôn gió/Bắn tim.",
    "Hài hước/Trend": "🎬 KỊCH BẢN: BẮT TREND\n🔸 HOOK: Nhạc nổi lên, nhân vật vào thế chuẩn bị.\n🔸 BODY: Nhảy theo nhạc hot hoặc diễn cảnh hài hước về ăn uống healthy.\n🔸 CTA: Chỉ tay vào sản phẩm mời gọi."
}

# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🌙 MOON'S CREATOR v3.1 (Final)")
st.write("👉 **Tính năng:** Sora Prompt (No Text) + Thoại Việt (Lip-sync) + Tự chia đoạn.")

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
    st.write("📜 **Kịch bản tóm tắt:**")
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
    
    # 3. SORA PROMPT (CÓ THOẠI TIẾNG VIỆT + NO TEXT)
    st.subheader("🎥 Tạo Video (Sora Clean Feed)")
    
    # Slider chọn tổng thời lượng
    total_duration = st.select_slider("Chọn TỔNG thời lượng video mong muốn:", options=["15s", "30s", "45s", "60s"], value="30s")
    
    # Logic chia đoạn + THOẠI
    segments = []
    if total_duration == "15s":
        segments = [
            ("Full Video", 
             "The character is speaking enthusiastically directly to the camera.",
             "Mệt mỏi quá à? Thử ngay ly sữa nghệ Hera này nha, đảm bảo hồi sinh năng lượng liền!")
        ]
    elif total_duration == "30s":
        segments = [
            ("Phần 1 (0-15s): Hook", 
             "The character looks worried/painful and speaks to the camera.",
             "Trời ơi, cái lưng cái bụng nó biểu tình rồi! Làm sao đây ta?"),
             
            ("Phần 2 (15-30s): Giải pháp", 
             "The character looks happy, holding the milk and speaking.",
             "May mà có em Hera này. Uống vào êm ru, ngủ ngon tới sáng. Chị em thử ngay nhé!")
        ]
    elif total_duration == "45s":
        segments = [
            ("Phần 1 (0-15s): Hook", 
             "The character describes the pain.",
             "Mấy nay đau dạ dày, ăn không ngon ngủ không yên, da dẻ sạm hết cả đi."),
             
            ("Phần 2 (15-30s): Giải pháp", 
             "The character introduces the product.",
             "Bí quyết của Moon là đây. Sữa nghệ Hera tách béo, không lo nóng, vị siêu ngon."),
             
            ("Phần 3 (30-45s): Kết quả", 
             "The character shows result and calls to action.",
             "Giờ thì khỏe re, da đẹp dáng xinh. Ai muốn như Moon thì inbox ngay nha!")
        ]
    else: # 60s
        segments = [
            ("Phần 1 (0-15s): Hook", "Speaking about the problem.", "Haizz, lại đau bao tử nữa rồi, chán ghê!"),
            ("Phần 2 (15-30s): Diễn biến", "Explaining the situation.", "Ăn uống thất thường nên nó hành vậy đó mọi người."),
            ("Phần 3 (30-45s): Giải pháp", "Showing the milk.", "Nhưng mà đừng lo, Moon có bảo bối sữa nghệ Hera này rồi."),
            ("Phần 4 (45-60s): Kết", "Happy ending.", "Uống 1 ly là êm ngay. Mọi người nhớ giữ sức khỏe nha!")
        ]

    # Vòng lặp hiển thị
    for name, action, vn_script in segments:
        st.markdown(f"**🎞️ {name}**")
        
        # Tạo prompt gộp
        sora_prompt = f"""
        {style_desc}.
        Subject: {char_desc}.
        Scene Context: Segment about '{video_topic}'.
        Action: {action}
        Speaking Line (Vietnamese): "{vn_script}"
        Lip-sync instruction: Ensure mouth moves naturally matching the dialogue.
        Constraint: NO TEXT OVERLAYS, NO SUBTITLES, CLEAN BACKGROUND.
        Details: Warm lighting, engaging eye contact.
        --duration 15s
        """
        st.code(sora_prompt, language='text')
        st.caption(f"💡 Thoại gợi ý: '{vn_script}'")
        
        st.divider()
