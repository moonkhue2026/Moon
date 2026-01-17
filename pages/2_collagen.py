import streamlit as st

st.set_page_config(page_title="Moon's Collagen Matrix", page_icon="🌸", layout="wide")

# =========================================================
# 1. DỮ LIỆU: 40 TRIỆU CHỨNG
# =========================================================

pain_points = {
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
    "🛏️ Sinh lý & Tiêu hóa": [
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

# =========================================================
# 2. MA TRẬN CHIẾN LƯỢC (4 TRỤ CỘT)
# =========================================================

pillars = {
    "🌱 1. Nuôi dưỡng & Niềm tin": {
        "formats": ["Kể chuyện (Storytelling)", "Tâm sự/Vlog"],
        "goal": "Tạo sự đồng cảm, tôi cũng từng bị như bạn.",
        "tone": "Thủ thỉ, ấm áp, chân thành"
    },
    "🎓 2. Giáo dục & Nhận thức": {
        "formats": ["Cảnh báo sai lầm", "Góc chuyên gia (Myth vs Fact)", "Phản biện"],
        "goal": "Chỉ ra nguyên nhân gốc rễ (Thiếu hụt nội tiết/Collagen).",
        "tone": "Chuyên gia, nghiêm túc, tin cậy"
    },
    "💰 3. Chuyển đổi bán hàng": {
        "formats": ["Trước - Sau (Transformation)", "Giải quyết vấn đề"],
        "goal": "Show kết quả, chốt đơn, khan hiếm.",
        "tone": "Hào hứng, năng lượng cao, thúc giục"
    },
    "❤️ 4. Chăm sóc & Giữ chân": {
        "formats": ["Trải nghiệm/Review", "Q&A (Hỏi đáp)"],
        "goal": "Hướng dẫn sử dụng, chăm sóc khách cũ.",
        "tone": "Tận tâm, vui vẻ"
    }
}

# =========================================================
# GIAO DIỆN APP
# =========================================================

st.title("🌸 COLLAGEN GOLD MINE v3.3")
st.markdown(f"*Phiên bản Prompt chuẩn Nelly: Gom gọn & Tối ưu*")

# --- BƯỚC 1: CHỌN NỖI ĐAU ---
c1, c2 = st.columns(2)
with c1:
    group_select = st.selectbox("Nhóm triệu chứng:", list(pain_points.keys()))
with c2:
    symptom_select = st.selectbox("Triệu chứng cụ thể:", pain_points[group_select])

symptom_vn = symptom_select.split("(")[0].replace(".", "").strip() # Lấy tên tiếng Việt

# --- BƯỚC 2: CHỌN CHIẾN LƯỢC ---
c3, c4 = st.columns(2)
with c3:
    pillar_select = st.selectbox("Mục tiêu (Trụ cột):", list(pillars.keys()))
with c4:
    video_type = st.selectbox("Kiểu video:", pillars[pillar_select]["formats"])

# --- BƯỚC 3: CẤU HÌNH ---
st.write("---")
c5, c6, c7 = st.columns(3)
with c5:
    duration_option = st.select_slider("Thời lượng:", options=["15s", "30s", "45s", "60s"], value="15s")
with c6:
    style_select = st.radio("Style:", ["3D Animation (Bé Collagen)", "KOL (Moon)"], horizontal=True)
with c7:
    model_select = st.radio("AI Model:", ["Sora (15s)", "Veo 3 (8s)"], horizontal=True)

# =========================================================
# XỬ LÝ LOGIC PROMPT (CHUNKING LOGIC)
# =========================================================

# Setup Style
if style_select == "3D Animation (Bé Collagen)":
    subject_prompt = "a cute anthropomorphic pink collagen drop character"
    visual_style = "Pixar style, soft lighting, 8k"
    move = "bouncy animation"
else:
    subject_prompt = "a beautiful Vietnamese woman 35yo (Moon), glowing skin, silk pajamas"
    visual_style = "Beauty commercial, Arri Alexa, 8k"
    move = "natural acting"

t_num = int(duration_option.replace("s", ""))
prompts_list = []
tone = pillars[pillar_select]["tone"]

# --- TẠO NỘI DUNG DỰA TRÊN TRỤ CỘT ---
if "Nuôi dưỡng" in pillar_select:
    script_summary = f"- HOOK: Đồng cảm 'Có ai bị {symptom_vn} như Moon không?'.\n- BODY: Kể chuyện đêm trằn trọc/soi gương thấy già.\n- CTA: Kêu gọi thả tim kết nối."
    action_15s = f"Start with close up of {subject_prompt} looking sad/tired. Cut to {subject_prompt} sighing at mirror. End with hugging self warmly."
    dialogue_15s = f"Có ai như Moon không? Dạo này bị {symptom_vn} hành hạ khổ sở. Ai cùng cảnh ngộ thì thả tim nha."

elif "Giáo dục" in pillar_select:
    script_summary = f"- HOOK: Cảnh báo '{symptom_vn} là dấu hiệu báo động'.\n- BODY: Giải thích nguyên nhân tụt collagen.\n- CTA: Kêu gọi bổ sung ngay."
    action_15s = f"Start with {subject_prompt} holding a red alert sign. Cut to pointing at a chart showing collagen decline. End with a serious nod."
    dialogue_15s = f"Cảnh báo! {symptom_vn} không tự nhiên mà có! Đó là tiếng kêu cứu của cơ thể khi thiếu Collagen. Bổ sung ngay đi nhé."

elif "Chuyển đổi" in pillar_select:
    script_summary = f"- HOOK: Show kết quả 'Tạm biệt {symptom_vn}'.\n- BODY: Uống Hera Collagen ngon lành.\n- CTA: Chốt đơn ưu đãi."
    action_15s = f"Start with {subject_prompt} showing glowing happy face. Cut to drinking pink collagen liquid enthusiastically. End with holding a 'Sale' sign."
    dialogue_15s = f"Tạm biệt {symptom_vn} chỉ sau 1 liệu trình! Nhờ em Hera Collagen này đây. Mua 3 tặng 1, rinh ngay kẻo lỡ!"

else: # Chăm sóc
    script_summary = f"- HOOK: Trả lời câu hỏi 'Uống bao lâu thì đỡ?'.\n- BODY: Show lịch trình 2 tuần.\n- CTA: Dặn dò uống đúng giờ."
    action_15s = f"Start with {subject_prompt} reading phone comments. Cut to showing a calendar with 2 weeks marked. End with blowing a kiss."
    dialogue_15s = f"Nhiều chị hỏi Moon uống bao lâu thì hết {symptom_vn}? Thường là 2 tuần nha. Nhớ uống đúng giờ Moon dặn nhé!"

# --- LOGIC CHIA PROMPT (15s BLOCKS) ---

if t_num == 15:
    prompts_list.append({
        "title": "🎞️ FULL VIDEO (15s)",
        "action": action_15s,
        "dialogue": dialogue_15s
    })

elif t_num == 30:
    prompts_list.append({
        "title": "🎞️ PHẦN 1 (0-15s): Mở đầu & Vấn đề",
        "action": f"Part 1 of 2. {action_15s.split('.')[0]}. Character explains the problem/situation with {tone} expression.",
        "dialogue": f"Về chuyện {symptom_vn} này, Moon muốn chia sẻ thật lòng với mọi người..."
    })
    prompts_list.append({
        "title": "🎞️ PHẦN 2 (15-30s): Giải pháp & Kết thúc",
        "action": f"Part 2 of 2. {action_15s.split('.')[-1]}. Character shows solution/happy result. Ends with call to action.",
        "dialogue": f"Đó là lý do tại sao Moon chọn cách này. Thử ngay và cho Moon biết kết quả nha!"
    })

elif t_num == 45:
    prompts_list.append({"title": "🎞️ PHẦN 1 (0-15s)", "action": f"Intro to {symptom_vn}, showing emotion", "dialogue": "Chào cả nhà..."})
    prompts_list.append({"title": "🎞️ PHẦN 2 (15-30s)", "action": "Deep dive/Explanation/Process", "dialogue": "Mọi người nhớ lưu ý..."})
    prompts_list.append({"title": "🎞️ PHẦN 3 (30-45s)", "action": "Result & CTA", "dialogue": "Kết quả bất ngờ chưa..."})

else: # 60s
    prompts_list.append({"title": "🎞️ PHẦN 1 (0-15s)", "action": f"Vlog intro about {symptom_vn}", "dialogue": "Hôm nay tâm sự mỏng..."})
    prompts_list.append({"title": "🎞️ PHẦN 2 (15-30s)", "action": "Sharing details/Storytelling", "dialogue": "Chuyện là thế này..."})
    prompts_list.append({"title": "🎞️ PHẦN 3 (30-45s)", "action": "Solution/Advice", "dialogue": "Moon khuyên thật lòng..."})
    prompts_list.append({"title": "🎞️ PHẦN 4 (45-60s)", "action": "Conclusion & Goodbye", "dialogue": "Yêu cả nhà nhiều!"})

# =========================================================
# HIỂN THỊ KẾT QUẢ
# =========================================================

# 1. Kịch bản tóm tắt (Luôn hiển thị đầu tiên)
with st.expander("📜 KỊCH BẢN TÓM TẮT (Tiếng Việt)", expanded=True):
    st.info(script_summary)

st.divider()

# 2. Tabs: Video & Bài viết
tab_video, tab_blog = st.tabs(["🎥 VIDEO PROMPT", "📝 BÀI VIẾT FACEBOOK"])

with tab_video:
    st.subheader(f"Prompt tạo video ({model_select})")
    
    for p in prompts_list:
        st.markdown(f"**{p['title']}**")
        
        if "Sora" in model_select:
            # Code Sora (Gộp)
            prompt = f"""
            {visual_style}.
            Subject: {subject_prompt}.
            Action: {p['action']}. {move}.
            Speaking Line (Vietnamese): "{p['dialogue']}"
            Lip-sync instruction: Match Vietnamese dialogue naturally.
            Context: Video about {symptom_vn}. Constraint: NO TEXT OVERLAYS.
            --duration 15s
            """
            st.code(prompt, language='text')
            st.caption(f"🗣️ Thoại: \"{p['dialogue']}\"")
        else:
            # Code Veo (8s)
            prompt = f"""
            Cinematic shot, {subject_prompt}.
            Action: {p['action'].split('.')[0]}. Speaking.
            Atmosphere: {tone}. {visual_style}.
            --duration 8s
            """
            st.code(prompt, language='text')
        
        st.divider()

with tab_blog:
    st.subheader("Copy lệnh cho ChatGPT:")
    st.code(f"""
    Đóng vai chuyên gia Moon. Viết bài về nỗi đau: **{symptom_vn}**.
    - Mục tiêu: {pillar_select}.
    - Tone giọng: {tone}.
    - Hashtag: #{symptom_vn.replace(' ','')} #HeraCollagen
    """, language='text')
