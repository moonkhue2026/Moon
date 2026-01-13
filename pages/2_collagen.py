import streamlit as st

# Cài đặt trang web (Icon hoa anh đào cho Collagen)
st.set_page_config(page_title="Moon's Collagen Creator", page_icon="🌸", layout="centered")

# =========================================================
# DỮ LIỆU HỆ THỐNG (COLLAGEN)
# =========================================================

# 1. CONTEXT SẢN PHẨM
product_context = """
Sản phẩm: Collagen Peptide Thủy Phân (Hera Collagen).
Thành phần: Collagen Peptide nhập khẩu Đức/Nhật, Vitamin C, HA (Hyaluronic Acid), Chiết xuất lựu đỏ.
Công dụng: Căng bóng da, mờ nếp nhăn, cấp ẩm, giúp tóc móng chắc khỏe, chống lão hóa.
Ưu điểm: Dạng thủy phân hấp thu nhanh gấp 10 lần, không gây nóng, không nổi mụn, vị trái cây dễ uống.
Đối tượng: Phụ nữ sau 25 tuổi, da khô sạm, có nếp nhăn, muốn trẻ hóa.
Thương hiệu cá nhân: Moon - Người chia sẻ bí quyết "Lão hóa ngược".
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
    "Nuôi dưỡng (Nurture)": "Viết bài Storytelling.\nChủ đề: Nỗi sợ già và mong muốn níu giữ thanh xuân.\nCấu trúc: Hook (Giật mình khi thấy nếp nhăn) -> Body (Hành trình tìm lại làn da căng mướt nhờ Collagen) -> Kết (Thông điệp yêu bản thân).\nTone: Tâm tình, thấu hiểu.",
    "Giáo dục (Educate)": "Viết bài Kiến thức.\nChủ đề: Tại sao uống Collagen mãi không đẹp? (Do chưa chọn đúng loại Peptide).\nCấu trúc: Hook (Sai lầm phổ biến) -> Body (Phân biệt Collagen thường vs Thủy phân Peptide) -> Kết (Chọn Hera để hấp thu tối đa).\nTone: Chuyên gia sắc đẹp.",
    "Chuyển đổi (Convert)": "Viết bài Bán hàng.\nChủ đề: Ưu đãi liệu trình 'Hồi sinh làn da'.\nCấu trúc: Hook (Show kết quả da căng bóng) -> Body (Giải quyết: Da khô, sạm -> Da mướt. Deal hời mua 3 tặng 1) -> CTA (Chốt đơn ngay).\nTone: Hào hứng, khan hiếm.",
    "Nghỉ ngơi/Story": "Viết Caption ngắn kèm ảnh chill/uống collagen.\nNội dung: Morning routine, skincare từ bên trong.\nTone: Sang chảnh, nhẹ nhàng."
}

# 4. KỊCH BẢN VIDEO (SCRIPT)
video_scripts = {
    "Kể chuyện (Story-based)": "🎬 KỊCH BẢN: THANH XUÂN TRỞ LẠI\n🔸 HOOK: Soi gương thấy vết chân chim, thở dài.\n🔸 BODY: Uống Collagen Hera, da dẻ hồng hào, tự tin selfie.\n🔸 CTA: Hất tóc tự tin, mời mọi người uống.",
    "Giải quyết vấn đề (Problem)": "🎬 KỊCH BẢN: DA KHÔ MỐC?\n🔸 HOOK: Makeup bị mốc nền (cakey), da nứt nẻ.\n🔸 BODY: Uống Collagen, da ngậm nước căng bóng như gương.\n🔸 CTA: Sờ tay lên má, cười thích thú.",
    "Cảnh báo sai lầm (Warning)": "🎬 KỊCH BẢN: UỐNG SAI CÁCH\n🔸 HOOK: Cầm viên thuốc to đùng khó nuốt, lắc đầu.\n🔸 BODY: Chuyển sang gói Collagen nước Hera, uống ngon lành.\n🔸 CTA: Giơ ngón cái (Like).",
    "Phản biện (Counter-Intuitive)": "🎬 KỊCH BẢN: ĂN DA HEO BỔ SUNG COLLAGEN?\n🔸 HOOK: Nhìn đống da heo/chân gà đầy dầu mỡ, sợ hãi.\n🔸 BODY: Cầm gói Hera nhỏ gọn tinh tế.\n🔸 CTA: Uống một hơi sảng khoái.",
    "Trước - Sau (Transformation)": "🎬 KỊCH BẢN: LỘT XÁC 28 NGÀY\n🔸 HOOK: Mặt mộc xám xịt, lỗ chân lông to.\n🔸 BODY: Biến hình (Transition) sang da căng bóng (Glass skin).\n🔸 CTA: Tạo dáng beauty queen.",
    "Trải nghiệm/Review": "🎬 KỊCH BẢN: VLOG BUỔI SÁNG\n🔸 HOOK: Cảnh xé gói collagen, pha nước màu hồng đẹp mắt.\n🔸 BODY: Uống chậm rãi, tận hưởng vị lựu đỏ.\n🔸 CTA: Zoom cận cảnh làn da mộc.",
    "Hài hước/Trend": "🎬 KỊCH BẢN: BẮT TREND\n🔸 HOOK: Nhân vật nhảy trend biến hình (Héo úa -> Tươi xanh).\n🔸 BODY: Điệu đà bên ly collagen.\n🔸 CTA: Mời gọi 'Về đội của Moon'."
}

# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🌸 MOON'S COLLAGEN CREATOR")
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
        full_prompt = f"""Đóng vai Moon (Thương hiệu cá nhân sức khỏe & Sắc đẹp).
{product_context}
NHIỆM VỤ: {text_prompts[today_task['text']]}
YÊU CẦU: Caption hấp dẫn, sang chảnh, thoại tự nhiên, có CTA. Hashtag: #HeraCollagen #DepDa #LaoHoaNguoc #MoonBeauty"""
        st.code(full_prompt, language='text')

