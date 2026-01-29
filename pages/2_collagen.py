import streamlit as st

# =========================================================
# 1. CẤU HÌNH DỮ LIỆU (GIỮ NGUYÊN FULL 40 TRIỆU CHỨNG)
# =========================================================
st.set_page_config(page_title="Collagen Gold Mine v3.4", page_icon="🌸", layout="wide")

# 1.1 DATA 5 NHÓM - 40 TRIỆU CHỨNG (Chuẩn dữ liệu gốc của Moon)
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

# 1.2 DATA MAPPING (Giữ nguyên logic phân loại)
pillar_mapping = {
    "🌱 1. Nuôi dưỡng & Niềm tin": ["Kể chuyện (Storytelling)", "Tâm sự/Vlog"],
    "🎓 2. Giáo dục & Nhận thức": ["Cảnh báo sai lầm", "Góc chuyên gia (Myth vs Fact)", "Phản biện"],
    "💰 3. Chuyển đổi bán hàng": ["Trước - Sau (Transformation)", "Giải quyết vấn đề"],
    "❤️ 4. Chăm sóc & Giữ chân": ["Trải nghiệm/Review", "Q&A (Hỏi đáp)"]
}

# =========================================================
# 2. GIAO DIỆN INPUT (BỔ SUNG THANH TRƯỢT THỜI LƯỢNG)
# =========================================================

c1, c2 = st.columns([1, 4])
with c1: st.title("🌸")
with c2: 
    st.title("COLLAGEN GOLD MINE v3.4")
    st.caption("Phiên bản 'Viral Content': Tùy chỉnh Độ sâu & Thời lượng (15s/30s/60s)")

st.divider()

# --- HÀNG 1: Triệu chứng ---
col_group, col_symptom = st.columns(2)
with col_group:
    selected_group = st.selectbox("Nhóm triệu chứng:", list(symptom_groups.keys()))
with col_symptom:
    selected_symptom = st.selectbox("Triệu chứng cụ thể:", symptom_groups[selected_group])

# --- HÀNG 2: Mục tiêu & Kiểu video ---
col_pillar, col_type = st.columns(2)
with col_pillar:
    selected_pillar = st.selectbox("Mục tiêu (Trụ cột):", list(pillar_mapping.keys()))
with col_type:
    available_types = pillar_mapping[selected_pillar]
    selected_type = st.selectbox("Kiểu video:", available_types)

st.write("") 

# --- HÀNG 3: Cấu hình Video (BỔ SUNG SLIDER Ở ĐÂY) ---
c_duration, c_style, c_model = st.columns([2, 1, 1])
with c_duration:
    # MỚI: Thanh trượt chọn thời lượng kịch bản
    script_duration = st.select_slider(
        "⏳ Thời lượng Kịch bản mong muốn:",
        options=["15s (Shorts/Reels)", "30s (TikTok Chuẩn)", "60s (Youtube/Podcast)"],
        value="30s (TikTok Chuẩn)"
    )
with c_style:
    style_select = st.radio("Style:", ["3D (Bé Collagen)", "KOL (Moon)"])
with c_model:
    ai_model = st.radio("AI Model:", ["Sora (15s)", "Veo 3 (8s)"])

st.divider()

# =========================================================
# 3. XỬ LÝ LOGIC (BRAIN) - KẾT HỢP DỮ LIỆU CŨ & LOGIC MỚI
# =========================================================

symptom_name = selected_symptom.split(". ")[1]

# 3.1 LOGIC MỚI: Xử lý độ sâu nội dung theo thời lượng
if "15s" in script_duration:
    word_limit = "40-50 từ"
    depth_desc = "Tốc độ nhanh, Hook mạnh, đi thẳng vào giải pháp. Phù hợp lướt xem nhanh."
    pacing = "Nhanh, gọn, dứt khoát."
elif "30s" in script_duration:
    word_limit = "80-100 từ"
    depth_desc = "Cấu trúc chuẩn: Mở - Thân - Kết. Đủ thời gian để giải thích ngữ cảnh."
    pacing = "Vừa phải, rõ ràng."
else: # 60s (Youtube/Podcast)
    word_limit = "180-220 từ"
    depth_desc = "Nội dung SÂU SẮC (Deep). Xây dựng bối cảnh, miêu tả cảm xúc chi tiết, có khoảng lặng để người xem 'thấm'."
    pacing = "Chậm rãi, thủ thỉ, tâm tình, có điểm ngắt nghỉ cảm xúc."

