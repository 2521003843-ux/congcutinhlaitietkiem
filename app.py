import streamlit as st
import pandas as pd
import numpy as np
st.image("logo.jpg")
# Cấu hình trang Streamlit
st.set_page_config(
    page_title="Ngân hàng Anh Pha",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh giao diện: Tối ưu độ tương phản chữ rõ nét, dễ đọc trên nền tối Địa Phủ
st.markdown("""
    <style>
    /* Màu nền chung cho trang */
    .main {
        background-color: #0b0b0f;
        color: #f0f0f5;
    }
    /* Sidebar */
    .stSidebar {
        background-color: #14141f;
        border-right: 1px solid #4a1515;
    }
    .stSidebar label {
        color: #ffcccc !important;
        font-weight: 600;
    }
    /* Tiêu đề chính to rõ */
    h1, h2, h3 {
        color: #ff4d4d !important;
        font-family: 'Cinzel', serif, sans-serif;
        text-shadow: 0px 0px 12px rgba(255, 77, 77, 0.6);
    }
    /* Card kết quả nổi bật, chữ sáng rõ */
    .metric-card {
        background: linear-gradient(135deg, #1f0f0f 0%, #2e1414 100%);
        border: 1px solid #ff5c5c;
        padding: 22px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(255, 0, 0, 0.25);
        text-align: center;
        margin-bottom: 15px;
    }
    .metric-value {
        font-size: 28px;
        font-weight: bold;
        color: #ffe066;
        text-shadow: 0 0 8px rgba(255, 224, 102, 0.4);
    }
    .metric-label {
        font-size: 15px;
        color: #dcdce6;
        margin-top: 8px;
        font-weight: 500;
    }
    /* Nút bấm */
    .stButton>button {
        background: linear-gradient(90deg, #d90429 0%, #ef233c 100%);
        color: #ffffff;
        font-weight: bold;
        border: 1px solid #ffa3a3;
        border-radius: 8px;
        padding: 10px 24px;
        box-shadow: 0 0 12px rgba(239, 35, 60, 0.6);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #ef233c 0%, #ff4d4d 100%);
        border-color: #ffffff;
        color: #ffffff;
    }
    /* Chữ hiển thị thông tin chung */
    p, span, div, label {
        color: #e2e2ec;
    }
    .stAlert {
        background-color: #1c1414 !important;
        color: #ffcccc !important;
        border: 1px solid #ff4d4d !important;
    }
    </style>
""", unsafe_allow_html=True)

# Tiêu đề ứng dụng
st.title("🔥 NGÂN HÀNG ĐỊA PHỦ - HỆ THỐNG GỬI TIẾT KIỆM ÂM PHỦ 🔥")
st.markdown("*(Cam kết sinh lời cực đại, rút gốc ở trần gian, nhận lãi ở... âm phủ!)*")

# Sidebar nhập liệu thông tin
st.sidebar.header("📜 HỒ SƠ GỬI TIỀN VÀNG MÃ")

with st.sidebar.form("saving_form"):
    deposit_type = st.radio("Loại tiền tệ gửi:", ["VNĐ Trần Gian (VNĐ)", "Vàng Mã / Đô La Âm Phủ"])
    
    if deposit_type == "VNĐ Trần Gian (VNĐ)":
        principal = st.number_input("Số tiền gửi (VNĐ):", min_value=1_000_000, max_value=1_000_000_000_000, value=100_000_000, step=10_000_000, format="%d")
        unit_str = "VNĐ"
    else:
        principal = st.number_input("Số tờ Vàng Mã / Đô La Âm Phủ:", min_value=1_000, max_value=10_000_000_000, value=50_000, step=1000, format="%d")
        unit_str = "Tờ/Đồng"

    term_months = st.slider("Kỳ hạn gửi (Tháng):", min_value=1, max_value=120, value=12)
    annual_rate = st.number_input("Lãi suất năm (%/năm):", min_value=0.1, max_value=99.9, value=8.5, step=0.1)
    calc_method = st.selectbox("Phương pháp tính lãi:", ["Lãi Đơn (Simple Interest)", "Lãi Kép (Compound Interest)"])
    payout_freq = st.selectbox("Hình thức lãnh lãi:", [
        "Lãnh lãi cuối kỳ", 
        "Lãnh lãi theo tháng", 
        "Lãnh lãi theo quý"
    ])

    submitted = st.form_submit_button("🔮 TÍNH TOÁN TÀI CHÍNH ÂM PHỦ")

# Thực hiện tính toán tự động khi người dùng bấm nút
if submitted:
    monthly_rate = (annual_rate / 100) / 12
    total_months = term_months
    
    periodic_interest = 0
    total_interest = 0
    total_amount = 0
    
    # --- LOGIC TÍNH TOÁN ---
    if "Lãi Đơn" in calc_method:
        total_interest = principal * (annual_rate / 100) * (total_months / 12)
        total_amount = principal + total_interest
        
        if payout_freq == "Lãnh lãi theo tháng":
            periodic_interest = total_interest / total_months
        elif payout_freq == "Lãnh lãi theo quý":
            periodic_interest = (total_interest / total_months) * 3
        else:
            periodic_interest = total_interest
    else:
        if payout_freq == "Lãnh lãi cuối kỳ":
            total_amount = principal * ((1 + monthly_rate) ** total_months)
            total_interest = total_amount - principal
            periodic_interest = 0
        elif payout_freq == "Lãnh lãi theo tháng":
            periodic_interest = principal * monthly_rate
            total_interest = periodic_interest * total_months
            total_amount = principal + total_interest
        elif payout_freq == "Lãnh lãi theo quý":
            quarterly_rate = monthly_rate * 3
            periodic_interest = principal * quarterly_rate
            num_quarters = total_months / 3
            total_interest = periodic_interest * num_quarters
            total_amount = principal

    # --- HIỂN THỊ KẾT QUẢ ---
    st.markdown("---")
    st.subheader("📊 KẾT QUẢ PHÂN TÍCH TÀI CHÍNH CHI TIẾT")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{periodic_interest:,.0f} {unit_str}</div>
                <div class="metric-label">Tiền Lãi Định Kỳ ({payout_freq})</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value" style="color: #ff6b6b;">{total_interest:,.0f} {unit_str}</div>
                <div class="metric-label">Tổng Tiền Lãi Nhận Được</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value" style="color: #38ef7d;">{total_amount:,.0f} {unit_str}</div>
                <div class="metric-label">Tổng Gốc + Lãi Khi Đáo Hạn</div>
            </div>
        """, unsafe_allow_html=True)

    # --- BIỂU ĐỒ TĂNG TRƯỞNG ---
    st.markdown("### 📈 Biểu đồ tăng trưởng tài sản âm phủ qua các tháng")
    chart_data = []
    
    for m in range(1, total_months + 1):
        if "Lãi Kép" in calc_method and payout_freq == "Lãnh lãi cuối kỳ":
            current_val = principal * ((1 + monthly_rate) ** m)
        else:
            if "Lãi Kép" in calc_method and payout_freq == "Lãnh lãi theo tháng":
                acc_int = principal * monthly_rate * m
                current_val = principal + acc_int
            else:
                acc_int = principal * (annual_rate / 100) * (m / 12)
                current_val = principal + acc_int
                
        chart_data.append({"Tháng": f"Tháng {m}", "Tổng Giá Trị (Gốc + Lãi)": current_val})
        
    df_chart = pd.DataFrame(chart_data).set_index("Tháng")
    st.line_chart(df_chart, color="#ff4d4d")

    # --- TIỆN ÍCH ĐỘC QUYỀN ĐỊA PHỦ ---
    st.markdown("---")
    st.subheader("🔱 TIỆN ÍCH ĐỘC QUYỀN ĐỊA PHỦ")

    tab1, tab2, tab3 = st.tabs(["🕯️ Bói Vận Mệnh Đầu Tư", "🛡️ Bảo Hiểm Đầu Thai", "👑 Đặc Quyền Diêm Vương"])

    with tab1:
        st.markdown("#### Xin xăm tài lộc âm phủ:")
        if st.button("Lắc ống xăm tài chính"):
            fortunes = [
                "Quẻ THƯỢNG THƯỢNG: Đầu tư vàng mã kỳ này, âm ti kết thực, đời sau làm đại gia bên kia thế giới!",
                "Quẻ TRUNG BÌNH: Lãi đủ trả tiền đò qua sông Nại Hà, không lo đói khát.",
                "Quẻ HẠ HẠ: Cẩn thận quỷ sứ lạm phát đốt nhầm tiền giả, đề nghị kiểm tra kỹ serial trước khi gửi!"
            ]
            import random
            st.info(f"📜 Kết quả xăm: {random.choice(fortunes)}")

    with tab2:
       
        ins_package = st.selectbox("Chọn cấp độ bảo hiểm:", [
            "Gói Thường (Bảo hiểm 50% tài sản khi gặp Diêm Vương xét duyệt sớm)",
            "Gói VIP (Bảo hiểm 100% gốc + tặng kèm 1 căn nhà giấy cao cấp âm phủ)",
            "Gói Siêu VIP (Miễn phí qua cầu Nại Hà, ưu tiên đầu thai làm con nhà quan)"
        ])
        if st.checkbox("Xác nhận trích 1% tiền lãi mua bảo hiểm"):
            st.success(f"Đã kích hoạt thành công: {ins_package}. Hồn phách và tài sản của bạn đã được bảo vệ tối đa!")

    with tab3:
        st.markdown("#### Đặc quyền gửi tiền số lượng lớn:")
        st.markdown("""
        - 🦇 **Miễn phí vận chuyển:** Không tốn phí đốt vàng mã trung gian.
        - 👻 **Hỗ trợ 24/7:** Tổng đài viên là các Hắc Bạch Vô Thường túc trực liên tục.
        - 💎 **Tặng phẩm đi kèm:** 1 bình phong thủy trừ tà khi gửi từ 500 triệu VNĐ trở lên.
        """)

else:
    st.info("👈 Vui lòng nhập thông tin khoản tiết kiệm ở cột bên trái và bấm nút **'Tính toán tài chính âm phủ'** để hệ thống tự động xuất toàn bộ thông tin chi tiết.")
