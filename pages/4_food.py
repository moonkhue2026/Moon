import streamlit as st

st.set_page_config(page_title="Moon's Fresh Food", page_icon="🥗", layout="wide")

# =========================================================
# 1. DỮ LIỆU
# =========================================================

categories = {
    "🍎 Trái cây (Fruits)": [
        "Táo", "Cam", "Chuối", "Dưa hấu", "Nho", "Thanh long", "Bơ",
        "Sầu riêng", "Măng cụt", "Vải thiều", "Nhãn", "Xoài", "Dâu tây"
    ],
    "🥦 Rau xanh (Vegetables)": [
        "Cải thìa", "Cà rốt", "Súp lơ", "Khổ qua", "Rau má", "Cà chua", "Khoai tây",
        "Rau ngót", "Bắp cải", "Bí đỏ", "Dưa leo"
    ],
    "🌶️ Gia vị & Thảo mộc (Spices)": [
        "Gừng", "Nghệ", "Sả", "Tỏi", "Hành tây", "Tiêu", "Ớt",
        "Ngải cứu", "Tía tô", "Lá mơ", "Diếp cá", "Húng quế"
    ]
}

themes = {
    "Dinh dưỡng & Vitamin": {
        "tone": "Tươi vui, năng động",
        "context": "Cung cấp vitamin, khoáng chất, năng lượng cho ngày mới",
        "action_base": "holding the item happily, eating/drinking, glowing with energy"
    },
    "Mẹo vặt nhà bếp": {
        "tone": "Thủ thỉ, mách nhỏ (Life Hacks)",
        "context": "Cách chọn lựa ngon, cách bảo quản, sơ chế đúng cách",
        "action_base": "showing a kitchen trick, selecting the item carefully, pointing finger up"
    },
    "Món ngon bài thuốc": {
        "tone": "Ấm áp, chăm sóc (Healing)",
        "context": "Món ăn giúp giải cảm, ấm bụng, tăng đề kháng",
        "action_base": "cooking in a cozy kitchen, smelling the aroma, offering a bowl"
    }
}

# =========================================================
# GIAO DIỆN APP
# =========================================================

st.title("🥗 MOON'S FOOD CREATOR (v6.0)")

# --- BƯỚC 1: CẤU HÌNH ---
c1, c2 = st.columns(2)
with c1:
    cat_select = st.selectbox("Chọn nhóm:", list(categories.keys()))
with c2:
    char_select = st.selectbox("Chọn nhân vật:", categories[cat_select])
    
theme_select = st.selectbox("Chủ đề:", list(themes.keys()))
current_theme = themes[theme_select]

st.divider()

# --- BƯỚC 2: CÀI ĐẶT VIDEO ---
col_v1, col_v2, col_v3 = st.columns(3)
with col_v1:
    style_select = st.radio("Style:", ["3D Animation (Pixar)", "KOL (Người thật)"])
with col_v2:
    model_select = st.radio("AI Model:", ["Sora (15s)", "Veo 3 (8s)"])
with col_v3:
    duration_option = st.select_slider("Thời lượng:", options=["15s", "30s", "45s", "60s"], value="15s")

# =========================================================
# XỬ LÝ LOGIC PROMPT (CHUNKING)
# =========================================================

# 1. Định nghĩa Style
if style_select == "3D Animation (Pixar)":
    subject_prompt = f"a cute anthropomorphic {char_select.split('(')[0]} character, Pixar style 3D"
    visual_style = "Disney Pixar style, vibrant colors, soft lighting, 8k"
    move = "bouncy animation"
else:
    subject_prompt = f"a professional Vietnamese nutritionist (KOL), holding fresh {char_select.split('(')[0]}"
    visual_style = "Cinematic lighting, photorealistic, Arri Alexa, 8k"
    move = "professional gestures"

t_num = int(duration_option.replace("s", ""))
prompts_list = []
item_name = char_select.split('(')[0]

# 2. Tạo Kịch bản & Action (Gốc)
if "Dinh dưỡng" in theme_select:
    script_sum = "- HOOK: Hỏi 'Biết gì chưa?'.\n- BODY: Nêu lợi ích Vitamin.\n- CTA: Kêu gọi ăn mỗi ngày."
    act_15s = f"Start with close up of {subject_prompt} looking surprised. Cut to character eating {item_name} and glowing. End with thumbs up."
    dia_15s = f"Biết gì chưa? {item_name} là vua vitamin đó! Ăn mỗi ngày giúp da đẹp dáng xinh. Thử ngay hôm nay nhé!"

