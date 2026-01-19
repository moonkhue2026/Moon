import streamlit as st

st.set_page_config(page_title="Moon's Fresh Food", page_icon="🥗", layout="wide")

# =========================================================
# 1. DỮ LIỆU DANH MỤC
# =========================================================

categories = {
    "🥤 Smoothie & Detox (Công thức vàng)": [
        "Chanh + Tỏi (Sạch mạch máu - Tim mạch)",
        "Chanh + Gừng (Tiêu hóa tốt)",
        "Chanh + Nha đam (Đẹp da - Mờ thâm)",
        "Chanh + Nghệ (Kháng viêm cực mạnh)",
        "Củ dền + Táo + Cà rốt (Bổ máu - Anemia)",
        "Bơ + Dưa leo + Gừng (Giảm viêm - Inflammation)",
        "Việt quất + Cà chua + Gừng (Tăng đề kháng)",
        "Cam + Táo + Nghệ (Giảm mệt mỏi - Fatigue)",
        "Bưởi + Cà rốt + Gừng (Giảm mỡ máu - Cholesterol)",
        "Kiwi + Xà lách + Gừng (Trị mất ngủ - Insomnia)"
    ],
    "🍎 Trái cây (Fruits)": [
        "Táo", "Cam", "Chuối", "Dưa hấu", "Nho", "Thanh long", "Bơ",
        "Sầu riêng", "Măng cụt", "Vải thiều", "Nhãn", "Xoài", "Dâu tây", "Chanh"
    ],
    "🥦 Rau xanh (Vegetables)": [
        "Cải thìa", "Cà rốt", "Súp lơ", "Khổ qua", "Rau má", "Cà chua", "Khoai tây",
        "Rau ngót", "Bắp cải", "Bí đỏ", "Dưa leo", "Cần tây"
    ],
    "🌶️ Gia vị & Thảo mộc (Spices)": [
        "Gừng", "Nghệ", "Sả", "Tỏi", "Hành tây", "Tiêu", "Ớt",
        "Ngải cứu", "Tía tô", "Lá mơ", "Diếp cá", "Húng quế", "Bạc hà"
    ]
}

# Từ điển dịch nguyên liệu Smoothie sang tiếng Anh cho Prompt
smoothie_map = {
    "Chanh + Tỏi": "Lemon, Garlic cloves and a glass of water",
    "Chanh + Gừng": "Lemon, Ginger slices and tea",
    "Chanh + Nha đam": "Lemon, Aloe Vera slices",
    "Chanh + Nghệ": "Lemon, Turmeric powder",
    "Củ dền + Táo + Cà rốt": "Beetroot, Apple, Carrot and red juice",
    "Bơ + Dưa leo + Gừng": "Avocado, Cucumber, Ginger and green smoothie",
    "Việt quất + Cà chua + Gừng": "Blueberries, Tomato, Ginger and purple smoothie",
    "Cam + Táo + Nghệ": "Orange, Apple, Turmeric and orange juice",
    "Bưởi + Cà rốt + Gừng": "Grapefruit, Carrot, Ginger and orange juice",
    "Kiwi + Xà lách + Gừng": "Kiwi fruit, Lettuce leaves, Ginger and green juice"
}

themes = {
    "Dinh dưỡng & Detox": {
        "tone": "Tươi mới, năng lượng (Fresh & Energetic)",
        "context": "Công thức nước ép, Detox thanh lọc, Vitamin tự nhiên",
        "action_kw": "making juice, drinking fresh smoothie, showing glowing skin"
    },
    "Mẹo vặt nhà bếp": {
        "tone": "Thông minh, hữu ích (Smart & Helpful)",
        "context": "Cách chọn lựa, bảo quản, sơ chế đúng cách",
        "action_kw": "showing kitchen hack, peeling tip, storing in fridge"
    },
    "Món ngon bài thuốc": {
        "tone": "Ấm áp, chữa lành (Healing & Cozy)",
        "context": "Món ăn giải cảm, ấm bụng, tăng đề kháng",
        "action_kw": "cooking soup, smelling aroma, steaming hot food"
    }
}

# =========================================================
# GIAO DIỆN APP
# =========================================================

st.title("🥗 MOON'S FOOD CREATOR (v6.1)")
st.markdown("*Kiến tạo Video Nông sản & Smoothie Triệu View*")

# --- BƯỚC 1: CẤU HÌNH ---
c1, c2 = st.columns(2)
with c1:
    cat_select = st.selectbox("Chọn nhóm:", list(categories.keys()))
    # Tự động chọn chủ đề phù hợp
    default_ix = 0
    if "Smoothie" in cat_select:
        default_ix = 0 # Dinh dưỡng
    elif "Gia vị" in cat_select:
        default_ix = 2 # Món ngon/Thuốc
        
    theme_select = st.selectbox("Chủ đề:", list(themes.keys()), index=default_ix)

