import streamlit as st

st.set_page_config(page_title="Zen Master - Kinh Pháp Cú", page_icon="🙏", layout="wide")

# =========================================================
# 1. DỮ LIỆU CẤU HÌNH (ĐÃ CẬP NHẬT 26 PHẨM)
# =========================================================

# Dictionary: Tên Tiếng Việt -> Từ khóa Tiếng Anh cho AI hiểu
topics = {
    "1️⃣ Phẩm Song Yếu (Khổ vui do tâm)": "Twin Verses, mind creates reality, duality of life",
    "2️⃣ Phẩm Không Phóng Dật (Tỉnh thức)": "Vigilance, mindfulness, awakening, path to immortality",
    "3️⃣ Phẩm Tâm (Điều phục tâm)": "The Mind, taming the mind, finding peace, meditation",
    "4️⃣ Phẩm Hoa (Vô thường)": "Flowers, impermanence, fragility of life, withering flowers",
    "5️⃣ Phẩm Kẻ Ngu (Vô minh)": "The Fool, ignorance, suffering, darkness vs light",
    "6️⃣ Phẩm Người Trí (Trí tuệ)": "The Wise, wisdom, liberation, guiding light",
    "7️⃣ Phẩm A-la-hán (Giải thoát)": "The Arhat/Saint, enlightenment, absolute freedom, nirvana",
    "8️⃣ Phẩm Ngàn (Lời pháp)": "Thousands, truth, meaningful words, better than empty speech",
    "9️⃣ Phẩm Ác (Tránh ác)": "Evil, karma, avoiding bad deeds, consequence",
    "🔟 Phẩm Hình Phạt (Từ bi)": "Punishment, non-violence, compassion, fear of suffering",
    "1️⃣1️⃣ Phẩm Già (Thân già)": "Old Age, aging, decay of body, time passing",
    "1️⃣2️⃣ Phẩm Tự Ngã (Tự độ)": "The Self, self-mastery, reliance on oneself",
    "1️⃣3️⃣ Phẩm Thế Gian (Danh lợi)": "The World, detachment, illusion of fame, lotus rising from mud",
    "1️⃣4️⃣ Phẩm Phật (Tỉnh thức)": "The Buddha, awakened one, purity, infinite light",
    "1️⃣5️⃣ Phẩm An Lạc (Không tham)": "Happiness, contentment, no greed, inner peace",
    "1️⃣6️⃣ Phẩm Hỷ (Hoan hỷ)": "Pleasure, joy in Dharma, spiritual bliss",
    "1️⃣7️⃣ Phẩm Phẫn Nộ (Diệt oán)": "Anger, forgiveness, love vs hate, overcoming anger",
    "1️⃣8️⃣ Phẩm Cấu Uế (Tâm nhiễm ô)": "Impurity, cleansing the mind, removing stains",
    "1️⃣9️⃣ Phẩm Pháp Trụ (Chân nhân)": "The Righteous, living by Dharma, justice, truth",
    "2️⃣0️⃣ Phẩm Đạo (Bát Chánh Đạo)": "The Path, Eightfold Path, the way to freedom",
    "2️⃣1️⃣ Phẩm Tạp (Lời dạy thực tiễn)": "Miscellaneous, practical wisdom, daily life practice",
    "2️⃣2️⃣ Phẩm Địa Ngục (Ác nghiệp)": "Hell/Woeful State, bad karma, suffering, warning",
    "2️⃣3️⃣ Phẩm Voi (Nhẫn nhục)": "The Elephant, endurance, patience, strength in battle",
    "2️⃣4️⃣ Phẩm Ái (Ái dục)": "Craving, attachment, binding ropes, letting go of desire",
    "2️⃣5️⃣ Phẩm Tỳ-kheo (Phạm hạnh)": "The Monk, holy life, discipline, serenity",
    "2️⃣6️⃣ Phẩm Bà-la-môn (Vượt sinh tử)": "The Brahmin/Holy Man, transcendence, no ego, pure heart"
}

visual_styles = {
    "Vàng Gold (Uy Nghiêm)": "Golden buddha statue, cinematic golden lighting, divine atmosphere, floating light particles",
    "Xanh Ngọc (Chữa Lành)": "Jade buddha statue, waterfall background, lush nature, soft mist, zen garden vibe",
    "Trăng Đêm (Tĩnh Lặng)": "Silhouette of buddha against full moon, night sky, reflection in water, deep blue tones, peaceful",
    "Thủy Mặc (Nghệ Thuật)": "Ink wash painting style, misty mountains, ancient aesthetics, soft brush strokes, ethereal"
}

