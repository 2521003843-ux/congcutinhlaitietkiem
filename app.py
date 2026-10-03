import streamlit as st
import pandas as pd
import numpy as np
st.image("logo.jpg")
# Cấu hình trang Streamlit
st.set_page_config(
    page_title="Ngân hàng Địa Phủ - Gửi Lãi Âm Phủ",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh giao diện chủ đề Ngân hàng Địa Phủ (Đỏ máu, Đen huyền bí, Vàng kim)
st.markdown("""
    <style>
    .main {
        background-color: #0b0b0f;
        color: #e5e5e5;
    }
    .stSidebar {
        background-color: #12121a;
        border-right: 1px solid #331111;
    }
    h1, h2, h3 {
        color: #ff3333 !important;
        font-family: 'Cinzel', serif, sans-serif;
        text-shadow: 0px 0px 10px rgba(255, 51, 51, 0.4);
    }
    .metric-card {
        background: linear-gradient(135deg, #1a0f0f 0%, #2b1111 100%);
        border: 1px solid #ff4d4d;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(255, 0, 0, 0.2);
        text-align: center;
        margin-bottom: 15px;
    }
    .metric-value {
        font-size: 26px;
        font-weight: bold;
        color: #ffcc00;
    }
    .metric-label {
        font-size: 14px;
        color: #b3b3b3;
        margin-top: 5px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #cc0000 0%, #ff3333 100%);
        color: white;
        font-weight: bold;
        border: 1px solid #ff9999;
        border-radius: 8px;
        padding: 10px 24px;
        box-shadow: 0 0 10px rgba(255, 0, 0, 0.5);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #ff3333 0%, #ff6666 100%);
        border-color: #ffffff;
    }
    .warning-box {
        background-color: #261111;
        border-left: 5px solid #ff3333;
        padding: 15px;
        border-radius: 4px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Tiêu đề ứng dụng
st.title("🔥 NGÂN HÀNG ĐỊA PHỦ - HỆ THỐNG GỬI TIẾT KIỆM ÂM PHỦ 🔥")
st.markdown("*(Cam kết sinh lời cực đại, rút gốc ở trần gian, nhận lãi ở... âm phủ!)*")

# Sidebar nhập liệu
st.sidebar.header("📜 HỒ SƠ GỬI TIỀN VÀNG MÃ")

with st.sidebar.form("saving_form"):
    # 1. Số tiền gửi (có thể quy đổi ra VNĐ hoặc Vàng Âm Phủ)
    deposit_type = st.radio("Loại tiền tệ gửi:", ["VNĐ Trần Gian (Tỷ VNĐ)", "Vàng Mã / Đô La Âm Phủ"])
    
    if deposit_type == "VNĐ Trần Gian (Tỷ VNĐ)":
        principal = st.number_input("Số tiền gửi (VNĐ):", min_value=1_000_000, max_value=1_000_000_000_000, value=100_000_000, step=10_000_000, format="%d")
        unit_str = "VNĐ"
    else:
        principal = st.number_input("Số tờ Vàng Mã / Đô La Âm Phủ:", min_value=1_000, max_value=10_000_000_000, value=50_000, step=1000, format="%d")
        unit_str = "Tờ/Đồng"

    # 2. Kỳ hạn
    term_months = st.slider("Kỳ hạn gửi (Tháng):", min_value=1, max_value=120, value=12)
    
    # 3. Lãi suất
    annual_rate = st.number_input("Lãi suất năm (%/năm):", min_value=0.1, max_value=99.9, value=8.5, step=0.1)

    # 4. Hình thức tính lãi
    calc_method = st.selectbox("Phương pháp tính lãi:", ["Lãi Đơn (Simple Interest)", "Lãi Kép (Compound Interest)"])

    # 5. Hình thức lãnh lãi
    payout_freq = st.selectbox("Hình thức lãnh lãi:", [
        "Lãnh lãi cuối kỳ", 
        "Lãnh lãi theo tháng", 
        "Lãnh lãi theo quý"
    ])

    submitted = st.form_submit_button("🔮 TIẾN HÀNH KHẤN VÁI & TÍNH LÃI")

# Xử lý logic tính toán khi submit
if submitted:
    # Chuyển đổi lãi suất sang tháng
    monthly_rate = (annual_rate / 100) / 12
    total_months = term_months
    
    periodic_interest = 0
    total_interest = 0
    total_amount = 0
    
    # --- LOGIC TÍNH TOÁN ---
    if "Lãi Đơn" in calc_method:
        # Lãi đơn: Lãi không nhập gốc
        total_interest = principal * (annual_rate / 100) * (total_months / 12)
        total_amount = principal + total_interest
        
        if payout_freq == "Lãnh lãi theo tháng":
            periodic_interest = total_interest / total_months
        elif payout_freq == "Lãnh lãi theo quý":
            periodic_interest = (total_interest / total_months) * 3
        else: # Cuối kỳ
            periodic_interest = total_interest # Nhận 1 lần cuối kỳ
            
    else:
        # Lãi kép: Gốc + Lãi nhập chung
        if payout_freq == "Lãnh lãi cuối kỳ":
            # Kép hàng tháng (mặc định cho cuối kỳ nếu không nói rõ)
            total_amount = principal * ((1 + monthly_rate) ** total_months)
            total_interest = total_amount - principal
            periodic_interest = 0 # cuối kỳ nhận trọn cục
        elif payout_freq == "Lãnh lãi theo tháng":
            # Lãi kép hàng tháng, nhưng định kỳ rút ra tiêu pha ở âm phủ hàng tháng
            periodic_interest = principal * monthly_rate
            total_interest = periodic_interest * total_months
            total_amount = principal + total_interest # thực chất tiền gốc không đổi vì đã rút lãi hàng tháng
        elif payout_freq == "Lãnh lãi theo quý":
            quarterly_rate = monthly_rate * 3
            periodic_interest = principal * quarterly_rate
            num_quarters = total_months / 3
            total_interest = periodic_interest * num_quarters
            total_amount = principal

    # --- HIỂN THỊ KẾT QUẢ ---
    st.markdown("---")
    st.subheader("📊 KẾT QUẢ PHÂN TÍCH TÀI CHÍNH ÂM PHỦ")

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
                <div class="metric-value" style="color: #ff4d4d;">{total_interest:,.0f} {unit_str}</div>
                <div class="metric-label">Tổng Tiền Lãi Nhận Được</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value" style="color: #00ffcc;">{total_amount:,.0f} {unit_str}</div>
                <div class="metric-label">Tổng Gốc + Lãi Khi Đáo Hạn</div>
            </div>
        """, unsafe_allow_html=True)

    # --- TÍNH NĂNG BỔ SUNG: BIỂU ĐỒ & BẢNG DÒNG TIỀN ---
    st.markdown("### 📈 Biểu đồ tăng trưởng tài sản âm phủ qua các tháng")
    
    # Tạo dữ liệu bảng dòng tiền theo tháng
    chart_data = []
    current_val = principal
    accumulated_interest = 0
    
    for m in range(1, total_months + 1):
        if "Lãi Kép" in calc_method and payout_freq == "Lãnh lãi cuối kỳ":
            current_val = principal * ((1 + monthly_rate) ** m)
            acc_int = current_val - principal
        else:
            if "Lãi Kép" in calc_method and payout_freq == "Lãnh lãi theo tháng":
                # Ví dụ đơn giản cho biểu đồ tăng trưởng tổng tài sản tích lũy
                acc_int = principal * monthly_rate * m
                current_val = principal + acc_int
            else:
                acc_int = principal * (annual_rate / 100) * (m / 12)
                current_val = principal + acc_int
                
        chart_data.append({"Tháng": f"Tháng {m}", "Tổng Giá Trị (Gốc + Lãi)": current_val})
        
    df_chart = pd.DataFrame(chart_data).set_index("Tháng")
    st.line_chart(df_chart, color="#ff3333")

    # --- CÁC TÍNH NĂNG SÁNG TẠO ĐỘC QUYỀN CHỦ ĐỀ NGÂN HÀNG ĐỊA PHỦ ---
    st.markdown("---")
    st.subheader("🔱 TIỆN ÍCH ĐỘC QUYỀN ĐỊA PHỦ")

    tab1, tab2, tab3 = st.tabs(["🕯️ Bói Vận Mệnh Đầu Tư", "🛡️ Bảo Hiểm Đầu Thai", "👑 Đặc Quyền Diêm Vương"])

    with tab1:
        st.markdown("#### Xin xăm tài lộc âm phủ:")
        if st.button("Lắc ống xăm tài chính"):
            fortunes = [
                "Quẻ THƯỢNG THƯỢng: Đầu tư vàng mã kỳ này, âm ti kết thực, đời sau làm đại gia bên kia thế giới!",
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
    st.info("👈 Vui lòng nhập đầy đủ thông số tài khoản tiết kiệm ở cột bên trái và bấm nút **'Tiến hành khấn vái & tính lãi'** để xem kết quả.")
