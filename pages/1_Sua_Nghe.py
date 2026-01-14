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

# 4. KỊCH BẢN VIDEO (SCRIPT GỐC)
video_scripts = {
    "Kể chuyện (Story-based)": "🎬 KỊCH BẢN: TỪ MỆT MỎI ĐẾN HẠNH PHÚC\n🔸 HOOK: Cảnh thở dài, gục xuống bàn vì áp lực.\n🔸 BODY: Uống Hera, mắt sáng lên, mỉm cười nhẹ nhõm.\n🔸 CTA: Giơ ly sữa mời mọi người.",
    "Giải quyết vấn đề (Problem)": "🎬 KỊCH BẢN: ĐAU DẠ DÀY\n🔸 HOOK: Ôm bụng nhăn nhó, đau đớn, tia sét đỏ.\n🔸 BODY: Uống Hera, hiệu ứng dịu mát lan tỏa, bụng êm.\n🔸 CTA: Giơ ngón tay Like, cười tươi.",
    "Cảnh báo sai lầm (Warning)": "🎬 KỊCH BẢN: CẢNH BÁO PHA SAI\n🔸 HOOK: Định chế nước sôi sùng sục vào ly. Hiện dấu X đỏ.\n🔸 BODY: Pha nước ấm 40 độ chuẩn, ly sữa vàng mịn.\n🔸 CTA: Mời uống và gật đầu hài lòng.",
    "Phản biện (Counter-Intuitive)": "🎬 KỊCH BẢN: SỢ BÉO?\n🔸 HOOK: Lắc đầu xua tay với hũ đường trắng.\n🔸 BODY: Ôm lá cỏ ngọt Stevia, show eo thon.\n🔸 CTA: Nháy mắt, uống ngon lành.",
    "Trước - Sau (Transformation)": "🎬 KỊCH BẢN: LỘT XÁC\n🔸 HOOK: Mặt buồn, da sạm, thiếu sức sống.\n🔸 BODY: Biến hình sang da hồng hào, tươi cười rạng rỡ.\n🔸 CTA: Tạo dáng tự tin bên sản phẩm.",
    "Trải nghiệm/Review": "🎬 KỊCH BẢN: NHẬT KÝ 7 NGÀY\n🔸 HOOK: Show tờ lịch hoặc giơ 7 ngón tay.\n🔸 BODY: Cảnh uống ngon lành vui vẻ.\n🔸 CTA: Hôn gió/Bắn tim.",
    "Hài hước/Trend": "🎬 KỊCH BẢN: BẮT TREND\n🔸 HOOK: Nhạc nổi lên, nhân vật vào thế chuẩn bị.\n🔸 BODY: Nhảy theo nhạc hot hoặc diễn cảnh hài hước về ăn uống healthy.\n🔸 CTA: Chỉ tay vào sản phẩm mời gọi."
}

