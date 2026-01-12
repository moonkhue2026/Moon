import streamlit as st

# Cài đặt trang web
st.set_page_config(page_title="Moon's Content Creator", page_icon="🌙", layout="centered")

# --- 🔐 BẢO MẬT: CHECK MẬT KHẨU ---
def check_password():
    """Hàm kiểm tra mật khẩu đơn giản"""
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if not st.session_state["password_correct"]:
        st.subheader("🔒 Đăng nhập hệ thống")
        password = st.text_input("Nhập mật khẩu quản trị:", type="password")
        if st.button("Đăng nhập"):
            if password == "moonxinh":  # <--- SỬA MẬT KHẨU CỦA BẠN Ở ĐÂY
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("Sai mật khẩu rồi!")
        st.stop()  # Dừng lại, không chạy code bên dưới nếu chưa đăng nhập

check_password() # Gọi hàm kiểm tra

# =========================================================
# NỘI DUNG CHÍNH CỦA APP (CHỈ HIỆN KHI ĐÃ NHẬP ĐÚNG PASS)
# =========================================================

# 1. CONTEXT SẢN PHẨM
product_context = """
Sản phẩm: Sữa nghệ Hera.
Thành phần: Tinh chất Curcumin cao cấp, Sữa tách béo New Zealand, Đường cỏ ngọt Stevia.
Công dụng: Hỗ trợ đau dạ dày, trào ngược, lành vết thương, đẹp da, ngủ ngon.
Ưu điểm: Không hăng, không đắng, không nóng, không béo.
Đối tượng: Người đau dạ dày, mẹ bỉm sữa, người sợ béo.
Thương hiệu cá nhân: Moon - Chân thành, thủ thỉ, chuyên gia gần gũi.
"""

# 2. LỊCH TRÌNH
schedule = {
    "Thứ 2": {"text": "Nuôi dưỡng (Nurture)", "video": "Kể chuyện (Story-based)"},
    "Thứ 3": {"text": "Không có bài viết", "video": "Giải quyết vấn đề (Problem)"},
    "Thứ 4": {"text": "Giáo dục (Educate)", "video": "Cảnh báo sai lầm (Warning)"},
    "Thứ 5": {"text": "Không có bài viết", "video": "Phản biện (Counter-Intuitive)"},
    "Thứ 6": {"text": "Chuyển đổi (Convert)", "video": "Trước - Sau (Transformation)"},
    "Thứ 7": {"text": "Không có bài viết", "video": "Trải nghiệm/Review"},
    "Chủ Nhật": {"text": "Nghỉ ngơi/Story", "video": "Hài hước/Trend"}
}

# 3. PROMPT TEMPLATES (TEXT)
text_prompts = {
    "Nuôi dưỡng (Nurture)": "Viết bài Facebook Storytelling.\nChủ đề: Sự bận rộn và nhu cầu chăm sóc bản thân.\nCấu trúc: Hook (Than thở nhẹ) -> Body (Bình yên bên ly sữa Hera) -> Kết (Hỏi thăm).\nTone: Ấm áp, thủ thỉ.",
    "Giáo dục (Educate)": "Viết bài Kiến thức (Myth vs Fact).\nChủ đề: So sánh Nghệ tươi/Bột nghệ thường VS Tinh chất Curcumin Hera.\nCấu trúc: Hook (Giật tít sai lầm) -> Body (Khoa học đơn giản: Tách dầu, Cỏ ngọt) -> Kết (Khuyên dùng tinh chế).\nTone: Chuyên gia.",
    "Chuyển đổi (Convert)": "Viết bài Bán hàng (Sales).\nChủ đề: Feedback khách hoặc Kết quả bản thân.\nCấu trúc: Hook (Lời khen/Kết quả) -> Body (Nỗi đau cũ -> Thay đổi nhờ Hera) -> CTA (Mua ngay, ưu đãi).\nTone: Hào hứng, tự tin.",
    "Nghỉ ngơi/Story": "Viết Caption ngắn kèm ảnh đi chơi.\nNội dung: Chúc cuối tuần, nhắc giữ sức khỏe.\nTone: Vui vẻ."
}

