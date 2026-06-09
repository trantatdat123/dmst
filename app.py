import streamlit as st
import pandas as pd
import os
import datetime
import requests

# --- HÀM LƯU DỮ LIỆU THẲNG VÀO GOOGLE SHEETS ---
def save_lead(email, intent_type):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. URL Form đích (Đã tự động chuyển viewform thành formResponse)
    url = "https://docs.google.com/forms/d/e/1FAIpQLSc8OUEVwzrGHgKNnml0Wn2i7IpUBEhdufm5LGN4HdsD1YY-IQ/formResponse"
    
    # 2. Dữ liệu map chính xác với Form của bạn
    form_data = {
        "entry.730150072": now,          # ID Câu 1: Thời gian
        "entry.2140267885": email,       # ID Câu 2: Email
        "entry.528554394": intent_type   # ID Câu 3: Hành động
    }
    
    # Bắn dữ liệu lên Google Sheets
    try:
        requests.post(url, data=form_data)
    except:
        pass # Nếu mạng lỗi thì bỏ qua để không làm sập giao diện web
# Cấu hình trang
st.set_page_config(page_title="Student Cloud GPU", page_icon="☁️", layout="wide")

# --- QUẢN LÝ TRẠNG THÁI (STATE) ---
if 'page' not in st.session_state:
    st.session_state.page = "Tổng quan"
if 'selected_gpu' not in st.session_state:
    st.session_state.selected_gpu = None

# --- SIDEBAR (MENU ĐIỀU HƯỚNG) ---
with st.sidebar:
    st.title("☁️ SCG Platform")
    st.markdown("---")
    
    # Nút điều hướng
    if st.button("📊 Tổng quan", use_container_width=True): 
        st.session_state.page = "Tổng quan"
    
    if st.button("🚀 Thuê GPU Mới", type="primary", use_container_width=True): 
        st.session_state.page = "Thuê GPU"
        st.session_state.selected_gpu = None # Reset thông báo khi chuyển trang
        
    if st.button("💻 Máy ảo đang chạy", use_container_width=True): 
        st.session_state.page = "Máy ảo"
        
    if st.button("💳 Nạp tiền & Lịch sử", use_container_width=True): 
        st.session_state.page = "Thanh toán"
        
    if st.button("🎧 Hỗ trợ kỹ thuật", use_container_width=True): 
        st.session_state.page = "Hỗ trợ"
    
    st.markdown("---")
    st.markdown("👤 **Tài khoản:** Khách (Chưa định danh)")
    st.markdown("🎓 **Hạng:** Mặc định")
    st.markdown("💰 **Số dư:** 0 VNĐ")

# ==========================================
# NỘI DUNG CÁC TRANG
# ==========================================
page = st.session_state.page

# ----------------- TRANG TỔNG QUAN -----------------
# ----------------- TRANG TỔNG QUAN -----------------
if page == "Tổng quan":
    st.header("📊 Dashboard Tổng quan")
    
    # --- PHẦN GIỚI THIỆU CHUNG (MỚI THÊM) ---
    st.markdown("""
    ### 🎓 Về Student Cloud GPU (SCG)
    **Student Cloud GPU** là nền tảng cung cấp máy chủ ảo (Cloud VPS) tích hợp Card đồ họa hiệu năng cao, được thiết kế và tối ưu hóa chi phí đặc biệt dành riêng cho sinh viên IT, AI và Data Science.
    
    **Tại sao bạn nên chọn SCG?**
    * ⚡ **Nhanh chóng & Mạnh mẽ:** Không còn cảnh chờ đợi mòn mỏi hay lỗi OOM (Out of Memory) khi train các model nặng như CNN, YOLO hay GANs.
    * 💰 **Tối ưu chi phí (Pay-as-you-go):** Thanh toán linh hoạt theo từng phút sử dụng, chỉ từ **4.500đ/giờ**. Phù hợp với túi tiền sinh viên, không bắt buộc mua gói tháng đắt đỏ.
    * 🛠️ **Môi trường "Mì ăn liền":** Khởi tạo máy ảo có ngay `Python 3.10`, `PyTorch`, `TensorFlow`, `CUDA` và `Jupyter Notebook`. Vào là code được ngay!
    """)
    
    st.divider()
    
    st.info("💡 Trạng thái tài khoản của bạn:")
    
    # --- PHẦN METRICS & LỊCH SỬ ---
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Số dư hiện tại", value="0 đ", delta="Cần nạp tiền", delta_color="off")
    col2.metric(label="Máy ảo đang chạy", value="0", delta="Chưa khởi tạo", delta_color="off")
    col3.metric(label="Tổng giờ đã train", value="0 Giờ")
    
    st.divider()
    st.subheader("⏱️ Hoạt động gần đây")
    st.caption("Chưa có lịch sử hoạt động nào. Hãy sang mục **Thuê GPU** để bắt đầu!")