with c2:
    char_select = st.selectbox("Chọn nguyên liệu/Công thức:", categories[cat_select])
    
current_theme = themes[theme_select]
item_name = char_select.split('(')[0] # Lấy tên tiếng Việt ngắn gọn

st.divider()

# --- BƯỚC 2: CÀI ĐẶT VIDEO ---
col_v1, col_v2, col_v3 = st.columns(3)
with col_v1:
    style_select = st.radio("Phong cách:", ["3D Animation (Pixar)", "KOL (Người thật)"])
with col_v2:
    model_select = st.radio("AI Model:", ["Sora (15s)", "Veo 3 (8s)"])
with col_v3:
    duration_option = st.select_slider("Thời lượng:", options=["15s", "30s", "45s", "60s"], value="15s")

# =========================================================
# XỬ LÝ LOGIC PROMPT (CHUNKING)
# =========================================================

# 1. Định nghĩa Visual Style & Ingredients
is_smoothie = "Smoothie" in cat_select
ingredients_en = item_name # Mặc định
if is_smoothie:
    # Tìm key tiếng Anh tương ứng
    for key, val in smoothie_map.items():
        if key in item_name:
            ingredients_en = val
            break

if style_select == "3D Animation (Pixar)":
    if is_smoothie:
        subject_prompt = f"a cute anthropomorphic glass of smoothie with {ingredients_en} nearby, Pixar style 3D"
    else:
        subject_prompt = f"a cute anthropomorphic {ingredients_en} character, Pixar style 3D"
    visual_style = "Disney Pixar style, vibrant colors, soft lighting, 8k"
    move = "bouncy animation"
else:
    if is_smoothie:
        subject_prompt = f"a professional Vietnamese nutritionist (KOL), making smoothie with {ingredients_en}"
    else:
        subject_prompt = f"a professional Vietnamese nutritionist (KOL), holding fresh {ingredients_en}"
    visual_style = "Cinematic lighting, photorealistic, Arri Alexa, 8k"
    move = "professional gestures"

t_num = int(duration_option.replace("s", ""))
prompts_list = []

# 2. Tạo Nội dung (Action & Dialogue)
if is_smoothie:
    # --- KỊCH BẢN RIÊNG CHO SMOOTHIE ---
    benefit = char_select.split('(')[-1].replace(')', '') # Lấy công dụng trong ngoặc
    script_sum = f"- HOOK: Gặp vấn đề {benefit}?\n- BODY: Xay {item_name}.\n- CTA: Uống mỗi ngày."
    
    act_15s = f"Start with close up of ingredients ({ingredients_en}). Cut to blender mixing them. Cut to character drinking fresh juice happily. End with thumbs up."
    dia_15s = f"Bạn đang lo lắng về {benefit}? Thử ngay công thức {item_name} này nhé! Vừa ngon, vừa khỏe, lại cực dễ làm. Thử liền nha!"
    
    act_part1 = f"Character looking tired/worried about health. Then points to the ingredients ({ingredients_en}) on the table."
    dia_part1 = f"Dạo này sức khỏe đi xuống, {benefit} làm bạn mệt mỏi? Moon mách bạn công thức vàng này nè."
    
    act_part2 = f"Show the blending process. The juice color is vibrant. Character drinks and smiles."
    dia_part2 = f"Kết hợp {item_name} tạo ra ly nước thần kỳ. Uống vào là thấy khỏe khoắn ngay. Nhớ lưu lại công thức nha!"

elif "Dinh dưỡng" in theme_select:
    # Trái cây đơn lẻ
    script_sum = f"- HOOK: Hỏi 'Muốn da đẹp/dáng thon?'.\n- BODY: Show {item_name}.\n- CTA: Kêu gọi thử ngay."
    act_15s = f"Start with close up of {subject_prompt}. Cut to eating/drinking and glowing. End with thumbs up."
    dia_15s = f"Muốn da đẹp dáng xinh? Ăn ngay {item_name} nhé! Vitamin tự nhiên giúp bạn tỏa sáng mỗi ngày. Thử liền nha!"
    act_part1, dia_part1 = act_15s, dia_15s # (Dùng tạm logic đơn giản cho 30s)
    act_part2, dia_part2 = act_15s, dia_15s

