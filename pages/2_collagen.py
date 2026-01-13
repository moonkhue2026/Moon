import streamlit as st

# Cài đặt trang web (Icon hoa anh đào cho Collagen)
st.set_page_config(page_title="Moon's Collagen Creator", page_icon="🌸", layout="centered")

# =========================================================
# DỮ LIỆU SẢN PHẨM (COLLAGEN)
# =========================================================

# 1. CONTEXT SẢN PHẨM
product_context = """
Sản phẩm: Collagen Peptide Thủy Phân (Hera Collagen).
Thành phần: Collagen Peptide nhập khẩu Đức/Nhật, Vitamin C, HA (Hyaluronic Acid), Chiết xuất lựu đỏ.
Công dụng: Căng bóng da, mờ nếp nhăn, cấp ẩm, giúp tóc móng chắc khỏe, chống lão hóa.
Ưu điểm: Dạng thủy phân hấp thu nhanh gấp 10 lần, không gây nóng, không nổi mụn, vị trái cây dễ uống.
Đối tượng: Phụ nữ sau 25 tuổi, da khô sạm, có nếp nhăn, muốn trẻ hóa.
Thương hiệu cá nhân: Moon - Người chia sẻ bí quyết "Lão hóa ngược".
"""

# 2. LỊCH TRÌNH (Giữ nguyên logic nhưng đổi tên chủ đề nếu cần)
schedule = {
    "Thứ 2": {"text": "Nuôi dưỡng (Nurture)", "video": "Kể chuyện (Story-based)"},
    "Thứ 3": {"text": "Không có bài viết", "video": "Giải quyết vấn đề (Problem)"},
    "Thứ 4": {"text": "Giáo dục (Educate)", "video": "Cảnh báo sai lầm (Warning)"},
    "Thứ 5": {"text": "Không có bài viết", "video": "Phản biện (Counter-Intuitive)"},
    "Thứ 6": {"text": "Chuyển đổi (Convert)", "video": "Trước - Sau (Transformation)"},
    "Thứ 7": {"text": "Không có bài viết", "video": "Trải nghiệm/Review"},
    "Chủ Nhật": {"text": "Nghỉ ngơi/Story", "video": "Hài hước/Trend"}
}

# 3. PROMPT TEXT (Đã sửa cho Collagen)
text_prompts = {
    "Nuôi dưỡng (Nurture)": "Viết bài Storytelling.\nChủ đề: Nỗi sợ già và mong muốn níu giữ thanh xuân.\nCấu trúc: Hook (Giật mình khi thấy nếp nhăn) -> Body (Hành trình tìm lại làn da căng mướt nhờ Collagen) -> Kết (Thông điệp yêu bản thân).\nTone: Tâm tình, thấu hiểu.",
    "Giáo dục (Educate)": "Viết bài Kiến thức.\nChủ đề: Tại sao uống Collagen mãi không đẹp? (Do chưa chọn đúng loại Peptide).\nCấu trúc: Hook (Sai lầm phổ biến) -> Body (Phân biệt Collagen thường vs Thủy phân Peptide) -> Kết (Chọn Hera để hấp thu tối đa).\nTone: Chuyên gia sắc đẹp.",
    "Chuyển đổi (Convert)": "Viết bài Bán hàng.\nChủ đề: Ưu đãi liệu trình 'Hồi sinh làn da'.\nCấu trúc: Hook (Show kết quả da căng bóng) -> Body (Giải quyết: Da khô, sạm -> Da mướt. Deal hời mua 3 tặng 1) -> CTA (Chốt đơn ngay).\nTone: Hào hứng, khan hiếm.",
    "Nghỉ ngơi/Story": "Viết Caption ngắn kèm ảnh chill/uống collagen.\nNội dung: Morning routine, skincare từ bên trong.\nTone: Sang chảnh, nhẹ nhàng."
}

