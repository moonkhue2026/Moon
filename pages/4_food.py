import streamlit as st
import random

st.set_page_config(page_title="Moon's Fresh Food", page_icon="🥗", layout="wide")

# =========================================================
# 1. DỮ LIỆU & LOGIC CAPTION HÀI HƯỚC
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

# Dịch & Data phụ trợ
smoothie_map = {
    "Chanh + Tỏi": {"en": "Lemon and Garlic", "cap": "Uống xong người yêu chạy mất dép nhưng tim mạch thì khỏe re! 🤣"},
    "Chanh + Gừng": {"en": "Lemon and Ginger", "cap": "Ấm bụng hơn cả người yêu cũ nhắn tin quay lại! 🔥"},
    "Chanh + Nha đam": {"en": "Lemon and Aloe Vera", "cap": "Da đẹp thế này thì ai chơi lại? 💅"},
    "Chanh + Nghệ": {"en": "Lemon and Turmeric", "cap": "Vàng da là do nghệ, chứ không phải do 'nghệ' sĩ đâu nha! 😜"},
    "Chanh + Mật ong": {"en": "Lemon and Honey", "cap": "Ngọt ngào đến mấy cũng tan thành... ly nước này thôi! 🍯"},
    "Trà chanh nóng": {"en": "Hot Tea with Lemon", "cap": "Chill một chút thì có sao, miễn là khỏe! ☕"},
    "Củ dền + Táo + Cà rốt": {"en": "Beetroot, Apple, Carrot", "cap": "Máu lên não nhanh hơn cả tốc độ lương về! 🚀"},
    "Bơ + Dưa leo + Gừng": {"en": "Avocado, Cucumber, Ginger", "cap": "Xanh mượt mà như tình yêu đầu đời! 💚"},
    "Việt quất + Cà chua + Gừng": {"en": "Blueberries, Tomato, Ginger", "cap": "Tăng đề kháng để còn 'chiến' với deadline! 💪"},
    "Cam + Táo + Nghệ": {"en": "Orange, Apple, Turmeric", "cap": "Hết mệt mỏi, chỉ còn 'mệt' vì quá xinh! 😎"},
    "Bưởi + Cà rốt + Gừng": {"en": "Grapefruit, Carrot, Ginger", "cap": "Mỡ đi nhé, đừng quay lại nữa! 👋"},
    "Kiwi + Xà lách + Gừng": {"en": "Kiwi, Lettuce, Ginger", "cap": "Uống xong ngủ ngon hơn cả lúc họp! 😴"}
}

# Ma trận 4 góc độ
pillars = {
    "🥣 1. Hướng dẫn (How-to/ASMR)": {"focus": "Tập trung vào âm thanh, hình ảnh ngon mắt, quy trình làm.", "tone": "Thư giãn, ngon miệng", "action_kw": "chopping, blending, pouring, ASMR style"},
    "🎓 2. Kiến thức (Education)": {"focus": "Giải thích tại sao công thức này tốt (Phân tích thành phần).", "tone": "Chuyên gia, tin cậy", "action_kw": "pointing to ingredients, showing health chart, nodding"},
    "⚠️ 3. Cảnh báo (Warning)": {"focus": "Những sai lầm khi uống (Uống giờ nào? Ai không nên uống?).", "tone": "Nghiêm túc, cảnh báo", "action_kw": "shaking head No, holding STOP sign, showing clock"},
    "💖 4. Câu chuyện (Story/Vlog)": {"focus": "Kể về trải nghiệm thực tế/Kết quả sau khi uống.", "tone": "Gần gũi, tâm tình", "action_kw": "talking to camera, drinking and smiling, showing before/after"}
}

# =========================================================
# GIAO DIỆN APP
# =========================================================

st.title("🥗 MOON'S FOOD MATRIX v7.1")
st.markdown("*Thêm: Ảnh minh họa Blog & Caption hài hước*")

# --- BƯỚC 1 & 2: CHỌN NGUYÊN LIỆU & GÓC ĐỘ ---
c1, c2, c3 = st.columns(3)
with c1: cat_select = st.selectbox("1. Chọn nhóm:", list(categories.keys()))
with c2: char_select = st.selectbox("2. Nguyên liệu/Công thức:", categories[cat_select])
with c3: pillar_select = st.selectbox("3. Góc độ Video:", list(pillars.keys()))

# Xử lý dữ liệu
item_name = char_select.split('(')[0]
benefit = char_select.split('(')[-1].replace(')', '') if '(' in char_select else "sức khỏe"
current_pillar = pillars[pillar_select]

# Lấy tên tiếng Anh và Caption hài
ingredients_en = item_name
funny_cap = f"Ai rồi cũng phải mê món {item_name} này thôi! 😋" # Mặc định
if "Smoothie" in cat_select:
    for key, val in smoothie_map.items():
        if key in item_name:
            ingredients_en = val["en"]
            funny_cap = val["cap"]
            break

