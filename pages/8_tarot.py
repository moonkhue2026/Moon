# Version: v3.2 (FIX ERROR - Vá lỗi xung đột dữ liệu cũ)
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

# 2. DỮ LIỆU BÀI TAROT
tarot_database = [
    # =======================
    # 💰 TÀI CHÍNH
    # =======================
    {
        "category": "Tài chính",
        "name": "Ace of Pentacles",
        "vn_name": "Át Tiền",
        "image_url": "https://i.pinimg.com/564x/a2/27/98/a22798e604de6e9e436894d7545e8550.jpg",
        "message": "Cánh cửa tài chính mở toang! Nguồn tiền khổng lồ đang chảy vào.",
        "affirmation": "Gõ 'TRIỆU PHÚ' để nhận chìa khóa kho báu!",
        "caption": "🔥 Tín hiệu vũ trụ: Dòng tiền lớn đang lao đến bạn! 💰\nSự túng thiếu kết thúc ngay hôm nay.\n👇 Gõ 'TRIỆU PHÚ' để nhận ngay!",
        "hashtags": "#TarotMoney #LuatHapDan #TaiChinh #GiauCo #Manifest",
        "visual_desc": "A giant glowing golden coin (Pentacle) appearing from a magical cloud, hovering over a lush green garden. Golden sparkles raining down like magic dust."
    },
    {
        "category": "Tài chính",
        "name": "10 of Pentacles",
        "vn_name": "Di Sản Thịnh Vượng",
        "image_url": "https://i.pinimg.com/564x/0f/68/73/0f68735500806443657754b23829035e.jpg",
        "message": "Sự sung túc trọn vẹn. Tiền bạc, bất động sản đang tới.",
        "affirmation": "Gõ 'SUNG TÚC' để đón lộc về nhà!",
        "caption": "🏠 Nhà cao cửa rộng, tiền bạc đầy kho! \nLá 10 Tiền báo hiệu sự viên mãn về vật chất.\n👇 Gõ 'SUNG TÚC' để nhận lộc đất đai!",
        "hashtags": "#10OfPentacles #BatDongSan #TaiLoc #GiaDinh",
        "visual_desc": "A magnificent ancient castle gate opening slowly. Inside is a treasure chest overflowing with gold coins and heirlooms. A happy family silhouette in the background. Warm sunset light."
    },
    {
        "category": "Tài chính",
        "name": "King of Pentacles",
        "vn_name": "Vua Tiền",
        "image_url": "https://i.pinimg.com/564x/4e/d8/4a/4ed84a1444634289895316315840428e.jpg",
        "message": "Sự giàu có bền vững và địa vị cao đang đến.",
        "affirmation": "Gõ 'THÀNH CÔNG' để kích hoạt năng lượng Vua Tiền!",
        "caption": "👑 Bạn sinh ra để làm chủ cuộc chơi! \nTiền bạc không chỉ đến, mà còn ở lại và sinh sôi.\n👇 Gõ 'THÀNH CÔNG' để nhận vía lãnh đạo!",
        "hashtags": "#KingOfPentacles #Business #CEO #TarotVietnam",
        "visual_desc": "A majestic King sitting on a throne made of vines and gold, holding a glowing golden coin. He is surrounded by a forest of abundance. Powerful and wealthy atmosphere."
    },
     {
        "category": "Tài chính",
        "name": "Wheel of Fortune",
        "vn_name": "Vòng Xoay Định Mệnh",
        "image_url": "https://i.pinimg.com/564x/e9/b3/ef/e9b3ef56158223945480746973970742.jpg",
        "message": "Vận may đảo chiều cực mạnh! Cơ hội đổi đời xuất hiện.",
        "affirmation": "Gõ 'MAY MẮN' để xoay chuyển càn khôn!",
        "caption": "🎰 Thời tới cản không kịp! \nVũ trụ đang quay bánh xe số phận. Từ bế tắc chuyển sang hanh thông.\n👇 Gõ 'MAY MẮN' để nhận vía đỏ!",
        "hashtags": "#WheelOfFortune #MayMan #DoiVan #TarotDaily",
        "visual_desc": "A giant mystical golden wheel spinning in the starry sky. As it stops, it glows intensely, turning grey clouds into golden light. Magical symbols floating around."
    },

    # =======================
    # 💘 TÌNH YÊU
    # =======================
    {
        "category": "Tình yêu",
        "name": "The Lovers",
        "vn_name": "Tình Yêu Đích Thực",
        "image_url": "https://i.pinimg.com/564x/53/76/75/5376752765b4528bf80016a504859bc0.jpg", 
        "message": "Soulmate đang đến. Bạn được yêu thương vô điều kiện.",
        "affirmation": "Gõ 'HẠNH PHÚC' để thu hút tri kỷ!",
        "caption": "💘 Soulmate của bạn đang đến gần!\nNgười này sẽ bù đắp mọi tổn thương quá khứ của bạn.\n👇 Gõ 'HẠNH PHÚC' để mở cửa trái tim!",
        "hashtags": "#TheLovers #Soulmate #TinhYeu #LuatHapDan",
        "visual_desc": "Two glowing souls (pink and blue energy) dancing in the galaxy, spiraling and merging into a radiant heart shape. An angel silhouette blessing them from above. Romantic and soft."
    },
    {
        "category": "Tình yêu",
        "name": "Ace of Cups",
        "vn_name": "Tình Yêu Chớm Nở",
        "image_url": "https://i.pinimg.com/564x/c3/0b/cf/c30bcf77356262198084f74668045501.jpg",
        "message": "Trái tim bạn sắp rung động lần nữa. Khởi đầu mới đầy cảm xúc.",
        "affirmation": "Gõ 'ĐÓN NHẬN' để tình yêu chảy vào tim!",
        "caption": "💌 Ai đó đang thầm thương trộm nhớ bạn... \nChiếc cốc tình yêu đang tràn đầy. Hãy mở lòng nhé!\n👇 Gõ 'ĐÓN NHẬN' để bật đèn xanh!",
        "hashtags": "#AceOfCups #Crush #TinhYeuMoi #HenHo",
        "visual_desc": "A golden chalice (Cup) overflowing with sparkling pink water. The water flows into a crystal clear lake where lotus flowers bloom instantly. Magical pink aura."
    },

    # =======================
    # 🌿 CHỮA LÀNH
    # =======================
    {
        "category": "Chữa lành",
        "name": "The Star",
        "vn_name": "Hy Vọng & Hồi Phục",
        "image_url": "https://i.pinimg.com/564x/27/b1/76/27b176711979318a6665796a5f15478d.jpg",
        "message": "Sau cơn mưa trời lại sáng. Vết thương lòng đang được xoa dịu.",
        "affirmation": "Gõ 'BÌNH YÊN' để gột rửa nỗi buồn!",
        "caption": "🌿 Gửi những tâm hồn đang mệt mỏi... \nThời kỳ đen tối nhất đã qua. Ánh sáng của sự bình yên đang về.\n👇 Gõ 'BÌNH YÊN' để thả trôi muộn phiền.",
        "hashtags": "#ChuaLanh #TheStar #Healing #MentalHealth",
        "visual_desc": "A large, bright star shining in a deep blue night sky, reflecting perfectly on a calm, mirror-like lake. Fireflies dancing around. The atmosphere is incredibly peaceful and serene."
    },
    {
        "category": "Chữa lành",
        "name": "The Hermit",
        "vn_name": "Quay Về Bên Trong",
        "image_url": "https://i.pinimg.com/564x/6a/0c/36/6a0c36098059049448831464303e878e.jpg",
        "message": "Câu trả lời nằm trong sự tĩnh lặng. Hãy lắng nghe trực giác.",
        "affirmation": "Gõ 'THẤU HIỂU' để kết nối bản thân!",
        "caption": "🕯 Đừng tìm kiếm bên ngoài nữa... \nÁnh sáng soi rọi vào tâm hồn bạn. Hãy dành thời gian nghỉ ngơi.\n👇 Gõ 'THẤU HIỂU' để tìm thấy bình an.",
        "hashtags": "#TheHermit #TinhLang #ThienDinh #HieuBanThan",
        "visual_desc": "A lone lantern glowing warmly in a misty, dark forest. The light cuts through the fog, revealing a path of moss and ancient stones. Quiet, solitary, and wise atmosphere."
    },

    # =======================
    # 🔥 ĐỘNG LỰC
    # =======================
    {
        "category": "Động lực",
        "name": "The Sun",
        "vn_name": "Mặt Trời Rực Rỡ",
        "image_url": "https://i.pinimg.com/564x/a6/f8/f1/a6f8f11059df1cb75f1df75e533d31d4.jpg",
        "message": "Thành công rực rỡ và niềm vui vỡ òa!",
        "affirmation": "Gõ 'TỎA SÁNG' để đón hào quang!",
        "caption": "☀️ Thời tới cản không kịp! \nMọi bóng tối bị xua tan. Bạn chính là Mặt Trời!\n👇 Gõ 'TỎA SÁNG' để nhận năng lượng!",
        "hashtags": "#TheSun #ThanhCong #VuiVe #NangLuongTichCuc",
        "visual_desc": "A giant radiant sun rising over a field of sunflowers. The sunflowers bloom rapidly in time-lapse. Bright yellow and orange colors, full of life and joy."
    },
    {
        "category": "Động lực",
        "name": "Strength",
        "vn_name": "Sức Mạnh Nội Tại",
        "image_url": "https://i.pinimg.com/564x/31/ee/b2/31eeb24f46757b8559648942b0051676.jpg",
        "message": "Bạn mạnh mẽ hơn bạn nghĩ. Chiến thắng đang ở rất gần!",
        "affirmation": "Gõ 'MẠNH MẼ' để đánh thức nội lực!",
        "caption": "🔥 Dịu dàng là sức mạnh! \nThử thách hiện tại chỉ để tôi luyện bản lĩnh của bạn.\n👇 Gõ 'MẠNH MẼ' để tiếp thêm năng lượng!",
        "hashtags": "#Strength #NoiLuc #KienNhan #PhuNuManhMe",
        "visual_desc": "Close up of a magnificent lion looking calm and peaceful. A woman's hand gently pets the lion's mane. A warm, glowing orange aura surrounds them. Symbolizing inner strength."
    }
]

