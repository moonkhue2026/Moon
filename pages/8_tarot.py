# Version: v3.0 (SUPER DATA - Giao diện Rộng v2.0)
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

# 2. DỮ LIỆU BÀI TAROT (ĐÃ CẬP NHẬT NHIỀU BÀI HƠN)
tarot_database = [
    # =======================
    # 💰 CHỦ ĐỀ: TÀI CHÍNH (MONEY) - > 10 LÁ
    # =======================
    {
        "category": "Tài chính",
        "name": "Ace of Pentacles - Át Tiền",
        "image_url": "https://i.pinimg.com/564x/a2/27/98/a22798e604de6e9e436894d7545e8550.jpg",
        "message": "Cánh cửa tài chính đang mở toang! Một nguồn tiền khổng lồ đang chảy vào túi bạn.",
        "affirmation": "Gõ 'TRIỆU PHÚ' để nhận chìa khóa kho báu!",
        "caption": "🔥 Tín hiệu vũ trụ: Dòng tiền lớn đang lao đến bạn! 💰\nSự túng thiếu kết thúc ngay hôm nay. Vũ trụ đang mở khóa kho báu dành riêng cho bạn.\n👇 Gõ 'TRIỆU PHÚ' để nhận ngay!",
        "hashtags": "#TarotMoney #LuatHapDan #TaiChinh #GiauCo #Manifest"
    },
    {
        "category": "Tài chính",
        "name": "10 of Pentacles - Di Sản Thịnh Vượng",
        "image_url": "https://i.pinimg.com/564x/0f/68/73/0f68735500806443657754b23829035e.jpg",
        "message": "Sự sung túc trọn vẹn cho cả gia đình. Tiền bạc, bất động sản đang trên đường tới.",
        "affirmation": "Gõ 'SUNG TÚC' để đón lộc về nhà!",
        "caption": "🏠 Nhà cao cửa rộng, tiền bạc đầy kho! \nLá 10 Tiền báo hiệu sự viên mãn về vật chất. Một khoản tiền lớn hoặc tài sản giá trị đang đến.\n👇 Gõ 'SUNG TÚC' để nhận lộc đất đai!",
        "hashtags": "#10OfPentacles #BatDongSan #TaiLoc #GiaDinh #TarotReading"
    },
    {
        "category": "Tài chính",
        "name": "King of Pentacles - Vua Tiền",
        "image_url": "https://i.pinimg.com/564x/4e/d8/4a/4ed84a1444634289895316315840428e.jpg",
        "message": "Bạn có khả năng của một nhà lãnh đạo tài ba. Sự giàu có bền vững và địa vị cao đang đến.",
        "affirmation": "Gõ 'THÀNH CÔNG' để kích hoạt năng lượng Vua Tiền!",
        "caption": "👑 Bạn sinh ra để làm chủ cuộc chơi! \nLá bài Vua Tiền xác nhận: Bạn sắp đạt được đỉnh cao sự nghiệp. Tiền bạc không chỉ đến, mà còn ở lại và sinh sôi.\n👇 Gõ 'THÀNH CÔNG' để nhận vía lãnh đạo!",
        "hashtags": "#KingOfPentacles #Business #KhoiNghiep #CEO #TarotVietnam"
    },
    {
        "category": "Tài chính",
        "name": "9 of Pentacles - Độc Lập & Sang Chảnh",
        "image_url": "https://i.pinimg.com/564x/e7/33/c7/e733c7f8a706598375971488c9f53265.jpg",
        "message": "Thành quả ngọt ngào đang chờ đón. Bạn sẽ tận hưởng cuộc sống sang trọng do chính mình tạo ra.",
        "affirmation": "Gõ 'TỰ DO' để tận hưởng sự giàu có!",
        "caption": "💎 Khí chất toát ra mùi tiền! \nBạn đã làm việc chăm chỉ, và giờ là lúc thu hoạch. Sự dư dả, xinh đẹp và tự do tài chính đang gõ cửa.\n👇 Gõ 'TỰ DO' để nhận thưởng từ vũ trụ!",
        "hashtags": "#9OfPentacles #DocLapTaiChinh #PhuNuKhiChat #LuxuryLife"
    },
    {
        "category": "Tài chính",
        "name": "Wheel of Fortune - Vòng Xoay Tài Lộc",
        "image_url": "https://i.pinimg.com/564x/e9/b3/ef/e9b3ef56158223945480746973970742.jpg",
        "message": "Vận may đang đảo chiều cực mạnh! Cơ hội 'trên trời rơi xuống' sẽ giúp bạn đổi đời.",
        "affirmation": "Gõ 'MAY MẮN' để xoay chuyển càn khôn!",
        "caption": "🎰 Thời tới cản không kịp! \nVũ trụ đang quay bánh xe số phận. Từ tay trắng làm nên cơ đồ, từ bế tắc chuyển sang hanh thông. Hãy chuẩn bị đón tin vui bất ngờ!\n👇 Gõ 'MAY MẮN' để nhận vía đỏ!",
        "hashtags": "#WheelOfFortune #MayMan #XoSo #DoiVan #TarotDaily"
    },
    {
        "category": "Tài chính",
        "name": "The Emperor - Đế Chế Vững Chắc",
        "image_url": "https://i.pinimg.com/564x/11/4f/2e/114f2ea5560942445851412030806443.jpg",
        "message": "Đã đến lúc thiết lập trật tự và kỷ luật. Bạn sẽ xây dựng được một đế chế tài chính vững chắc.",
        "affirmation": "Gõ 'LÀM CHỦ' để nắm quyền kiểm soát!",
        "caption": "🏛️ Xây dựng cơ đồ vững chắc! \nThe Emperor nhắc bạn: Hãy quyết đoán và có kế hoạch. Tiền bạc sẽ đến từ sự kỷ luật và tầm nhìn xa của bạn.\n👇 Gõ 'LÀM CHỦ' để khẳng định vị thế!",
        "hashtags": "#TheEmperor #LanhDao #SuNghiep #CareerGoals #Tarot"
    },
    {
        "category": "Tài chính",
        "name": "6 of Pentacles - Cho & Nhận",
        "image_url": "https://i.pinimg.com/564x/08/94/a3/0894a39012678f5647000d6621746654.jpg",
        "message": "Dòng chảy tiền bạc đang lưu thông. Những gì bạn cho đi sẽ quay lại gấp 10 lần.",
        "affirmation": "Gõ 'THỊNH VƯỢNG' để khơi thông dòng chảy!",
        "caption": "💸 Tiền đi rồi tiền lại về gấp 10 lần! \nLuật cân bằng đang vận hành. Sự tử tế của bạn trong quá khứ giờ đây nở hoa thành tài lộc. Ví bạn sắp rung lên rồi!\n👇 Gõ 'THỊNH VƯỢNG' để mở ví đón tiền về!",
        "hashtags": "#6OfPentacles #MoneyFlow #LuatNhanQua #TaiChinh"
    },
    {
        "category": "Tài chính",
        "name": "The Magician - Nhà Giả Kim",
        "image_url": "https://i.pinimg.com/564x/d5/43/d2/d543d2215d209196726715f696614450.jpg",
        "message": "Bạn có đủ mọi công cụ để biến ý tưởng thành vàng. Hãy hành động ngay!",
        "affirmation": "Gõ 'PHÉP MÀU' để biến ước mơ thành hiện thực!",
        "caption": "✨ Bạn chính là nam châm hút tiền! \nThe Magician nói rằng bạn có đầy đủ kỹ năng và nguồn lực. Chỉ cần bạn bắt tay vào làm, tiền sẽ tự tìm đến.\n👇 Gõ 'PHÉP MÀU' để kích hoạt năng lực!",
        "hashtags": "#TheMagician #Manifestation #KhoiNghiep #SangTao #Tarot"
    },

    # =======================
    # 💘 CHỦ ĐỀ: TÌNH YÊU (LOVE)
    # =======================
    {
        "category": "Tình yêu",
        "name": "The Lovers - Tình Yêu Đích Thực",
        "image_url": "https://i.pinimg.com/564x/53/76/75/5376752765b4528bf80016a504859bc0.jpg", 
        "message": "Một kết nối linh hồn sâu sắc (Soulmate) đang đến. Bạn được yêu thương vô điều kiện.",
        "affirmation": "Gõ 'HẠNH PHÚC' để thu hút tri kỷ!",
        "caption": "💘 Soulmate của bạn đang đến gần!\nVũ trụ đã sắp xếp một cuộc gặp gỡ định mệnh. Người này sẽ bù đắp mọi tổn thương quá khứ của bạn.\n👇 Gõ 'HẠNH PHÚC' để mở cửa trái tim!",
        "hashtags": "#TheLovers #Soulmate #TinhYeu #LuatHapDan #BoiBaiTinhYeu"
    },
    {
        "category": "Tình yêu",
        "name": "Ace of Cups - Tình Yêu Chớm Nở",
        "image_url": "https://i.pinimg.com/564x/c3/0b/cf/c30bcf77356262198084f74668045501.jpg",
        "message": "Trái tim bạn sắp rung động lần nữa. Một lời tỏ tình hoặc một sự khởi đầu mới đầy cảm xúc.",
        "affirmation": "Gõ 'ĐÓN NHẬN' để tình yêu chảy vào tim!",
        "caption": "💌 Ai đó đang thầm thương trộm nhớ bạn... \nChiếc cốc tình yêu đang tràn đầy. Một mối quan hệ mới đầy lãng mạn sắp bắt đầu. Hãy mở lòng nhé!\n👇 Gõ 'ĐÓN NHẬN' để bật đèn xanh!",
        "hashtags": "#AceOfCups #Crush #TinhYeuMoi #HenHo #TarotLove"
    },
    {
        "category": "Tình yêu",
        "name": "10 of Cups - Hạnh Phúc Viên Mãn",
        "image_url": "https://i.pinimg.com/564x/b8/b5/4f/b8b54f9a0c776092040032c18408253a.jpg",
        "message": "Cầu vồng hạnh phúc xuất hiện. Một gia đình êm ấm và tình yêu bền vững là đích đến.",
        "affirmation": "Gõ 'VIÊN MÃN' để gia đạo êm ấm!",
        "caption": "🌈 Happy Ending là có thật! \nLá 10 Ly báo hiệu một cái kết có hậu. Gia đình hạnh phúc, con cái ngoan ngoãn, tình cảm thăng hoa.\n👇 Gõ 'VIÊN MÃN' để cầu phúc cho gia đình!",
        "hashtags": "#10OfCups #GiaDinh #HanhPhuc #CuoiHoi #TarotVietnam"
    },
    {
        "category": "Tình yêu",
        "name": "2 of Cups - Sự Hòa Hợp",
        "image_url": "https://i.pinimg.com/564x/b8/0e/4d/b80e4d026926955743df07823f982959.jpg",
        "message": "Sự thấu hiểu và kết nối sâu sắc. Gương vỡ lại lành hoặc gặp người tâm đầu ý hợp.",
        "affirmation": "Gõ 'KẾT NỐI' để tìm thấy một nửa!",
        "caption": "💞 Hai tâm hồn, một nhịp đập! \nSự chia cách (nếu có) sẽ chấm dứt. Một cuộc hội ngộ hoặc làm lành đang đến rất gần.\n👇 Gõ 'KẾT NỐI' để hàn gắn yêu thương!",
        "hashtags": "#2OfCups #TuongTac #HenHo #LoveStory #Tarot"
    },

    # =======================
    # 🌿 CHỦ ĐỀ: CHỮA LÀNH (HEALING)
    # =======================
    {
        "category": "Chữa lành",
        "name": "The Star - Hy Vọng & Hồi Phục",
        "image_url": "https://i.pinimg.com/564x/27/b1/76/27b176711979318a6665796a5f15478d.jpg",
        "message": "Sau cơn mưa trời lại sáng. Mọi vết thương lòng đang được vũ trụ xoa dịu.",
        "affirmation": "Gõ 'BÌNH YÊN' để gột rửa nỗi buồn!",
        "caption": "🌿 Gửi những tâm hồn đang mệt mỏi... \nBạn đã vất vả rồi. The Star nói rằng thời kỳ đen tối nhất đã qua. Ánh sáng của sự bình yên đang về.\n👇 Gõ 'BÌNH YÊN' để thả trôi muộn phiền.",
        "hashtags": "#ChuaLanh #TheStar #Healing #MentalHealth #TarotVietnam"
    },
    {
        "category": "Chữa lành",
        "name": "The Hermit - Quay Về Bên Trong",
        "image_url": "https://i.pinimg.com/564x/6a/0c/36/6a0c36098059049448831464303e878e.jpg",
        "message": "Câu trả lời nằm trong sự tĩnh lặng. Hãy tách mình khỏi ồn ào để lắng nghe trực giác.",
        "affirmation": "Gõ 'THẤU HIỂU' để kết nối bản thân!",
        "caption": "🕯 Đừng tìm kiếm bên ngoài nữa... \nÁnh sáng soi rọi vào tâm hồn bạn. Hãy dành thời gian nghỉ ngơi, bạn sẽ thấy lối ra.\n👇 Gõ 'THẤU HIỂU' để tìm thấy bình an.",
        "hashtags": "#TheHermit #TinhLang #ThienDinh #HieuBanThan #Tarot"
    },
    {
        "category": "Chữa lành",
        "name": "Temperance - Cân Bằng",
        "image_url": "https://i.pinimg.com/564x/36/41/7d/36417d848784770267868512f4504190.jpg",
        "message": "Mọi thứ đang được điều chỉnh về trạng thái cân bằng. Hãy kiên nhẫn và trôi theo dòng chảy.",
        "affirmation": "Gõ 'CÂN BẰNG' để hòa hợp thân tâm!",
        "caption": "🌊 Nước chảy đá mòn... \nĐừng cố gắng cưỡng cầu. Hãy mềm mỏng như nước, mọi nút thắt sẽ tự động được tháo gỡ.\n👇 Gõ 'CÂN BẰNG' để chữa lành tâm trí.",
        "hashtags": "#Temperance #Yoga #Thienco #HealingVibes #Tarot"
    },

    # =======================
    # 🔥 CHỦ ĐỀ: ĐỘNG LỰC (MOTIVATION)
    # =======================
    {
        "category": "Động lực",
        "name": "The Sun - Mặt Trời Rực Rỡ",
        "image_url": "https://i.pinimg.com/564x/a6/f8/f1/a6f8f11059df1cb75f1df75e533d31d4.jpg",
        "message": "Thành công rực rỡ và niềm vui vỡ òa! Bạn là trung tâm của ánh sáng.",
        "affirmation": "Gõ 'TỎA SÁNG' để đón hào quang!",
        "caption": "☀️ Thời tới cản không kịp! \nMọi bóng tối bị xua tan. Chỉ còn lại thành công và niềm vui. Bạn chính là Mặt Trời!\n👇 Gõ 'TỎA SÁNG' để nhận năng lượng!",
        "hashtags": "#TheSun #ThanhCong #VuiVe #NangLuongTichCuc #Tarot"
    },
    {
        "category": "Động lực",
        "name": "The Chariot - Chiến Xa",
        "image_url": "https://i.pinimg.com/564x/87/4c/9c/874c9c18512d7742261688691515291b.jpg",
        "message": "Tập trung cao độ và tiến lên! Không gì có thể ngăn cản ý chí sắt đá của bạn.",
        "affirmation": "Gõ 'CHIẾN THẮNG' để bứt phá giới hạn!",
        "caption": "🐎 Thẳng tiến về đích! \nĐừng do dự nữa. The Chariot là tín hiệu bạn cần hành động ngay lập tức. Chiến thắng đã nằm trong tầm tay.\n👇 Gõ 'CHIẾN THẮNG' để tăng tốc!",
        "hashtags": "#TheChariot #MucTieu #QuyetTam #DongLucCuocSong #Tarot"
    },
    {
        "category": "Động lực",
        "name": "Strength - Sức Mạnh Nội Tại",
        "image_url": "https://i.pinimg.com/564x/31/ee/b2/31eeb24f46757b8559648942b0051676.jpg",
        "message": "Bạn mạnh mẽ hơn bạn nghĩ. Đừng bỏ cuộc, chiến thắng đang ở rất gần!",
        "affirmation": "Gõ 'MẠNH MẼ' để đánh thức nội lực!",
        "caption": "🔥 Dịu dàng là sức mạnh! \nThử thách hiện tại chỉ để tôi luyện bản lĩnh của bạn. Hãy đứng dậy và chiến đấu!\n👇 Gõ 'MẠNH MẼ' để tiếp thêm năng lượng!",
        "hashtags": "#Strength #NoiLuc #KienNhan #PhuNuManhMe #Tarot"
    }
]

