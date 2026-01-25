import streamlit as st
import random

# 1. CẤU HÌNH TRANG (Phải đặt ở dòng đầu tiên)
st.set_page_config(
    page_title="Moon's Tarot Message",
    page_icon="🔮",
    layout="centered"
)

# 2. CSS TÙY CHỈNH (Để giao diện đẹp và lung linh hơn)
st.markdown("""
    <style>
    .stButton>button {
        background-color: #7E57C2;
        color: white;
        border-radius: 20px;
        font-weight: bold;
        border: none;
        padding: 10px 24px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #5E35B1;
        transform: scale(1.05);
    }
    .affirmation-box {
        background-color: #f0f2f6;
        border-left: 5px solid #FFD700;
        padding: 15px;
        border-radius: 5px;
        font-style: italic;
        color: #333;
    }
    .highlight-text {
        font-weight: bold;
        color: #D32F2F;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. DỮ LIỆU BÀI TAROT (Đã update nội dung theo phong cách Video của bạn)
tarot_deck = [
    {
        "name": "Ace of Pentacles - Át Tiền",
        "image_url": "https://i.pinimg.com/564x/a2/27/98/a22798e604de6e9e436894d7545e8550.jpg", # Thay link ảnh của bạn
        "keywords": ["Cơ hội vàng", "Tiền mặt", "Khởi đầu thịnh vượng"],
        "message": "Cánh cửa tài chính đang mở toang! Một nguồn tiền khổng lồ hoặc một cơ hội kinh doanh 'triệu đô' đang chảy thẳng vào túi bạn. Đây là chiếc chìa khóa kho báu mà vũ trụ trao tặng.",
        "affirmation": "Gõ 'TRIỆU PHÚ' để kích hoạt chìa khóa kho báu này ngay lập tức!",
        "type": "money"
    },
    {
        "name": "Justice - Công Lý (Quý Nhân)",
        "image_url": "https://i.pinimg.com/564x/e7/33/c7/e733c7f8a706598375971488c9f53265.jpg", # Thay link ảnh của bạn
        "keywords": ["Quý nhân", "Sự thật", "Cân bằng lại"],
        "message": "Đừng lo lắng nữa! Giữa lúc bế tắc nhất, một QUÝ NHÂN quyền lực sẽ xuất hiện và đưa tay kéo bạn lên. Họ vừa mang đến tiền bạc, vừa mở lối đi giúp bạn lội ngược dòng ngoạn mục.",
        "affirmation": "Gõ 'QUÝ NHÂN' để đón nhận sự giúp đỡ thần kỳ này!",
        "type": "destiny"
    },
    {
        "name": "6 of Pentacles - Dòng Chảy May Mắn",
        "image_url": "https://i.pinimg.com/564x/08/94/a3/0894a39012678f5647000d6621746654.jpg", # Thay link ảnh của bạn
        "keywords": ["Cho và nhận", "May mắn", "Hanh thông"],
        "message": "Dòng chảy may mắn đang được sắp xếp lại để mang cơ hội đổi đời đến cho bạn. Những gì bạn đã cho đi giờ đây đang quay trở lại gấp 10 lần. Ngày mai sẽ là một ngày rực rỡ!",
        "affirmation": "Gõ 'MAY MẮN' để xác nhận dòng chảy thịnh vượng này!",
        "type": "money"
    },
     {
        "name": "The Sun - Mặt Trời",
        "image_url": "https://i.pinimg.com/564x/a6/f8/f1/a6f8f11059df1cb75f1df75e533d31d4.jpg",
        "keywords": ["Thành công", "Niềm vui", "Sáng tỏ"],
        "message": "Mọi bóng tối đã lùi xa. Ánh sáng của sự thành công và hạnh phúc đang chiếu rọi vào cuộc sống của bạn. Năng lượng tích cực này sẽ thiêu đốt mọi xui xẻo cũ.",
        "affirmation": "Gõ 'TỎA SÁNG' để đón nhận hào quang thành công!",
        "type": "success"
    }
]

# Link Chatbot Elima
ELIMA_LINK = "https://chatgpt.com/g/g-68ab318836f48191a9b7fae7afcca279-elima-tarot"

# 4. HÀM XỬ LÝ
def draw_card():
    """Hàm rút bài ngẫu nhiên"""
    selected_card = random.choice(tarot_deck)
    st.session_state['card_result'] = selected_card

# 5. GIAO DIỆN CHÍNH (UI)
def main():
    st.title("🌙 Moon's Tarot Message")
    st.caption("Thông điệp vũ trụ gửi riêng cho bạn hôm nay")
    
    st.divider()

    # Khu vực nút bấm (nếu chưa có kết quả thì hiện nút to)
    if 'card_result' not in st.session_state:
        st.markdown("<h3 style='text-align: center;'>Hít thở sâu & Đón nhận tín hiệu</h3>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("✨ RÚT LÁ BÀI CỦA BẠN ✨", use_container_width=True):
                draw_card()
                st.rerun() # Load lại trang để hiện kết quả
    
    # Khu vực hiển thị kết quả
    else:
        card = st.session_state['card_result']
        
        # Layout 2 cột: Ảnh và Lời giải
        c1, c2 = st.columns([1, 1.2])
        
        with c1:
            st.image(card['image_url'], use_column_width=True, caption=card['name'])
            
            # Nút rút lại bài
            if st.button("🔄 Rút lá khác"):
                del st.session_state['card_result']
                st.rerun()

        with c2:
            st.subheader(f"🔮 {card['name']}")
            st.write(f"**Keywords:** {' | '.join(card['keywords'])}")
            
            st.divider()
            
            # Thông điệp chính (Message)
            st.markdown("### 💌 Thông điệp:")
            st.write(card['message'])
            
            st.markdown("---")
            
            # KHU VỰC MANIFEST (Luật hấp dẫn) - Giống trong video
            st.markdown('<div class="affirmation-box">', unsafe_allow_html=True)
            st.markdown("#### 🔥 Lời khẳng định (Manifest):")
            st.markdown(f"👉 *{card['affirmation']}*")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.write("") # Khoảng trống
            
            # Call to Action về Elima
            st.info("Bạn muốn biết chính xác KHI NÀO điều này xảy ra?")
            st.link_button(
                label="💬 Hỏi chi tiết Elima Tarot ngay",
                url=ELIMA_LINK,
                type="primary",
                use_container_width=True
            )

# Chạy ứng dụng
if __name__ == "__main__":
    main()
