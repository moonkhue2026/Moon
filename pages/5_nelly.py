import streamlit as st
import random
import datetime

# ... (Giữ nguyên phần st.set_page_config và các khai báo thư viện) ...

st.title("👠 NELLY MANAGER v9.1 (Fixed Logic)")
st.markdown("*Phiên bản sửa lỗi Caption & Bổ sung Kịch bản chi tiết*")

# =========================================================
# 1. DATA CENTER (ĐÃ NÂNG CẤP ĐỂ KHÔNG BỊ NHẦM)
# =========================================================

# Dictionary Caption riêng cho từng chủ đề (Để không bị râu ông nọ cắm cằm bà kia)
caption_templates = {
    "Dancing & Trends": {
        "base": "🔥 Đốt cháy sàn diễn hôm nay! Ai bảo tập nhảy là mệt? Vừa đẹp dáng vừa thần thái ngút ngàn.",
        "hashtags": "#NellyDance #SexyDance #HighHeels #DanceChallenge"
    },
    "Bohemian": { # Tách riêng Bohemian ra nếu nó là style đặc biệt
        "base": "🌿 Tự do, phóng khoáng và một chút hoang dại. Về với thiên nhiên cùng Nelly nhé.",
        "hashtags": "#BohoChic #NellyStyle #FreeSpirit #Vintage"
    }, 
    "👗 Hack Dáng & Phối Đồ": {
        "base": "👗 Mặc đẹp không khó, quan trọng là biết 'hack'! Lưu ngay bí kíp này kẻo lỡ nha mấy bà.",
        "hashtags": "#FashionTips #HackDang #OOTD #NellyFashion"
    },
    "📸 Tạo Dáng (Posing)": {
        "base": "📸 Đừng để bức ảnh 'chết trân'! Thử ngay dáng này để like tăng vù vù nào.",
        "hashtags": "#PosingTips #TaoDangChupAnh #Slay #InstaGood"
    },
    "💄 Làm Đẹp (Beauty)": {
        "base": "✨ Muốn đẹp tự nhiên nhưng không tự nhiên mà đẹp. Đây là bí mật của Nelly!",
        "hashtags": "#BeautyHacks #GlowUp #SkincareRoutine #Makeup"
    },
    "🥂 Lifestyle": {
        "base": "🥂 Sống chậm lại một chút, yêu bản thân nhiều chút. Nhật ký ngày hôm nay...",
        "hashtags": "#Lifestyle #DailyVlog #SelfLove #Motivation"
    }
}

# (Giữ nguyên viral_hooks, weekly_schedule, categories, music_library cũ)
# ... [Paste lại phần viral_hooks, categories... từ code cũ vào đây] ... 

# Copy lại data categories để code chạy (Tớ để rút gọn ở đây cho Moon dễ nhìn, nhớ giữ lại full data nhé)
categories = {
    "💃 Dancing & Trends": ["Bohemian Dance", "Sexy Dance", "Shuffle Dance", "Trend TikTok"],
    "👗 Hack Dáng & Phối Đồ": ["Hack chân dài", "Che bụng mỡ", "Phối đồ Gym", "Outfit công sở"],
    "📸 Tạo Dáng (Posing)": ["Dáng đứng hack chân", "Thần thái sang chảnh", "Tạo dáng với ghế", "Góc mặt đẹp"],
    "💄 Làm Đẹp (Beauty)": ["Makeup Tone Tây", "Skincare Glass Skin", "Tóc hack tuổi", "Nước hoa bad girl"],
    "🥂 Lifestyle": ["Tư duy phụ nữ hiện đại", "Vlog 1 ngày", "Eat Clean giữ dáng", "Quản lý tài chính"]
}
viral_hooks = {
    "⚠️ Cảnh báo/Sai lầm": ["❌ Dừng ngay việc...", "⚠️ 3 Lỗi sai chết người..."],
    "🔥 Biến hình/Lột xác": ["✨ Từ 'Bà thím' hóa 'Chị đại'...", "😱 Không thể tin đây là cùng một người..."],
    "🎯 Nỗi đau cụ thể": ["😭 Chân ngắn 1m50 mặc gì...", "🥑 Bụng mỡ dưới to..."]
}

# =========================================================
# GIAO DIỆN & LOGIC XỬ LÝ
# =========================================================

# --- SIDEBAR (Giữ nguyên) ---
# ...

