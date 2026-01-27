import streamlit as st
import random

# 1. CẤU HÌNH TRANG
st.set_page_config(
    page_title="Moon's Content Station",
    page_icon="🎬",
    layout="wide"
)

# Link Chatbot Elima
ELIMA_LINK = "https://chatgpt.com/g/g-68ab318836f48191a9b7fae7afcca279-elima-tarot"

# 2. DỮ LIỆU BÀI TAROT (Database gốc)
tarot_database = [
    # === TÀI CHÍNH ===
    {
        "category": "Tài chính",
        "name": "Ace of Pentacles - Át Tiền",
        "image_url": "https://i.pinimg.com/564x/a2/27/98/a22798e604de6e9e436894d7545e8550.jpg",
        "message": "Cánh cửa tài chính đang mở toang! Một nguồn tiền khổng lồ đang chảy vào túi bạn.",
        "affirmation": "Gõ 'TRIỆU PHÚ' để nhận chìa khóa kho báu!",
        "caption_template": "🔥 Tín hiệu vũ trụ: Dòng tiền lớn đang lao đến bạn! 💰\nSự túng thiếu kết thúc ngay hôm nay. Vũ trụ đang mở khóa kho báu dành riêng cho bạn.\n👇 Gõ 'TRIỆU PHÚ' để nhận ngay!",
        "hashtags": "#TarotMoney #LuatHapDan #TaiChinh #GiauCo #Manifest"
    },
    {
        "category": "Tài chính",
        "name": "Justice - Quý Nhân",
        "image_url": "https://i.pinimg.com/564x/e7/33/c7/e733c7f8a706598375971488c9f53265.jpg",
        "message": "Quý nhân quyền lực sẽ xuất hiện giúp bạn lội ngược dòng ngoạn mục.",
        "affirmation": "Gõ 'QUÝ NHÂN' để kết nối người dẫn đường!",
        "caption_template": "⚡️ Bế tắc sẽ chấm dứt! Quý nhân của bạn đã xuất hiện.\nNgười này sẽ mang đến cơ hội và công lý cho bạn.\n👇 Gõ 'QUÝ NHÂN' để đón nhận sự giúp đỡ!",
        "hashtags": "#TarotReading #QuyNhan #JusticeCard #DoiDoi #SuNghiep"
    },
    {
        "category": "Tài chính",
        "name": "10 of Pentacles - Di Sản Thịnh Vượng",
        "image_url": "https://i.pinimg.com/564x/0f/68/73/0f68735500806443657754b23829035e.jpg",
        "message": "Sự sung túc trọn vẹn cho cả gia đình. Tiền bạc, bất động sản đang trên đường tới.",
        "affirmation": "Gõ 'SUNG TÚC' để đón lộc về nhà!",
        "caption_template": "🏠 Nhà cao cửa rộng, tiền bạc đầy kho! \nLá 10 Tiền báo hiệu sự viên mãn về vật chất. Một khoản tiền lớn hoặc tài sản giá trị đang đến.\n👇 Gõ 'SUNG TÚC' để nhận lộc đất đai!",
        "hashtags": "#10OfPentacles #BatDongSan #TaiLoc #GiaDinh #TarotReading"
    },

    # === TÌNH YÊU ===
    {
        "category": "Tình yêu",
        "name": "The Lovers - Tình Yêu Đích Thực",
        "image_url": "https://i.pinimg.com/564x/53/76/75/5376752765b4528bf80016a504859bc0.jpg", 
        "message": "Một kết nối linh hồn sâu sắc đang đến. Người ấy sẽ yêu thương bạn vô điều kiện.",
        "affirmation": "Gõ 'HẠNH PHÚC' để thu hút tri kỷ!",
        "caption_template": "💘 Đừng lướt qua nếu bạn đang cô đơn! Soulmate của bạn đang đến gần.\nNgười này sẽ bù đắp mọi tổn thương trong quá khứ của bạn.\n👇 Gõ 'HẠNH PHÚC' để mở cửa trái tim!",
        "hashtags": "#TarotLove #TinhYeu #Soulmate #LuatHapDan #BoiBaiTinhYeu"
    },
    {
        "category": "Tình yêu",
        "name": "2 of Cups - Sự Hòa Hợp",
        "image_url": "https://i.pinimg.com/564x/b8/0e/4d/b80e4d026926955743df07823f982959.jpg",
        "message": "Gương vỡ lại lành, hoặc một mối quan hệ mới đầy thấu hiểu sắp bắt đầu.",
        "affirmation": "Gõ 'KẾT NỐI' để chữa lành mối quan hệ!",
        "caption_template": "💌 Ai đó đang rất nhớ bạn... \nCó thể là người cũ muốn quay lại, hoặc một người mới đang thầm thương trộm nhớ.\n👇 Gõ 'KẾT NỐI' để nhận tín hiệu!",
        "hashtags": "#2OfCups #TarotCrush #NguoiYeuCu #TinhYeu #ThongDiepVuTru"
    },

    # === CHỮA LÀNH ===
    {
        "category": "Chữa lành",
        "name": "The Star - Hy Vọng & Chữa Lành",
        "image_url": "https://i.pinimg.com/564x/27/b1/76/27b176711979318a6665796a5f15478d.jpg",
        "message": "Sau cơn mưa trời lại sáng. Mọi vết thương lòng đang được vũ trụ xoa dịu.",
        "affirmation": "Gõ 'BÌNH YÊN' để gột rửa mọi nỗi buồn!",
        "caption_template": "🌿 Gửi những tâm hồn đang mệt mỏi... \nBạn đã vất vả rồi. The Star nói rằng: Thời kỳ đen tối nhất đã qua. Ánh sáng của sự bình yên đang về.\n👇 Gõ 'BÌNH YÊN' để thả trôi muộn phiền.",
        "hashtags": "#ChuaLanh #TheStar #Healing #MentalHealth #TarotVietnam"
    },

    # === ĐỘNG LỰC ===
    {
        "category": "Động lực",
        "name": "The Sun - Mặt Trời Rực Rỡ",
        "image_url": "https://i.pinimg.com/564x/a6/f8/f1/a6f8f11059df1cb75f1df75e533d31d4.jpg",
        "message": "Thành công rực rỡ và niềm vui vỡ òa! Bạn là trung tâm của ánh sáng và sự chú ý.",
        "affirmation": "Gõ 'TỎA SÁNG' để đón hào quang!",
        "caption_template": "☀️ Thời tới cản không kịp! \nMọi bóng tối bị xua tan. Chỉ còn lại thành công và niềm vui. Bạn chính là Mặt Trời!\n👇 Gõ 'TỎA SÁNG' để nhận năng lượng!",
        "hashtags": "#TheSun #ThanhCong #VuiVe #NangLuongTichCuc #Tarot"
    },
     {
        "category": "Động lực",
        "name": "Strength - Sức Mạnh Nội Tại",
        "image_url": "https://i.pinimg.com/564x/31/ee/b2/31eeb24f46757b8559648942b0051676.jpg",
        "message": "Bạn mạnh mẽ hơn bạn nghĩ. Đừng bỏ cuộc, chiến thắng đang ở rất gần!",
        "affirmation": "Gõ 'MẠNH MẼ' để đánh thức con hổ bên trong bạn!",
        "caption_template": "🔥 Đừng bỏ cuộc ngay trước vạch đích! \nThử thách hiện tại chỉ để tôi luyện bản lĩnh của bạn. Hãy đứng dậy và chiến đấu!\n👇 Gõ 'MẠNH MẼ' để tiếp thêm năng lượng!",
        "hashtags": "#DongLuc #StrengthCard #Motivation #PhatTrienBanThan #NeverGiveUp"
    }
]

