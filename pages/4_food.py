import streamlit as st

st.set_page_config(page_title="Moon's Fresh Food", page_icon="🥗", layout="wide")

# =========================================================
# 1. DỮ LIỆU: 12 CÔNG THỨC VÀNG
# =========================================================

categories = {
    "🥤 Smoothie & Detox (12 Công thức vàng)": [
        "1. Chanh + Tỏi (Sạch mạch máu)",
        "2. Chanh + Gừng (Tiêu hóa tốt)",
        "3. Chanh + Nha đam (Đẹp da)",
        "4. Chanh + Nghệ (Kháng viêm)",
        "5. Chanh + Mật ong (Tăng đề kháng)",
        "6. Trà chanh nóng (Thanh lọc)",
        "7. Củ dền + Táo + Cà rốt (Bổ máu)",
        "8. Bơ + Dưa leo + Gừng (Giảm viêm)",
        "9. Việt quất + Cà chua + Gừng (Tăng miễn dịch)",
        "10. Cam + Táo + Nghệ (Giảm mệt mỏi)",
        "11. Bưởi + Cà rốt + Gừng (Giảm mỡ máu)",
        "12. Kiwi + Xà lách + Gừng (Trị mất ngủ)"
    ],
    "🍎 Trái cây (Fruits)": [
        "Táo", "Cam", "Chuối", "Dưa hấu", "Nho", "Thanh long", "Bơ",
        "Sầu riêng", "Măng cụt", "Vải thiều", "Nhãn", "Xoài", "Dâu tây", "Chanh"
    ],
    "🥦 Rau xanh (Vegetables)": [
        "Cải thìa", "Cà rốt", "Súp lơ", "Khổ qua", "Rau má", "Cà chua", "Khoai tây",
        "Rau ngót", "Bắp cải", "Bí đỏ", "Dưa leo", "Cần tây"
    ]
}

# Dịch nguyên liệu sang tiếng Anh
smoothie_map = {
    "Chanh + Tỏi": "Lemon and Garlic",
    "Chanh + Gừng": "Lemon and Ginger",
    "Chanh + Nha đam": "Lemon and Aloe Vera",
    "Chanh + Nghệ": "Lemon and Turmeric",
    "Chanh + Mật ong": "Lemon and Honey",
    "Trà chanh nóng": "Hot Tea with Lemon",
    "Củ dền + Táo + Cà rốt": "Beetroot, Apple, Carrot",
    "Bơ + Dưa leo + Gừng": "Avocado, Cucumber, Ginger",
    "Việt quất + Cà chua + Gừng": "Blueberries, Tomato, Ginger",
    "Cam + Táo + Nghệ": "Orange, Apple, Turmeric",
    "Bưởi + Cà rốt + Gừng": "Grapefruit, Carrot, Ginger",
    "Kiwi + Xà lách + Gừng": "Kiwi, Lettuce, Ginger"
}

# =========================================================
# 2. MA TRẬN 4 GÓC ĐỘ (PILLARS)
# =========================================================

pillars = {
    "🥣 1. Hướng dẫn (How-to/ASMR)": {
        "focus": "Tập trung vào âm thanh, hình ảnh ngon mắt, quy trình làm.",
        "tone": "Thư giãn, ngon miệng (Chill & Tasty)",
        "action_kw": "chopping, blending, pouring, ASMR style"
    },
    "🎓 2. Kiến thức (Education)": {
        "focus": "Giải thích tại sao công thức này tốt (Phân tích thành phần).",
        "tone": "Chuyên gia, tin cậy (Expert & Trust)",
        "action_kw": "pointing to ingredients, showing health chart, nodding"
    },
    "⚠️ 3. Cảnh báo (Warning)": {
        "focus": "Những sai lầm khi uống (Uống giờ nào? Ai không nên uống?).",
        "tone": "Nghiêm túc, cảnh báo (Serious & Alert)",
        "action_kw": "shaking head No, holding STOP sign, showing clock"
    },
    "💖 4. Câu chuyện (Story/Vlog)": {
        "focus": "Kể về trải nghiệm thực tế/Kết quả sau khi uống.",
        "tone": "Gần gũi, tâm tình (Emotional & Personal)",
        "action_kw": "talking to camera, drinking and smiling, showing before/after"
    }
}