# --- MAIN CONFIG ---
with st.expander("⚙️ CẤU HÌNH CHIẾN LƯỢC", expanded=True):
    c1, c2 = st.columns(2)
    with c1: 
        group_select = st.selectbox("1. Nhóm chủ đề:", list(categories.keys()))
        topic_select = st.selectbox("2. Chủ đề cụ thể:", categories[group_select])
    with c2:
        hook_type = st.selectbox("3. Chiến thuật Viral (Hook):", list(viral_hooks.keys()))
        selected_hook = st.selectbox("👉 Chọn câu giật tít:", viral_hooks[hook_type])

    # --- XỬ LÝ LOGIC CAPTION CHUẨN (FIXED) ---
    # Logic cũ bị sai, đây là logic mới:
    current_caption_data = caption_templates.get(group_select, caption_templates["🥂 Lifestyle"]) # Mặc định là Lifestyle nếu lỗi
    
    # Xử lý riêng ngoại lệ Bohemian nằm trong nhóm Dancing hoặc nhóm khác
    if "Bohemian" in topic_select:
        current_caption_data = caption_templates["Bohemian"]

    # --- TỰ ĐỘNG GỢI Ý OUTFIT ---
    if "Bohemian" in topic_select: 
        outfit = "Boho-chic maxi dress, headband, vintage accessories"
        music_key = "Bohemian"
    elif "Dancing" in group_select: 
        outfit = "Sexy Cut-out Bodysuit & High Heels 👠" if "Sexy" in topic_select else "Trendy gym set & Sneakers"
        music_key = "Dancing"
    elif "Styling" in group_select:
        outfit = "High-fashion blazer & jeans, heels"
        music_key = "Styling"
    else:
        outfit = "Elegant daily wear"
        music_key = "Lifestyle"

# =========================================================
# HIỂN THỊ KẾT QUẢ (UPDATED)
# =========================================================

tab_content, tab_video, tab_script = st.tabs(["📝 CAPTION & ẢNH", "🎥 PROMPT VIDEO", "🎬 KỊCH BẢN CHI TIẾT (NEW)"])

# --- TAB 1: CAPTION ---
with tab_content:
    st.subheader("📝 Caption Facebook/TikTok")
    st.info("💡 Caption đã được fix theo đúng chủ đề bạn chọn!")
    
    final_caption = f"""
    {selected_hook} 
    
    {current_caption_data['base']}
    
    👇 Sự thật là... (Xem hết video để thấy sự thay đổi nhé!)
    
    {current_caption_data['hashtags']} #{topic_select.replace(' ','')} #Viral
    """
    st.text_area("Copy nội dung này:", final_caption, height=200)

# --- TAB 2: VIDEO ---
with tab_video:
    st.write(f"Đang tạo prompt cho: **{topic_select}**")
    # ... (Giữ nguyên logic prompt cũ) ...
    st.code(f"/imagine prompt: Nelly wearing {outfit}, performing {topic_select}, cinematic lighting --ar 9:16", language="text")

# --- TAB 3: KỊCH BẢN (TÍNH NĂNG MỚI ĐỀN BÙ CHO MOON) ---
with tab_script:
    st.header(f"🎬 Kịch bản quay: {topic_select}")
    
    # Logic tạo kịch bản dựa trên HOOK
    if "Cảnh báo" in hook_type:
        act_1 = "Gương mặt nghiêm trọng/Hoảng hốt. Giơ tay ra dấu 'STOP' ❌."
        act_2 = "Chỉ vào lỗi sai (Ví dụ: Đang mặc bộ đồ dìm dáng). Lắc đầu ngao ngán."
        act_3 = "Biến hình sang bộ đẹp (Outfit chuẩn). Cười tươi, pose dáng tự tin."
    elif "Biến hình" in hook_type:
        act_1 = "Mặt mộc/Đồ ngủ lôi thôi. Nhìn vào gương thở dài."
        act_2 = "Hiệu ứng búng tay/Đá chân vào ống kính (Transition)."
        act_3 = "Bùm! Xuất hiện lộng lẫy trong bộ " + outfit + ". Nhảy/Đi catwalk cực cháy."
    else: # Nỗi đau
        act_1 = "Ngồi buồn rầu, tay che khuyết điểm (bụng/chân)."
        act_2 = "Text hiện lên: 'Đừng lo!'. Nelly xuất hiện đưa ra giải pháp."
        act_3 = "Diện đồ đẹp, xoay 1 vòng hạnh phúc."

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### ⏱️ 0-3s (Hook)")
        st.warning(act_1)
        st.caption(f"🗣️ Voice: {selected_hook}")
    with col2:
        st.markdown("#### ⏱️ 3-15s (Body)")
        st.info(act_2)
        st.caption("🗣️ Voice: 'Đây là lý do bạn mãi chưa đẹp...'")
    with col3:
        st.markdown("#### ⏱️ 15s+ (Kết)")
        st.success(act_3)
        st.caption("🗣️ Voice: 'Thử ngay đi nha!'")
