import streamlit as st
import random

st.set_page_config(page_title="Nelly's Fashion Matrix", page_icon="👠", layout="wide")

# =========================================================
# 1. KHO TÀNG Ý TƯỞNG & CAPTION VIRAL
# =========================================================

categories = {
    "👗 Hack Dáng & Phối Đồ (Styling)": [
        "Hack chân dài cho nấm lùn 1m50",
        "Che bụng mỡ dưới thần thánh",
        "Phối đồ cho người vai rộng/thô",
        "Biến đồ công sở nhàm chán thành Sang chảnh",
        "Mặc đồ rẻ tiền (Local Brand) trông như hàng hiệu",
        "Tips chọn quần Jeans tôn vòng 3",
        "Phối màu đơn sắc (Monochrome) tinh tế"
    ],
    "📸 Tạo Dáng & Thần Thái (Posing)": [
        "3 Dáng đứng chụp ảnh 'kéo chân' ảo diệu",
        "Tạo dáng ngồi quán cafe sao cho sang?",
        "Cách cười tự nhiên không bị gượng gạo",
        "Xử lý tay khi chụp ảnh (đỡ bị đơ)",
        "Góc mặt thần thánh của bạn ở đâu?",
        "Pose dáng với ghế/cầu thang",
        "Thần thái 'Chị Đại' (Boss Girl Energy)"
    ],
    "💄 Làm Đẹp & Skincare (Beauty)": [
        "Makeup trong veo đi làm 5 phút",
        "Tips đánh son không bị lem/trôi",
        "Quy trình dưỡng da Glass Skin buổi tối",
        "Xử lý tóc bết khẩn cấp khi đi tiệc",
        "Chọn mùi nước hoa 'Signature' quyến rũ",
        "Mẹo kẻ mắt (Eyeliner) cho người mới",
        "Cách giữ lớp nền lâu trôi cả ngày"
    ],
    "🥂 Phong Cách Sống (Lifestyle)": [
        "Xây dựng sự tự tin từ bên trong",
        "Quản lý tài chính cho cô nàng nghiện mua sắm",
        "Một ngày làm việc hiệu quả của Nelly",
        "Cách từ chối thanh lịch & sang trọng",
        "Dọn tủ đồ tối giản (Declutter Wardrobe)",
        "Tư duy phụ nữ hiện đại: Độc lập & Hạnh phúc"
    ]
}

# Dictionary chứa Caption mẫu theo từng nhóm chủ đề
caption_library = {
    "Styling": [
        "Quần áo không làm nên con người, nhưng làm nên thần thái! 😎",
        "Không có phụ nữ lùn, chỉ có phụ nữ chưa biết hack dáng! 👠",
        "Mặc đẹp không phải để ai ngắm, mà là để mình vui! ✨",
        "Outfit hôm nay: 10 điểm không có nhưng! 🔥"
    ],
    "Posing": [
        "Đứng im cũng đẹp, mà cười cái là 'đổ' luôn! 📸",
        "Thần thái là thứ không mua được bằng tiền, nhưng luyện tập thì được! 💃",
        "Lưu ngay bí kíp tạo dáng này kẻo xóa video nha mấy bà! 🤫",
        "Góc nghiêng thần thánh hay góc chết? Xem kết quả nhé! 😉"
    ],
    "Beauty": [
        "Đẹp tự nhiên nhưng không phải tự nhiên mà đẹp! 💄",
        "Dưỡng da là khoản đầu tư không bao giờ lỗ. 💖",
        "Makeup sương sương nhưng sát thương cực lớn! 💋",
        "Mùi hương là vũ khí bí mật của phụ nữ. 🌸"
    ],
    "Lifestyle": [
        "Sống sang không phải là khoe tiền, mà là biết yêu bản thân. 🥂",
        "Phụ nữ hiện đại: Kiếm tiền giỏi, Sống chất chơi! 👑",
        "Đừng chờ ai mang hoa đến, hãy tự trồng vườn hoa của mình. 🌻",
        "Hạnh phúc là khi được là chính mình phiên bản tốt nhất. ✨"
    ]
}

# =========================================================
# 2. MA TRẬN GÓC ĐỘ (ANGLES)
# =========================================================