# 3. HÀM TẠO SORA PROMPT TỰ ĐỘNG
def generate_sora_prompt_dynamic(description, duration):
    """Tạo prompt Sora dựa trên input mô tả của User (lấy từ Elima)"""
    style_keywords = "Cinematic lighting, photorealistic, 8k, highly detailed, magical atmosphere, vertical ratio 9:16."
    
    if duration == "15s (Shorts)":
        return f"Fast paced close-up shot. Visual focus: {description}. High energy, visual hook, vivid colors. {style_keywords}"
    elif duration == "30s (Story)":
        return f"Medium shot, storytelling flow. Scene description: {description}. Emotional connection, smooth camera movement. {style_keywords}"
    else: # 60s
        return f"Wide establishing shot zooming in. Narrative journey: {description}. Epic scale, deep depth of field, slow motion moments. {style_keywords}"

# 4. CSS TÙY CHỈNH
def inject_custom_css(color_theme):
    st.markdown(f"""
    <style>
    .stButton>button {{
        background-color: {color_theme};
        color: white;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
    }}
    .stButton>button:hover {{ filter: brightness(90%); }}
    .affirmation-box {{
        background-color: #f0f2f6;
        border-left: 8px solid {color_theme};
        padding: 20px;
        border-radius: 8px;
        font-size: 1.1em;
        margin-top: 10px;
    }}
    .step-box {{
        border: 1px dashed #ccc;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 5. HÀM XỬ LÝ RÚT BÀI
def draw_card(category):
    if category == "Tất cả":
        filtered = tarot_database
    else:
        filtered = [c for c in tarot_database if c["category"] == category]
    
    if filtered:
        st.session_state['card_result'] = random.choice(filtered)

# 6. GIAO DIỆN CHÍNH
def main():
    st.title("🎬 Moon's Content Station")
    st.caption("Quy trình chuẩn: Rút bài -> Hỏi Elima (Kịch bản/Ảnh) -> Tạo Prompt Video -> Đăng bài")
    
    # --- THANH MENU CHỌN CHỦ ĐỀ ---
    col_menu, col_btn = st.columns([1, 2])
    with col_menu:
        topic = st.selectbox("Chọn chủ đề video:", ("Tài chính", "Tình yêu", "Chữa lành", "Động lực", "Tất cả"))
    
    # Màu sắc theo chủ đề
    colors = {"Tài chính": "#FFD700", "Tình yêu": "#FF69B4", "Chữa lành": "#00CED1", "Động lực": "#FF4500", "Tất cả": "#7E57C2"}
    current_color = colors.get(topic, "#7E57C2")
    inject_custom_css(current_color)
    
    with col_btn:
        st.write("")
        st.write("")
        if st.button(f"✨ SẢN XUẤT VIDEO: {topic.upper()} ✨", use_container_width=True):
            draw_card(topic)
            st.rerun()
            
    st.divider()

    # --- HIỂN THỊ KẾT QUẢ ---
    if 'card_result' in st.session_state:
        card = st.session_state['card_result']
        
        # Chia 2 cột: Trái (Visual/Vibe) - Phải (Công cụ Creator)
        col_left, col_right = st.columns([1, 1.4])
        
        # === CỘT TRÁI: HIỂN THỊ LÁ BÀI & THÔNG ĐIỆP ===
        with col_left:
            st.subheader(f"🔮 {card['name']}")
            st.image(card['image_url'], use_column_width=True)
            st.info(f"💌 **Thông điệp:** {card['message']}")
            
            # Manifest Box
            st.markdown(f"""
            <div class="affirmation-box">
                <b>🔥 MANIFEST NGAY:</b><br>
                <i>"{card['affirmation']}"</i>
            </div>
            """, unsafe_allow_html=True)
            
            st.write("")
            if st.button("🔄 Rút bài khác"):
                draw_card(topic)
                st.rerun()

        # === CỘT PHẢI: CÔNG CỤ SÁNG TẠO (QUY TRÌNH 3 BƯỚC) ===
        with col_right:
            st.subheader("🛠️ Công cụ Creator")

            # --- BƯỚC 1: ELIMA (Kịch bản & Ảnh) ---
            st.markdown("#### 1️⃣ Bước 1: Gặp Elima lấy nội dung")
            st.markdown('<div class="step-box">', unsafe_allow_html=True)
            
            # Tạo câu lệnh mẫu để user copy
            prompt_for_elima = f"Tôi vừa rút được lá bài '{card['name']}' về chủ đề '{card['category']}'. Hãy đóng vai một Tarot Reader chuyên nghiệp, viết cho tôi kịch bản video ngắn (gồm Hook giật gân, Body cảm động, Call to Action: '{card['affirmation']}'). Sau đó hãy vẽ giúp tôi hình ảnh lá bài này theo phong cách 3D, ánh sáng huyền ảo để làm nền video."
            
            st.text_area("Copy câu lệnh này gửi cho Elima:", value=prompt_for_elima, height=100)
            
            st.link_button(
                "💬 Chat với Elima ngay (Lấy Kịch bản & Ảnh)", 
                ELIMA_LINK, 
                type="primary", 
                use_container_width=True
            )
            st.markdown('</div>', unsafe_allow_html=True)

            # --- BƯỚC 2: TẠO PROMPT SORA (Từ mô tả của Elima) ---
            st.markdown("#### 2️⃣ Bước 2: Tạo Prompt Video (Sora)")
            st.markdown('<div class="step-box">', unsafe_allow_html=True)
            st.caption("Sau khi Elima mô tả cảnh/hình ảnh, hãy copy đoạn mô tả đó dán vào đây:")
            
            # Ô nhập liệu từ User
            user_desc = st.text_area("Dán mô tả hình ảnh từ Elima vào đây:", placeholder="Ví dụ: Một dòng sông vàng chảy qua thung lũng...")
            
            # Logic tạo Prompt
            tabs = st.tabs(["15s (Shorts)", "30s (Story)", "60s (Full)"])
            for i, tab in enumerate(tabs):
                durations = ["15s (Shorts)", "30s (Story)", "60s (Full)"]
                with tab:
                    if user_desc:
                        # Nếu có input từ Elima -> Tạo prompt mới
                        final_prompt = generate_sora_prompt_dynamic(user_desc, durations[i])
                        st.code(final_prompt, language="text")
                        st.success("✅ Đã tạo Prompt theo ý Elima!")
                    else:
                        # Nếu chưa có input -> Hiện prompt mặc định (nếu có trong DB) hoặc nhắc nhở
                        st.info("👈 Hãy dán mô tả từ Elima vào ô bên trên để tạo Prompt.")
            st.markdown('</div>', unsafe_allow_html=True)

            # --- BƯỚC 3: CAPTION & HASHTAG (Dự phòng) ---
            with st.expander("3️⃣ Bước 3: Caption & Hashtag mẫu (Dùng ngay)", expanded=False):
                st.text_area("Caption:", value=card['caption_template'], height=120)
                st.code(card['hashtags'], language="text")

    else:
        # Màn hình chờ
        st.markdown(f"""
        <div style='text-align: center; color: #666; padding: 50px;'>
            <h3>👋 Chào Moon!</h3>
            <p>Hôm nay chúng ta sẽ lan tỏa thông điệp ánh sáng nào? <br>Hãy chọn chủ đề bên trên để bắt đầu nhé.</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
