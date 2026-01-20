import streamlit as st

st.set_page_config(page_title="Zen Master - Lời Phật Dạy", page_icon="🙏", layout="wide")

# =========================================================
# 1. DỮ LIỆU CẤU HÌNH
# =========================================================

# Các chủ đề Tâm linh
topics = {
    "🌿 Buông bỏ & An nhiên": "Letting go, inner peace, calmness",
    "🔥 Chuyển hóa Nóng giận": "Overcoming anger, mindfulness, patience",
    "🙏 Hiếu thảo & Gia đình": "Filial piety, gratitude, family love",
    "💰 Tài lộc & Phước báu": "Generosity, karma, abundance mindset",
    "💔 Tình yêu & Duyên nợ": "Love, attachment, impermanence",
    "🌙 Giấc ngủ & Chữa lành": "Deep sleep, healing energy, relaxation"
}

# Các phong cách Hình ảnh (Cinematic)
visual_styles = {
    "Vàng Gold (Uy Nghiêm)": "Golden buddha statue, cinematic golden lighting, divine atmosphere, floating light particles",
    "Xanh Ngọc (Chữa Lành)": "Jade buddha statue, waterfall background, lush nature, soft mist, zen garden vibe",
    "Trăng Đêm (Tĩnh Lặng)": "Silhouette of buddha against full moon, night sky, reflection in water, deep blue tones, peaceful",
    "Thủy Mặc (Nghệ Thuật)": "Ink wash painting style, misty mountains, ancient aesthetics, soft brush strokes, ethereal"
}

# [MỚI] Các định dạng Video (Format)
formats = {
    "📜 Lời Nhắc (Quote - 15s)": {
        "desc": "Câu nói ngắn gọn, video nền chậm",
        "prompt_mod": "Static shot, very subtle movement, focus on atmosphere",
        "duration": "15s"
    },
    "📖 Kể Chuyện (Story - 60s)": {
        "desc": "Kể tích truyện nhân quả/cổ học",
        "prompt_mod": "Narrative shot, slow panning, revealing details of the scene",
        "duration": "60s"
    },
    "🎶 Nhạc Thiền (Mantra - Loop)": {
        "desc": "Video lặp lại để nghe nhạc/thiền",
        "prompt_mod": "Seamless loop, mesmerizing fluid motion (water/smoke/light)",
        "duration": "60s"
    },
    "❓ Giải Mã (Q&A - 30s)": {
        "desc": "Hỏi đáp thắc mắc đời thường",
        "prompt_mod": "Close-up on peaceful details (hands/face), engaging angle",
        "duration": "30s"
    }
}

# Link Trợ lý GPT của Moon
GPT_LINK = "https://chatgpt.com/g/g-693137cfde808191b2a5f60c8a49c862-chia-khoa-tam-linh-bac-giac-ngo"

# =========================================================
# GIAO DIỆN APP
# =========================================================
st.title("🙏 ZEN MASTER MANAGER v2.0")
st.markdown("*Kiến tạo Video Tâm linh - Tích hợp Trợ lý Bác Giác Ngộ*")

# --- BƯỚC 1: LÊN Ý TƯỞNG ---
c1, c2, c3 = st.columns(3)
with c1:
    topic_select = st.selectbox("1. Chủ đề:", list(topics.keys()))
with c2:
    format_select = st.selectbox("2. Định dạng:", list(formats.keys()))
with c3:
    style_select = st.selectbox("3. Style ảnh:", list(visual_styles.keys()))

current_format = formats[format_select]
visual_prompt = visual_styles[style_select]
context_kw = topics[topic_select]

st.divider()

# =========================================================
# XỬ LÝ LOGIC (GENERATOR)
# =========================================================

# 1. Prompt Video (Sora/Runway) - Tinh chỉnh theo Format
video_prompt = f"""
Cinematic shot, {visual_prompt}.
Subject: Statue of Buddha (or symbolic Zen element like Lotus/Hands).
Format Style: {current_format['prompt_mod']}.
Motion: Slow motion, cinematic depth of field.
Context: {context_kw}. 
Atmosphere: Peaceful, Holy.
--duration {current_format['duration']}
"""

# 2. Prompt Ảnh (Midjourney)
mj_prompt = f"/imagine prompt: A majestic {visual_prompt}. Context: {context_kw}. High detail, photorealistic, 8k, unreal engine 5 render, spiritual atmosphere --ar 9:16"

# 3. Lệnh cho Trợ lý GPT (Prompt Content)
gpt_command = f"""
Tôi muốn làm video dạng: **{format_select}**.
Chủ đề: **{topic_select}**.
Hãy viết nội dung kịch bản chi tiết:
- Nếu là Quote: Cho tôi 1 câu nói hay và ngắn gọn.
- Nếu là Kể chuyện: Viết kịch bản ngắn gọn, có bài học nhân quả.
- Nếu là Nhạc thiền: Gợi ý tên bản nhạc và dòng mô tả video (Caption).
- Giọng văn: Ấm áp, chữa lành, sâu sắc.
"""

# =========================================================
# HIỂN THỊ KẾT QUẢ
# =========================================================

# NÚT TRUY CẬP TRỢ LÝ (Điểm nhấn)
st.success("👇 **BƯỚC 1: BẤM VÀO ĐÂY ĐỂ GẶP TRỢ LÝ 'BÁC GIÁC NGỘ'**")
st.link_button("🧘‍♂️ Mở Trợ Lý: Chìa Khóa Tâm Linh", GPT_LINK)

# TABS CÔNG CỤ
t1, t2, t3 = st.tabs(["📝 LỆNH VIẾT (Cho GPT)", "🎥 PROMPT VIDEO (Sora)", "📸 PROMPT ẢNH (MJ)"])

with t1:
    st.info("👉 Copy lệnh bên dưới và dán vào Chat với 'Bác Giác Ngộ':")
    st.code(gpt_command, language='text')

with t2:
    st.subheader(f"Prompt Video ({current_format['duration']})")
    st.code(video_prompt, language='text')

with t3:
    st.subheader("Prompt Ảnh Bìa/Thumbnail")
    st.code(mj_prompt, language='text')