# ----------------- TRANG THUÊ GPU (FAKE DOOR CHÍNH) -----------------
elif page == "Thuê GPU":
    st.header("🚀 Khởi tạo Môi trường GPU")
    st.info("💡 Hệ thống cấu hình sẵn Python 3.10, PyTorch, TensorFlow, CUDA 11.8 và Jupyter Notebook.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.subheader("🟢 Gói Basic (T4)")
            st.text("Phù hợp: Chạy code test, Data Analysis")
            st.progress(80, text="Tình trạng Server: Còn trống nhiều")
            st.markdown("- **1x Nvidia T4 (16GB)**\n- 32 GB RAM | 8 vCPUs\n- 100 GB NVMe")
            st.markdown("### 4.500 đ / giờ")
            if st.button("Thuê máy này (T4)", key="t4", use_container_width=True):
                st.session_state.selected_gpu = "Gói T4"

    with col2:
        with st.container(border=True):
            st.subheader("🟡 Gói Đồ án (3090)")
            st.text("Phù hợp: Train CNN, YOLO, GANs")
            st.progress(95, text="Tình trạng Server: Gần đầy")
            st.markdown("- **1x RTX 3090 (24GB)**\n- 64 GB RAM | 16 vCPUs\n- 200 GB NVMe")
            st.markdown("### 9.500 đ / giờ")
            if st.button("Thuê máy này (3090)", type="primary", key="3090", use_container_width=True):
                st.session_state.selected_gpu = "Gói RTX 3090"

    with col3:
        with st.container(border=True):
            st.subheader("🔴 Gói Master (4090)")
            st.text("Phù hợp: Train LLM, AI tạo sinh")
            st.progress(10, text="Tình trạng Server: Còn trống")
            st.markdown("- **1x RTX 4090 (24GB)**\n- 128 GB RAM | 32 vCPUs\n- 500 GB NVMe")
            st.markdown("### 18.000 đ / giờ")
            if st.button("Thuê máy này (4090)", key="4090", use_container_width=True):
                st.session_state.selected_gpu = "Gói RTX 4090"

    # XỬ LÝ FAKE DOOR
    if st.session_state.selected_gpu:
        st.markdown("---")
        st.warning(f"⚠️ **Thông báo từ hệ thống:** Bạn đã yêu cầu khởi tạo **{st.session_state.selected_gpu}**.")
        st.error("Rất tiếc! Số lượng sinh viên truy cập đợt này quá lớn, Data Center hiện tại của chúng mình đang tạm hết tài nguyên trống cho gói này.")
        
        st.markdown("### 🎁 Nhận 50.000đ dùng thử đợt mở rộng ngày mai!")
        st.markdown("Hệ thống sẽ cắm thêm Card vào sáng mai. Hãy để lại **Email (ưu tiên đuôi .edu.vn)** hoặc **MSSV**, chúng mình sẽ giữ chỗ và tự động cộng **50.000 VNĐ** vào tài khoản của bạn ngay khi máy chủ trực tuyến trở lại.")
        
        with st.form("lead_form"):
            email_input = st.text_input("Nhập Email hoặc MSSV của bạn:")
            submit = st.form_submit_button("Nhận 50.000đ & Giữ chỗ", type="primary")
            
            if submit:
                if email_input.strip() == "":
                    st.error("Vui lòng nhập Email hoặc MSSV!")
                else:
                    save_lead(email_input, st.session_state.selected_gpu)
                    st.success("✅ Tuyệt vời! Thông tin đã được ghi nhận. Vui lòng kiểm tra email vào sáng ngày mai nhé!")
                    st.balloons()

# ----------------- TRANG MÁY ẢO -----------------
elif page == "Máy ảo":
    st.header("💻 Quản lý máy ảo đang chạy")
    st.info("Hiện tại bạn chưa khởi tạo máy ảo nào. Hãy sang mục **Thuê GPU** để bắt đầu.")

# ----------------- TRANG THANH TOÁN (FAKE DOOR PHỤ) -----------------
elif page == "Thanh toán":
    st.header("💳 Nạp tiền vào hệ thống")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_mobile_English_Wikipedia.svg", caption="Quét mã QR bằng Momo/ZaloPay")
    with col2:
        st.selectbox("Chọn phương thức", ["Momo", "ZaloPay", "Thẻ nội địa / VietQR"])
        st.number_input("Số tiền muốn nạp (VNĐ)", min_value=10000, step=10000, value=50000)
        
        # Fake door cho những ai thực sự có ý định trả tiền
        if st.button("Xác nhận nạp tiền", type="primary"):
            st.error("Cổng thanh toán tự động đang nâng cấp định kỳ.")
            st.info("Để nạp tiền thủ công, vui lòng để lại Email/Số điện thoại, nhân viên CSKH sẽ liên hệ hỗ trợ bạn nạp tiền ngay lập tức!")
            with st.form("payment_form"):
                pay_email = st.text_input("Email/SĐT của bạn:")
                if st.form_submit_button("Yêu cầu hỗ trợ nạp tiền"):
                    if pay_email:
                        save_lead(pay_email, "Yêu cầu Nạp tiền")
                        st.success("Đã ghi nhận! CSKH sẽ liên hệ với bạn trong 5 phút nữa.")

# ----------------- TRANG HỖ TRỢ -----------------
elif page == "Hỗ trợ":
    st.header("🎧 Hỗ trợ kỹ thuật")
    st.text_input("Tiêu đề (Ví dụ: Không cài được thư viện, Cần xuất hóa đơn...)")
    st.text_area("Mô tả chi tiết")
    if st.button("Gửi ticket hỗ trợ"):
        st.success("Đã gửi yêu cầu hỗ trợ thành công!")