formats = {
    "📜 Lời Nhắc (Quote)": {"desc": "Câu nói ngắn gọn, thấm thía", "motion": "Static shot, very subtle movement"},
    "❓ Giải Mã (Q&A)": {"desc": "Hỏi đáp thắc mắc đời thường", "motion": "Close-up on peaceful details"},
    "📖 Kể Chuyện (Story)": {"desc": "Kể tích truyện nhân quả", "motion": "Narrative shot, slow panning"},
    "🎶 Nhạc Thiền (Mantra)": {"desc": "Video lặp lại để nghe nhạc", "motion": "Seamless loop, fluid motion"}
}

# FULL CAMERA ANGLES (V3.3)
camera_angles = {
    "--- NHÓM ZEN/TĨNH (Khuyên dùng) ---": "", 
    "🔍 Macro Extreme Close-up (Cận cảnh cực đại)": "Extreme close-up macro shot of details (eyes/hands/lotus texture), sharp focus",
    "🦅 God’s Eye View (Góc nhìn thượng đế)": "Top-down god's eye view, looking down from the sky, epic scale",
    "🧘 Immersive POV (Góc nhìn nhập vai)": "First-person POV shot, as if walking towards the Buddha, handheld camera movement",
    "🛡️ Low Angle 'Hero Shot' (Góc thấp tôn vinh)": "Low angle shot looking up, making the subject look majestic and powerful",
    "🎥 Dolly Zoom (Hiệu ứng Vertigo)": "Dolly zoom effect (Hitchcock zoom), subject size remains same while background expands, trippy spiritual effect",
    "⚖️ Gimbal Stabilization (Mượt mà)": "Smooth gimbal stabilization, floating camera movement",
    "--- NHÓM ACTION/MẠNH (Kịch tính) ---": "",
    "⚡ Crash Zoom (Zoom sốc)": "Rapid crash zoom onto the face, dramatic and intense impact",
    "😵 Whip Pan (Lia máy vút)": "Fast whip pan camera transition, dynamic blur motion",
    "📏 Dutch Angle (Góc nghiêng)": "Dutch angle (tilted camera), creating a sense of unease or mystery",
    "🌪️ SnorriCam (Gắn thân)": "Snorricam style, camera locked to the subject while background rotates dizzyingly"
}

GPT_LINK = "https://chatgpt.com/g/g-693137cfde808191b2a5f60c8a49c862-chia-khoa-tam-linh-bac-giac-ngo"

# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🙏 ZEN MASTER: 26 PHẨM KINH PHÁP CÚ")
st.markdown("*Lộ trình xây kênh bài bản: Từ Phẩm 1 -> Phẩm 26*")

# --- CẤU HÌNH ---
c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    use_existing_image = st.checkbox("🔒 Đã có Ảnh cũ", value=True)
    if not use_existing_image:
        style_select = st.selectbox("Style ảnh:", list(visual_styles.keys()))
        visual_prompt = visual_styles[style_select]
    else:
        visual_prompt = "Golden buddha statue, cinematic golden lighting" 

with c2: topic_select = st.selectbox("2. Chọn Phẩm:", list(topics.keys()))
with c3: format_select = st.selectbox("3. Định dạng:", list(formats.keys()))
with c4: duration_option = st.select_slider("4. Thời lượng:", options=["15s", "30s", "45s", "60s"], value="15s")
with c5: 
    valid_angles = [k for k in camera_angles.keys() if "---" not in k]
    angle_select = st.selectbox("5. Góc máy:", valid_angles, index=0)

current_format = formats[format_select]
context_kw = topics[topic_select] # Lấy từ khóa tiếng Anh tương ứng
angle_prompt = camera_angles[angle_select]
t_num = int(duration_option.replace("s", ""))

# =========================================================
# XỬ LÝ LOGIC
# =========================================================

# 1. Prompt Ảnh (Midjourney) - Dùng Context Keywords mới
mj_prompt = f"/imagine prompt: A majestic {visual_prompt}. Context: {context_kw}. High detail, photorealistic, 8k, spiritual atmosphere --ar 9:16"

# 2. Logic Lệnh GPT
word_count = int(t_num * 2.5)
if "Lời Nhắc" in format_select:
    gpt_req = f"Viết 1 câu QUOTE ngắn gọn (< {word_count} từ)."
elif "Giải Mã" in format_select:
    gpt_req = f"Viết kịch bản HỎI XOÁY ĐÁP XOAY ({t_num}s)."
