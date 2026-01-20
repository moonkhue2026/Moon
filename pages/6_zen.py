import streamlit as st

st.set_page_config(page_title="Zen Master - Lời Phật Dạy", page_icon="🙏", layout="wide")

# =========================================================
# 1. DỮ LIỆU CẤU HÌNH
# =========================================================

topics = {
    "🌿 Buông bỏ & An nhiên": "Letting go, inner peace, calmness",
    "🔥 Chuyển hóa Nóng giận": "Overcoming anger, mindfulness, patience",
    "🙏 Hiếu thảo & Gia đình": "Filial piety, gratitude, family love",
    "💰 Tài lộc & Phước báu": "Generosity, karma, abundance mindset",
    "💔 Tình yêu & Duyên nợ": "Love, attachment, impermanence",
    "🌙 Giấc ngủ & Chữa lành": "Deep sleep, healing energy, relaxation"
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

# [MỚI] DANH SÁCH GÓC QUAY (FULL OPTION)
camera_angles = {
    "--- NHÓM ZEN/TĨNH (Khuyên dùng) ---": "", # Header, không chọn
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
st.title("🙏 ZEN MASTER MANAGER v3.3")
st.markdown("*Full Option: Góc máy điện ảnh Hollywood*")

# --- CẤU HÌNH ---
c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    use_existing_image = st.checkbox("🔒 Đã có Ảnh cũ", value=True)
    if not use_existing_image:
        style_select = st.selectbox("Style ảnh:", list(visual_styles.keys()))
        visual_prompt = visual_styles[style_select]
    else:
        visual_prompt = "Golden buddha statue, cinematic golden lighting" 

with c2: topic_select = st.selectbox("2. Chủ đề:", list(topics.keys()))
with c3: format_select = st.selectbox("3. Định dạng:", list(formats.keys()))
with c4: duration_option = st.select_slider("4. Thời lượng:", options=["15s", "30s", "45s", "60s"], value="15s")
with c5: 
    # Logic lọc bỏ Header trong dropdown
    valid_angles = [k for k in camera_angles.keys() if "---" not in k]
    angle_select = st.selectbox("5. Góc máy:", valid_angles, index=0)

current_format = formats[format_select]
context_kw = topics[topic_select]
angle_prompt = camera_angles[angle_select]
t_num = int(duration_option.replace("s", ""))

# =========================================================
# XỬ LÝ LOGIC
# =========================================================

# 1. Prompt Ảnh
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

# 3. Logic Prompt Video (Đã thêm Camera Angle)
base_video_prompt = f"""
Cinematic shot.
Subject: Statue of Buddha.
CAMERA: {angle_prompt}.
Action: {current_format['motion']}. Slow motion, cinematic depth of field.
Lighting: Soft, volumetric lighting.
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
    st.subheader(f"👉 Tạo Video: {angle_select}")
    
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
    # (Giữ nguyên logic 45, 60s)

    for vp in video_prompts:
        st.markdown(f"**{vp['title']}**")
        st.code(vp['prompt'], language='text')
