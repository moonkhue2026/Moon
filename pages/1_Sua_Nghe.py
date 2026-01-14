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

# 5. DỮ LIỆU SORA CHI TIẾT (MAPPING ĐÚNG CHỦ ĐỀ - ĐỦ 45s/60s)
sora_scenarios = {
    "Kể chuyện (Story-based)": {
        "15s": [("Full Video", "Character looks tired at desk, then drinks milk and smiles peacefully.", "Haizz, đuối sức quá... May mà có ly sữa nghệ này, nạp lại năng lượng yêu thương liền!")],
        "30s": [
            ("Phần 1 (0-15s)", "Character sighs deeply, looking exhausted/stressed.", "Công việc ngập đầu, người cứ uể oải, chán ghê..."),
            ("Phần 2 (15-30s)", "Character drinks milk, eyes light up, looks refreshed.", "Nhưng mà có Hera là khác liền. 1 ly ấm nóng, tỉnh táo hẳn ra!")
        ],
        "45s": [
            ("Phần 1 (0-15s)", "Character looks stressed, working late at night.", "Deadline dí chạy không kịp thở, mệt muốn xỉu luôn mấy bà ơi."),
            ("Phần 2 (15-30s)", "Character takes a break, makes a glass of golden milk.", "Thôi nghỉ tay xíu, tự thưởng cho mình ly sữa nghệ nóng hổi nè."),
            ("Phần 3 (30-45s)", "Character drinks, smiles, back to work happily.", "Uống xong ấm bụng, tinh thần phấn chấn làm việc tiếp. Cố lên!")
        ],
        "60s": [
            ("Phần 1 (0-15s)", "Character walking heavily, looking down.", "Có những ngày đi làm về chỉ muốn nằm bẹp một chỗ thôi."),
            ("Phần 2 (15-30s)", "Character sees the milk tin on shelf.", "May mà trong bếp lúc nào cũng có sẵn 'người bạn' này."),
            ("Phần 3 (30-45s)", "Character preparing drink carefully.", "Mùi nghệ thơm nhẹ, không hăng chút nào, pha nước ấm là ngon nhất."),
            ("Phần 4 (45-60s)", "Character enjoying and waving.", "Nạp lại năng lượng rồi. Chị em nhớ thương bản thân mình nha!")
        ]
    },
    "Giải quyết vấn đề (Problem)": {
        "15s": [("Full Video", "Character holds stomach in pain, then drinks and feels better.", "Trời ơi cái bao tử nó hành! May mà có Hera, uống vô êm ru bà con ơi!")],
        "30s": [
            ("Phần 1 (0-15s)", "Character clutches stomach, grimacing in pain.", "Ui da, đau bao tử quá, ăn không ngon ngủ không yên!"),
            ("Phần 2 (15-30s)", "Character drinks golden milk, rubs tummy happily.", "Bí quyết là đây nè. Sữa nghệ Hera, êm dịu dạ dày, hết đau liền nha.")
        ],
        "45s": [
            ("Phần 1 (0-15s)", "Character tossing in bed, holding stomach.", "Đêm nào cũng trằn trọc vì cái bao tử biểu tình, khổ tâm ghê."),
            ("Phần 2 (15-30s)", "Character gets up, drinks Hera.", "Dậy pha ngay ly sữa nghệ Hera. Curcumin cao cấp giúp lành vết thương nhanh lắm."),
            ("Phần 3 (30-45s)", "Character sleeping peacefully.", "Giờ thì êm ru, ngủ ngon tới sáng. Ai đau bao tử nhớ thử nha.")
        ],
        "60s": [
            ("Phần 1 (0-15s)", "Character eating spicy food, then pain strikes.", "Hồi chiều lỡ ăn cay chút xíu mà giờ cái bụng nó 'kêu gào' rồi."),
            ("Phần 2 (15-30s)", "Character searches for medicine but shakes head.", "Uống thuốc tây hoài thì nóng. Để Moon chỉ cách này lành tính hơn."),
            ("Phần 3 (30-45s)", "Character shows Hera box and drinks.", "Sữa nghệ tách béo, vừa ngon vừa hỗ trợ dạ dày cực tốt."),
            ("Phần 4 (45-60s)", "Character happy, thumbs up.", "Bụng êm re, không còn khó chịu nữa. Duyệt 10 điểm!")
        ]
    },
    "Cảnh báo sai lầm (Warning)": {
        "15s": [("Full Video", "Character stops boiling water, uses warm water instead.", "Dừng lại! Đừng pha nước sôi nha, mất hết chất đó! Pha nước ấm 40 độ thôi nè.")],
        "30s": [
            ("Phần 1 (0-15s)", "Character holds a boiling kettle, big RED X appears.", "Dừng lại ngay! Pha sữa nghệ mà dùng nước sôi sùng sục là hỏng hết Curcumin đó!"),
            ("Phần 2 (15-30s)", "Character pours warm water, drinks happily.", "Nhớ nha, chỉ dùng nước ấm 40 độ thôi. Vừa ngon vừa giữ trọn dưỡng chất!")
        ],
        "45s": [
            ("Phần 1 (0-15s)", "Character pouring boiling water, milk turns clumpy.", "Trời ơi, pha nước sôi là sữa nó vón cục, uống kì lắm!"),
            ("Phần 2 (15-30s)", "Character explains (finger wagging) and corrects.", "Sai lầm tai hại nha. Curcumin gặp nhiệt độ cao là mất tác dụng hết."),
            ("Phần 3 (30-45s)", "Character drinks correctly prepared glass.", "Nước ấm tầm 40-50 độ là chuẩn bài. Thơm ngon bổ dưỡng!")
        ],
        "60s": [
            ("Phần 1 (0-15s)", "Character confused with many cups.", "Có nhiều bà hỏi Moon sao uống hoài không thấy đẹp?"),
            ("Phần 2 (15-30s)", "Character realizes boiling water mistake.", "Hóa ra là toàn pha nước sôi 100 độ không à. Uổng tiền lắm mấy bà ơi."),
            ("Phần 3 (30-45s)", "Character demonstrates correct way.", "Nhìn Moon nè: Nước ấm vừa tay, khuấy nhẹ là tan đều."),
            ("Phần 4 (45-60s)", "Character winks.", "Uống đúng cách mới đẹp được nha. Lưu lại mẹo này liền đi!")
        ]
    },
    "Phản biện (Counter-Intuitive)": {
        "15s": [("Full Video", "Character pushes away sugar, points to slim waist.", "Sợ béo hả? Xưa rồi! Hera dùng đường cỏ ngọt, 0 calo, uống thả ga nha!")],
        "30s": [
            ("Phần 1 (0-15s)", "Character looks at sugar jar and shakes head 'No'.", "Nhiều bà sợ uống sữa bị béo đúng không? Đừng lo nha!"),
            ("Phần 2 (15-30s)", "Character shows Stevia leaf and slim figure.", "Hera dùng đường cỏ ngọt Stevia ăn kiêng, không sợ béo mà dáng còn xinh nữa nè.")
        ],
        "45s": [
            ("Phần 1 (0-15s)", "Character stepping on scale, looks worried.", "Cứ nghe tới sữa là sợ tăng cân, ám ảnh cái cân ghê gớm."),
            ("Phần 2 (15-30s)", "Character reads label 'Skimmed Milk'.", "Nhưng đọc kỹ nè: Sữa tách béo nhập khẩu New Zealand nha."),
            ("Phần 3 (30-45s)", "Character dancing happily.", "Vừa đẹp da, tốt dạ dày mà eo vẫn thon. Còn gì bằng!")
        ],
        "60s": [
            ("Phần 1 (0-15s)", "Character refusing sweet cake.", "Moon là chúa sợ đồ ngọt, sợ mập lắm."),
            ("Phần 2 (15-30s)", "Character tries Hera milk carefully.", "Nên lúc đầu cũng rén lắm. Ai dè uống thử thấy ngọt thanh nhẹ nhàng."),
            ("Phần 3 (30-45s)", "Character explains Stevia.", "Tìm hiểu mới biết là đường cỏ ngọt, người tiểu đường cũng dùng được luôn."),
            ("Phần 4 (45-60s)", "Character cheers.", "Yên tâm chốt đơn nha. Đẹp không cần kiêng khem khổ sở đâu!")
        ]
    },
    "Trước - Sau (Transformation)": {
        "15s": [("Full Video", "Split screen: Dull skin vs Glowing skin.", "Nhìn da Moon hồi trước chán chưa? Còn giờ thì hồng hào nhờ Hera nè!")],
        "30s": [
            ("Phần 1 (0-15s)", "Character looks sad in mirror, touching dull face.", "Hồi trước da mình sạm đen, nhìn thiếu sức sống lắm, buồn ghê..."),
            ("Phần 2 (15-30s)", "Character spins around, showing glowing skin.", "Từ ngày uống Hera, da dẻ hồng hào, ai cũng khen. Thích lắm luôn!")
        ],
        "45s": [
            ("Phần 1 (0-15s)", "Character looking at old photo.", "Xem lại hình cũ mà hết hồn, nhìn như bà cô già đau khổ."),
            ("Phần 2 (15-30s)", "Character drinking milk daily (time lapse).", "Kiên trì mỗi ngày 1 ly thôi, mà thay đổi thần kỳ luôn đó."),
            ("Phần 3 (30-45s)", "Character posing now.", "Giờ ra đường tự tin mặt mộc. Phụ nữ là phải biết yêu mình nha!")
        ],
        "60s": [
            ("Phần 1 (0-15s)", "Character feeling weak and pale.", "Sau khi sinh xong người mình yếu hẳn, da dẻ xuống cấp trầm trọng."),
            ("Phần 2 (15-30s)", "Character discovers Hera.", "Được chị bạn giới thiệu cho em sữa nghệ này."),
            ("Phần 3 (30-45s)", "Character drinking and feeling stronger.", "Mới uống 2 tuần là thấy ăn ngon ngủ ngon, da bắt đầu sáng lên."),
            ("Phần 4 (45-60s)", "Character happy with family/friends.", "Giờ ai gặp cũng khen trẻ ra. Bí quyết nằm ở ly sữa vàng này đó.")
        ]
    },
     "Trải nghiệm/Review": {
        "15s": [("Full Video", "Montage of drinking milk happily.", "Thử thách 7 ngày uống Hera cùng Moon nha! Ngày nào cũng một ly, khỏe đẹp từ bên trong.")],
        "30s": [
             ("Phần 1 (0-15s)", "Character points to calendar/7 fingers.", "Cùng Moon thực hiện thử thách 7 ngày thay đổi bản thân với Sữa Nghệ Hera nha."),
             ("Phần 2 (15-30s)", "Drinking shot and blowing a kiss.", "Vị ngon, dễ uống, mà kết quả thì mê ly. Chị em thử ngay đi!")
        ],
        "45s": [
             ("Phần 1 (0-15s)", "Character unboxing the product.", "Hôm nay đập hộp em siêu phẩm Sữa Nghệ Hera cho cả nhà xem nè."),
             ("Phần 2 (15-30s)", "Character making the drink.", "Bột mịn tơi, màu vàng nghệ tự nhiên, mùi thơm thoang thoảng."),
             ("Phần 3 (30-45s)", "Character tasting and nodding.", "Uống vào là ấm cả người. Duyệt nha, đáng đồng tiền bát gạo!")
        ],
        "60s": [
             ("Phần 1 (0-15s)", "Character talking to camera like a vlogger.", "Có nhiều bạn hỏi Moon uống gì buổi sáng? Đây, câu trả lời đây."),
             ("Phần 2 (15-30s)", "Close up of the texture.", "Không lợn cợn, không bị hăng mùi nghệ đâu, ngon như sữa hạt vậy á."),
             ("Phần 3 (30-45s)", "Character shows empty glass.", "Vèo cái hết bay. Uống cái này ghiền thật sự."),
             ("Phần 4 (45-60s)", "Character waves goodbye.", "Ai muốn trải nghiệm thì inbox Moon tư vấn cho nha. Bye bye!")
        ]
    },
    "Hài hước/Trend": {
         "15s": [("Full Video", "Dancing nicely with the product.", "Muốn khỏe đẹp thì về đội của Moon! Nhảy cùng Hera nào!")],
         "30s": [
             ("Phần 1 (0-15s)", "Funny dance moves start.", "Nhạc lên là quẩy lên! Tập thể dục cùng Sữa Nghệ nào cả nhà ơi."),
             ("Phần 2 (15-30s)", "Pose with product.", "Vừa vui vừa khỏe. Nhớ uống Hera mỗi ngày nha!")
         ],
         "45s": [
             ("Phần 1 (0-15s)", "Character trying to do yoga/exercise but failing.", "Tập thể dục thì lười..."),
             ("Phần 2 (15-30s)", "Character grabs milk instead.", "...nhưng uống sữa đẹp da thì siêng lắm nha!"),
             ("Phần 3 (30-45s)", "Character dancing happy.", "Khỏe bên trong đẹp bên ngoài mới là chân ái. A hi hi!")
         ],
         "60s": [
             ("Phần 1 (0-15s)", "Character acting cool with sunglasses.", "Ngầu chưa ngầu chưa?"),
             ("Phần 2 (15-30s)", "Trips over something funny.", "Ủa... xém té. Nhưng không sao, thần thái vẫn quan trọng."),
             ("Phần 3 (30-45s)", "Recovers by drinking milk.", "Làm ngụm sữa lấy lại bình tĩnh cái đã."),
             ("Phần 4 (45-60s)", "Ends with a funny pose.", "Cuộc sống có lúc lên lúc xuống, nhưng uống Hera là phải uống đều nha!")
         ]
    }
}


# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🌙 MOON'S CREATOR v3.3 (Full Duration)")
st.write("👉 **Tính năng:** Sora Prompt chuẩn chủ đề + Đủ thời lượng (15s/30s/45s/60s).")

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
    
    # Slider chọn tổng thời lượng (ĐÃ BỔ SUNG 45s, 60s)
    total_duration = st.select_slider("Chọn TỔNG thời lượng video mong muốn:", options=["15s", "30s", "45s", "60s"], value="30s")
    
    # Lấy dữ liệu Sora dựa trên CHỦ ĐỀ HIỆN TẠI (video_topic)
    # Nếu không tìm thấy chủ đề (lỗi), dùng default là story-based
    current_scenario_data = sora_scenarios.get(video_topic, sora_scenarios["Kể chuyện (Story-based)"])
    
    # Lấy segments dựa trên THỜI LƯỢNG
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
