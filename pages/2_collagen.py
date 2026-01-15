import streamlit as st

st.set_page_config(page_title="Moon's Collagen Matrix", page_icon="🌸", layout="wide")

# =========================================================
# 1. DỮ LIỆU: 40 TRIỆU CHỨNG (MỎ VÀNG)
# =========================================================

pain_points = {
    "🔥 Bốc hỏa & Thân nhiệt": [
        "Cơn bốc hỏa (Hot flashes)", "Ớn lạnh (Cold flashes)", "Đổ mồ hôi đêm (Night sweats)", 
        "Da dính nhớp (Clammy feeling)", "Thay đổi mùi cơ thể (Changed body odor)"
    ],
    "🧠 Tâm lý & Thần kinh": [
        "Cáu gắt (Irritability)", "Tâm trạng thất thường (Mood swings)", "Lo âu (Anxiety)", 
        "Trầm cảm (Depression)", "Mất tập trung (Lack of focus)", "Hay quên (Faulty memory)", 
        "Chóng mặt (Dizziness)", "Đau đầu (Headaches)"
    ],
    "💅 Ngoại hình & Lão hóa": [
        "Rụng tóc/Tóc mỏng (Hair loss)", "Móng tay yếu (Weakened fingernails)", "Tăng cân (Weight gain)", 
        "Nổi mụn/Ngứa da (Itchy skin)", "Có ria mép (Facial hair)", "Chảy máu nướu (Bleeding gums)",
        "Nếp nhăn/Da chảy xệ (Wrinkles)", "Khô da (Dry skin)"
    ],
    "🦴 Cơ thể & Vận động": [
        "Đau nhức xương khớp (Achy joints)", "Căng cơ (Tense muscles)", "Loãng xương (Osteoporosis)", 
        "Mệt mỏi (Fatigue)", "Tim đập nhanh (Heart palpitations)", "Ù tai (Tinnitus)", "Đầy hơi (Bloating)"
    ],
    "🛏️ Sinh lý & Giấc ngủ": [
        "Khó ngủ (Trouble sleeping)", "Giảm ham muốn (Low sex drive)", "Khô hạn (Dry vagina)", 
        "Rối loạn kinh nguyệt (Irregular periods)", "Đau ngực (Sore breasts)"
    ]
}

# =========================================================
# 2. MA TRẬN: 4 TRỤ CỘT x 7 KIỂU VIDEO
# =========================================================

pillars = {
    "🌱 1. Nuôi dưỡng & Niềm tin (Nurture)": {
        "formats": ["Kể chuyện (Storytelling)", "Tâm sự/Vlog (Daily Life)"],
        "goal": "Tạo sự đồng cảm, tôi cũng từng bị như bạn.",
        "tone": "Thủ thỉ, ấm áp, chân thành"
    },
    "🎓 2. Giáo dục & Nhận thức (Educate)": {
        "formats": ["Cảnh báo sai lầm (Warning)", "Góc chuyên gia (Myth vs Fact)", "Phản biện (Counter-Intuitive)"],
        "goal": "Chỉ ra nguyên nhân gốc rễ (Thiếu hụt nội tiết/Collagen).",
        "tone": "Chuyên gia, nghiêm túc, tin cậy"
    },
    "💰 3. Chuyển đổi bán hàng (Convert)": {
        "formats": ["Trước - Sau (Transformation)", "Giải quyết vấn đề (Problem-Solution)"],
        "goal": "Show kết quả, chốt đơn, khan hiếm.",
        "tone": "Hào hứng, năng lượng cao, thúc giục"
    },
    "❤️ 4. Chăm sóc & Giữ chân (Care)": {
        "formats": ["Trải nghiệm/Review (Feedback)", "Q&A (Hỏi đáp)"],
        "goal": "Hướng dẫn sử dụng, chăm sóc khách cũ.",
        "tone": "Tận tâm, vui vẻ"
    }
}

# =========================================================
# GIAO DIỆN APP
# =========================================================

st.title("🌸 COLLAGEN CONTENT MATRIX (v3.1)")
st.markdown("*Công thức: 4 Trụ cột x 7 Video x 40 Nỗi đau = Mỏ vàng 999.9*")

# --- BƯỚC 1: CHỌN NGUYÊN LIỆU ---
st.header("1️⃣ CHỌN NGUYÊN LIỆU")
c1, c2 = st.columns(2)
with c1:
    group_select = st.selectbox("Chọn nhóm vấn đề:", list(pain_points.keys()))
with c2:
    symptom_select = st.selectbox("Chọn 'Nỗi đau' khách hàng:", pain_points[group_select])

symptom_vn = symptom_select.split("(")[0].strip() # Lấy tên tiếng Việt

# --- BƯỚC 2: CHỌN CHIẾN LƯỢC (TRỤ CỘT) ---
st.header("2️⃣ CHỌN CHIẾN LƯỢC")
c3, c4 = st.columns(2)
with c3:
    pillar_select = st.selectbox("Mục tiêu video (Trụ cột):", list(pillars.keys()))
with c4:
    # Gợi ý kiểu video dựa trên trụ cột
    video_type = st.selectbox("Kiểu video (Gợi ý):", pillars[pillar_select]["formats"])

# --- BƯỚC 3: SẢN XUẤT ---
st.header("3️⃣ SẢN XUẤT")
c5, c6, c7 = st.columns(3)
with c5:
    duration_option = st.radio("Thời lượng:", ["15s", "30s", "60s"], horizontal=True)