pillars = {
    "🔥 1. Biến hình/Kết quả (Transformation)": {
        "desc": "Show Before/After để gây choáng ngợp.",
        "tone": "Hào hứng, Nhạc Trend, Nhanh",
        "action_kw": "snapping fingers transition, spinning transformation, glowing up"
    },
    "🎓 2. Hướng dẫn/Mẹo (Tutorial)": {
        "desc": "Cầm tay chỉ việc, từng bước một.",
        "tone": "Chuyên gia, Rõ ràng, Chậm rãi",
        "action_kw": "pointing to details, demonstrating step-by-step, nodding"
    },
    "⚠️ 3. Sai lầm/Cảnh báo (Mistakes)": {
        "desc": "Đánh vào nỗi sợ 'Làm sai nên xấu'.",
        "tone": "Nghiêm túc, Drama hóa",
        "action_kw": "shaking head No, holding STOP sign, showing 'X' mark"
    },
    "💖 4. Tâm sự/Vlog (Storytelling)": {
        "desc": "Kể chuyện cá nhân để hút fan trung thành.",
        "tone": "Thủ thỉ, Gần gũi, Cảm xúc",
        "action_kw": "talking to camera, drinking coffee, looking thoughtful"
    }
}

# =========================================================
# GIAO DIỆN APP
# =========================================================

st.title("👠 NELLY'S FASHION MATRIX v4.1")
st.markdown("*Giao diện tối ưu: Copy 1 lần là xong!*")

# --- BƯỚC 1: CHỌN CHỦ ĐỀ ---
c1, c2 = st.columns(2)
with c1:
    group_select = st.selectbox("1. Nhóm chủ đề:", list(categories.keys()))
with c2:
    topic_select = st.selectbox("2. Chủ đề cụ thể (Viral Topic):", categories[group_select])

# --- BƯỚC 2: CHỌN GÓC ĐỘ ---
st.divider()
c3, c4 = st.columns(2)
with c3:
    pillar_select = st.selectbox("3. Góc quay (Style):", list(pillars.keys()))
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

# 1. Setup Visual Style
if style_select == "KOL (Người thật)":
    subject_prompt = "A stunning Vietnamese fashion KOL (Nelly), wearing trendy outfit, confident aura"
    visual_style = "High-end fashion commercial, Vogue magazine style, 8k"
else:
    subject_prompt = "A cute 3D fashion doll character (Nelly), Pixar style"
    visual_style = "Disney Pixar style, vibrant colors, 8k"

# 2. Chọn Caption ngẫu nhiên theo nhóm
if "Styling" in group_select: cap_list = caption_library["Styling"]
elif "Posing" in group_select: cap_list = caption_library["Posing"]
elif "Beauty" in group_select: cap_list = caption_library["Beauty"]
else: cap_list = caption_library["Lifestyle"]
selected_cap = random.choice(cap_list)

# 3. Logic Kịch bản (Auto-Writing)
t_num = int(duration_option.replace("s", ""))
prompts_list = []

# (Logic Hook-Body-CTA như bản cũ, giữ nguyên chất lượng)
if "Biến hình" in pillar_select:
    script_sum = f"- HOOK: Nelly trông xuề xòa với vấn đề '{topic_select}'.\n- BODY: Búng tay biến hình sang chảnh.\n- CTA: Thần thái ngút ngàn."
    act_15s = f"Start with {subject_prompt} looking messy/sad wearing bad outfit. Action: Snaps fingers/Spins. Cut to: {subject_prompt} wearing luxury outfit, looking perfect. End with winking at camera."
    dia_15s = f"Đừng để ai nhìn thấy bạn lúc này! 1, 2, 3... Biến hình! Đây mới là đẳng cấp của {topic_select}. Bạn chấm mấy điểm?"
elif "Hướng dẫn" in pillar_select:
    script_sum = f"- HOOK: Khổ sở vì chưa biết {topic_select}?\n- BODY: Nelly chỉ 3 bước thực hiện.\n- CTA: Kết quả đẹp mỹ mãn."
    act_15s = f"Start with {subject_prompt} gesturing 'Follow me'. Cut to showing step-by-step guide on {topic_select}. End with showing the final beautiful result."
    dia_15s = f"Muốn {topic_select} chuẩn như Stylist? Lưu ngay 3 bước này của Nelly nhé. Đơn giản nhưng hiệu quả bất ngờ đấy!"
