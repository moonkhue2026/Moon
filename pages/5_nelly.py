import streamlit as st
import random

st.set_page_config(page_title="Nelly's Viral Matrix", page_icon="💃", layout="wide")

# =========================================================
# 1. KHO TÀNG Ý TƯỞNG (5 NHÓM VIRAL)
# =========================================================

categories = {
    "💃 Dancing & Trends (Vũ đạo Viral)": [
        "Nhảy Cover Trend TikTok mới nhất",
        "Aerobic đốt mỡ bụng tại nhà",
        "Sexy Dance thần thái (High Heels)",
        "Shuffle Dance cực cuốn",
        "Dance Sport sang trọng (Cha Cha Cha/Rumba)",
        "Biến hình: Từ đồ ngủ sang Đồ nhảy (Transformation)",
        "Nhảy Free-style ngẫu hứng trên phố"
    ],
    "👗 Hack Dáng & Phối Đồ (Styling)": [
        "Hack chân dài cho nấm lùn 1m50",
        "Che bụng mỡ dưới thần thánh",
        "Phối đồ Gym/Sporty đi chơi vẫn sang",
        "Biến đồ công sở nhàm chán thành Sang chảnh",
        "Tips chọn quần Jeans tôn vòng 3",
        "Phối màu đơn sắc (Monochrome) tinh tế"
    ],
    "📸 Tạo Dáng & Thần Thái (Posing)": [
        "3 Dáng đứng chụp ảnh 'kéo chân' ảo diệu",
        "Tạo dáng với gương phòng tập (Gym Mirror)",
        "Cách cười tự nhiên không bị gượng gạo",
        "Xử lý tay khi chụp ảnh (đỡ bị đơ)",
        "Thần thái 'Chị Đại' (Boss Girl Energy)"
    ],
    "💄 Làm Đẹp & Skincare (Beauty)": [
        "Makeup tone Tây đi tiệc/đi quẩy",
        "Tips giữ lớp nền không trôi khi tập Gym",
        "Quy trình dưỡng da Glass Skin buổi tối",
        "Chọn mùi nước hoa 'Bad Girl' quyến rũ",
        "Cách buộc tóc đuôi ngựa (Ponytail) hack tuổi"
    ],
    "🥂 Phong Cách Sống (Lifestyle)": [
        "Xây dựng sự tự tin từ bên trong",
        "Vlog: Một ngày đi tập & làm việc của Nelly",
        "Chế độ ăn Eat Clean giữ dáng",
        "Tư duy phụ nữ hiện đại: Độc lập & Hạnh phúc"
    ]
}

# CAPTION THƯ VIỆN (Tự động nhảy theo chủ đề)
caption_library = {
    "Dancing": [
        "Nhảy xấu không sao, quan trọng là thần thái! 💃🔥",
        "Đốt cháy sàn diễn (và cả mỡ bụng) cùng Nelly! 💦",
        "Nhạc lên là em lên! Ai đu trend này chưa? 🎶",
        "Tập luyện là cách yêu bản thân tốt nhất. Go hard or go home! 💪"
    ],
    "Styling": [
        "Quần áo không làm nên con người, nhưng làm nên thần thái! 😎",
        "Không có phụ nữ lùn, chỉ có phụ nữ chưa biết hack dáng! 👠",
        "Mặc đẹp không phải để ai ngắm, mà là để mình vui! ✨"
    ],
    "Posing": [
        "Đứng im cũng đẹp, mà cười cái là 'đổ' luôn! 📸",
        "Thần thái là thứ không mua được bằng tiền, nhưng luyện tập thì được! 💃",
        "Lưu ngay bí kíp tạo dáng này kẻo xóa video nha mấy bà! 🤫"
    ],
    "Beauty": [
        "Đẹp tự nhiên nhưng không phải tự nhiên mà đẹp! 💄",
        "Mồ hôi là lớp makeup đẹp nhất của cô gái phòng Gym! 💦",
        "Makeup sương sương nhưng sát thương cực lớn! 💋"
    ],
    "Lifestyle": [
        "Sống sang không phải là khoe tiền, mà là biết yêu bản thân. 🥂",
        "Phụ nữ hiện đại: Kiếm tiền giỏi, Sống chất chơi! 👑",
        "Body này được tạo nên từ kỷ luật, không phải may mắn. 🔥"
    ]
}

# MA TRẬN GÓC ĐỘ
pillars = {
    "🔥 1. Biến hình/Kết quả (Transformation)": {"desc": "Show Before/After gây choáng ngợp.", "tone": "Hào hứng, Nhạc Trend", "action_kw": "snapping fingers transition, spinning transformation, glowing up"},
    "🎓 2. Hướng dẫn/Mẹo (Tutorial)": {"desc": "Cầm tay chỉ việc, từng bước một.", "tone": "Chuyên gia, Rõ ràng", "action_kw": "pointing to details, demonstrating step-by-step"},
    "⚠️ 3. Sai lầm/Cảnh báo (Mistakes)": {"desc": "Đánh vào nỗi sợ 'Làm sai'.", "tone": "Nghiêm túc, Drama hóa", "action_kw": "shaking head No, holding STOP sign"},
    "💖 4. Biểu diễn/Vlog (Performance)": {"desc": "Show kỹ năng hoặc kể chuyện.", "tone": "Cuốn hút, Cảm xúc", "action_kw": "performing confidently, smiling at camera, energetic movement"}
}

