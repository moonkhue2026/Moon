import streamlit as st

# =========================================================
# 1. CẤU HÌNH DỮ LIỆU (CHUẨN 40 TRIỆU CHỨNG - 5 NHÓM)
# =========================================================
st.set_page_config(page_title="Collagen Gold Mine v3.3", page_icon="🌸", layout="wide")

# 1.1 DATA 5 NHÓM - 40 TRIỆU CHỨNG (Full data từ Screenshot 192 & 193)
symptom_groups = {
    "🔥 Bốc hỏa & Nhiệt độ cơ thể": [
        "1. Cơn bốc hỏa (Hot flashes)", 
        "2. Ớn lạnh (Cold flashes)",
        "3. Đổ mồ hôi đêm (Night sweats)", 
        "4. Cảm giác dính nhớp (Clammy feeling)",
        "32. Thay đổi mùi cơ thể (Changed body odor)",
        "33. Cảm giác như điện giật (Electric shock feelings)"
    ],
    "🧠 Tâm lý & Thần kinh": [
        "6. Cáu gắt (Irritability)", 
        "7. Tâm trạng thất thường (Mood swings)", 
        "13. Lo âu (Anxiety)", 
        "14. Trầm cảm (Depression)",
        "15. Mất tập trung (Lack of focus)",
        "16. Kém tập trung (Poor concentration)",
        "17. Hay quên (Faulty memory)",
        "23. Đau đầu (Headaches)",
        "30. Chóng mặt (Dizziness)",
        "31. Choáng váng (Vertigo)"
    ],
    "💅 Ngoại hình (Da/Tóc/Móng)": [
        "27. Tăng cân (Weight gain)",
        "28. Rụng tóc/Tóc mỏng (Hair loss)", 
        "39. Móng tay yếu/gãy (Weakened fingernails)",
        "19. Ngứa da/Kiến bò (Itchy, crawly skin)",
        "29. Mọc ria mép (More facial hair)",
        "35. Chảy máu nướu (Bleeding gums)",
        "37. Hôi miệng mãn tính (Chronic bad breath)"
    ],
    "🦴 Cơ thể & Vận động": [
        "20. Đau nhức xương khớp (Achy joints)",
        "21. Căng cơ (Tense muscles)",
        "38. Loãng xương (Osteoporosis)", 
        "12. Mệt mỏi kiệt sức (Fatigue)",
        "5. Tim đập nhanh (Heart palpitations)",
        "40. Ù tai (Ringing ears/Tinnitus)",
        "34. Tê bì chân tay (Tingling extremities)",
        "36. Rát lưỡi/Vòm miệng (Burning tongue)"
    ],
    "🛌 Sinh lý & Tiêu hóa": [
        "8. Khó ngủ (Trouble sleeping)",
        "10. Giảm ham muốn (Low sex drive)",
        "11. Khô hạn (Dry vagina)",
        "9. Rối loạn kinh nguyệt (Irregular periods)",
        "22. Đau ngực (Sore breasts)",
        "18. Són tiểu (Incontinence)",
        "24. Vấn đề tiêu hóa (Digestive issues)",
        "25. Đầy hơi (Bloating)",
        "26. Dị ứng nặng hơn (Allergies worsen)"
    ]
}

# 1.2 DATA MAPPING: MỤC TIÊU -> KIỂU VIDEO
pillar_mapping = {
    "🌱 1. Nuôi dưỡng & Niềm tin": ["Kể chuyện (Storytelling)", "Tâm sự/Vlog"],
    "🎓 2. Giáo dục & Nhận thức": ["Cảnh báo sai lầm", "Góc chuyên gia (Myth vs Fact)", "Phản biện"],
    "💰 3. Chuyển đổi bán hàng": ["Trước - Sau (Transformation)", "Giải quyết vấn đề"],
    "❤️ 4. Chăm sóc & Giữ chân": ["Trải nghiệm/Review", "Q&A (Hỏi đáp)"]
}

# =========================================================
# 2. GIAO DIỆN CHỌN (INPUT)
# =========================================================

c1, c2 = st.columns([1, 4])
with c1: st.title("🌸")
with c2: 
    st.title("COLLAGEN GOLD MINE v3.3")
    st.caption("Phiên bản Prompt chuẩn Nelly: Full 40 Triệu chứng & Logic Phân loại sâu")

st.divider()