# =========================================================
# GIAO DIỆN APP
# =========================================================

st.title("🥗 MOON'S FOOD MATRIX (v7.0)")
st.markdown("*12 Công thức x 4 Góc độ = Không bao giờ cạn ý tưởng*")

# --- BƯỚC 1: CHỌN NGUYÊN LIỆU ---
c1, c2 = st.columns(2)
with c1:
    cat_select = st.selectbox("Chọn nhóm:", list(categories.keys()))
with c2:
    char_select = st.selectbox("Chọn nguyên liệu/Công thức:", categories[cat_select])

item_name = char_select.split('(')[0]
ingredients_en = item_name
# Map tiếng Anh nếu là Smoothie
for key, val in smoothie_map.items():
    if key in item_name:
        ingredients_en = val
        break

# --- BƯỚC 2: CHỌN GÓC KHAI THÁC ---
st.divider()
c3, c4 = st.columns(2)
with c3:
    pillar_select = st.selectbox("Chọn Góc độ Video:", list(pillars.keys()))
with c4:
    current_pillar = pillars[pillar_select]
    st.info(f"💡 **Trọng tâm:** {current_pillar['focus']}")

# --- BƯỚC 3: CẤU HÌNH ---
st.divider()
col_v1, col_v2, col_v3 = st.columns(3)
with col_v1:
    style_select = st.radio("Style:", ["3D Animation (Pixar)", "KOL (Người thật)"])
with col_v2:
    model_select = st.radio("AI Model:", ["Sora (15s)", "Veo 3 (8s)"])
with col_v3:
    duration_option = st.select_slider("Thời lượng:", options=["15s", "30s", "45s", "60s"], value="15s")

# =========================================================
# XỬ LÝ LOGIC PROMPT (MATRIX + CHUNKING)
# =========================================================

# Style Visual
if style_select == "3D Animation (Pixar)":
    subject_prompt = f"a cute anthropomorphic {ingredients_en.split(',')[0]} character, Pixar style 3D"
    visual_style = "Disney Pixar style, vibrant colors, soft lighting, 8k"
else:
    subject_prompt = f"a professional Vietnamese nutritionist (KOL) with {ingredients_en}"
    visual_style = "Cinematic lighting, photorealistic, Arri Alexa, 8k"

t_num = int(duration_option.replace("s", ""))
prompts_list = []
benefit = char_select.split('(')[-1].replace(')', '') if '(' in char_select else "sức khỏe"

# --- LOGIC KỊCH BẢN THEO GÓC ĐỘ (PILLARS) ---

if "Hướng dẫn" in pillar_select:
    script_sum = f"- HOOK: Cận cảnh ly {item_name} hấp dẫn.\n- BODY: Quy trình xay/ép (ASMR).\n- CTA: Mời gọi làm thử."
    act_15s = f"Start with close up of fresh {ingredients_en}. Cut to blender mixing vibrant colors. Cut to pouring into glass. End with offering to camera."
    dia_15s = f"Cùng Moon làm ly {item_name} siêu ngon này nhé! Chỉ 3 bước đơn giản là có ngay 'thần dược' {benefit}. Thử ngay nào!"

elif "Kiến thức" in pillar_select:
    script_sum = f"- HOOK: Tại sao {item_name} tốt cho {benefit}?\n- BODY: Phân tích vitamin/dưỡng chất.\n- CTA: Lưu kiến thức."
    act_15s = f"Start with {subject_prompt} pointing to a floating health chart. Cut to showing {ingredients_en} glowing. End with nodding wisely."
    dia_15s = f"Tại sao {item_name} lại là khắc tinh của {benefit}? Vì trong này chứa lượng lớn hoạt chất quý. Nghe Moon giải thích nhé!"