with tab2:
    st.subheader(f"Chủ đề: {video_topic}")
    st.write("📜 **Kịch bản tóm tắt:**")
    st.code(video_scripts.get(video_topic, ""), language='text')
    
    st.divider()
    
    # 1. CHỌN PHONG CÁCH
    video_style = st.radio("Chọn phong cách video:", ["3D Animation (Bé Collagen)", "KOL (Người thật)"], horizontal=True)
    
    # Thiết lập biến Style
    if video_style == "3D Animation (Bé Collagen)":
        style_desc = "Pixar 3D animation style, cute anthropomorphic pink collagen drop character"
        char_desc = "The character is a cute, glowing pink water drop with big sparkly eyes and smooth skin"
        action_verb = "animating"
        product_desc = "a glass of pink pomegranate collagen drink"
    else:
        style_desc = "High-quality realistic cinematic video, photorealistic, 8k, beauty commercial style"
        char_desc = "A beautiful Vietnamese female beauty expert (Moon), flawless glowing skin, elegant silk pajamas or white dress"
        action_verb = "acting"
        product_desc = "a glass of pink pomegranate collagen drink"

    # 2. MIDJOURNEY PROMPT (THUMBNAIL)
    st.write("🎨 **Prompt Ảnh Thumbnail (Midjourney):**")
    prompt_mj = f"/imagine prompt: {char_desc} holding {product_desc}, {action_verb} in a bright clean bedroom setting about {video_topic}. {style_desc}, soft beauty lighting, 8k --ar 9:16"
    st.code(prompt_mj, language='text')
    
    st.divider()
    
    # 3. SORA PROMPT (CÓ THOẠI TIẾNG VIỆT + NO TEXT)
    st.subheader("🎥 Tạo Video (Sora Clean Feed)")
    
    # Slider chọn tổng thời lượng
    total_duration = st.select_slider("Chọn TỔNG thời lượng video mong muốn:", options=["15s", "30s", "45s", "60s"], value="30s")
    
    # Logic chia đoạn + THOẠI (COLLAGEN)
    segments = []
    if total_duration == "15s":
        segments = [
            ("Full Video", 
             "The character is touching her cheek and speaking enthusiastically.",
             "Da dẻ dạo này chán quá mấy bà ơi! May mà tìm được chân ái Hera này, da mướt rượt luôn nè!")
        ]
    elif total_duration == "30s":
        segments = [
            ("Phần 1 (0-15s): Hook", 
             "The character looks sad, looking in the mirror, touching wrinkles.",
             "Trời ơi, mới 25 tuổi mà nếp nhăn đuôi mắt xuất hiện rồi. Cứu tui với!"),
             
            ("Phần 2 (15-30s): Giải pháp", 
             "The character looks happy, drinking the pink collagen drink.",
             "Bí mật là đây nè. Collagen Hera vị lựu, uống 1 gói bằng 10 lần đắp mặt nạ. Thử đi ghiền đó!")
        ]
    elif total_duration == "45s":
        segments = [
            ("Phần 1 (0-15s): Hook", 
             "The character looks tired, dull skin.",
             "Mấy nay thức khuya cày phim, da sạm đi thấy rõ luôn. Nhìn vào gương mà buồn nẫu ruột."),
             
            ("Phần 2 (15-30s): Giải pháp", 
             "The character introduces the product happily.",
             "Nhưng mà Moon không lo đâu. Mỗi sáng làm 1 gói Hera Collagen này là lấy lại phong độ ngay."),
             
            ("Phần 3 (30-45s): Kết quả", 
             "The character shows glowing skin close-up.",
             "Nhìn nè, da căng bóng như gương luôn. Chị em nào muốn lão hóa ngược thì inbox Moon nha.")
        ]
    else: # 60s
        segments = [
            ("Phần 1 (0-15s): Hook", "Sad/Worried about skin.", "Mọi người có tin là uống cái này trẻ ra 5 tuổi không?"),
            ("Phần 2 (15-30s): Diễn biến", "Explaining the science (simple).", "Hồi xưa Moon cũng không tin, mà từ hồi uống Peptide thủy phân này da khác hẳn."),
            ("Phần 3 (30-45s): Giải pháp", "Drinking and enjoying.", "Vị lựu ngon xỉu, không hề tanh nha. Mà quan trọng là không bị nóng trong người."),
            ("Phần 4 (45-60s): Kết", "Happy ending & CTA.", "Đầu tư cho nhan sắc là không bao giờ lỗ. Rinh ngay kẻo lỡ ưu đãi nha!")
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
        Details: Soft beauty lighting, glowing skin texture.
        --duration 15s
        """
        st.code(sora_prompt, language='text')
        st.caption(f"💡 Thoại gợi ý: '{vn_script}'")
        
        st.divider()