# --- HÀNG 1: Triệu chứng ---
col_group, col_symptom = st.columns(2)
with col_group:
    selected_group = st.selectbox("Nhóm triệu chứng:", list(symptom_groups.keys()))
with col_symptom:
    selected_symptom = st.selectbox("Triệu chứng cụ thể:", symptom_groups[selected_group])

# --- HÀNG 2: Mục tiêu & Kiểu video (Logic Mẹ chọn gì Con hiện nấy) ---
col_pillar, col_type = st.columns(2)
with col_pillar:
    selected_pillar = st.selectbox("Mục tiêu (Trụ cột):", list(pillar_mapping.keys()))
with col_type:
    # Lọc danh sách video theo mục tiêu
    available_types = pillar_mapping[selected_pillar]
    selected_type = st.selectbox("Kiểu video:", available_types)

st.write("") 

# --- HÀNG 3: Cấu hình Video ---
col_style, col_model = st.columns(2)
with col_style:
    style_select = st.radio("Style:", ["3D Animation (Bé Collagen)", "KOL (Moon)"], horizontal=True)
with col_model:
    ai_model = st.radio("AI Model:", ["Sora (15s)", "Veo 3 (8s)"], horizontal=True)

st.divider()

# =========================================================
# 3. XỬ LÝ LOGIC NỘI DUNG (BRAIN)
# =========================================================

symptom_name = selected_symptom.split(". ")[1] # Lấy tên triệu chứng bỏ số thứ tự

def get_detailed_instructions(pillar, v_type, symptom):
    instruction = ""
    tone = ""
    
    # --- NHÓM 1: NUÔI DƯỠNG ---
    if "Nuôi dưỡng" in pillar:
        if "Kể chuyện" in v_type:
            instruction = f"""
            - Cấu trúc: 3 hồi (Bối cảnh đời thường -> Biến cố khi cơn '{symptom}' ập tới -> Bài học rút ra).
            - Yêu cầu: Kể lại một sự việc cụ thể (ví dụ: đang đi tiệc, họp lớp, gặp đối tác...).
            - Chi tiết: Miêu tả kỹ sự bối rối, khó xử hoặc mệt mỏi lúc đó.
            """
            tone = "Kể lể, dẫn dắt, Drama nhẹ nhàng."
        elif "Tâm sự" in v_type:
            instruction = f"""
            - Cấu trúc: Monologue (Độc thoại).
            - Yêu cầu: Không cần cốt truyện, tập trung vào CẢM XÚC nội tâm thầm kín nhất về '{symptom}'.
            - Thông điệp: 'Moon hiểu cảm giác đó', 'Bạn không cô đơn'.
            """
            tone = "Thủ thỉ, sâu lắng, chữa lành (Healing)."

    # --- NHÓM 2: GIÁO DỤC ---
    elif "Giáo dục" in pillar:
        if "Cảnh báo" in v_type:
            instruction = f"""
            - Hook: 'Dừng ngay...', 'Sai lầm tai hại khi trị {symptom}...'.
            - Body: Chỉ ra thói quen sai lầm mà chị em hay mắc phải. Hậu quả là gì.
            """
            tone = "Nghiêm túc, Cảnh báo, Mạnh mẽ."
        elif "Góc chuyên gia" in v_type:
            instruction = f"""
            - Hook: Sự thật về '{symptom}' mà bác sĩ ít nói cho bạn biết.
            - Body: Giải thích cơ chế thiếu hụt Collagen/Nội tiết gây ra vấn đề này thế nào. Dùng ngôn ngữ khoa học dễ hiểu.
            """
            tone = "Uy tín, Chuyên gia, Khách quan."
        elif "Phản biện" in v_type:
            instruction = f"""
            - Hook: 'Mọi người tưởng A... nhưng thực tế là B'.
            - Body: Lật ngược quan điểm cũ kỹ về cách chăm sóc '{symptom}'.
            """
            tone = "Thẳng thắn, Sắc sảo."

    # --- NHÓM 3: BÁN HÀNG ---
    elif "Bán hàng" in pillar:
        if "Trước - Sau" in v_type:
            instruction = f"""
            - Yêu cầu: Tập trung miêu tả sự đối lập. Trước đây khổ sở vì '{symptom}' thế nào -> Sau khi dùng Pizkie thay đổi ra sao.
            - Nhấn mạnh: Kết quả nhìn thấy được.
            """
            tone = "Hào hứng, Tự hào, Wow."
        elif "Giải quyết vấn đề" in v_type:
            instruction = f"""
            - Cấu trúc: Nỗi đau (Pain) -> Giải pháp (Pizkie Collagen) -> Lợi ích (Gain).
            - Kêu gọi hành động: Mua ngay ưu đãi.
            """
            tone = "Dứt khoát, Thuyết phục, Kêu gọi (Sales)."

    # --- NHÓM 4: CHĂM SÓC ---
    elif "Chăm sóc" in pillar:
        if "Trải nghiệm" in v_type:
            instruction = f"""
            - Format: Review chân thực như người dùng.
            - Nội dung: 'Sau 2 tuần Moon thấy...', 'Cảm nhận vị thế nào', 'Thay đổi nhỏ gì đầu tiên'.
            """
            tone = "Chân thực, Gần gũi, Khách quan."
        elif "Q&A" in v_type:
            instruction = f"""
            - Format: Đọc câu hỏi của khách -> Trả lời ngắn gọn.
            - Câu hỏi: Liên quan đến cách dùng Collagen trị '{symptom}'.
            """
            tone = "Tận tâm, Hữu ích, Nhanh gọn."
            
    return instruction, tone

