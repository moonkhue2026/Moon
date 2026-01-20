import streamlit as st

st.set_page_config(page_title="Zen Master - Lời Phật Dạy", page_icon="🙏", layout="wide")

# =========================================================
# DỮ LIỆU CHỦ ĐỀ
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

# =========================================================
# GIAO DIỆN
# =========================================================
st.title("🙏 ZEN MASTER - KÊNH LỜI PHẬT DẠY")
st.markdown("*Kiến tạo Video Tâm linh phong cách Điện ảnh (Cinematic)*")

c1, c2 = st.columns(2)
with c1:
    topic_select = st.selectbox("Chủ đề Lời dạy:", list(topics.keys()))
with c2:
    style_select = st.selectbox("Phong cách Hình ảnh:", list(visual_styles.keys()))

st.divider()

# =========================================================
# GENERATOR
# =========================================================
visual_prompt = visual_styles[style_select]
context_kw = topics[topic_select]

# Prompt Midjourney (Vẽ ảnh bìa/ảnh tĩnh)
mj_prompt = f"/imagine prompt: A majestic and serene {visual_prompt}. The buddha is in a meditative pose. Context: {context_kw}. High detail, photorealistic, 8k, unreal engine 5 render, spiritual atmosphere --ar 9:16"

# Prompt Sora/Runway (Tạo video động)
video_prompt = f"""
Cinematic shot, {visual_prompt}.
Subject: Statue of Buddha focusing on the serene face or hands.
Motion: Very slow, subtle movement. Floating lotus petals, drifting incense smoke, or gently flowing water.
Atmosphere: Peaceful, holy, divine. 
Lighting: Soft, volumetric lighting. 
--duration 15s
"""

# Prompt ChatGPT (Viết nội dung)
content_prompt = f"""
Đóng vai một Thiền sư uyên bác, giọng văn ấm áp, sâu sắc.
Hãy viết một kịch bản video ngắn (60s) về chủ đề: **{topic_select}**.
- Mở đầu: Một câu hỏi hoặc vấn đề trăn trở của chúng sinh.
- Thân bài: Lời dạy của Phật hoặc triết lý nhân quả (ngắn gọn, thấm thía).
- Kết bài: Một lời khuyên tu tập/ứng dụng vào đời sống.
- Văn phong: Nhẹ nhàng, chữa lành, không giáo điều nặng nề.
"""

# HIỂN THỊ
t1, t2, t3 = st.tabs(["🎥 Prompt Video (Sora)", "📸 Prompt Ảnh (Midjourney)", "📝 Kịch bản (ChatGPT)"])

with t1:
    st.success("💡 Mẹo: Video tâm linh cần chuyển động cực chậm (Slow motion) để tạo cảm giác thiền.")
    st.code(video_prompt, language='text')

with t2:
    st.info("💡 Mẹo: Dùng ảnh này làm Thumbnail hoặc cho vào Runway Gen-2 để làm động.")
    st.code(mj_prompt, language='text')

with t3:
    st.warning("💡 Copy đoạn này gửi cho ChatGPT Tâm linh của Moon:")
    st.code(content_prompt, language='text')