# 4. KỊCH BẢN VIDEO (Đã sửa cho Collagen)
video_scripts = {
    "Kể chuyện (Story-based)": "🎬 KỊCH BẢN: THANH XUÂN TRỞ LẠI\n[0-15s] Soi gương thấy vết chân chim, thở dài buồn bã. Text: '25 tuổi mà ngỡ 35...'\n[15-45s] Uống Collagen Hera, da dẻ hồng hào, tự tin selfie. Text: 'Đánh thức thanh xuân mỗi sáng.'",
    "Giải quyết vấn đề (Problem)": "🎬 KỊCH BẢN: DA KHÔ MỐC?\n[0-15s] Makeup bị mốc nền (cakey), da nứt nẻ. Text: 'Da khô như ngói vỡ!'\n[15-45s] Uống Collagen, da ngậm nước căng bóng (Hiệu ứng nước). Text: 'Cấp nước tầng sâu, nền da mướt mịn.'",
    "Cảnh báo sai lầm (Warning)": "🎬 KỊCH BẢN: UỐNG SAI CÁCH\n[0-15s] Uống Collagen viên to khó nuốt hoặc loại gây nóng nổi mụn. Text: 'Dừng lại! Đừng nạp thêm mụn!'\n[15-30s] Chuyển sang Collagen Peptide Hera mát lành. Text: 'Chọn Peptide thủy phân, không lo nóng.'",
    "Phản biện (Counter-Intuitive)": "🎬 KỊCH BẢN: ĂN DA HEO BỔ SUNG COLLAGEN?\n[0-15s] Ăn đống da heo/chân gà. Lắc đầu. Text: 'Ăn cái này chỉ béo thôi!'\n[15-30s] Cầm gói Collagen nhỏ gọn. Text: '1 gói Hera = 10kg chân gà (về lượng Peptide).'",
    "Trước - Sau (Transformation)": "🎬 KỊCH BẢN: LỘT XÁC 28 NGÀY\n[0-20s] Trái: Da xám xịt, lỗ chân lông to. Text: 'Day 1: Tuyệt vọng.'\n[20-45s] Phải: Da phát sáng (Glass skin), mộc 100%. Text: 'Day 28: Chấp cả Camera thường.'",
    "Trải nghiệm/Review": "🎬 KỊCH BẢN: VLOG BUỔI SÁNG\n[0-20s] Cảnh pha Collagen màu hồng đỏ đẹp mắt, uống ngon lành. Text: 'Vị lựu đỏ ngon xỉu...'\n[20-45s] Zoom cận da. Text: 'Bí quyết da đẹp của Moon đây. Chị em thử ngay nha.'",
    "Hài hước/Trend": "🎬 KỊCH BẢN: BẮT TREND\nNhân vật (Bé Giọt Nước/Collagen) nhảy trend biến hình: Từ quả táo héo -> Quả táo căng mọng."
}

# --- GIAO DIỆN APP ---
st.title("🌸 MOON'S COLLAGEN CREATOR")
st.write("👉 **Mẹo:** Rê chuột vào góc phải khung đen để thấy nút **Copy** 📄")

# Sidebar
selected_day = st.selectbox("📅 Hôm nay là thứ mấy?", list(schedule.keys()))
today_task = schedule[selected_day]
video_topic = today_task['video']

st.info(f"Nhiệm vụ: {selected_day} | Video: {video_topic}")

# TABS
tab1, tab2 = st.tabs(["📝 BÀI VIẾT (CHATGPT)", "🎬 VIDEO (KỊCH BẢN & ẢNH)"])

with tab1:
    if today_task['text'] == "Không có bài viết":
        st.caption("Hôm nay nghỉ viết bài dài.")
    else:
        st.subheader("Copy lệnh này cho ChatGPT:")
        full_prompt = f"""Đóng vai Moon (Thương hiệu cá nhân sức khỏe & Sắc đẹp).
{product_context}
NHIỆM VỤ: {text_prompts[today_task['text']]}
YÊU CẦU: Viết tiếng Việt tự nhiên, sang trọng, dùng icon hoa lá, hashtag: #HeraCollagen #DepDa #LaoHoaNguoc #MoonBeauty"""
        st.code(full_prompt, language='text')

with tab2:
    st.subheader(f"Chủ đề: {video_topic}")
    
    # 1. KỊCH BẢN TEXT
    st.write("📜 **Kịch bản quay/dựng:**")
    st.code(video_scripts.get(video_topic, ""), language='text')
    
    st.divider()
    
    # 2. CHỌN PHONG CÁCH
    video_style = st.radio("Chọn phong cách video:", ["3D Animation (Mascot)", "KOL (Người thật)"], horizontal=True)
    
    if video_style == "3D Animation (Mascot)":
        st.write("🎨 **Prompt tạo ảnh 3D (Midjourney):**")
        # Prompt mới cho Collagen: Nhân vật Giọt nước/Tinh thể lấp lánh hoặc Cô gái Pixar da đẹp
        prompt_3d = f"/imagine prompt: A cute anthropomorphic glowing collagen drop character (or a cute pink crystal fairy). The character has big shiny eyes and smooth skin, looking happy in a scene about: {video_topic}. Pixar 3D style, soft pink and white lighting, beauty product photography aesthetic, 8k --ar 9:16"
        st.code(prompt_3d, language='text')
    else:
        st.info("💡 **HƯỚNG DẪN QUAY KOL (NGƯỜI THẬT):**")
        st.markdown("""
        * **Bối cảnh:** Bàn trang điểm, phòng ngủ sáng sủa, rèm trắng.
        * **Trang phục:** Đồ ngủ lụa hoặc đồ tập sáng màu (Gợi cảm giác tươi trẻ).
        * **Góc máy:** Ưu tiên góc quay cận da (Macro) để show độ căng bóng.
        * **Sản phẩm:** Cầm ly nước màu hồng/đỏ (Collagen vị lựu).
        """)