inst_text, tone_text = get_detailed_instructions(selected_pillar, selected_type, symptom_name)

# =========================================================
# 4. HIỂN THỊ KẾT QUẢ (TAB)
# =========================================================

tab1, tab2 = st.tabs(["📝 BÀI VIẾT (ChatGPT)", "🎬 VIDEO PROMPT (Sora)"])

# --- TAB 1: LỆNH CHATGPT (Update Caption 6-10 chữ & Hashtag) ---
with tab1:
    st.subheader("Copy lệnh này gửi cho ChatGPT:")
    chatgpt_prompt = f"""
Đóng vai: Chuyên gia Moon (Am hiểu tâm lý phụ nữ trung niên).
Nhiệm vụ: Viết nội dung Facebook & Kịch bản video ngắn.
Chủ đề: {symptom_name}.
Mục tiêu: {selected_pillar}.
Kiểu video: {selected_type}.

👇 YÊU CẦU CẤU TRÚC OUTPUT:

1. CAPTION (Tiêu đề):
   - Viết 1 câu giật tít (độ dài 6-10 chữ).
   - Yêu cầu: Đánh trúng nỗi đau thầm kín hoặc gây tò mò về '{symptom_name}'.

2. NỘI DUNG CHÍNH (Thân bài):
{inst_text}

3. HASHTAG:
   - Viết đúng 5 hashtag liên quan nhất (Ví dụ: #PizkieCollagen #{symptom_name.replace(" ","")} #MoonShare...)

4. TONE GIỌNG: {tone_text}
"""
    st.code(chatgpt_prompt, language='text')

# --- TAB 2: PROMPT SORA (Update "Sạch", No Text) ---
with tab2:
    st.subheader(f"Prompt Video ({ai_model.split(' ')[0]})")
    
    # Logic Visual
    if "3D" in style_select:
        visual_subject = "Cute 3D character 'Baby Collagen', pink glowing skin, friendly expression, Disney Pixar style render"
    else:
        visual_subject = "Professional female KOL (Moon), 35 years old, vietnamese, elegant fashion, glowing skin, natural makeup"
        
    # Logic Action (Tùy biến theo kiểu video)
    action_desc = f"talking expressively about health, {tone_text} vibe"
    if "Kể chuyện" in selected_type: 
        action_desc = "hand gestures retelling a story, sitting in a cozy coffee shop, expressive face"
    elif "Tâm sự" in selected_type: 
        action_desc = "close-up shot, looking directly at camera lens, soft eye contact, gentle smile, speaking softly, bedroom background"
    elif "Trước - Sau" in selected_type: 
        action_desc = "split screen effect (optional) or transition from tired face to glowing happy face"
    elif "Review" in selected_type:
        action_desc = "holding a small collagen bottle, pointing at it, nodding in approval"
    
    # Prompt chuẩn Sora (Tuyệt đối không chữ)
    sora_prompt = f"""
Subject: {visual_subject}.
Action: {action_desc}.
Lighting: Soft studio lighting, cinematic depth of field.
Quality: 8k resolution, photorealistic, highly detailed.
Constraint: ABSOLUTELY NO TEXT, NO CAPTIONS, NO LOGOS, NO WATERMARKS, NO ONSCREEN TEXT.
--duration {ai_model.split('(')[1].replace(')','')}
"""
    st.code(sora_prompt, language='text')