# --- BƯỚC 3: CẤU HÌNH ---
st.divider()
col_v1, col_v2, col_v3 = st.columns(3)
with col_v1: style_select = st.radio("Style:", ["3D Animation (Pixar)", "KOL (Người thật)"])
with col_v2: model_select = st.radio("AI Model:", ["Sora (15s)", "Veo 3 (8s)"])
with col_v3: duration_option = st.select_slider("Thời lượng:", options=["15s", "30s", "45s", "60s"], value="15s")

# =========================================================
# XỬ LÝ LOGIC PROMPT (VISUAL & SCRIPT)
# =========================================================
# ... (Giữ nguyên logic Visual Style & Kịch bản như v7.0) ...
if style_select == "3D Animation (Pixar)":
    subject_prompt = f"a cute anthropomorphic {ingredients_en.split(',')[0]} character, Pixar style 3D"
    visual_style = "Disney Pixar style, vibrant colors, soft lighting, 8k"
else:
    subject_prompt = f"a professional Vietnamese nutritionist (KOL) with {ingredients_en}"
    visual_style = "Cinematic lighting, photorealistic, Arri Alexa, 8k"

t_num = int(duration_option.replace("s", ""))
prompts_list = []

# (Logic Kịch bản rút gọn để tiết kiệm chỗ - Vẫn hoạt động như v7.0)
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

# (Logic Chia Prompt rút gọn - Vẫn hoạt động như v7.0)
if t_num == 15: prompts_list.append({"title": "🎞️ FULL VIDEO (15s) - GOM GỌN", "action": act_15s, "dialogue": dia_15s})
elif t_num == 30:
    prompts_list.append({"title": "🎞️ PHẦN 1 (0-15s): Mở đầu", "action": f"Part 1 of 2. {act_15s.split('.')[0]}...", "dialogue": f"{dia_15s.split('.')[0]}..."})
    prompts_list.append({"title": "🎞️ PHẦN 2 (15-30s): Kết thúc", "action": f"Part 2 of 2. {act_15s.split('.')[-1]}...", "dialogue": f"...{dia_15s.split('.')[-1]}"})
# ... (Tương tự cho 45s, 60s)

# =========================================================
# HIỂN THỊ KẾT QUẢ (ĐÃ NÂNG CẤP)
# =========================================================

with st.expander("📜 KỊCH BẢN TÓM TẮT (Tiếng Việt)", expanded=True):
    st.info(script_sum)

st.divider()

tab_video, tab_blog = st.tabs(["🎥 VIDEO & CAPTION", "📝 BÀI VIẾT & ẢNH BLOG"])

# --- TAB 1: VIDEO + CAPTION HÀI ---
with tab_video:
    # 1. Hiển thị Caption Hài hước trước
    st.success(f"🤣 **Gợi ý Caption (Copy đăng TikTok/Reels):**\n\n>>> {funny_cap} <<< \n\n#SongKhoeCungMoon #{item_name.replace(' + ','').replace(' ','')}")
    
    st.divider()
    
    # 2. Hiển thị Prompt Video
    st.subheader(f"Prompt tạo video ({model_select})")
    for p in prompts_list:
        st.markdown(f"**{p['title']}**")
        if "Sora" in model_select:
            prompt = f"""
            {visual_style}. Subject: {subject_prompt}.
            Action: {p['action']}. {current_pillar['action_kw']}.
            Speaking Line (Vietnamese): "{p['dialogue']}"
            Lip-sync instruction: Match naturally. Context: {current_pillar['focus']}. Constraint: NO TEXT. --duration 15s
            """
            st.code(prompt, language='text')
            st.caption(f"🗣️ Thoại: \"{p['dialogue']}\"")
        else:
            # ... (Code Veo giữ nguyên)
            pass
        st.divider()

# --- TAB 2: BÀI VIẾT + ẢNH MINH HỌA ---
with tab_blog:
    c_blog, c_img = st.columns(2)
    
    with c_blog:
        st.subheader("1. Prompt viết bài (Cho ChatGPT):")
        st.code(f"""
        Viết bài Facebook về: {item_name}.
        - Góc độ khai thác: {pillar_select} ({current_pillar['focus']}).
        - Tone giọng: {current_pillar['tone']}.
        - Hashtag: #{item_name.replace(' + ','').replace(' ','')} #SongKhoe
        """, language='text')
        
    with c_img:
        st.subheader("2. Prompt ảnh minh họa (Cho Midjourney):")
        mj_prompt = f"/imagine prompt: A vibrant, appetizing photograph of {ingredients_en} arranged beautifully on a rustic wooden table, natural morning light, fresh ingredients, cinematic depth of field. {current_pillar['tone']} atmosphere. 8k --ar 16:9"
        st.code(mj_prompt, language='text')
        st.caption("👉 Copy dòng này vào Midjourney để tạo ảnh cover đẹp cho bài viết.")