# 3.2 LOGIC CŨ: Xử lý nội dung theo Mục tiêu (Giữ nguyên yêu cầu của Moon)
def get_detailed_instructions(pillar, v_type, symptom):
    instruction = ""
    tone = ""
    
    # --- NUÔI DƯỠNG (Logic Podcast cũ Moon thích) ---
    if "Nuôi dưỡng" in pillar:
        if "Kể chuyện" in v_type:
            instruction = f"""
            - Cấu trúc: Storytelling 3 hồi (Bối cảnh -> Biến cố -> Bài học).
            - Yêu cầu: Kể lại sự việc cụ thể (đi tiệc, họp hành...) bị '{symptom}' làm phiền.
            """
            tone = "Kể lể, dẫn dắt, Drama nhẹ nhàng."
        elif "Tâm sự" in v_type:
            instruction = f"""
            - Phong cách: **PODCAST/TÂM TÌNH**.
            - Yêu cầu: Thủ thỉ đêm khuya. Dùng từ ngữ giàu hình ảnh (ví dụ: 'nỗi buồn mỏng như sương', 'đêm trằn trọc').
            - Nội dung: Miêu tả khoảnh khắc cô đơn khi đối diện với '{symptom}'. 
            """
            tone = "Thủ thỉ, sâu lắng, chữa lành (Healing)."

    # --- GIÁO DỤC ---
    elif "Giáo dục" in pillar:
        instruction = f"""
        - Yêu cầu: Giải thích nguyên nhân gốc rễ của '{symptom}'. Phân tích sai lầm thường gặp.
        - Nội dung: Kiến thức chuyên gia nhưng dễ hiểu.
        """
        tone = "Chuyên gia, điềm đạm, tin cậy."

    # --- BÁN HÀNG ---
    elif "Bán hàng" in pillar:
        instruction = f"""
        - Yêu cầu: Khắc họa nỗi đau '{symptom}' -> Show ngay giải pháp Pizkie -> Kêu gọi mua hàng.
        - Nhấn mạnh: Sự thay đổi trước/sau.
        """
        tone = "Hào hứng, tự tin, năng lượng cao."

    # --- CHĂM SÓC ---
    elif "Chăm sóc" in pillar:
        instruction = f"""
        - Yêu cầu: Chia sẻ trải nghiệm thật, review chi tiết hoặc trả lời câu hỏi khách hàng.
        """
        tone = "Chân thực, gần gũi, hữu ích."
            
    return instruction, tone

inst_text, tone_text = get_detailed_instructions(selected_pillar, selected_type, symptom_name)

# =========================================================
# 4. HIỂN THỊ KẾT QUẢ
# =========================================================

tab1, tab2 = st.tabs(["📝 KỊCH BẢN (ChatGPT)", "🎬 VIDEO PROMPT"])

# --- TAB 1: OUTPUT CHO CHATGPT (Cập nhật thêm phần Thời lượng) ---
with tab1:
    st.subheader(f"Copy lệnh này gửi ChatGPT ({script_duration})")
    
    chatgpt_prompt = f"""
Đóng vai: Moon (Người kể chuyện chữa lành & Chuyên gia Collagen).
Nhiệm vụ: Viết kịch bản video ({script_duration}).
Chủ đề: {symptom_name}.
Mục tiêu: {selected_pillar}.
Kiểu video: {selected_type}.

⏳ YÊU CẦU VỀ THỜI LƯỢNG & ĐỘ SÂU:
- Thời lượng kịch bản: **{script_duration}**.
- Giới hạn từ: **{word_limit}** (Bắt buộc tuân thủ để khớp khẩu hình).
- Nhịp điệu (Pacing): {pacing}
- Độ sâu: {depth_desc}

🎨 TONE & STYLE: {tone_text}

👇 CẤU TRÚC OUTPUT:

1. CAPTION (Tiêu đề):
   - 1 câu giật tít (6-10 chữ) đậm chất văn học hoặc đánh trúng tim đen.

2. KỊCH BẢN CHI TIẾT (Voice-over):
   {inst_text}
   *(Lưu ý: Chia nhỏ các đoạn văn, đánh dấu chỗ cần ngắt nghỉ để đọc diễn cảm)*

3. HASHTAG (5 cái): #PizkieCollagen #{symptom_name.replace(" ","")} ...
"""
    st.code(chatgpt_prompt, language='text')

# --- TAB 2: OUTPUT CHO SORA (Giữ nguyên logic No Text) ---
with tab2:
    st.subheader(f"Prompt Video (Tạo nền Visual - {ai_model})")
    st.info("💡 Mẹo: Nếu làm video dài 60s, hãy dùng Prompt này tạo 4-5 clip ngắn rồi ghép lại để tránh bị lỗi hình ảnh.")
    
    if "3D" in style_select:
        visual = "Cute 3D character 'Baby Collagen', pink glowing skin, Disney Pixar style"
    else:
        visual = "Professional female KOL (Moon), 35yo, vietnamese, elegant, glowing skin"
        
    action = f"talking regarding {symptom_name}, {tone_text} vibe"
    if "Nuôi dưỡng" in selected_pillar:
        action = "cinematic close-up, emotional eyes looking at camera, soft lighting, gentle expression, storytelling mood"
    
    sora_prompt = f"""
Subject: {visual}. 
Action: {action}.
Lighting: Soft studio lighting, cinematic depth of field.
Constraint: ABSOLUTELY NO TEXT, NO CAPTIONS, NO LOGOS.
--duration {ai_model.split('(')[1].replace(')','')}
"""
    st.code(sora_prompt, language='text')