# 3. HÀM TẠO SORA PROMPT TỰ ĐỘNG
def generate_sora_prompt_dynamic(description, duration):
    style_keywords = "Cinematic lighting, photorealistic, 8k, highly detailed, magical atmosphere, vertical ratio 9:16."
    if duration == "15s (Shorts)":
        return f"Fast paced close-up shot. Visual focus: {description}. High energy, visual hook, vivid colors. {style_keywords}"
    elif duration == "30s (Story)":
        return f"Medium shot, storytelling flow. Scene description: {description}. Emotional connection, smooth camera movement. {style_keywords}"
    else: # 60s
        return f"Wide establishing shot zooming in. Narrative journey: {description}. Epic scale, deep depth of field, slow motion moments. {style_keywords}"

# 4. CSS TÙY CHỈNH (Giữ nguyên font chữ to)
def inject_custom_css(color_theme):
    st.markdown(f"""
    <style>
    /* Button Style */
    .stButton>button {{
        background-color: {color_theme};
        color: white;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        padding: 12px 24px;
        font-size: 16px;
    }}
    .stButton>button:hover {{ filter: brightness(90%); }}
    
    /* Affirmation Box */
    .affirmation-box {{
        background-color: #f0f2f6;
        border-left: 10px solid {color_theme};
        padding: 25px;
        border-radius: 10px;
        font-size: 1.2em;
        margin-top: 15px;
        margin-bottom: 25px;
    }}
    
    /* Step Header */
    .step-header {{
        color: {color_theme};
        font-size: 1.5em;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 10px;
        border-bottom: 2px solid #eee;
        padding-bottom: 5px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 5. HÀM RÚT BÀI
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
    st.caption("Trạm sáng tạo Video Tarot: Đã cập nhật dữ liệu đa dạng hơn")
    
    # --- MENU CHỌN CHỦ ĐỀ ---
    col_menu, col_btn = st.columns([1, 2])
    with col_menu:
        topic = st.selectbox("Chọn chủ đề video:", ("Tài chính", "Tình yêu", "Chữa lành", "Động lực", "Tất cả"))
    
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

    # --- HIỂN THỊ KẾT QUẢ (PHẦN TRÊN) ---
    if 'card_result' in st.session_state:
        card = st.session_state['card_result']
        
        col_img, col_info = st.columns([1, 1.5], gap="large")
        
        with col_img:
            st.image(card['image_url'], use_container_width=True)
            
        with col_info:
            st.markdown(f"## 🔮 {card['name']}")
            st.info(f"💌 **Thông điệp:** {card['message']}")
            
            # Manifest Box
            st.markdown(f"""
            <div class="affirmation-box">
                <b>🔥 MANIFEST NGAY:</b><br>
                <i>"{card['affirmation']}"</i>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔄 Rút bài khác"):
                draw_card(topic)
                st.rerun()

        # --- CÔNG CỤ CREATOR (PHẦN DƯỚI) ---
        st.markdown("---")
        st.markdown(f"<div class='step-header'>🛠️ CÔNG CỤ SẢN XUẤT (Full Màn Hình)</div>", unsafe_allow_html=True)

        # 1. BƯỚC 1: LẤY PROMPT CHO ELIMA
        st.markdown("#### 1️⃣ Bước 1: Copy câu lệnh này gửi cho Elima")
        prompt_for_elima = f"Tôi vừa rút được lá bài '{card['name']}' về chủ đề '{card['category']}'. Hãy đóng vai một Tarot Reader chuyên nghiệp, viết cho tôi kịch bản video ngắn (gồm Hook giật gân, Body cảm động, Call to Action: '{card['affirmation']}'). Sau đó hãy vẽ giúp tôi hình ảnh lá bài này theo phong cách 3D, ánh sáng huyền ảo để làm nền video."
        st.code(prompt_for_elima, language="text")
        st.link_button("💬 Mở Chat với Elima ngay", ELIMA_LINK, type="primary", use_container_width=True)

        st.write("")

        # 2. BƯỚC 2: NHẬP LIỆU & TẠO PROMPT
        st.markdown("#### 2️⃣ Bước 2: Dán nội dung từ Elima vào đây")
        st.caption("Dán đoạn mô tả hình ảnh vào ô bên dưới. Ô nhập liệu đã được mở rộng.")
        
        user_desc = st.text_area(
            label="Dán mô tả hình ảnh tại đây:", 
            placeholder="Ví dụ: Một dòng sông vàng chảy qua thung lũng, bầu trời rực rỡ...",
            height=300 
        )
        
        # 3. KẾT QUẢ
        if user_desc:
            st.success("✅ Đã nhận mô tả! Dưới đây là Prompt Video cho bạn:")
            tabs = st.tabs(["15s (Shorts)", "30s (Story)", "60s (Full)"])
            durations = ["15s (Shorts)", "30s (Story)", "60s (Full)"]
            
            for i, tab in enumerate(tabs):
                with tab:
                    final_prompt = generate_sora_prompt_dynamic(user_desc, durations[i])
                    st.code(final_prompt, language="text")
        
        # Caption & Hashtag
        st.markdown("#### 3️⃣ Bước 3: Caption & Hashtag (Copy đăng bài)")
        default_caption = card.get('caption', 'Chưa có caption mẫu.')
        default_hashtags = card.get('hashtags', '#Tarot')
        
        col_cap, col_hash = st.columns(2)
        with col_cap:
            st.text_area("Caption Facebook/TikTok:", value=default_caption, height=150)
        with col_hash:
            st.text_area("Hashtags:", value=default_hashtags, height=150)

    else:
        st.markdown(f"""
        <div style='text-align: center; color: #666; padding: 50px;'>
            <h3>👋 Chào Moon!</h3>
            <p>Dữ liệu đã được nạp đầy đủ (hơn 20 lá bài).<br>Hãy chọn chủ đề bên trên để bắt đầu nhé.</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