elif "Sai lầm" in pillar_select:
    script_sum = f"- HOOK: Dừng lại! Đừng làm thế này nếu 'quê'.\n- BODY: Chỉ lỗi sai & Cách sửa.\n- CTA: Sửa lại ngay."
    act_15s = f"Start with {subject_prompt} holding a red 'X' sign looking shocked. Cut to demonstrating the wrong way vs the right way of {topic_select}. End with nodding 'Yes'."
    dia_15s = f"Sai lầm tai hại khi {topic_select} mà 90% chị em mắc phải! Bỏ ngay kiểu này đi nhé. Sửa thế này mới sang nè!"
else: # Tâm sự
    script_sum = f"- HOOK: Nelly cũng từng tự ti về {topic_select}...\n- BODY: Hành trình thay đổi.\n- CTA: Truyền động lực."
    act_15s = f"Start with {subject_prompt} sitting on sofa looking thoughtful. Cut to flashback of hard work. End with confident smile looking at horizon."
    dia_15s = f"Mọi người hay khen Nelly mặc đẹp, nhưng ít ai biết trước đây... {topic_select} từng là nỗi ám ảnh của mình. Hãy tin vào bản thân nhé!"

# Logic Chia Prompt (Chunking)
if t_num == 15:
    prompts_list.append({"title": "🎞️ FULL VIDEO (15s) - GOM GỌN", "action": act_15s, "dialogue": dia_15s})
elif t_num == 30:
    prompts_list.append({"title": "🎞️ PHẦN 1 (0-15s): Vấn đề", "action": f"Part 1. {act_15s.split('.')[0]}...", "dialogue": f"{dia_15s.split('.')[0]}..."})
    prompts_list.append({"title": "🎞️ PHẦN 2 (15-30s): Giải pháp", "action": f"Part 2. {act_15s.split('.')[-1]}...", "dialogue": f"...{dia_15s.split('.')[-1]}"})
# ... (Giữ nguyên logic 45s, 60s nếu cần)

# =========================================================
# HIỂN THỊ KẾT QUẢ (GIAO DIỆN MỚI)
# =========================================================

with st.expander("📜 KỊCH BẢN TÓM TẮT (Tiếng Việt)", expanded=True):
    st.info(script_sum)

st.divider()

# TẠO TABS CHUYÊN NGHIỆP
tab_video, tab_blog = st.tabs(["🎥 VIDEO & CAPTION", "📝 BÀI VIẾT & ẢNH BLOG"])

# --- TAB 1: VIDEO + CAPTION HÀI ---
with tab_video:
    # 1. Caption Hài hước (Dễ Copy)
    st.subheader("🤣 Caption TikTok/Reels (Copy ngay):")
    caption_text = f"""{selected_cap}

#NellyFashion #StyleTips #{topic_select.replace(' ','')}"""
    st.code(caption_text, language="text")
    
    st.divider()
    
    # 2. Prompt Video
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

# --- TAB 2: BÀI VIẾT + ẢNH MINH HỌA (CHIA ĐÔI CỘT) ---
with tab_blog:
    c_blog, c_img = st.columns(2)
    
    with c_blog:
        st.subheader("1. Prompt viết bài (ChatGPT):")
        st.code(f"""
        Viết bài Facebook/Blog về: {topic_select}.
        - Góc độ khai thác: {pillar_select}.
        - Tone giọng: {current_pillar['tone']}.
        - Kêu gọi hành động: Share ngay nếu thấy đúng.
        - Hashtag: #NellyFashion #StyleTips
        """, language='text')
        
    with c_img:
        st.subheader("2. Prompt ảnh bìa (Midjourney):")
        # Prompt Midjourney được tối ưu cho Fashion
        mj_prompt = f"/imagine prompt: A high-fashion photography shot of Nelly (Vietnamese beauty), wearing stylish outfit relevant to {topic_select}, posing confidently in a luxury city street background or modern studio. Golden hour lighting, vogue magazine style, cinematic depth of field, 8k --ar 3:4"
        st.code(mj_prompt, language='text')
        st.caption("👉 Dùng ảnh này làm bìa Video hoặc ảnh bài viết.")