# 3. HÀM TẠO SORA PROMPT (AUTO)
def generate_sora_prompt_auto(card_name, visual_desc, duration):
    style = "Cinematic lighting, photorealistic, 8k, highly detailed, magical atmosphere, depth of field."
    base_subject = f"A clear, cinematic close-up view of the Tarot card '{card_name}'. The card art is visible."
    content = f"{base_subject} {visual_desc}"
    negative = "--negative text, subtitles, captions, words, voice, speech"
    sound = "--sound mystical ambiance, magic chimes, cinematic sound effects, nature sounds, NO voice"

    if duration == "15s (Shorts)":
        return f"Fast paced close-up. {content}. High energy visual hook. {style} {sound} {negative}"
    elif duration == "30s (Story)":
        return f"Medium shot, storytelling flow. {content}. Smooth camera movement revealing the environment. {style} {sound} {negative}"
    else: # 60s
        return f"Wide establishing shot zooming into the card. Narrative journey. {content}. Epic scale, slow motion moments. {style} {sound} {negative}"

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
        padding: 12px 24px;
        font-size: 16px;
    }}
    .stButton>button:hover {{ filter: brightness(90%); }}
    .affirmation-box {{
        background-color: #f0f2f6;
        border-left: 10px solid {color_theme};
        padding: 25px;
        border-radius: 10px;
        font-size: 1.2em;
        margin-top: 15px;
        margin-bottom: 25px;
    }}
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
    st.caption("v3.2 - Fix Error: Đã vá lỗi xung đột dữ liệu cũ")
    
    # --- MENU ---
    col_menu, col_btn = st.columns([1, 2])
    with col_menu:
        topic = st.selectbox("Chọn chủ đề:", ("Tài chính", "Tình yêu", "Chữa lành", "Động lực", "Tất cả"))
    
    colors = {"Tài chính": "#FFD700", "Tình yêu": "#FF69B4", "Chữa lành": "#00CED1", "Động lực": "#FF4500", "Tất cả": "#7E57C2"}
    inject_custom_css(colors.get(topic, "#7E57C2"))
    
    with col_btn:
        st.write("")
        st.write("")
        if st.button(f"✨ RÚT BÀI & TẠO CONTENT: {topic.upper()} ✨", use_container_width=True):
            draw_card(topic)
            st.rerun()
            
    st.divider()

    # --- KẾT QUẢ ---
    if 'card_result' in st.session_state:
        card = st.session_state['card_result']
        
        # PHẦN TRÊN: VISUAL
        col_img, col_info = st.columns([1, 1.5], gap="large")
        with col_img:
            st.image(card['image_url'], use_container_width=True)
        with col_info:
            # === [ĐOẠN CODE VÁ LỖI Ở ĐÂY] ===
            # Sử dụng .get('vn_name', '') để nếu không có tên tiếng Việt thì không bị lỗi
            vn_name = card.get('vn_name', '') 
            st.markdown(f"## 🔮 {card['name']} - {vn_name}")
            
            st.info(f"💌 **Thông điệp:** {card['message']}")
            st.markdown(f"""<div class="affirmation-box"><b>🔥 MANIFEST:</b><br><i>"{card['affirmation']}"</i></div>""", unsafe_allow_html=True)
            if st.button("🔄 Rút bài khác"):
                draw_card(topic)
                st.rerun()

        # PHẦN DƯỚI: CÔNG CỤ TỰ ĐỘNG
        st.markdown("---")
        st.markdown(f"<div class='step-header'>🛠️ CÔNG CỤ SẢN XUẤT (Auto)</div>", unsafe_allow_html=True)

        col_left, col_right = st.columns(2, gap="large")

        # CỘT TRÁI: SORA PROMPT (VIDEO)
        with col_left:
            st.subheader("🎥 1. Lấy Prompt Video (Sora)")
            st.caption("Prompt đã được tự động tối ưu: Rõ lá bài + Huyền bí + Không chữ.")
            
            tabs = st.tabs(["15s (Shorts)", "30s (Story)", "60s (Full)"])
            durations = ["15s (Shorts)", "30s (Story)", "60s (Full)"]
            
            for i, tab in enumerate(tabs):
                with tab:
                    final_prompt = generate_sora_prompt_auto(card['name'], card.get('visual_desc', ''), durations[i])
                    st.code(final_prompt, language="text")
                    st.success("👉 Copy dán vào Sora/Runway.")

        # CỘT PHẢI: ELIMA PROMPT (VOICE SCRIPT)
        with col_right:
            st.subheader("🎙️ 2. Lấy Kịch bản Voice (Elima)")
            st.caption("Dùng lệnh này để Elima viết lời bình (Voiceover) cho bạn.")
            
            prompt_voice = f"Tôi rút được lá '{card['name']}' ({vn_name}) về '{card['category']}'. Hãy viết kịch bản Voiceover ngắn gọn (3 phần: Hook - Body - CTA '{card['affirmation']}'). Tone giọng huyền bí, lôi cuốn. Đừng viết mô tả ảnh, chỉ viết lời bình để đọc."
            st.code(prompt_voice, language="text")
            st.link_button("💬 Chat với Elima ngay", ELIMA_LINK, type="primary", use_container_width=True)
            
            st.markdown("---")
            st.caption("📝 **Caption & Hashtags (Dự phòng):**")
            # Dùng .get() cho caption để tránh lỗi luôn
            st.code(f"{card.get('caption', '')}\n\n{card.get('hashtags', '')}", language="text")

    else:
        st.info("👋 Hãy chọn chủ đề và bấm Rút Bài để bắt đầu.")

if __name__ == "__main__":
    main()