elif "Mẹo vặt" in theme_select:
    script_sum = "- HOOK: Cảnh báo/Thách thức.\n- BODY: Chỉ mẹo chọn/bảo quản.\n- CTA: Lưu lại ngay."
    act_15s = f"Start with {subject_prompt} holding {item_name} looking confused. Cut to character showing how to check freshness/peel it. End with nodding wisely."
    dia_15s = f"Đừng chọn {item_name} bừa bãi nha! Để Moon chỉ cho cách chọn quả ngon nhất. Lưu lại mẹo này ngay kẻo quên!"

else: # Món ngon
    script_sum = "- HOOK: Thèm thuồng/Mời gọi.\n- BODY: Cảnh nấu nướng hấp dẫn.\n- CTA: Xin công thức."
    act_15s = f"Start with {subject_prompt} smelling delicious aroma. Cut to cooking {item_name} in a pot. End with offering a spoon to camera."
    dia_15s = f"Trời lạnh thế này mà có món {item_name} thì hết sảy! Thơm nức mũi luôn. Ai muốn công thức thì comment Mlem nha."

# 3. Phân chia Prompt theo Thời lượng
if t_num == 15:
    prompts_list.append({
        "title": "🎞️ FULL VIDEO (15s)",
        "action": act_15s,
        "dialogue": dia_15s
    })

elif t_num == 30:
    prompts_list.append({
        "title": "🎞️ PHẦN 1 (0-15s): Mở đầu",
        "action": f"Part 1 of 2. {act_15s.split('.')[0]}. Character introduces the topic about {item_name}.",
        "dialogue": f"Hôm nay Moon sẽ bật mí một bí mật về {item_name} mà ít ai biết..."
    })
    prompts_list.append({
        "title": "🎞️ PHẦN 2 (15-30s): Nội dung & Kết",
        "action": f"Part 2 of 2. {act_15s.split('.')[-1]}. Character demonstrates and shows result.",
        "dialogue": f"Đó, chỉ cần làm như vậy thôi. Đơn giản mà hiệu quả cực kỳ. Nhớ follow Moon nha!"
    })

elif t_num == 45:
    prompts_list.append({"title": "🎞️ PHẦN 1 (0-15s)", "action": f"Intro to {item_name}", "dialogue": "Hello cả nhà..."})
    prompts_list.append({"title": "🎞️ PHẦN 2 (15-30s)", "action": "Demonstration/Cooking process", "dialogue": "Bước quan trọng nhất là..."})
    prompts_list.append({"title": "🎞️ PHẦN 3 (30-45s)", "action": "Result & CTA", "dialogue": "Và đây là kết quả..."})

else: # 60s
    prompts_list.append({"title": "🎞️ PHẦN 1 (0-15s)", "action": "Vlog intro", "dialogue": "Hôm nay đi chợ cùng Moon..."})
    prompts_list.append({"title": "🎞️ PHẦN 2 (15-30s)", "action": "Main activity", "dialogue": "Đầu tiên chúng ta cần..."})
    prompts_list.append({"title": "🎞️ PHẦN 3 (30-45s)", "action": "Detailed tip", "dialogue": "Lưu ý nhỏ là..."})
    prompts_list.append({"title": "🎞️ PHẦN 4 (45-60s)", "action": "Outro", "dialogue": "Chúc cả nhà thành công!"})

# =========================================================
# HIỂN THỊ KẾT QUẢ
# =========================================================

with st.expander("📜 KỊCH BẢN TÓM TẮT (Tiếng Việt)", expanded=True):
    st.info(script_sum)

tab_video, tab_blog = st.tabs(["🎥 VIDEO PROMPT", "📝 BÀI VIẾT FACEBOOK"])

with tab_video:
    st.subheader(f"Prompt tạo video ({model_select})")
    for p in prompts_list:
        st.markdown(f"**{p['title']}**")
        
        if "Sora" in model_select:
            # Code Sora (Gộp)
            prompt = f"""
            {visual_style}.
            Subject: {subject_prompt}.
            Action: {p['action']}. {move}.
            Speaking Line (Vietnamese): "{p['dialogue']}"
            Lip-sync instruction: Match Vietnamese dialogue naturally.
            Context: {current_theme['context']}. Constraint: NO TEXT OVERLAYS.
            --duration 15s
            """
            st.code(prompt, language='text')
            st.caption(f"🗣️ Thoại: \"{p['dialogue']}\"")
        else:
            # Code Veo (8s)
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
    Viết bài Facebook về lợi ích của {char_select}. 
    Tone: {current_theme['tone']}. 
    Hashtag: #DinhDuong #SongKhoe #{item_name.replace(' ','')}
    """, language='text')
