import streamlit as st
import random

# 1. CẤU HÌNH TRANG
st.set_page_config(
    page_title="Moon's Content Station",
    page_icon="🎬",
    layout="wide"
)

# 2. DỮ LIỆU BÀI TAROT ĐA DẠNG (TIỀN - TÌNH - CHỮA LÀNH)
tarot_database = [
    # === CHỦ ĐỀ: TÀI CHÍNH (MONEY) ===
    {
        "category": "Tài chính",
        "name": "Ace of Pentacles - Át Tiền",
        "image_url": "https://i.pinimg.com/564x/a2/27/98/a22798e604de6e9e436894d7545e8550.jpg",
        "message": "Cánh cửa tài chính đang mở toang! Một nguồn tiền khổng lồ đang chảy vào túi bạn.",
        "affirmation": "Gõ 'TRIỆU PHÚ' để nhận chìa khóa kho báu!",
        "caption": "🔥 Tín hiệu vũ trụ: Dòng tiền lớn đang lao đến bạn! 💰\nSự túng thiếu kết thúc ngay hôm nay. Vũ trụ đang mở khóa kho báu dành riêng cho bạn.\n👇 Gõ 'TRIỆU PHÚ' để nhận ngay!",
        "hashtags": "#TarotMoney #LuatHapDan #TaiChinh #GiauCo #Manifest",
        "color": "#FFD700", # Vàng
        "sora_prompts": {
            "15s": "Cinematic close-up, golden coin spinning in mid-air, bursting into sparkles. Luxury vibe.",
            "30s": "A hand opening a treasure chest glowing with golden light. The light illuminates a dark room.",
            "60s": "A path paved with gold leading to a majestic castle. A person walks confidently towards it. The sky is golden hour. Symbolizing the journey to wealth."
        }
    },
    {
        "category": "Tài chính",
        "name": "Justice - Quý Nhân",
        "image_url": "https://i.pinimg.com/564x/e7/33/c7/e733c7f8a706598375971488c9f53265.jpg",
        "message": "Quý nhân quyền lực sẽ xuất hiện giúp bạn lội ngược dòng ngoạn mục.",
        "affirmation": "Gõ 'QUÝ NHÂN' để kết nối người dẫn đường!",
        "caption": "⚡️ Bế tắc sẽ chấm dứt! Quý nhân của bạn đã xuất hiện.\nNgười này sẽ mang đến cơ hội và công lý cho bạn. Những ai chơi xấu bạn sẽ lùi bước.\n👇 Gõ 'QUÝ NHÂN' để đón nhận sự giúp đỡ!",
        "hashtags": "#TarotReading #QuyNhan #JusticeCard #DoiDoi #SuNghiep",
        "color": "#FFD700",
        "sora_prompts": {
            "15s": "A golden scale balancing perfectly. A sword of light cuts through darkness.",
            "30s": "A person stuck in fog. A glowing hand reaches down from the sky to pull them up.",
            "60s": "Lady Justice standing tall on a mountain top, clouds clearing away to reveal a bright blue sky. A path opens up for the protagonist."
        }
    },

    # === CHỦ ĐỀ: TÌNH YÊU (LOVE) ===
    {
        "category": "Tình yêu",
        "name": "The Lovers - Tình Yêu Đích Thực",
        "image_url": "https://i.pinimg.com/564x/53/76/75/5376752765b4528bf80016a504859bc0.jpg", 
        "message": "Một kết nối linh hồn sâu sắc đang đến. Người ấy sẽ yêu thương và trân trọng bạn vô điều kiện.",
        "affirmation": "Gõ 'HẠNH PHÚC' để thu hút tri kỷ (Soulmate)!",
        "caption": "💘 Đừng lướt qua nếu bạn đang cô đơn! Soulmate của bạn đang đến gần.\nVũ trụ đã sắp xếp một cuộc gặp gỡ định mệnh. Người này sẽ bù đắp mọi tổn thương trong quá khứ của bạn.\n👇 Gõ 'HẠNH PHÚC' để mở cửa trái tim!",
        "hashtags": "#TarotLove #TinhYeu #Soulmate #LuatHapDan #BoiBaiTinhYeu",
        "color": "#FF69B4", # Hồng
        "sora_prompts": {
            "15s": "Two glowing souls (pink and blue energy) spiraling and merging into a heart shape. Romantic and soft.",
            "30s": "A couple silhouette standing under a galaxy sky full of shooting stars. They hold hands, and sparks fly.",
            "60s": "A split screen showing two people walking in different places. An invisible red thread connects their pinky fingers. They slowly walk towards each other until they meet in a field of flowers. Cinematic romance."
        }
    },
    {
        "category": "Tình yêu",
        "name": "2 of Cups - Sự Hòa Hợp",
        "image_url": "https://i.pinimg.com/564x/b8/0e/4d/b80e4d026926955743df07823f982959.jpg",
        "message": "Gương vỡ lại lành, hoặc một mối quan hệ mới đầy thấu hiểu sắp bắt đầu.",
        "affirmation": "Gõ 'KẾT NỐI' để chữa lành mối quan hệ!",
        "caption": "💌 Ai đó đang rất nhớ bạn... \nCó thể là người cũ muốn quay lại, hoặc một người mới đang thầm thương trộm nhớ. Tần số rung động của tình yêu đang rất mạnh.\n👇 Gõ 'KẾT NỐI' để nhận tín hiệu!",
        "hashtags": "#2OfCups #TarotCrush #NguoiYeuCu #TinhYeu #ThongDiepVuTru",
        "color": "#FF69B4",
        "sora_prompts": {
            "15s": "Two golden cups clinking together, liquid light overflowing and turning into rose petals.",
            "30s": "A message in a bottle floating on a pink ocean, reaching the shore. A hand picks it up.",
            "60s": "A beautiful garden scene. Two figures approach each other and exchange cups. As they drink, an aura of pink light surrounds them, healing the withered plants around them. Symbolizing healing love."
        }
    },

    # === CHỦ ĐỀ: CHỮA LÀNH (HEALING) ===
    {
        "category": "Chữa lành",
        "name": "The Star - Hy Vọng & Chữa Lành",
        "image_url": "https://i.pinimg.com/564x/27/b1/76/27b176711979318a6665796a5f15478d.jpg",
        "message": "Sau cơn mưa trời lại sáng. Mọi vết thương lòng đang được vũ trụ xoa dịu.",
        "affirmation": "Gõ 'BÌNH YÊN' để gột rửa mọi nỗi buồn!",
        "caption": "🌿 Gửi những tâm hồn đang mệt mỏi... \nBạn đã vất vả rồi. Vũ trụ gửi lá bài The Star để nói rằng: Thời kỳ đen tối nhất đã qua. Ánh sáng của sự bình yên đang về.\n👇 Gõ 'BÌNH YÊN' để thả trôi muộn phiền.",
        "hashtags": "#ChuaLanh #TheStar #Healing #MentalHealth #TarotVietnam",
        "color": "#00CED1", # Xanh ngọc
        "sora_prompts": {
            "15s": "A bright star shining in a night sky, reflecting on a calm lake. Peaceful and serene.",
            "30s": "A woman pouring water from a jug into a stream. The water glows, and flowers bloom instantly where the water touches.",
            "60s": "A person sitting in rain (symbolizing sadness). The rain stops, clouds part, and a giant beautiful star appears. The person stands up, their clothes dry instantly, and they look up with a smile. Transformation from sadness to hope."
        }
    },
    
    # === CHỦ ĐỀ: ĐỘNG LỰC (MOTIVATION) ===
    {
        "category": "Động lực",
        "name": "Strength - Sức Mạnh Nội Tại",
        "image_url": "https://i.pinimg.com/564x/31/ee/b2/31eeb24f46757b8559648942b0051676.jpg",
        "message": "Bạn mạnh mẽ hơn bạn nghĩ. Đừng bỏ cuộc, chiến thắng đang ở rất gần!",
        "affirmation": "Gõ 'MẠNH MẼ' để đánh thức con hổ bên trong bạn!",
        "caption": "🔥 Đừng bỏ cuộc ngay trước vạch đích! \nThử thách hiện tại chỉ để tôi luyện bản lĩnh của bạn. Bạn có sức mạnh của một chiến binh. Hãy đứng dậy và chiến đấu!\n👇 Gõ 'MẠNH MẼ' để tiếp thêm năng lượng!",
        "hashtags": "#DongLuc #StrengthCard #Motivation #PhatTrienBanThan #NeverGiveUp",
        "color": "#FF4500", # Đỏ cam
        "sora_prompts": {
            "15s": "Close up of a lion's eye, zooming out to a woman gently petting a lion. Radiant orange aura.",
            "30s": "A phoenix rising from ashes, spreading wings made of fire. Epic and empowering.",
            "60s": "A runner exhausted, falling down. They look at a glowing light ahead, stand up with determination, and run faster than before, breaking through a brick wall. High energy visual."
        }
    }
]