with c6:
    style_select = st.radio("Style:", ["3D Animation (Bé Collagen)", "KOL (Moon)"], horizontal=True)
with c7:
    model_select = st.radio("AI Model:", ["Sora (15s)", "Veo 3 (8s)"], horizontal=True)

# =========================================================
# XỬ LÝ LOGIC KỊCH BẢN (THE MATRIX)
# =========================================================

t_total = int(duration_option.replace("s", ""))
current_pillar = pillars[pillar_select]
segments = []

# --- LOGIC 1: NUÔI DƯỠNG (STORYTELLING) ---
if "Nuôi dưỡng" in pillar_select:
    segments = [
        ("HOOK", "Đồng cảm", f"Có ai như Moon không? Dạo này bị {symptom_vn} hành hạ khổ sở.", "Character looking sad/tired."),
        ("BODY", "Kể chuyện", f"Đêm nào cũng trằn trọc/soi gương thấy già đi, stress kinh khủng.", "Character sighing looking at mirror."),
        ("CTA", "Kết nối", f"Ai cùng cảnh ngộ thì thả tim để Moon biết mình không cô đơn nha.", "Character hugging self.")
    ]

# --- LOGIC 2: GIÁO DỤC (CẢNH BÁO/KIẾN THỨC) ---
elif "Giáo dục" in pillar_select:
    segments = [
        ("HOOK", "Giật gân", f"Cảnh báo! {symptom_vn} không tự nhiên mà có!", "Character with red alert sign."),
        ("BODY", "Nguyên nhân", f"Đó là tiếng kêu cứu của buồng trứng khi collagen sụt giảm.", "Character pointing to chart/internal body."),
        ("CTA", "Giải pháp", f"Đừng lờ đi nữa, bổ sung ngay trước khi quá muộn.", "Character serious nod.")
    ]

# --- LOGIC 3: BÁN HÀNG (BEFORE/AFTER) ---
elif "Chuyển đổi" in pillar_select:
    segments = [
        ("HOOK", "Kết quả", f"Tạm biệt {symptom_vn} chỉ sau 1 liệu trình!", "Character happy showing result."),
        ("BODY", "Sản phẩm", f"Nhờ em Hera Collagen này đây. 1 gói = 10 lần đắp mặt nạ.", "Character drinking product enthusiastically."),
        ("CTA", "Chốt đơn", f"Ưu đãi mua 3 tặng 1 chỉ hôm nay. Rinh ngay!", "Character holding sale sign.")
    ]

# --- LOGIC 4: CHĂM SÓC (REVIEW) ---
else: 
    segments = [
        ("HOOK", "Câu hỏi", f"Nhiều chị hỏi Moon uống Hera bao lâu thì hết {symptom_vn}?", "Character reading phone/comments."),
        ("BODY", "Review", f"Tùy cơ địa nha, nhưng thường 2 tuần là thấy êm ru rồi.", "Character showing calendar."),
        ("CTA", "Dặn dò", f"Nhớ uống đúng giờ Moon dặn nha. Yêu cả nhà!", "Character blowing kiss.")
    ]

# Điều chỉnh thời lượng (nếu 30s/60s thì thêm đoạn giữa)
if t_total > 15:
    segments.insert(1, ("BODY 2", "Chi tiết", f"Quan trọng là phải kiên trì, bổ sung đủ nước và ngủ sớm nữa.", "Character drinking water/sleeping."))

# =========================================================
# HIỂN THỊ KẾT QUẢ
# =========================================================

st.divider()
st.subheader("📜 Kịch bản chi tiết")
script_text = ""
for name, role, vn, en in segments:
    script_text += f"🔸 {name} ({role}): \"{vn}\"\n"
st.info(script_text)

# TAB BÀI VIẾT (Hỗ trợ ChatGPT)
with st.expander("📝 Prompt viết bài Facebook (Copy cái này)"):
    st.code(f"""
    Đóng vai chuyên gia. Viết bài về nỗi đau: **{symptom_vn}**.
    - Mục tiêu bài viết: {pillar_select} ({current_pillar['goal']}).
    - Định dạng: {video_type}.
    - Tone giọng: {current_theme['tone'] if 'current_theme' in locals() else 'Gần gũi'}.
    - Hashtag: #{symptom_vn.replace(' ','')} #HeraCollagen
    """, language='text')

# VIDEO PROMPT
st.subheader(f"🎥 Prompt Video ({model_select})")

# Setup Style
if style_select == "3D Animation (Bé Collagen)":
    subject_prompt = "a cute anthropomorphic pink collagen drop character"
    style_kw = "Pixar style, soft lighting, 8k"
    move = "bouncy animation"
else:
    subject_prompt = "a beautiful Vietnamese woman 35yo (Moon), glowing skin, silk pajamas"
    style_kw = "Beauty commercial, Arri Alexa, 8k"
    move = "natural acting"

for name, role, vn, en in segments:
    st.markdown(f"**🎞️ {name}: {role}**")
    if "Sora" in model_select:
        prompt = f"""
        {style_kw}. Subject: {subject_prompt}. 
        Action: {en} {move}. 
        Speaking Line: "{vn}". Lip-sync: Match Vietnamese dialogue. 
        Context: Video regarding {symptom_select}. Constraint: NO TEXT. 
        --duration 15s
        """
    else:
        prompt = f"""
        Cinematic shot, {subject_prompt}. 
        Action: {en} {move}. Speaking. 
        Atmosphere: {current_pillar['tone']}. {style_kw}. 
        --duration 8s
        """
    st.code(prompt, language='text')