# =========================================================
# GIAO DIỆN APP
# =========================================================

st.title("💃 NELLY'S VIRAL MATRIX v5.0")
st.markdown("*Chiến thần Viral: Fashion x Dancing x Lifestyle*")

# --- BƯỚC 1: CHỌN CHỦ ĐỀ ---
c1, c2 = st.columns(2)
with c1:
    group_select = st.selectbox("1. Nhóm chủ đề:", list(categories.keys()))
with c2:
    topic_select = st.selectbox("2. Chủ đề cụ thể:", categories[group_select])

# --- BƯỚC 2: CHỌN GÓC ĐỘ ---
st.divider()
c3, c4 = st.columns(2)
with c3:
    pillar_select = st.selectbox("3. Góc quay (Angle):", list(pillars.keys()))
with c4:
    current_pillar = pillars[pillar_select]
    st.info(f"💡 **Cách làm:** {current_pillar['desc']}")

# --- BƯỚC 3: CẤU HÌNH ---
st.divider()
col_v1, col_v2, col_v3 = st.columns(3)
with col_v1:
    style_select = st.radio("Style:", ["KOL (Người thật)", "3D Animation (Mascot)"])
with col_v2:
    model_select = st.radio("AI Model:", ["Sora (15s)", "Veo 3 (8s)"])
with col_v3:
    duration_option = st.select_slider("Thời lượng:", options=["15s", "30s", "45s", "60s"], value="15s")

# =========================================================
# XỬ LÝ LOGIC (GENERATOR)
# =========================================================

# 1. XỬ LÝ VISUAL STYLE (Quan trọng: Đổi style khi chọn Dancing)
is_dancing = "Dancing" in group_select

if style_select == "KOL (Người thật)":
    if is_dancing:
        subject_prompt = "A fit and stunning Vietnamese fashion KOL (Nelly), wearing trendy sporty gym set (crop top & leggings), energetic aura"
        visual_style = "High-energy dance video, TikTok viral style, dynamic camera movement, bright studio lighting, 4k"
        outfit_desc = "Sporty Gym Wear"
    else:
        subject_prompt = "A stunning Vietnamese fashion KOL (Nelly), wearing trendy high-fashion outfit, confident aura"
        visual_style = "High-end fashion commercial, Vogue magazine style, cinematic lighting, 8k"
        outfit_desc = "High Fashion"
else:
    subject_prompt = "A cute 3D fashion doll character (Nelly), Pixar style"
    visual_style = "Disney Pixar style, vibrant colors, 8k"
    outfit_desc = "Cute 3D Outfit"

# 2. CHỌN CAPTION NGẪU NHIÊN
cap_key = "Lifestyle"
if "Dancing" in group_select: cap_key = "Dancing"
elif "Styling" in group_select: cap_key = "Styling"
elif "Posing" in group_select: cap_key = "Posing"
elif "Beauty" in group_select: cap_key = "Beauty"
selected_cap = random.choice(caption_library[cap_key])

# 3. LOGIC KỊCH BẢN (Tùy biến cho Dancing)
t_num = int(duration_option.replace("s", ""))
prompts_list = []

if is_dancing:
    # Kịch bản riêng cho Nhảy
    if "Biến hình" in pillar_select:
        act_15s = f"Start with Nelly wearing pajamas looking tired. Action: Claps hands/Jumps. Cut to: Nelly in {outfit_desc} dancing energetically to the beat. End with a cool ending pose."
        dia_15s = "Lên đồ đi tập thôi nào! Đừng lười biếng nữa. 1.. 2.. 3.. Let's go!"
        script_sum = "- HOOK: Nelly mặc đồ ngủ lôi thôi.\n- BODY: Biến hình sang đồ tập sexy, nhảy cực sung.\n- CTA: Pose dáng thần thái."
    elif "Hướng dẫn" in pillar_select:
        act_15s = f"Start with Nelly showing a difficult dance move fast. Cut to: Nelly doing it slow-motion, breaking down steps 1-2-3. End with doing it fast again perfectly."
        dia_15s = "Trend này nhìn khó vậy thôi chứ dễ lắm. Để Nelly chỉ cho nha. Bước 1... Bước 2... Thấy chưa, thử liền đi!"
        script_sum = "- HOOK: Demo động tác khó.\n- BODY: Hướng dẫn chậm (Slow-mo).\n- CTA: Thách thức khán giả làm theo."
    else: # Biểu diễn
        act_15s = f"Start with close-up of Nelly's confident face. Cut to full body shot performing {topic_select} with high energy and precision. Dynamic camera angles following her moves."
        dia_15s = "(Music playing) Nhảy cùng Nelly nào! Cảm nhận nhịp điệu và tỏa sáng nhé!"
        script_sum = "- HOOK: Thần thái cuốn hút.\n- BODY: Full bài nhảy sôi động, góc quay đẹp.\n- CTA: Kêu gọi duet."
