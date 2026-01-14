import streamlit as st

# Cài đặt trang web
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

# 4. KỊCH BẢN TÓM TẮT
video_scripts = {
    "Kể chuyện (Story-based)": "🎬 KỊCH BẢN: THANH XUÂN TRỞ LẠI\n🔸 HOOK: Soi gương thấy vết chân chim, thở dài.\n🔸 BODY: Uống Collagen Hera, da dẻ hồng hào, tự tin selfie.\n🔸 CTA: Hất tóc tự tin, mời mọi người uống.",
    "Giải quyết vấn đề (Problem)": "🎬 KỊCH BẢN: DA KHÔ MỐC?\n🔸 HOOK: Makeup bị mốc nền (cakey), da nứt nẻ.\n🔸 BODY: Uống Collagen, da ngậm nước căng bóng như gương.\n🔸 CTA: Sờ tay lên má, cười thích thú.",
    "Cảnh báo sai lầm (Warning)": "🎬 KỊCH BẢN: UỐNG SAI CÁCH\n🔸 HOOK: Cầm viên thuốc to đùng khó nuốt, lắc đầu.\n🔸 BODY: Chuyển sang gói Collagen nước Hera, uống ngon lành.\n🔸 CTA: Giơ ngón cái (Like).",
    "Phản biện (Counter-Intuitive)": "🎬 KỊCH BẢN: ĂN DA HEO BỔ SUNG COLLAGEN?\n🔸 HOOK: Nhìn đống da heo/chân gà đầy dầu mỡ, sợ hãi.\n🔸 BODY: Cầm gói Hera nhỏ gọn tinh tế.\n🔸 CTA: Uống một hơi sảng khoái.",
    "Trước - Sau (Transformation)": "🎬 KỊCH BẢN: LỘT XÁC 28 NGÀY\n🔸 HOOK: Mặt mộc xám xịt, lỗ chân lông to.\n🔸 BODY: Biến hình (Transition) sang da căng bóng (Glass skin).\n🔸 CTA: Tạo dáng beauty queen.",
    "Trải nghiệm/Review": "🎬 KỊCH BẢN: VLOG BUỔI SÁNG\n🔸 HOOK: Cảnh xé gói collagen, pha nước màu hồng đẹp mắt.\n🔸 BODY: Uống chậm rãi, tận hưởng vị lựu đỏ.\n🔸 CTA: Zoom cận cảnh làn da mộc.",
    "Hài hước/Trend": "🎬 KỊCH BẢN: BẮT TREND\n🔸 HOOK: Nhân vật nhảy trend biến hình (Héo úa -> Tươi xanh).\n🔸 BODY: Điệu đà bên ly collagen.\n🔸 CTA: Mời gọi 'Về đội của Moon'."
}