# Link Chatbot Elima
ELIMA_LINK = "https://chatgpt.com/g/g-68ab318836f48191a9b7fae7afcca279-elima-tarot"

# 3. CSS TÙY CHỈNH (DYNAMIC)
def inject_custom_css(color_theme):
    st.markdown(f"""
    <style>
    .stButton>button {{
        background-color: {color_theme};
        color: white;
        border-radius: 20px;
        font-weight: bold;
        border: none;
        padding: 10px 24px;
        transition: all 0.3s;
    }}
    .stButton>button:hover {{
        filter: brightness(85%);
        transform: scale(1.05);
    }}
    .affirmation-box {{
        background-color: #f8f9fa;
        border-left: 8px solid {color_theme};
        padding: 20px;
        border-radius: 8px;
        font-size: 1.1em;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. HÀM XỬ LÝ
def draw_card(category):
    # Lọc bài theo chủ đề
    if category == "Tất cả":
        filtered_deck = tarot_database
    else:
        filtered_deck = [card for card in tarot_database if card["category"] == category]
    
    if filtered_deck:
        selected_card = random.choice(filtered_deck)
        st.session_state['card_result'] = selected_card
    else:
        st.error("Chưa có dữ liệu cho chủ đề này.")

# 5. GIAO DIỆN CHÍNH
def main():
    st.title("🎬 Moon's Content Station")
    st.caption("Trạm sáng tạo Video Tarot: Tiền - Tình - Chữa Lành - Động Lực")
    
    # --- THANH CÔNG CỤ (SIDEBAR HOẶC TOP) ---
    col_filter, col_action = st.columns([1, 2])
    
    with col_filter:
        topic = st.selectbox(
            "Hôm nay Moon muốn làm video chủ đề gì?",
            ("Tài chính", "Tình yêu", "Chữa lành", "Động lực", "Tất cả"),
            index=0
        )

    # Xác định màu chủ đề để đổi giao diện
    theme_colors = {
        "Tài chính": "#FFD700", # Vàng
        "Tình yêu": "#FF69B4",  # Hồng
        "Chữa lành": "#00CED1", # Xanh
        "Động lực": "#FF4500",  # Đỏ
        "Tất cả": "#7E57C2"     # Tím
    }
    current_color = theme_colors.get(topic, "#7E57C2")
    inject_custom_css(current_color)

    with col_action:
        st.write("") # Spacer
        st.write("") # Spacer
        if st.button(f"✨ SẢN XUẤT VIDEO: {topic.upper()} ✨", use_container_width=True):
            draw_card(topic)
            st.rerun()

    st.divider()
    
    # --- HIỂN THỊ KẾT QUẢ ---
    if 'card_result' in st.session_state:
        card = st.session_state['card_result']
        
        # Chia layout 2 cột
        col_left, col_right = st.columns([1, 1.5])
        
        with col_left:
            st.markdown(f"### 🔮 {card['name']}")
            st.image(card['image_url'], use_column_width=True)
            
            # Khung thông điệp
            st.info(f"💌 **Thông điệp:** {card['message']}")
            
            # Khung Affirmation (Điểm nhấn để quay video chỉ tay vào)
            st.markdown(f"""
            <div class="affirmation-box">
                <b>🔥 MANIFEST NGAY:</b><br>
                <i>"{card['affirmation']}"</i>
            </div>
            """, unsafe_allow_html=True)
            
            st.write("")
            if st.button("🔄 Rút bài khác"):
                draw_card(topic) # Rút lại cùng chủ đề
                st.rerun()

        with col_right:
            st.subheader("🛠️ Công cụ Creator (Copy & Paste)")
            
            # Tab Caption
            with st.expander("📝 Kịch bản Caption & Hashtag", expanded=True):
                st.markdown("**Caption Facebook/TikTok:**")
                st.code(card['caption'], language="text")
                st.markdown("**Hashtags chuẩn SEO:**")
                st.code(card['hashtags'], language="text")

            # Tab Prompt Sora
            st.markdown(f"### 🎥 Sora Prompts ({topic})")
            st.caption("Prompt được tối ưu hóa visual theo đúng chủ đề bạn chọn.")
            
            t1, t2, t3 = st.tabs(["15s (Shorts)", "30s (Story)", "60s (Full)"])
            with t1: st.code(card['sora_prompts']['15s'], language="text")
            with t2: st.code(card['sora_prompts']['30s'], language="text")
            with t3: st.code(card['sora_prompts']['60s'], language="text")

            st.markdown("---")
            st.info(f"Bạn cần lời khuyên sâu sắc hơn về {topic}?")
            st.link_button(
                f"💬 Chat sâu với Elima về {topic}", 
                ELIMA_LINK, 
                use_container_width=True
            )

    else:
        # Màn hình chờ
        st.markdown(f"""
        <div style='text-align: center; color: #666; padding: 50px;'>
            <h3>👋 Chào Moon!</h3>
            <p>Hôm nay năng lượng của bạn thế nào? <br>Hãy chọn chủ đề bên trên để nhận thông điệp ánh sáng nhé.</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