elif "Mẹo vặt" in theme_select:
    script_sum = f"- HOOK: Cảnh báo sai lầm.\n- BODY: Chỉ mẹo {item_name}.\n- CTA: Lưu lại."
    act_15s = f"Start with {subject_prompt} shaking head 'No'. Cut to showing the right way. End with nodding."
    dia_15s = f"Đừng dùng {item_name} sai cách! Để Moon chỉ cho bạn mẹo này. Lưu lại ngay kẻo quên nha!"
    act_part1, dia_part1 = act_15s, dia_15s
    act_part2, dia_part2 = act_15s, dia_15s

else: # Món ngon
    script_sum = f"- HOOK: Thèm thuồng {item_name}.\n- BODY: Nấu ăn.\n- CTA: Xin công thức."
    act_15s = f"Start with smelling delicious aroma of {item_name}. Cut to cooking. End with offering spoon."
    dia_15s = f"Trời lạnh mà có món {item_name} này thì hết sảy! Thơm nức mũi. Ai muốn công thức comment 'Mlem' nha."
    act_part1, dia_part1 = act_15s, dia_15s
    act_part2, dia_part2 = act_15s, dia_15s

# 3. Phân chia Prompt (Gom & Tách)
if t_num == 15:
    prompts_list.append({
        "title": "🎞️ FULL VIDEO (15s) - GOM GỌN",
        "action": act_15s,
        "dialogue": dia_15s
    })

elif t_num == 30:
    prompts_list.append({
        "title": "🎞️ PHẦN 1 (0-15s): Mở đầu",
        "action": f"Part 1 of 2. {act_part1}. {move}.",
        "dialogue": dia_part1
    })
    prompts_list.append({
        "title": "🎞️ PHẦN 2 (15-30s): Kết quả",
        "action": f"Part 2 of 2. {act_part2}. {move}.",
        "dialogue": dia_part2
    })

elif t_num == 45:
    prompts_list.append({"title": "🎞️ PHẦN 1 (0-15s)", "action": f"Intro to topic {item_name}", "dialogue": "Chào cả nhà..."})
    prompts_list.append({"title": "🎞️ PHẦN 2 (15-30s)", "action": "Demonstration/Process", "dialogue": "Bước tiếp theo là..."})
    prompts_list.append({"title": "🎞️ PHẦN 3 (30-45s)", "action": "Result & CTA", "dialogue": "Và đây là kết quả..."})

else: # 60s
    prompts_list.append({"title": "🎞️ PHẦN 1 (0-15s)", "action": "Intro", "dialogue": "Hôm nay Moon chia sẻ..."})
    prompts_list.append({"title": "🎞️ PHẦN 2 (15-30s)", "action": "Process 1", "dialogue": "Đầu tiên là..."})
    prompts_list.append({"title": "🎞️ PHẦN 3 (30-45s)", "action": "Process 2", "dialogue": "Tiếp theo là..."})
    prompts_list.append({"title": "🎞️ PHẦN 4 (45-60s)", "action": "Outro", "dialogue": "Bye bye cả nhà!"})

# =========================================================
# HIỂN THỊ KẾT QUẢ
# =========================================================

# Kịch bản tóm tắt
with st.expander("📜 KỊCH BẢN TÓM TẮT (Tiếng Việt)", expanded=True):
    st.info(script_sum)

st.divider()

# Tabs hiển thị
tab_video, tab_blog = st.tabs(["🎥 VIDEO PROMPT", "📝 BÀI VIẾT FACEBOOK"])

with tab_video:
    st.subheader(f"Prompt tạo video ({model_select})")
    
    for p in prompts_list:
        st.markdown(f"**{p['title']}**")
        
        if "Sora" in model_select:
            # Code Sora (Prompt dài - Có Lip-sync)
            prompt = f"""
            {visual_style}.
            Subject: {subject_prompt}.
            Action: {p['action']}.
            Speaking Line (Vietnamese): "{p['dialogue']}"
            Lip-sync instruction: Match Vietnamese dialogue naturally.
            Context: {current_theme['context']}. Constraint: NO TEXT OVERLAYS.
            --duration 15s
            """
            st.code(prompt, language='text')
            st.caption(f"🗣️ Thoại: \"{p['dialogue']}\"")
        else:
            # Code Veo (Prompt ngắn - 8s)
            prompt = f"""
            Cinematic shot, {subject_prompt}.
            Action: {p['action'].split('.')[0]}. Speaking.
            Atmosphere: {current_theme['tone']}. {visual_style}.
            --duration 8s
            """
            st.code(prompt, language='text')
        
        st.divider()

with tab_blog:
    st.subheader("Copy lệnh cho ChatGPT:")
    st.code(f"""
    Viết bài Facebook chia sẻ công thức: {item_name}.
    - Tone giọng: {current_theme['tone']}.
    - Mục tiêu: {current_theme['context']}.
    - Hashtag: #Smoothie #Detox #{item_name.replace(' + ','').replace(' ','')}
    """, language='text')