# 4. KỊCH BẢN VIDEO
video_scripts = {
    "Kể chuyện (Story-based)": "🎬 KỊCH BẢN: TỪ MỆT MỎI ĐẾN HẠNH PHÚC\n[0-15s] Cảnh mệt mỏi, áp lực cuối ngày. Text: 'Đuối sức...'\n[15-45s] Uống Hera, tươi tỉnh, mỉm cười. Text: 'Nạp lại năng lượng yêu thương.'",
    "Giải quyết vấn đề (Problem)": "🎬 KỊCH BẢN: ĐAU DẠ DÀY\n[0-15s] Ôm bụng đau, nhăn nhó, tia sét đỏ. Text: 'Đau bao tử lại hành!'\n[15-45s] Uống Hera, bụng êm, giơ ngón tay Like. Text: 'Êm ru sau 1 ly.'",
    "Cảnh báo sai lầm (Warning)": "🎬 KỊCH BẢN: CẢNH BÁO PHA SAI\n[0-15s] Cầm ấm nước sôi sùng sục. Hiện dấu X ĐỎ. Text: 'Dừng lại! Nước sôi hỏng hết!'\n[15-30s] Pha nước ấm 40 độ. Uống ngon. Text: 'Nước ấm mới giữ được Curcumin.'",
    "Phản biện (Counter-Intuitive)": "🎬 KỊCH BẢN: SỢ BÉO?\n[0-15s] Đẩy đường trắng ra xa. Lắc đầu. Text: 'Sợ béo? Xưa rồi!'\n[15-30s] Ôm lá cỏ ngọt Stevia. Show eo thon. Text: 'Đường cỏ ngọt 0 Calo, dáng xinh.'",
    "Trước - Sau (Transformation)": "🎬 KỊCH BẢN: LỘT XÁC (SPLIT SCREEN)\n[0-20s] Trái: Da sạm, buồn, đau. Text: 'Trước khi gặp Hera...'\n[20-45s] Phải: Da hồng, vui, khỏe. Text: 'Sau 7 ngày: Khỏe đẹp từ bên trong.'",
    "Trải nghiệm/Review": "🎬 KỊCH BẢN: NHẬT KÝ 7 NGÀY\n[0-20s] Cảnh cắt nhanh 7 ngày uống sữa. Text: 'Ngày 1: Ngon. Ngày 3: Êm...'\n[20-45s] Chốt lại vui vẻ. Text: 'Duyệt nha! Mẹ nào đau bao tử inbox Moon.'",
    "Hài hước/Trend": "🎬 KỊCH BẢN: BẮT TREND\nNhân vật Bé Nghệ nhảy theo nhạc hot hoặc diễn cảnh hài hước về ăn uống healthy."
}

# --- GIAO DIỆN APP ---
st.title("🌙 MOON'S CREATOR v2.2 (Secured)")
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
        full_prompt = f"""Đóng vai Moon (Thương hiệu cá nhân sức khỏe).
{product_context}
NHIỆM VỤ: {text_prompts[today_task['text']]}
YÊU CẦU: Viết tiếng Việt tự nhiên, dùng icon, hashtag: #SuaNgheHera #HaPhanMinhNguyet"""
        st.code(full_prompt, language='text')

with tab2:
    st.subheader(f"Chủ đề: {video_topic}")
    
    # Kịch bản text
    st.write("📜 **Kịch bản quay/dựng:**")
    st.code(video_scripts.get(video_topic, ""), language='text')
    
    st.write("---")
    
    # Prompt ảnh 3D
    st.write("🎨 **Prompt tạo ảnh 3D (Midjourney):**")
    prompt_3d = f"/imagine prompt: A cute anthropomorphic turmeric root character acting in a scene about: {video_topic}. It is holding a glass of warm, creamy golden-yellow turmeric milk. Pixar 3D style, warm lighting, expressive face, 8k --ar 9:16"
    st.code(prompt_3d, language='text')