elif "Kể Chuyện" in format_select:
    gpt_req = f"Viết truyện ngắn NHÂN QUẢ ({t_num}s)."
else:
    gpt_req = f"Gợi ý Nhạc thiền & Caption ({t_num}s)."

gpt_command = f"""
Chủ đề: **{topic_select}**. Thời lượng: **{duration_option}**.
Yêu cầu: {gpt_req}
Giọng văn: Ấm áp, chữa lành.
"""

# 3. Logic Prompt Video (Base)
base_video_prompt = f"""
Cinematic shot.
Subject: Statue of Buddha.
CAMERA: {angle_prompt}.
Action: {current_format['motion']}. Slow motion, cinematic depth of field.
Lighting: Soft, volumetric lighting.
Context: {context_kw}.
AUDIO: Zen music + Warm Vietnamese voiceover.
CONSTRAINT: NO TEXT, NO LOGO.
"""

# =========================================================
# HIỂN THỊ KẾT QUẢ
# =========================================================

t1, t2, t3 = st.tabs(["1️⃣ PROMPT ẢNH (MJ)", "2️⃣ LẤY NỘI DUNG (GPT)", "3️⃣ PROMPT VIDEO (Sora)"])

# --- TAB 1: ẢNH ---
with t1:
    if use_existing_image:
        st.info("🔒 ĐANG DÙNG ẢNH CŨ (BRANDING)")
    else:
        st.code(mj_prompt, language='text')

# --- TAB 2: NỘI DUNG ---
with t2:
    st.link_button("🧘‍♂️ Mở 'Bác Giác Ngộ' (GPT)", GPT_LINK)
    st.code(gpt_command, language='text')

# --- TAB 3: VIDEO ---
with t3:
    st.subheader(f"👉 Tạo Video: {topic_select}")
    
    st.markdown("### 🎙️ Dán lời bình (Voiceover):")
    voice_text = st.text_area("Voiceover script:", height=80)
    
    def get_final_prompt(base, text):
        if text: return base.replace("Warm Vietnamese voiceover.", f"Warm Vietnamese voiceover narrating: '{text[:100]}...'")
        return base

    video_prompts = []
    if t_num == 15:
        video_prompts.append({"title": "🎞️ FULL VIDEO (15s)", "prompt": f"[INPUT ẢNH]\n{get_final_prompt(base_video_prompt, voice_text)} --duration 15s"})
    elif t_num == 30:
        video_prompts.append({"title": "🎞️ PHẦN 1 (0-15s)", "prompt": f"[INPUT ẢNH]\n{get_final_prompt(base_video_prompt, voice_text)} --duration 15s"})
        video_prompts.append({"title": "🎞️ PHẦN 2 (15-30s)", "prompt": f"[INPUT: FRAME CUỐI P1]\n{base_video_prompt} (Continue motion) --duration 15s"})
    elif t_num == 45:
        video_prompts.append({"title": "🎞️ PHẦN 1 (0-15s)", "prompt": f"[INPUT ẢNH]\n{get_final_prompt(base_video_prompt, voice_text)} --duration 15s"})
        video_prompts.append({"title": "🎞️ PHẦN 2 (15-30s)", "prompt": f"[INPUT: FRAME CUỐI P1]\n{base_video_prompt} --duration 15s"})
        video_prompts.append({"title": "🎞️ PHẦN 3 (30-45s)", "prompt": f"[INPUT: FRAME CUỐI P2]\n{base_video_prompt} --duration 15s"})
    else: # 60s
        video_prompts.append({"title": "🎞️ PHẦN 1 (0-15s)", "prompt": f"[INPUT ẢNH]\n{get_final_prompt(base_video_prompt, voice_text)} --duration 15s"})
        video_prompts.append({"title": "🎞️ PHẦN 2 (15-30s)", "prompt": f"[INPUT: FRAME CUỐI P1]\n{base_video_prompt} --duration 15s"})
        video_prompts.append({"title": "🎞️ PHẦN 3 (30-45s)", "prompt": f"[INPUT: FRAME CUỐI P2]\n{base_video_prompt} --duration 15s"})
        video_prompts.append({"title": "🎞️ PHẦN 4 (45-60s)", "prompt": f"[INPUT: FRAME CUỐI P3]\n{base_video_prompt} --duration 15s"})

    for vp in video_prompts:
        st.markdown(f"**{vp['title']}**")
        st.code(vp['prompt'], language='text')
