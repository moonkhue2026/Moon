import streamlit as st
import pandas as pd

# 1. CẤU HÌNH TRANG (Bắt buộc phải nằm ở dòng đầu tiên)
st.set_page_config(page_title="Moon's 3D Anatomy", page_icon="🧬", layout="wide")

# 2. TIÊU ĐỀ CHÍNH
st.title("Moon's 3D Studio: Cơ Thể & Làm Đẹp 🧬")
st.markdown("---")

# 3. CHIA 2 TAB LỚN (Giải phẫu & Làm đẹp)
main_tab1, main_tab2 = st.tabs(["🍔 Giải phẫu (Food & Organ)", "💄 Làm đẹp (Beauty & Skincare)"])

# ==================================================
# KHU VỰC 1: GIẢI PHẪU (NỘI TẠNG & THỨC ĂN)
# ==================================================
with main_tab1:
    st.header("Anatomy Viral Station 🩺")
    st.caption("Chuyên khu mô phỏng quá trình tiêu hóa thức ăn (Food Digestion)")
    
    # Chia 2 cột: Cột trái nhập liệu - Cột phải quản lý
    col_a, col_b = st.columns([1, 1.5])

    # --- CỘT TRÁI: MÁY TẠO KỊCH BẢN ---
    with col_a:
        st.subheader("💡 Tạo ý tưởng Viral")
        with st.form("food_form"):
            topic = st.text_input("Món ăn/Vật thể (VD: Mì cay, Trân châu)", "Mì cay cấp 7")
            body_part = st.selectbox("Bộ phận tác động", ["Dạ dày", "Phổi", "Gan", "Ruột", "Não"])
            effect = st.text_input("Hiệu ứng (VD: Sủi bọt, Chảy máu)", "Dạ dày đỏ rực, co thắt mạnh")
            
            submit_food = st.form_submit_button("🚀 Viết kịch bản ngay")
            
            if submit_food:
                st.success("✅ Đã xuất kịch bản!")
                st.info(f"""
                **Tên Video:** {topic} vs {body_part}
                \n**Hook:** ĐỪNG ăn {topic} nếu bạn chưa thấy cảnh này trong {body_part}! 😱
                \n**Visual:** {body_part} {effect}. Zoom cận cảnh tế bào đang phản ứng.
                \n**Âm thanh:** Tiếng nhai rộp rộp + Tiếng dạ dày sôi ục ục (ASMR).
                """)

    # --- CỘT PHẢI: BẢNG QUẢN LÝ ---
    with col_b:
        st.subheader("📅 Quản lý sản xuất (Food)")
        # Tạo dữ liệu mẫu
        df_food = pd.DataFrame({
            "Chủ đề": ["Mật ong", "Mì cay", "Trân châu", "Nước đá", "Kẹo cao su"],
            "Loại": ["Chữa lành", "Cảnh báo", "Tò mò", "Cảnh báo", "Tò mò"],
            "Trạng thái": ["Đã xong", "Đang render", "Chờ kịch bản", "Idea", "Đã Post"]
        })
        # Hiển thị bảng cho phép chỉnh sửa
        st.data_editor(df_food, num_rows="dynamic", use_container_width=True, key="editor_food")
    
    # --- PHẦN DƯỚI: GALLERY DEMO ---
    st.divider()
    st.subheader("👀 Góc nhìn tham khảo (Demo)")
    img_col1, img_col2, img_col3 = st.columns(3)
    with img_col1:
        st.image("https://source.unsplash.com/400x300/?stomach", caption="Dạ dày tiêu hóa")
    with img_col2:
        st.image("https://source.unsplash.com/400x300/?vegetables", caption="Chất xơ làm sạch ruột")
    with img_col3:
        st.image("https://source.unsplash.com/400x300/?honey", caption="Mật ong chữa lành")


