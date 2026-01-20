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
    "📜 Lời Nhắc (Quote - 15s)": {
        "desc": "Câu nói ngắn gọn, thấm thía",
        "prompt_mod": "Static shot, very subtle movement",
        "duration": "15s"
    },
    "❓ Giải Mã (Hỏi Xoáy Đáp Xoay - 60s)": {
        "desc": "Hỏi đáp thắc mắc đời thường",
        "prompt_mod": "Close-up on peaceful details",
        "duration": "60s"
    },
    "📖 Kể Chuyện (Story - 60s)": {
        "desc": "Kể tích truyện nhân quả",
        "prompt_mod": "Narrative shot, slow panning",
        "duration": "60s"
    },
    "🎶 Nhạc Thiền (Mantra - Loop)": {
        "desc": "Video lặp lại để nghe nhạc",
        "prompt_mod": "Seamless loop, fluid motion",
        "duration": "60s"
    }
}

GPT_LINK = "https://chatgpt.com/g/g-693137cfde808191b2a5f60c8a49c862-chia-khoa-tam-linh-bac-giac-ngo"

# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🙏 ZEN MASTER MANAGER v2.3")
st.markdown("*Video Tâm linh: Có Giọng Đọc (Voice) & Nhạc Thiền*")

# --- BƯỚC 1: CẤU HÌNH ---
c1, c2, c3 = st.columns(3)
with c1: topic_select = st.selectbox("1. Chủ đề:", list(topics.keys()))
with c2: format_select = st.selectbox("2. Định dạng:", list(formats.keys()))
with c3: style_select = st.selectbox("3. Style ảnh:", list(visual_styles.keys()))

# --- BƯỚC 2: NHẬP LỜI BÌNH (MỚI) ---
st.divider()
st.markdown("### 🎙️ Nhập nội dung Lời bình (Voiceover):")
voice_text = st.text_area("Dán nội dung mà 'Bác Giác Ngộ' đã viết vào đây để AI đọc:", 
                          placeholder="Ví dụ: Buông bỏ không phải là mất tất cả, mà là để đôi tay thảnh thơi...", height=100)

current_format = formats[format_select]
visual_prompt = visual_styles[style_select]
context_kw = topics[topic_select]

# =========================================================
# XỬ LÝ LOGIC PROMPT (CÓ VOICE & AUDIO)
# =========================================================

# Lệnh GPT (Giữ nguyên)
if "Lời Nhắc" in format_select:
    gpt_command = f"Viết QUOTE ngắn về: {topic_select}. Sâu sắc, ngắn gọn."
elif "Giải Mã" in format_select:
    gpt_command = f"Viết kịch bản HỎI XOÁY ĐÁP XOAY về: {topic_select}. Có Hook, Body, CTA."
elif "Kể Chuyện" in format_select:
    gpt_command = f"Viết truyện ngắn NHÂN QUẢ về: {topic_select}. Có bài học."
else:
    gpt_command = f"Gợi ý Nhạc thiền & Caption cho chủ đề: {topic_select}."

# Prompt Ảnh (Midjourney)
mj_prompt = f"/imagine prompt: A majestic {visual_prompt}. Context: {context_kw}. High detail, photorealistic, 8k, spiritual atmosphere --ar 9:16"

# Prompt Video (Sora) - ĐÃ THÊM PHẦN AUDIO & VOICE
# Nếu người dùng chưa nhập text, để placeholder
voice_content = voice_text if voice_text else "[Paste your script here]"

video_prompt = f"""
Cinematic shot, {visual_prompt}.
Subject: Statue of Buddha (or symbolic Zen element).
Action: {current_format['prompt_mod']}. Slow motion, cinematic depth of field.
Lighting: Soft, volumetric lighting, divine atmosphere.

AUDIO SETTINGS:
- Background Music: Soft, peaceful Zen music (Flute/Piano/Nature sounds), 432Hz frequency.
- Voiceover: A warm, soothing Vietnamese voice narrating the following text: "{voice_content}"
- Mix: Balanced audio, voice is clear over the music.

CONSTRAINT: NO TEXT OVERLAYS, NO SUBTITLES, NO LOGOS, CLEAN BACKGROUND.
--duration {current_format['duration']}
"""

# =========================================================
# HIỂN THỊ KẾT QUẢ
# =========================================================

st.success("👇 **BƯỚC 1: LẤY NỘI DUNG TỪ TRỢ LÝ**")
st.link_button("🧘‍♂️ Mở 'Bác Giác Ngộ' (GPT)", GPT_LINK)
st.code(gpt_command, language='text')

st.divider()

st.success("👇 **BƯỚC 2: COPY PROMPT TẠO VIDEO (ĐÃ CÓ VOICE)**")
t1, t2 = st.tabs(["🎥 VIDEO PROMPT (Sora)", "📸 IMAGE PROMPT (MJ)"])

with t1:
    st.info("💡 Prompt này đã bao gồm lệnh: Đọc tiếng Việt + Giữ nhạc nền + Không hiện chữ.")
    st.code(video_prompt, language='text')

with t2:
    st.code(mj_prompt, language='text')