else:
    # Kịch bản cho Fashion/Beauty (Giữ nguyên logic cũ)
    if "Biến hình" in pillar_select:
        act_15s = f"Start with {subject_prompt} looking messy. Snaps fingers. Cut to {subject_prompt} looking perfect. End with winking."
        dia_15s = f"Biến hình cùng Nelly nha! {topic_select} chưa bao giờ dễ đến thế."
        script_sum = "- HOOK: Before xuề xòa.\n- BODY: Biến hình After sang chảnh.\n- CTA: Thả tim."
    else:
        act_15s = f"Start with {subject_prompt} talking to camera. Cut to demonstrating {topic_select}. End with happy result."
        dia_15s = f"Hôm nay Nelly chia sẻ về {topic_select}. Mọi người lưu lại ngay nhé!"
        script_sum = f"- HOOK: Giới thiệu {topic_select}.\n- BODY: Nội dung chính.\n- CTA: Kêu gọi share."

# Logic Chia Prompt (Chunking)
if t_num == 15:
    prompts_list.append({"title": "🎞️ FULL VIDEO (15s) - GOM GỌN", "action": act_15s, "dialogue": dia_15s})
elif t_num == 30:
    prompts_list.append({"title": "🎞️ PHẦN 1 (0-15s)", "action": f"Part 1. {act_15s.split('.')[0]}...", "dialogue": f"{dia_15s.split('.')[0]}..."})
    prompts_list.append({"title": "🎞️ PHẦN 2 (15-30s)", "action": f"Part 2. {act_15s.split('.')[-1]}...", "dialogue": f"...{dia_15s.split('.')[-1]}"})

# =========================================================
# HIỂN THỊ KẾT QUẢ
# =========================================================

with st.expander("📜 KỊCH BẢN TÓM TẮT (Tiếng Việt)", expanded=True):
    st.info(script_sum)

st.divider()

tab_video, tab_blog = st.tabs(["🎥 VIDEO & CAPTION", "📝 BÀI VIẾT & ẢNH BLOG"])

# TAB 1: VIDEO + CAPTION (Dễ Copy)
with tab_video:
    st.subheader("🤣 Caption TikTok/Reels (Copy ngay):")
    caption_text = f"""{selected_cap}

#Nelly{cap_key} #{topic_select.replace(' ','')} #Trending"""
    st.code(caption_text, language="text")
    
    st.divider()
    
    st.subheader(f"Prompt tạo video ({model_select})")
    for p in prompts_list:
        st.markdown(f"**{p['title']}**")
        if "Sora" in model_select:
            prompt = f"""
            {visual_style}. Subject: {subject_prompt}.
            Action: {p['action']}. {current_pillar['action_kw']}.
            Speaking Line (Vietnamese): "{p['dialogue']}"
            Lip-sync instruction: Match naturally. Context: {topic_select}. Constraint: NO TEXT. --duration 15s
            """
            st.code(prompt, language='text')
            st.caption(f"🗣️ Thoại: \"{p['dialogue']}\"")
        else:
            prompt = f"""
            Cinematic shot, {subject_prompt}.
            Action: {p['action'].split('.')[0]}. Speaking.
            Atmosphere: {current_pillar['tone']}. {visual_style}.
            --duration 8s
            """
            st.code(prompt, language='text')
        st.divider()

# TAB 2: BÀI VIẾT + ẢNH (Chia đôi cột)
with tab_blog:
    c_blog, c_img = st.columns(2)
    with c_blog:
        st.subheader("1. Prompt viết bài (ChatGPT):")
        st.code(f"""
        Viết bài Facebook/TikTok về: {topic_select}.
        - Phong cách: {outfit_desc} (Năng động/Sang trọng).
        - Góc độ: {pillar_select}.
        - Tone giọng: {current_pillar['tone']}.
        - Hashtag: #{topic_select.replace(' ','')} #NellyTeam
        """, language='text')
    with c_img:
        st.subheader("2. Prompt ảnh bìa (Midjourney):")
        # Prompt ảnh cũng đổi style theo chủ đề
        mj_vibe = "dynamic dance studio, neon lights, energetic atmosphere" if is_dancing else "luxury city street, golden hour, vogue style"
        mj_outfit = "trendy gym wear" if is_dancing else "high fashion outfit"
        
        mj_prompt = f"/imagine prompt: A stunning photography shot of Nelly (Vietnamese beauty), wearing {mj_outfit}, posing confidently in {mj_vibe}. Cinematic depth of field, 8k --ar 3:4"
        st.code(mj_prompt, language='text')