# 5. DỮ LIỆU SORA CHI TIẾT
sora_scenarios = {
    "Kể chuyện (Story-based)": {
        "15s": [("Full Video", "Character looks at mirror sadly, then drinks collagen and smiles.", "Mới có 25 tuổi mà nếp nhăn đã ghé thăm rồi. Cứu tui với Hera ơi!")],
        "30s": [
            ("Phần 1 (0-15s)", "Character touches wrinkles/dry skin in mirror.", "Soi gương mà buồn nẫu ruột, da dẻ chán đời quá đi mất."),
            ("Phần 2 (15-30s)", "Character drinks pink drink, skin glows.", "Nhưng từ khi có Hera, thanh xuân như trở lại. Yêu lắm cơ!")
        ],
        "45s": [
            ("Phần 1 (0-15s)", "Character looking tired working late.", "Công việc áp lực làm da mình xuống cấp không phanh."),
            ("Phần 2 (15-30s)", "Character takes a break with Hera Collagen.", "Bí quyết 'hồi sinh' của Moon là gói collagen vị lựu này nè."),
            ("Phần 3 (30-45s)", "Character confident and happy.", "Uống xong thấy tươi tỉnh hẳn. Phụ nữ là phải đẹp bất chấp nha!")
        ],
        "60s": [
            ("Phần 1 (0-15s)", "Character scrolling phone, seeing beautiful girls.", "Lướt mạng thấy ai cũng da đẹp dáng xinh mà tủi thân ghê."),
            ("Phần 2 (15-30s)", "Character decides to change, buys Hera.", "Quyết tâm thay đổi! Bắt đầu với Collagen Peptide thủy phân Hera."),
            ("Phần 3 (30-45s)", "Character drinking consistently.", "Vị ngon, dễ uống, không lo nóng trong người."),
            ("Phần 4 (45-60s)", "Character showing result.", "Kết quả sau 1 tháng nè. Da mướt rượt, chồng khen nức nở luôn!")
        ]
    },
    "Giải quyết vấn đề (Problem)": {
        "15s": [("Full Video", "Character trying to makeup but skin is dry/cakey, then drinks collagen.", "Makeup mà da mốc meo chán ghê. Để Hera cấp nước thần tốc cho nè!")],
        "30s": [
            ("Phần 1 (0-15s)", "Character applying powder, it looks bad.", "Trời ơi, đánh phấn mà nó không ăn, da khô như ngói vỡ."),
            ("Phần 2 (15-30s)", "Character drinks collagen, skin becomes glass-skin.", "Uống ngay Hera Collagen. Cấp ẩm tầng sâu, da căng bóng liền.")
        ],
        "45s": [
            ("Phần 1 (0-15s)", "Character feeling dry skin in AC room.", "Ngồi điều hòa cả ngày da khô khốc, nứt nẻ khó chịu lắm."),
            ("Phần 2 (15-30s)", "Character drinks Hera.", "Cấp cứu ngay bằng một ly Collagen mát lạnh."),
            ("Phần 3 (30-45s)", "Character touching smooth cheek.", "Sờ lên da thấy mướt mịn thích ghê. Mùa này không thể thiếu em nó đâu.")
        ],
        "60s": [
            ("Phần 1 (0-15s)", "Character complaining about aging signs.", "Dạo này cười là thấy nếp nhăn, lo sốt vó luôn mấy bà."),
            ("Phần 2 (15-30s)", "Character researching, chooses Hera.", "Tìm hiểu mãi mới chốt được em Hera này vì hàm lượng Peptide cao."),
            ("Phần 3 (30-45s)", "Character drinking happy.", "Uống vào thấy da đàn hồi tốt hơn hẳn, vết chân chim mờ dần."),
            ("Phần 4 (45-60s)", "Character wink/kiss.", "Đừng để già mới chống. Chăm da từ bên trong ngay đi nhé!")
        ]
    },
    "Cảnh báo sai lầm (Warning)": {
        "15s": [("Full Video", "Character holding giant pills, shakes head. Drinks liquid instead.", "Uống viên to mắc nghẹn mà hấp thu kém lắm. Chuyển sang dạng nước thủy phân đi!")],
        "30s": [
            ("Phần 1 (0-15s)", "Character struggling to swallow pills.", "Ám ảnh nhất là uống mấy viên collagen to đùng, vừa khó nuốt vừa nóng."),
            ("Phần 2 (15-30s)", "Character drinks liquid Hera easily.", "Chuyển qua Hera dạng nước đi. Hấp thu gấp 10 lần mà ngon như nước trái cây.")
        ],
        "45s": [
            ("Phần 1 (0-15s)", "Character with pimples (acne).", "Nhiều người sợ uống collagen bị nổi mụn. Moon cũng từng sợ vậy."),
            ("Phần 2 (15-30s)", "Character explains 'Hydrolyzed'.", "Nhưng đó là loại thường thôi. Hera là Peptide thủy phân, mát lắm nha."),
            ("Phần 3 (30-45s)", "Character showing clear skin.", "Uống êm ru, da láng o, không hề có một cục mụn nào luôn.")
        ],
        "60s": [
            ("Phần 1 (0-15s)", "Character pouring money down the drain.", "Uống sai cách là tiền mất tật mang đó mấy bà ơi."),
            ("Phần 2 (15-30s)", "Character holds Hera box.", "Chọn collagen là phải chọn loại có Vitamin C và HA đi kèm mới chuẩn."),
            ("Phần 3 (30-45s)", "Character reading ingredients.", "Hera có đủ combo vàng: Peptide, Vitamin C, HA, Lựu đỏ."),
            ("Phần 4 (45-60s)", "Character thumbs up.", "Đầu tư thông minh là phải chọn Hera. Đẹp bền vững luôn!")
        ]
    },
    "Phản biện (Counter-Intuitive)": {
        "15s": [("Full Video", "Character looking at fatty pig skin, refuses. Drinks Hera.", "Ăn da heo chỉ béo thôi! 1 gói Hera bằng 10kg chân gà đó nha!")],
        "30s": [
            ("Phần 1 (0-15s)", "Character surrounded by greasy food.", "Ăn chân gà, da heo để bổ sung collagen? Sai lầm nha, chỉ tổ béo bụng thôi!"),
            ("Phần 2 (15-30s)", "Character holds slim sachet.", "Nhỏ nhưng có võ. 1 gói Hera chứa hàm lượng collagen tinh khiết cực cao.")
        ],
        "45s": [
            ("Phần 1 (0-15s)", "Character pinching belly fat.", "Sợ uống ngọt bị mập hả? Tâm lý chung của chị em mình rồi."),
            ("Phần 2 (15-30s)", "Character shows 'Sugar Free/Stevia'.", "Yên tâm nha, Hera dùng đường cỏ ngọt, không sinh năng lượng."),
            ("Phần 3 (30-45s)", "Character showing waist.", "Uống thả ga mà dáng vẫn 'mi nhon'. Mê chưa mê chưa?")
        ],
        "60s": [
            ("Phần 1 (0-15s)", "Character thinking collagen is expensive.", "Nhiều người nghĩ làm đẹp tốn kém lắm."),
            ("Phần 2 (15-30s)", "Character holding product, calculating.", "Tính ra mỗi ngày chỉ bằng một ly trà sữa thôi hà."),
            ("Phần 3 (30-45s)", "Character pushing away milk tea.", "Bớt trà sữa lại, thêm collagen vào. Lời to luôn đó."),
            ("Phần 4 (45-60s)", "Character beautiful.", "Vừa khỏe vừa đẹp, chồng yêu chiều. Đầu tư đi ngại chi!")
        ]
    },
    "Trước - Sau (Transformation)": {
        "15s": [("Full Video", "Split screen: Old/Sad vs New/Happy.", "Hành trình lột xác 28 ngày của Moon nè. Không tin nổi luôn đúng không?")],
        "30s": [
            ("Phần 1 (0-15s)", "Character looking at Before photo (dull).", "Nhìn lại ảnh cũ mà hết hồn. Da xám xịt, nhìn già chát."),
            ("Phần 2 (15-30s)", "Character looking at After (now).", "Còn giờ thì chấp camera thường luôn. Da căng bóng, tự tin hơn hẳn.")
        ],
        "45s": [
            ("Phần 1 (0-15s)", "Character marking calendar Day 1.", "Ngày đầu tiên bắt đầu hành trình tìm lại thanh xuân."),
            ("Phần 2 (15-30s)", "Time lapse drinking over days.", "Kiên trì, kỷ luật. Ngày nào cũng 1 gói vào buổi sáng."),
            ("Phần 3 (30-45s)", "Character marking Day 28.", "Và đây là kết quả sau 1 liệu trình. Da mướt như da em bé!")
        ],
        "60s": [
            ("Phần 1 (0-15s)", "Character telling a story.", "Có ai từng tự ti vì mặt mộc như Moon không?"),
            ("Phần 2 (15-30s)", "Character showing the product solution.", "Đừng buồn nữa, giải pháp nằm trong tay bạn nè."),
            ("Phần 3 (30-45s)", "Character drinking and smiling.", "Uống Hera không chỉ đẹp da mà tóc móng cũng chắc khỏe hơn nhiều."),
            ("Phần 4 (45-60s)", "Character inspiring others.", "Phụ nữ hiện đại là phải biết chăm sóc bản thân. Cùng Moon tỏa sáng nha!")
        ]
    },
     "Trải nghiệm/Review": {
        "15s": [("Full Video", "Vlog style: Mixing and drinking.", "Morning routine của Moon! Một ly Collagen lựu đỏ cho ngày mới rạng rỡ.")],
        "30s": [
             ("Phần 1 (0-15s)", "Character opening box, showing sachets.", "Đập hộp Hera Collagen cùng Moon nha. Bao bì hồng xinh xỉu."),
             ("Phần 2 (15-30s)", "Character tasting.", "Vị chua ngọt thanh mát, thơm mùi lựu, không hề tanh chút nào.")
        ],
        "45s": [
             ("Phần 1 (0-15s)", "Character preparing breakfast.", "Bữa sáng healthy không thể thiếu món này."),
             ("Phần 2 (15-30s)", "Mixing collagen into water/yogurt.", "Pha với nước lọc hoặc sữa chua đều ngon tuyệt cú mèo."),
             ("Phần 3 (30-45s)", "Character enjoying.", "Nạp vitamin xinh đẹp vào người thôi. Mời cả nhà nha!")
        ],
        "60s": [
             ("Phần 1 (0-15s)", "Character talking to camera.", "Hôm nay Moon review chân thật về em Collagen đang hot này nha."),
             ("Phần 2 (15-30s)", "Zoom into texture/color.", "Nước màu hồng ngọc đẹp mắt, bột tan siêu nhanh."),
             ("Phần 3 (30-45s)", "Character drinking.", "Cảm giác uống vào người nó mát, sảng khoái lắm."),
             ("Phần 4 (45-60s)", "Character recommending.", "Chấm 10/10 nha. Chị em nào muốn da đẹp thì chốt đơn lẹ lẹ!")
        ]
    },
    "Hài hước/Trend": {
         "15s": [("Full Video", "Transformation trend with music.", "Biến hình! Từ bà cô già nua thành hot girl da đẹp nhờ Hera nè!")],
         "30s": [
             ("Phần 1 (0-15s)", "Character looks messy/tired.", "Sáng ngủ dậy đầu bù tóc rối, da dẻ sần sùi..."),
             ("Phần 2 (15-30s)", "Character spins -> Glamorous.", "Uống Hera xong biến hình lộng lẫy liền. Phép thuật Winx đó!")
         ],
         "45s": [
             ("Phần 1 (0-15s)", "Character refusing other drinks.", "Trà sữa? No. Nước ngọt? No no."),
             ("Phần 2 (15-30s)", "Character grabs Hera.", "Collagen Hera? Yes yes yes!"),
             ("Phần 3 (30-45s)", "Character dancing happy.", "Chân ái cuộc đời tui là đây. A hi hi đồ ngốc!")
         ],
         "60s": [
             ("Phần 1 (0-15s)", "Character acting dramatic/sad.", "Cuộc đời thật bất công..."),
             ("Phần 2 (15-30s)", "Character reveals why.", "...tại sao mình không biết đến Hera sớm hơn!"),
             ("Phần 3 (30-45s)", "Character drinking greedily.", "Giờ phải uống bù mới được. Ngon quá xá là ngon."),
             ("Phần 4 (45-60s)", "Character laughing.", "Đùa xíu thôi chứ uống đúng liều lượng nha mấy bà. Đẹp từ từ mà chắc!")
        ]
    }
}


# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🌸 MOON'S COLLAGEN CREATOR v2.2 (Full Task)")
st.write("👉 **Tính năng:** Sora Prompt chuẩn chủ đề + Đủ thời lượng + Hiện đầy đủ nhiệm vụ.")

# Sidebar
selected_day = st.selectbox("📅 Hôm nay là thứ mấy?", list(schedule.keys()))
today_task = schedule[selected_day]
video_topic = today_task['video']

# --- ĐÃ SỬA: HIỂN THỊ CẢ BÀI VIẾT VÀ VIDEO ---
st.info(f"Nhiệm vụ: {selected_day} | 📝 Bài viết: {today_task['text']} | 🎬 Video: {video_topic}")
# ---------------------------------------------

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
    
    # 3. SORA PROMPT (LOGIC MỚI - CHUẨN THEO CHỦ ĐỀ)
    st.subheader("🎥 Tạo Video (Sora Clean Feed)")
    
    # Slider chọn tổng thời lượng
    total_duration = st.select_slider("Chọn TỔNG thời lượng video mong muốn:", options=["15s", "30s", "45s", "60s"], value="30s")
    
    # Lấy dữ liệu Sora dựa trên CHỦ ĐỀ HIỆN TẠI (video_topic)
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
        Details: Soft beauty lighting, glowing skin texture.
        --duration 15s
        """
        st.code(sora_prompt, language='text')
        st.caption(f"💡 Thoại gợi ý: '{vn_script}'")
        
        st.divider()
