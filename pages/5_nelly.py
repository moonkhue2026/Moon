import streamlit as st
import datetime
import random

# --- CẤU HÌNH TRANG (Giữ nguyên vẻ sang trọng) ---
st.set_page_config(
    page_title="Nelly's Week v9.8 - Fashion & Lifestyle Manager",
    page_icon="👠",
    layout="wide"
)

# --- CSS TÙY CHỈNH (Giữ nguyên) ---
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; font-weight: 700; color: #333; text-align: center; }
    .sub-header { font-size: 1.2rem; font-style: italic; color: #666; text-align: center; margin-bottom: 10px; }
    .version-caption { text-align: center; color: #888; font-size: 0.9rem; margin-bottom: 30px; }
    /* Style cho các box nhiệm vụ */
    .task-box-sang { border-left: 5px solid #d4af37; background-color: #fffbf0; padding: 15px; border-radius: 8px; }
    .task-box-chieu { border-left: 5px solid #333; background-color: #f4f4f4; padding: 15px; border-radius: 8px; }
    .task-box-toi { border-left: 5px solid #9c27b0; background-color: #f8f0fb; padding: 15px; border-radius: 8px; }
    /* Style cho tiêu đề ngày */
    .day-header { color: #d4af37; font-weight: bold; font-size: 1.3rem; margin-top: 20px;}
    /* Nút bấm */
    .stButton>button { border-radius: 20px; }
    /* Style cho code block */
    .stCode { border: 1px solid #d4af37; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# --- DỮ LIỆU: KHO PROMPT MẪU (ĐÃ KIỆN TOÀN Ở v9.7) ---
prompts = {
    # 1. Prompt cho Status/Caption ngắn
    "stt_sangchanh": """
Tôi là Nelly, một KOL Fashion & Lifestyle theo phong cách sang trọng, hiện đại, tự tin.
Hãy viết cho tôi một caption Facebook/Instagram ngắn (dưới 100 từ) kèm 3 hashtag.
Chủ đề: [Chủ đề nhiệm vụ hiện tại].
Tone giọng: Quyền lực, tự tin, truyền cảm hứng nhưng vẫn gần gũi.
Yêu cầu bắt buộc:
- Bắt đầu bằng một câu hook (câu dẫn) ấn tượng để thu hút sự chú ý ngay lập tức.
- Sử dụng ngôn từ tinh tế, đắt giá, tránh dùng từ ngữ quá bình dân hoặc sến súa để giữ vững hình ảnh sang trọng.
""",

    # 2. Prompt cho Kịch bản video ngắn
    "video_kịch_bản": """
Tôi là Nelly (KOL Fashion/Lifestyle sang trọng). Hãy viết cho tôi một kịch bản video ngắn (Reels/TikTok) khoảng 30-45 giây.
Chủ đề: [Chủ đề nhiệm vụ hiện tại].
Tone giọng: Năng động, cuốn hút, chuyên nghiệp.
Cấu trúc:
- 0-3s (Hook): Gây tò mò hoặc đánh vào nỗi đau/mong muốn của khán giả.
- 3-15s (Thân): Chia sẻ 2-3 tips chính hoặc show các góc quay đẹp nhất.
- 15s+ (Call to Action): Kêu gọi tương tác (lưu lại, chia sẻ, follow).
Yêu cầu thêm:
- Mô tả ngắn gọn hành động hoặc bối cảnh (Visual cues) trong ngoặc đơn () để người quay dễ hình dung. Ví dụ: (Cận cảnh tay cầm túi), (Góc toàn cảnh bước đi tự tin).
""",

    # 3. Prompt cho bài viết dài/hướng dẫn
    "guide_post": """
Tôi là Nelly (KOL Fashion/Lifestyle sang trọng). Hãy viết một bài blog/bài post Facebook chi tiết, sâu sắc.
Chủ đề: [Chủ đề nhiệm vụ hiện tại].
Tone giọng: Chuyên gia, tinh tế, chia sẻ chân thành như một người chị đi trước.
Cấu trúc:
1. Tiêu đề thu hút (có thể dùng con số).
2. Đặt vấn đề (Tại sao việc này quan trọng với phụ nữ hiện đại?).
3. Giải pháp chi tiết (Các bước thực hiện cụ thể, các tips nhỏ "đắt giá").
4. Kết luận truyền cảm hứng & Kêu gọi hành động nhẹ nhàng.
Yêu cầu trình bày:
- Sử dụng emoji tinh tế, phù hợp, không lạm dụng quá nhiều.
- Chia đoạn rõ ràng, dễ đọc trên điện thoại.
"""
}

# --- DỮ LIỆU: LỊCH TRÌNH CỐ ĐỊNH CẢ TUẦN (Giữ nguyên) ---
weekly_plan = {
    # --- THỨ 2 ---
    ("Monday", "Sáng"): {
        "task": "🔥 Khởi động tuần mới: Power Outfit & Kế hoạch",
        "detail": "Chọn một bộ đồ 'quyền lực' nhất (Power Outfit) để đi họp hoặc cafe đầu tuần. Thể hiện thần thái tổng tài/sang chảnh để set mood cho cả tuần.",
        "prompt_type": "stt_sangchanh"
    },
    ("Monday", "Chiều"): {
        "task": "✨ Thử thách Styling: Biến đồ công sở nhàm chán thành Sang chảnh",
        "detail": "Lấy một món basic (sơ mi trắng/quần âu đen) và dùng phụ kiện cao cấp (khăn lụa, trang sức gold, túi hiệu) để nâng tầm nó. Quay video biến hình.",
        "prompt_type": "video_kịch_bản"
    },
    ("Monday", "Tối"): {
        "task": "Self-care: Dưỡng da Luxury & Tổng kết",
        "detail": "Routine skincare buổi tối thư giãn với các sản phẩm yêu thích. Viết một story nhẹ nhàng tổng kết cảm xúc.",
        "prompt_type": "stt_sangchanh"
    },

    # --- THỨ 3 ---
    ("Tuesday", "Sáng"): {
        "task": "Cafe sáng & Chụp ảnh flatlay phụ kiện",
        "detail": "Đi một quán cafe đẹp, sang trọng. Sắp xếp và chụp ảnh flatlay chi tiết các phụ kiện (túi, giày, kính, nước hoa) bạn dùng hôm nay.",
        "prompt_type": "stt_sangchanh"
    },
    ("Tuesday", "Chiều"): {
        "task": "Quay Video: Tips phối màu trang phục (Color Blocking/Monochrome)",
        "detail": "Chia sẻ kiến thức về phối màu sao cho sang trọng, không bị lòe loẹt.",
        "prompt_type": "video_kịch_bản"
    },
    ("Tuesday", "Tối"): {
        "task": "Nghiên cứu trend & Tương tác cộng đồng",
        "detail": "Dành thời gian lướt Pinterest/Vogue nắm bắt xu hướng. Trả lời Q&A trên Story để giữ kết nối.",
        "prompt_type": None # Không cần prompt
    },

    # --- THỨ 4 ---
    ("Wednesday", "Sáng"): {
        "task": "Họp đối tác/Sự kiện & OOTD Chuyên nghiệp",
        "detail": "Trang phục đi gặp đối tác quan trọng. Chia sẻ góc nhìn về sự chuyên nghiệp và thần thái trong công việc.",
        "prompt_type": "stt_sangchanh"
    },
    ("Wednesday", "Chiều"): {
        "task": "Review sản phẩm High-end (Mỹ phẩm/Thời trang)",
        "detail": "Bài viết review chi tiết một sản phẩm đắt tiền bạn tâm đắc. Nhấn mạnh vào trải nghiệm, chất lượng xứng đáng với giá tiền.",
        "prompt_type": "guide_post"
    },
    ("Wednesday", "Tối"): {
        "task": "Wellness: Tập luyện giữ dáng (Pilates/Yoga)",
        "detail": "Chia sẻ hình ảnh tập luyện trong không gian đẹp. Truyền cảm hứng về lối sống lành mạnh, yêu bản thân.",
        "prompt_type": "stt_sangchanh"
    },
    # (Các ngày khác có thể bổ sung tiếp tục theo cấu trúc này)
}

# Hàm hỗ trợ lấy ngày trong tuần (tiếng Anh để khớp với data)
def get_weekday_name(day_index):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[day_index]

# Hàm tạo block hiển thị prompt (Logic giữ nguyên)
def show_prompt_block(prompt_key, task_subject):
    if prompt_key in prompts:
        st.markdown("#### 🤖 Gợi ý câu lệnh (Prompt) cho ChatGPT:")
        st.info("👉 Copy toàn bộ đoạn code bên dưới và dán vào ChatGPT để nhận nội dung chất lượng như trong ảnh mẫu nha!")
        # Thay thế [Chủ đề...] bằng nhiệm vụ thực tế
        final_prompt = prompts[prompt_key].replace("[Chủ đề nhiệm vụ hiện tại]", task_subject)
        # Hiển thị dạng code block để dễ copy
        st.code(final_prompt, language="markdown")
    else:
        st.warning("Nhiệm vụ này cần sự sáng tạo tự do của Nelly, không có prompt mẫu!")

# --- GIAO DIỆN CHÍNH ---
st.markdown('<p class="main-header">👠 NELLY\'S WEEKLY MANAGER & AI PROMPTS</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">"Quản lý lịch trình sang trọng & Lấy prompt chuẩn chỉ trong 1 cú click"</p>', unsafe_allow_html=True)
# Cập nhật phiên bản hiển thị
st.markdown('<p class="version-caption">Phiên bản: Nelly v9.8 (Kiện toàn Prompt)</p>', unsafe_allow_html=True)


# Thanh chọn ngày
today = datetime.date.today()
days_in_week = [today + datetime.timedelta(days=i) for i in range(7)]
day_mapping = {day.strftime("%Y-%m-%d"): get_weekday_name(day.weekday()) for day in days_in_week}
vietnamese_days = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"]
day_labels = [f"{vietnamese_days[day.weekday()]} - {day.strftime('%d/%m')}" for day in days_in_week]

selected_day_label = st.selectbox("📅 Chọn ngày bạn muốn xem lịch:", day_labels, index=0)
selected_date_str = days_in_week[day_labels.index(selected_day_label)].strftime("%Y-%m-%d")
selected_weekday_en = day_mapping[selected_date_str]

st.divider()

# --- HIỂN THỊ NHIỆM VỤ THEO 3 BUỔI ---
task_sang = weekly_plan.get((selected_weekday_en, "Sáng"))
task_chieu = weekly_plan.get((selected_weekday_en, "Chiều"))
task_toi = weekly_plan.get((selected_weekday_en, "Tối"))

# Sử dụng st.tabs cho 3 buổi
tab1, tab2, tab3 = st.tabs(["🌅 SÁNG (Morning)", "☀️ CHIỀU (Afternoon)", "🌙 TỐI (Evening)"])

# --- TAB SÁNG ---
with tab1:
    if task_sang:
        st.markdown(f'<div class="task-box-sang"><h3>{task_sang["task"]}</h3><p>{task_sang["detail"]}</p></div>', unsafe_allow_html=True)
        st.divider()
        
        st.write("### 👩‍💻 Khu vực sáng tạo & Lấy Prompt")
        # Radio button chọn loại content (Ví dụ cho Thứ 2 Sáng)
        content_type_am = st.radio("Chọn loại nội dung sẽ làm:", ["Ảnh OOTD kèm Caption chất", "Story nhanh"], horizontal=True, key="am_radio")
        
        if content_type_am == "Ảnh OOTD kèm Caption chất":
            # Hiển thị prompt mặc định của task đó
            if task_sang.get("prompt_type"):
                show_prompt_block(task_sang["prompt_type"], task_sang["task"])

        st.text_area("✍️ Ghi chú thêm:", height=80, key="am_note")
        st.checkbox("✅ Đã hoàn thành", key="am_check")
    else:
        st.info("Chưa có lịch cho buổi sáng này. Enjoy your free time!")

# --- TAB CHIỀU ---
with tab2:
    if task_chieu:
        st.markdown(f'<div class="task-box-chieu"><h3>{task_chieu["task"]}</h3><p>{task_chieu["detail"]}</p></div>', unsafe_allow_html=True)
        st.divider()
        
        st.write("### 👩‍💻 Khu vực sáng tạo & Lấy Prompt")
        # Radio button chọn loại content (Ví dụ cho Thứ 2 Chiều)
        content_type_pm = st.radio("Chọn loại nội dung sẽ làm:", ["Quay Video Biến Hình (Reels)", "Bài viết Hướng dẫn chi tiết"], horizontal=True, key="pm_radio")
        
        # --- LOGIC HIỂN THỊ PROMPT LINH HOẠT ---
        if content_type_pm == "Quay Video Biến Hình (Reels)":
             # Buộc hiển thị prompt kịch bản video
            show_prompt_block("video_kịch_bản", task_chieu["task"])

        elif content_type_pm == "Bài viết Hướng dẫn chi tiết":
            # Buộc hiển thị prompt bài viết hướng dẫn
            show_prompt_block("guide_post", task_chieu["task"])
            
        st.text_area("✍️ Ghi chú kịch bản/ý tưởng:", height=100, key="pm_note")
        st.checkbox("✅ Đã hoàn thành", key="pm_check")
    else:
        st.info("Chưa có lịch cho buổi chiều này.")

# --- TAB TỐI ---
with tab3:
    if task_toi:
        st.markdown(f'<div class="task-box-toi"><h3>{task_toi["task"]}</h3><p>{task_toi["detail"]}</p></div>', unsafe_allow_html=True)
        st.divider()
        
        st.write("### 👩‍💻 Khu vực sáng tạo & Lấy Prompt")
        content_type_night = st.radio("Chọn hoạt động:", ["Viết Story tổng kết/Tâm sự", "Chỉ tương tác (Không viết bài)"], horizontal=True, key="night_radio")

        if content_type_night == "Viết Story tổng kết/Tâm sự":
             if task_toi.get("prompt_type"):
                show_prompt_block(task_toi["prompt_type"], task_toi["task"])

        st.text_area("✍️ Ghi lại cảm xúc cuối ngày:", height=80, key="night_note")
        st.checkbox("✅ Đã hoàn thành", key="night_check")
    else:
        st.info("Buổi tối tự do nghỉ ngơi!")

# --- FOOTER ---
st.divider()
if st.button("💾 Cập nhật trạng thái ngày hôm nay"):
    st.balloons()
    st.success("Đã lưu lại tiến độ! Nelly đã có một ngày làm việc hiệu quả và sang trọng.")
