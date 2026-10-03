import streamlit as st
st.image("logo.jpg")
# Cấu hình trang
st.set_page_config(page_title="Ngân hàng lãi tiết kiệm địa phủ", page_icon="💰", layout="centered")

def format_vnd(amount):
    """Hàm định dạng số tiền sang chuẩn VNĐ (VD: 1.000.000 VNĐ)"""
    return f"{amount:,.0f}".replace(",", ".") + " VNĐ"

st.title("Ngân hàng quỷ santan")
st.markdown("Nhập thông tin khoản gửi của bạn để tính toán chi tiết tiền lãi nhận được.")

# --- KHU VỰC NHẬP LIỆU ---
with st.container():
    st.subheader("📝 Thông tin gửi tiền")
    col1, col2 = st.columns(2)
    
    with col1:
        so_tien_gui = st.number_input("Số tiền gửi (VNĐ):", min_value=0.0, value=100000000.0, step=1000000.0, format="%f")
        ky_han = st.number_input("Kỳ hạn (Tháng):", min_value=1, value=12, step=1)
        
    with col2:
        lai_suat = st.number_input("Lãi suất (%/năm):", min_value=0.0, value=6.0, step=0.1)
        loai_lai = st.selectbox("Loại tính lãi:", ["Lãi đơn", "Lãi kép"])
        hinh_thuc = st.selectbox("Hình thức lãnh lãi:", ["Hàng tháng", "Hàng quý", "Cuối kỳ"])

# --- XỬ LÝ TÍNH TOÁN ---
r = lai_suat / 100  # Lãi suất theo số thập phân
t = ky_han / 12     # Kỳ hạn tính theo năm

lai_dinh_ky = 0
tong_lai = 0
tong_tien = 0

if loai_lai == "Lãi đơn":
    # Công thức lãi đơn: I = P * r * t
    tong_lai = so_tien_gui * r * t
    tong_tien = so_tien_gui + tong_lai
    
    if hinh_thuc == "Hàng tháng":
        lai_dinh_ky = so_tien_gui * (r / 12)
    elif hinh_thuc == "Hàng quý":
        lai_dinh_ky = so_tien_gui * (r / 4)
    else:
        lai_dinh_ky = 0

elif loai_lai == "Lãi kép":
    # Xác định số lần ghép lãi trong năm (n)
    if hinh_thuc == "Hàng tháng":
        n = 12
    elif hinh_thuc == "Hàng quý":
        n = 4
    else: 
        n = 1 # Cuối kỳ: giả sử ghép lãi định kỳ 1 năm 1 lần (hoặc tính gộp cho 1 chu kỳ)

    total_periods = n * t # Tổng số kỳ ghép lãi
    
    # Công thức lãi kép: A = P(1 + r/n)^(nt)
    tong_tien = so_tien_gui * ((1 + r / n) ** total_periods)
    tong_lai = tong_tien - so_tien_gui
    
    # Đối với lãi kép, tiền lãi tăng dần theo từng kỳ. 
    # Ở đây hiển thị tiền lãi của kỳ đầu tiên làm mốc tham khảo.
    if hinh_thuc == "Hàng tháng":
        lai_dinh_ky = so_tien_gui * (r / 12)
    elif hinh_thuc == "Hàng quý":
        lai_dinh_ky = so_tien_gui * (r / 4)
    else:
        lai_dinh_ky = 0

st.divider()

# --- KHU VỰC HIỂN THỊ KẾT QUẢ ---
st.subheader("📊 Kết quả tính toán")

# Dùng st.metric để hiển thị UI đẹp mắt hơn
col3, col4 = st.columns(2)
col3.metric(label="Tổng số tiền gốc và lãi", value=format_vnd(tong_tien))
col4.metric(label="Tổng tiền lãi nhận được", value=format_vnd(tong_lai))

if hinh_thuc != "Cuối kỳ":
    if loai_lai == "Lãi đơn":
        st.info(f"**Tiền lãi định kỳ ({hinh_thuc.lower()}):** {format_vnd(lai_dinh_ky)}")
    else:
        st.info(f"**Tiền lãi kỳ đầu tiên ({hinh_thuc.lower()}):** {format_vnd(lai_dinh_ky)}  \n*(Lưu ý: Do là lãi kép nên tiền lãi các kỳ sau sẽ tăng dần do lãi nhập gốc)*")
else:
    st.info("Nhận toàn bộ gốc và lãi một lần vào cuối kỳ hạn.")
