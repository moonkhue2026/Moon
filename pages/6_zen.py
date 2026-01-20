import streamlit as st

st.set_page_config(page_title="Zen Master - Lời Phật Dạy", page_icon="🙏", layout="wide")

# =========================================================
# 1. DỮ LIỆU CẤU HÌNH (Giữ nguyên)
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

GPT_LINK = "https://chatgpt.com/g/g-693137cfde808191b2a5f60c8a49c862-chia-khoa-tam-linh-bac-giac-ngo"

# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🙏 ZEN MASTER MANAGER v3.1")
st.markdown("*Quy trình chuẩn: 1. Tạo Ảnh -> 2. Lấy Nội Dung -> 3. Tạo Video*")

# --- CẤU HÌNH ---
c1, c2, c3, c4 = st.columns(4)
with c1: style_select = st.selectbox("1. Style ảnh (Trước):", list(visual_styles.keys()))
with c2: topic_select = st.selectbox("2. Chủ đề:", list(topics.keys()))
with c3: format_select = st.selectbox("3. Định dạng:", list(formats.keys()))
with c4: duration_option = st.select_slider("4. Thời lượng:", options=["15s", "30s", "45s", "60s"], value="15s")

current_format = formats[format_select]
visual_prompt = visual_styles[style_select]
context_kw = topics[topic_select]
t_num = int(duration_option.replace("s", ""))

# =========================================================
# XỬ LÝ LOGIC
# =========================================================

# 1. Prompt Ảnh
mj_prompt = f"/imagine prompt: A majestic {visual_prompt}. Context: {context_kw}. High detail, photorealistic, 8k, spiritual atmosphere --ar 9:16"

# 2. Logic Lệnh GPT
word_count = int(t_num * 2.5)
if "Lời Nhắc" in format_select:
    gpt_req = f"Viết 1 câu QUOTE ngắn gọn, sâu sắc (< {word_count} từ)."
elif "Giải Mã" in format_select:
    gpt_req = f"Viết kịch bản HỎI XOÁY ĐÁP XOAY ({t_num}s). Hook gây tò mò, Body giải thích thấu đáo, CTA hành động."
elif "Kể Chuyện" in format_select:
    gpt_req = f"Viết truyện ngắn NHÂN QUẢ ({t_num}s, khoảng {word_count} từ). Có bài học sâu sắc."
else:
    gpt_req = f"Gợi ý Nhạc thiền & Caption ({t_num}s)."

gpt_command = f"""
Chủ đề: **{topic_select}**. Thời lượng video: **{duration_option}**.
Yêu cầu: {gpt_req}
Giọng văn: Ấm áp, chữa lành.
"""

# 3. Logic Prompt Video (Base)
base_video_prompt = f"""
Cinematic shot.
Subject: Statue of Buddha.
Action: {current_format['motion']}. Slow motion, cinematic depth of field.
Lighting: Soft, volumetric lighting.
AUDIO: Zen music + Warm Vietnamese voiceover.
CONSTRAINT: NO TEXT, NO LOGO.
"""

# =========================================================
# HIỂN THỊ KẾT QUẢ (TAB ĐÚNG THỨ TỰ)
# =========================================================

# ĐÃ SẮP XẾP LẠI THEO Ý MOON
t1, t2, t3 = st.tabs(["1️⃣ PROMPT ẢNH (MJ)", "2️⃣ LẤY NỘI DUNG (GPT)", "3️⃣ PROMPT VIDEO (Sora)"])

# --- TAB 1: ẢNH ---
with t1:
    st.subheader("👉 BƯỚC 1: Tạo Ảnh Bìa")
    st.caption("Dùng Prompt này tạo ảnh nền đẹp trước.")
    st.code(mj_prompt, language='text')

# --- TAB 2: NỘI DUNG ---
with t2:
    st.subheader(f"👉 BƯỚC 2: Lấy Nội dung ({duration_option})")
    st.link_button("🧘‍♂️ Mở 'Bác Giác Ngộ' (GPT)", GPT_LINK)
    st.caption("Bấm nút trên để mở GPT, sau đó copy lệnh dưới này dán vào:")
    st.code(gpt_command, language='text')

# --- TAB 3: VIDEO ---
with t3:
    st.subheader(f"👉 BƯỚC 3: Tạo Video & Lồng tiếng")
    
    st.markdown("### 🎙️ Dán nội dung Bác Giác Ngộ vừa viết vào đây:")
    voice_text = st.text_area("AI sẽ dùng nội dung này để đọc Voiceover:", height=100, placeholder="Ví dụ: Buông bỏ là hạnh phúc...")
    
    # Logic tạo Prompt Video sau khi có text
    video_prompts = []
    
    # Hàm xử lý chèn voice
    def get_final_prompt(base, text):
        if text:
            return base.replace("Warm Vietnamese voiceover.", f"Warm Vietnamese voiceover narrating: '{text[:100]}...' (See full script)")
        return base

    if t_num == 15:
        video_prompts.append({"title": "🎞️ FULL VIDEO (15s)", "prompt": f"[INPUT ẢNH TỪ BƯỚC 1]\n{get_final_prompt(base_video_prompt, voice_text)} --duration 15s"})
    elif t_num == 30:
        video_prompts.append({"title": "🎞️ PHẦN 1 (0-15s)", "prompt": f"[INPUT ẢNH TỪ BƯỚC 1]\n{get_final_prompt(base_video_prompt, voice_text)} --duration 15s"})
        video_prompts.append({"title": "🎞️ PHẦN 2 (15-30s)", "prompt": f"[INPUT: FRAME CUỐI PHẦN 1]\n{base_video_prompt} (Continue motion) --duration 15s"})
    elif t_num == 45:
        video_prompts.append({"title": "🎞️ PHẦN 1 (0-15s)", "prompt": f"[INPUT ẢNH TỪ BƯỚC 1]\n{get_final_prompt(base_video_prompt, voice_text)} --duration 15s"})
        video_prompts.append({"title": "🎞️ PHẦN 2 (15-30s)", "prompt": f"[INPUT: FRAME CUỐI PHẦN 1]\n{base_video_prompt} --duration 15s"})
        video_prompts.append({"title": "🎞️ PHẦN 3 (30-45s)", "prompt": f"[INPUT: FRAME CUỐI PHẦN 2]\n{base_video_prompt} --duration 15s"})
    else: # 60s
        video_prompts.append({"title": "🎞️ PHẦN 1 (0-15s)", "prompt": f"[INPUT ẢNH TỪ BƯỚC 1]\n{get_final_prompt(base_video_prompt, voice_text)} --duration 15s"})
        video_prompts.append({"title": "🎞️ PHẦN 2 (15-30s)", "prompt": f"[INPUT: FRAME CUỐI PHẦN 1]\n{base_video_prompt} --duration 15s"})
        video_prompts.append({"title": "🎞️ PHẦN 3 (30-45s)", "prompt": f"[INPUT: FRAME CUỐI PHẦN 2]\n{base_video_prompt} --duration 15s"})
        video_prompts.append({"title": "🎞️ PHẦN 4 (45-60s)", "prompt": f"[INPUT: FRAME CUỐI PHẦN 3]\n{base_video_prompt} --duration 15s"})

    for vp in video_prompts:
        st.markdown(f"**{vp['title']}**")
        st.code(vp['prompt'], language='text')