elif "Cảnh báo" in pillar_select:
    script_sum = f"- HOOK: Dừng lại! Đừng uống {item_name} sai cách.\n- BODY: Chỉ ra sai lầm (ví dụ uống đói).\n- CTA: Dặn dò kỹ."
    act_15s = f"Start with {subject_prompt} holding a STOP sign looking serious. Cut to showing a clock or 'X' mark. End with finger pointing up warningly."
    dia_15s = f"Cảnh báo! Tuyệt đối không uống {item_name} vào thời điểm này nếu không muốn hại dạ dày. Xem hết video để tránh nhé!"

else: # Câu chuyện
    script_sum = f"- HOOK: Moon từng khổ sở vì {benefit}...\n- BODY: Hành trình thay đổi nhờ {item_name}.\n- CTA: Truyền cảm hứng."
    act_15s = f"Start with {subject_prompt} looking sad/tired. Cut to drinking {item_name} everyday. Cut to happy glowing face. End with heart hands."
    dia_15s = f"Trước đây Moon khổ sở vì {benefit} lắm. Nhưng từ khi biết đến {item_name}, mọi thứ thay đổi hẳn. Kiên trì 1 tuần là thấy khác liền!"

# --- LOGIC CHIA PROMPT (GOM & TÁCH) ---

if t_num == 15:
    prompts_list.append({
        "title": "🎞️ FULL VIDEO (15s) - GOM GỌN",
        "action": act_15s,
        "dialogue": dia_15s
    })

elif t_num == 30:
    prompts_list.append({
        "title": "🎞️ PHẦN 1 (0-15s): Mở đầu",
        "action": f"Part 1 of 2. {act_15s.split('.')[0]}. Character introduces the topic.",
        "dialogue": f"{dia_15s.split('.')[0]}..."
    })
    prompts_list.append({
        "title": "🎞️ PHẦN 2 (15-30s): Kết thúc",
        "action": f"Part 2 of 2. {act_15s.split('.')[-1]}. Character concludes.",
        "dialogue": f"...{dia_15s.split('.')[-1]}"
    })

elif t_num == 45:
    prompts_list.append({"title": "🎞️ PHẦN 1 (0-15s)", "action": "Intro", "dialogue": "Chào cả nhà..."})
    prompts_list.append({"title": "🎞️ PHẦN 2 (15-30s)", "action": "Content", "dialogue": "Nội dung chính..."})
    prompts_list.append({"title": "🎞️ PHẦN 3 (30-45s)", "action": "Outro", "dialogue": "Kết quả..."})

else: # 60s
    prompts_list.append({"title": "🎞️ PHẦN 1", "action": "Intro", "dialogue": "..."})
    prompts_list.append({"title": "🎞️ PHẦN 2", "action": "Body 1", "dialogue": "..."})
    prompts_list.append({"title": "🎞️ PHẦN 3", "action": "Body 2", "dialogue": "..."})
    prompts_list.append({"title": "🎞️ PHẦN 4", "action": "Outro", "dialogue": "..."})

# =========================================================
# HIỂN THỊ KẾT QUẢ
# =========================================================

with st.expander("📜 KỊCH BẢN TÓM TẮT (Tiếng Việt)", expanded=True):
    st.info(script_sum)

st.divider()

tab_video, tab_blog = st.tabs(["🎥 VIDEO PROMPT", "📝 BÀI VIẾT FACEBOOK"])

with tab_video:
    st.subheader(f"Prompt tạo video ({model_select})")
    for p in prompts_list:
        st.markdown(f"**{p['title']}**")
        
        if "Sora" in model_select:
            prompt = f"""
            {visual_style}.
            Subject: {subject_prompt}.
            Action: {p['action']}. {current_pillar['action_kw']}.
            Speaking Line (Vietnamese): "{p['dialogue']}"
            Lip-sync instruction: Match Vietnamese dialogue naturally.
            Context: {current_pillar['focus']}. Constraint: NO TEXT OVERLAYS.
            --duration 15s
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

with tab_blog:
    st.subheader("Copy lệnh cho ChatGPT:")
    st.code(f"""
    Viết bài Facebook về: {item_name}.
    - Góc độ khai thác: {pillar_select}.
    - Tone giọng: {current_pillar['tone']}.
    - Hashtag: #{item_name.replace(' + ','').replace(' ','')} #SongKhoe
    """, language='text')