# 5. DỮ LIỆU SORA CHI TIẾT (MAPPING ĐÚNG CHỦ ĐỀ)
sora_scenarios = {
    "Kể chuyện (Story-based)": {
        "15s": [("Full Video", "Character looks tired at desk, then drinks milk and smiles peacefully.", "Haizz, đuối sức quá... May mà có ly sữa nghệ này, nạp lại năng lượng yêu thương liền!")],
        "30s": [
            ("Phần 1 (0-15s)", "Character sighs deeply, looking exhausted/stressed.", "Công việc ngập đầu, người cứ uể oải, chán ghê..."),
            ("Phần 2 (15-30s)", "Character drinks milk, eyes light up, looks refreshed.", "Nhưng mà có Hera là khác liền. 1 ly ấm nóng, tỉnh táo hẳn ra!")
        ]
    },
    "Giải quyết vấn đề (Problem)": {
        "15s": [("Full Video", "Character holds stomach in pain, then drinks and feels better.", "Trời ơi cái bao tử nó hành! May mà có Hera, uống vô êm ru bà con ơi!")],
        "30s": [
            ("Phần 1 (0-15s)", "Character clutches stomach, grimacing in pain.", "Ui da, đau bao tử quá, ăn không ngon ngủ không yên!"),
            ("Phần 2 (15-30s)", "Character drinks golden milk, rubs tummy happily.", "Bí quyết là đây nè. Sữa nghệ Hera, êm dịu dạ dày, hết đau liền nha.")
        ]
    },
    "Cảnh báo sai lầm (Warning)": {
        "15s": [("Full Video", "Character stops boiling water, uses warm water instead.", "Dừng lại! Đừng pha nước sôi nha, mất hết chất đó! Pha nước ấm 40 độ thôi nè.")],
        "30s": [
            ("Phần 1 (0-15s)", "Character holds a boiling kettle, big RED X appears.", "Dừng lại ngay! Pha sữa nghệ mà dùng nước sôi sùng sục là hỏng hết Curcumin đó!"),
            ("Phần 2 (15-30s)", "Character pours warm water, drinks happily.", "Nhớ nha, chỉ dùng nước ấm 40 độ thôi. Vừa ngon vừa giữ trọn dưỡng chất!")
        ]
    },
    "Phản biện (Counter-Intuitive)": {
        "15s": [("Full Video", "Character pushes away sugar, points to slim waist.", "Sợ béo hả? Xưa rồi! Hera dùng đường cỏ ngọt, 0 calo, uống thả ga nha!")],
        "30s": [
            ("Phần 1 (0-15s)", "Character looks at sugar jar and shakes head 'No'.", "Nhiều bà sợ uống sữa bị béo đúng không? Đừng lo nha!"),
            ("Phần 2 (15-30s)", "Character shows Stevia leaf and slim figure.", "Hera dùng đường cỏ ngọt Stevia ăn kiêng, không sợ béo mà dáng còn xinh nữa nè.")
        ]
    },
    "Trước - Sau (Transformation)": {
        "15s": [("Full Video", "Split screen: Dull skin vs Glowing skin.", "Nhìn da Moon hồi trước chán chưa? Còn giờ thì hồng hào nhờ Hera nè!")],
        "30s": [
            ("Phần 1 (0-15s)", "Character looks sad in mirror, touching dull face.", "Hồi trước da mình sạm đen, nhìn thiếu sức sống lắm, buồn ghê..."),
            ("Phần 2 (15-30s)", "Character spins around, showing glowing skin.", "Từ ngày uống Hera, da dẻ hồng hào, ai cũng khen. Thích lắm luôn!")
        ]
    },
     "Trải nghiệm/Review": {
        "15s": [("Full Video", "Montage of drinking milk happily.", "Thử thách 7 ngày uống Hera cùng Moon nha! Ngày nào cũng một ly, khỏe đẹp từ bên trong.")],
        "30s": [
             ("Phần 1 (0-15s)", "Character points to calendar/7 fingers.", "Cùng Moon thực hiện thử thách 7 ngày thay đổi bản thân với Sữa Nghệ Hera nha."),
             ("Phần 2 (15-30s)", "Drinking shot and blowing a kiss.", "Vị ngon, dễ uống, mà kết quả thì mê ly. Chị em thử ngay đi!")
        ]
    },
    "Hài hước/Trend": {
         "15s": [("Full Video", "Dancing nicely with the product.", "Muốn khỏe đẹp thì về đội của Moon! Nhảy cùng Hera nào!")],
         "30s": [
             ("Phần 1 (0-15s)", "Funny dance moves start.", "Nhạc lên là quẩy lên! Tập thể dục cùng Sữa Nghệ nào cả nhà ơi."),
             ("Phần 2 (15-30s)", "Pose with product.", "Vừa vui vừa khỏe. Nhớ uống Hera mỗi ngày nha!")
         ]
    }
}


# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🌙 MOON'S CREATOR v3.2 (Fixed Logic)")
st.write("👉 **Tính năng:** Sora Prompt chuẩn theo từng chủ đề + Thoại Việt khớp ngữ cảnh.")

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
    
    # 3. SORA PROMPT (LOGIC MỚI - CHUẨN THEO CHỦ ĐỀ)
    st.subheader("🎥 Tạo Video (Sora Clean Feed)")
    
    # Slider chọn tổng thời lượng
    total_duration = st.select_slider("Chọn TỔNG thời lượng video mong muốn:", options=["15s", "30s"], value="30s")
    
    # Lấy dữ liệu Sora dựa trên CHỦ ĐỀ HIỆN TẠI (video_topic)
    # Nếu không tìm thấy chủ đề (lỗi), dùng default là story-based
    current_scenario_data = sora_scenarios.get(video_topic, sora_scenarios["Kể chuyện (Story-based)"])
    
    # Lấy segments dựa trên THỜI LƯỢNG
    # Nếu chọn 45s/60s mà chưa setup kịch bản, nó sẽ tự lùi về 30s
    if total_duration not in current_scenario_data:
        st.warning(f"Chưa có kịch bản chi tiết {total_duration} cho chủ đề này, đang hiển thị bản 30s.")
        segments = current_scenario_data.get("30s", [])
    else:
        segments = current_scenario_data[total_duration]

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