# ==================================================
# KHU VỰC 2: LÀM ĐẸP (BEAUTY / FILLER / NHA KHOA)
# ==================================================
with main_tab2:
    st.header("Beauty 3D Studio 💉👄")
    st.caption("Chuyên khu mô phỏng thẩm mỹ: Filler, Botox, Nha khoa, Skincare dưới góc nhìn tế bào.")

    # Chia 2 cột
    b_col1, b_col2 = st.columns([1, 1.5])

    # --- CỘT TRÁI: KHO PROMPT MỞ RỘNG ---
    with b_col1:
        st.subheader("✨ Kho Prompt Làm Đẹp")
        
        # 1. Chọn danh mục lớn
        category = st.selectbox("Chọn nhóm chủ đề:", 
                                ["💉 Thẩm mỹ nội khoa (Filler/Botox)", 
                                 "🔪 Phẫu thuật thẩm mỹ (Surgery)", 
                                 "🧴 Da liễu & Skincare", 
                                 "🦷 Nha khoa (Dental)"])
        
        # 2. Logic xử lý hiển thị theo từng nhóm
        prompt_content = ""
        choice = ""

        if category == "💉 Thẩm mỹ nội khoa (Filler/Botox)":
            choice = st.selectbox("Chọn video cụ thể:", ["Tiêm Filler Môi", "Botox Xóa Nhăn", "Căng chỉ Collagen"])
            if choice == "Tiêm Filler Môi":
                prompt_content = "**Visual:** Kim tiêm đưa gel Hyaluronic Acid vào lớp trung bì môi. Các phân tử gel ngậm nước phồng lên. \n**Kết quả:** Môi mỏng -> Môi trái tim căng mọng."
            elif choice == "Botox Xóa Nhăn":
                prompt_content = "**Visual:** Tinh chất đi vào khớp nối thần kinh cơ. Cơ trán đang co rút -> thả lỏng ngay lập tức. \n**Hook:** Botox đóng băng cơ mặt thế nào?"
            elif choice == "Căng chỉ Collagen":
                prompt_content = "**Visual:** Sợi chỉ gai luồn dưới da, móc vào mô mỡ và kéo căng da mặt lên. Theo thời gian, collagen bám quanh sợi chỉ."

        elif category == "🔪 Phẫu thuật thẩm mỹ (Surgery)":
            choice = st.selectbox("Chọn video cụ thể:", ["Nâng mũi cấu trúc", "Hút mỡ bụng", "Độn cằm"])
            if choice == "Nâng mũi cấu trúc":
                prompt_content = "**Visual:** Bóc tách da mũi. Đặt sụn nhân tạo lên sống mũi. Lấy sụn tai bọc đầu mũi. Khâu lại."
            elif choice == "Hút mỡ bụng":
                prompt_content = "**Visual:** Ống hút kim loại đi vào lớp mỡ vàng dưới da. Hút đến đâu, lớp mỡ xẹp xuống đến đó. Da bụng phẳng lì."

        elif category == "🧴 Da liễu & Skincare":
            choice = st.selectbox("Chọn video cụ thể:", ["Nặn mụn đầu đen", "Serum Vitamin C", "Kem chống nắng"])
            if choice == "Nặn mụn đầu đen":
                prompt_content = "**Visual (Zoom 1000x):** Lỗ chân lông bị bít tắc bởi dầu và bụi bẩn (màu đen). Lực ép đẩy nhân mụn trồi lên như nấm mọc."
            elif choice == "Kem chống nắng":
                prompt_content = "**Visual:** Tia UV bắn vào da như những mũi tên. Lớp kem tạo thành tấm khiên phản xạ lại toàn bộ tia UV."

        elif category == "🦷 Nha khoa (Dental)":
            choice = st.selectbox("Chọn video cụ thể:", ["Niềng răng", "Cấy ghép Implant", "Lấy cao răng"])
            if choice == "Niềng răng":
                prompt_content = "**Visual (Time-lapse):** Dây cung siết lại. Chân răng di chuyển rẽ sóng trong xương hàm. Xương mới bồi đắp."
            elif choice == "Cấy ghép Implant":
                prompt_content = "**Visual:** Khoan một lỗ vào xương hàm. Vặn trụ Titanium vào như vặn ốc vít. Lắp răng sứ lên trên."
            elif choice == "Lấy cao răng":
                prompt_content = "**Visual:** Đầu máy rung siêu âm chạm vào mảng bám. Mảng bám vỡ vụn rơi ra từng tảng."

        # Hiển thị Prompt kết quả
        st.info(f"**Kịch bản cho: {choice}**")
        st.markdown(prompt_content)
        
        if st.button("Copy Prompt này", key="copy_beauty_new"):
             st.toast("Đã copy nội dung vào bộ nhớ đệm!", icon="📋")

    # --- CỘT PHẢI: BẢNG QUẢN LÝ ---
    with b_col2:
        st.subheader("📅 Tiến độ Beauty")
        # Bảng quản lý Beauty
        df_beauty = pd.DataFrame({
            "Chủ đề Beauty": ["Filler Môi", "Botox Trán", "Niềng răng", "Cấy tóc", "Hút mỡ", "Trị mụn"],
            "Phân loại": ["Nội khoa", "Nội khoa", "Nha khoa", "Da liễu", "Phẫu thuật", "Da liễu"],
            "Deadline": ["25/01", "27/01", "29/01", "--", "--", "--"],
            "Trạng thái": ["Đã xong", "Đang render", "Chờ kịch bản", "Idea", "Idea", "Idea"]
        })
        st.data_editor(df_beauty, num_rows="dynamic", use_container_width=True, key="editor_beauty")
