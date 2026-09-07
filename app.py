
import streamlit as st

from database import violation_fine, user_data
from violation_detection import detect_violation
from number_plate_recognition import num_plt
from chalan_generation import chalan_gen


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="TrafficGuard | Challan Automation",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 5px;
}

.subtitle {
    color: #94a3b8;
    font-size: 17px;
    margin-bottom: 30px;
}

.card {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 15px;
}

.section-title {
    color: #f8fafc;
    font-size: 23px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

.pipeline {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    color: #cbd5e1;
    font-weight: 600;
}

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid #1e293b;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🚦 TrafficGuard")

    st.caption("Automated Traffic Challan System")

    st.markdown("---")

    page = st.radio(
        "MENU",
        [
            "🏠 Dashboard",
            "📷 Detect Violation",
            "📋 Challan Details"
        ]
    )

    st.markdown("---")

    st.markdown("### SYSTEM")

    st.success("🟢 System Online")

    st.markdown("")

    st.caption("Computer Vision")
    st.caption("OCR Recognition")
    st.caption("SQLite Database")


# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="main-title">🚦 TrafficGuard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'AI-powered traffic violation detection & challan automation'
        '</div>',
        unsafe_allow_html=True
    )

    # KPI CARDS

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🔍 Detection",
            "AI Powered"
        )

    with col2:
        st.metric(
            "🚗 OCR",
            "PP-OCR"
        )

    with col3:
        st.metric(
            "🗄️ Database",
            "SQLite"
        )

    with col4:
        st.metric(
            "🟢 Status",
            "Online"
        )

    st.markdown(
        '<div class="section-title">⚡ Automated Pipeline</div>',
        unsafe_allow_html=True
    )

    p1, p2, p3, p4, p5 = st.columns(5)

    with p1:
        st.markdown(
            '<div class="pipeline">📷<br>Image</div>',
            unsafe_allow_html=True
        )

    with p2:
        st.markdown(
            '<div class="pipeline">🔍<br>Violation</div>',
            unsafe_allow_html=True
        )

    with p3:
        st.markdown(
            '<div class="pipeline">🚗<br>OCR</div>',
            unsafe_allow_html=True
        )

    with p4:
        st.markdown(
            '<div class="pipeline">🗄️<br>Database</div>',
            unsafe_allow_html=True
        )

    with p5:
        st.markdown(
            '<div class="pipeline">📄<br>Challan</div>',
            unsafe_allow_html=True
        )

    st.markdown("")

    st.info(
        "Upload a traffic image from **📷 Detect Violation** "
        "to start the automated pipeline."
    )


# =========================================================
# DETECTION PAGE
# =========================================================

elif page == "📷 Detect Violation":

    st.markdown(
        '<div class="main-title">📷 Violation Detection</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Upload an image to detect traffic violations and identify the vehicle.'
        '</div>',
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Choose traffic image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        col1, col2 = st.columns([1.4, 1])

        # -------------------------------------------------
        # IMAGE
        # -------------------------------------------------

        with col1:

            st.subheader("🖼️ Vehicle Image")

            st.image(
                uploaded_file,
                use_container_width=True
            )

        # -------------------------------------------------
        # ANALYSIS
        # -------------------------------------------------

        with col2:

            st.subheader("⚙️ Analysis")

            st.write(
                "Run the complete AI pipeline on this image."
            )

            detect_button = st.button(
                "🚀 Analyze Image",
                use_container_width=True
            )

            if detect_button:

                with st.spinner(
                    "Running violation detection, OCR and database lookup..."
                ):

                    # Your existing working pipeline

                    violation = detect_violation(
                        "no_parking1.jpg"
                    )

                    vehicle_num = num_plt()

                    chalan = violation_fine(
                        violation
                    )

                    info = user_data(
                        vehicle_num
                    )

                    notice = chalan_gen(
                        violation,
                        info,
                        chalan
                    )

                    # Save results

                    st.session_state["violation"] = violation
                    st.session_state["vehicle_num"] = vehicle_num
                    st.session_state["chalan"] = chalan
                    st.session_state["info"] = info
                    st.session_state["notice"] = notice

                st.success(
                    "✅ Analysis completed successfully!"
                )

    # =====================================================
    # RESULTS
    # =====================================================

    if "violation" in st.session_state:

        st.markdown("---")

        st.subheader("📊 Detection Results")

        violation = st.session_state["violation"]
        vehicle_num = st.session_state["vehicle_num"]
        chalan = st.session_state["chalan"]
        info = st.session_state["info"]

        # If database returns (600,)
        if isinstance(chalan, tuple):
            chalan_display = chalan[0]
        else:
            chalan_display = chalan

        # -------------------------------------------------
        # MAIN RESULTS
        # -------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.error(
                f"⚠️ VIOLATION\n\n{violation.upper()}"
            )

        with col2:

            st.success(
                f"💰 FINE AMOUNT\n\n₹{chalan_display}"
            )

        with col3:

            st.info(
                f"🚗 VEHICLE NUMBER\n\n{vehicle_num}"
            )

        # -------------------------------------------------
        # OWNER DETAILS
        # -------------------------------------------------

        st.subheader("👤 Vehicle Owner")

        owner1, owner2, owner3, owner4 = st.columns(4)

        with owner1:

            st.metric(
                "Owner",
                info[0]
            )

        with owner2:

            st.metric(
                "Vehicle Type",
                info[1]
            )

        with owner3:

            st.metric(
                "Registration",
                info[2]
            )

        with owner4:

            st.metric(
                "Mobile",
                info[3]
            )


# =========================================================
# CHALLAN PAGE
# =========================================================

elif page == "📋 Challan Details":

    st.markdown(
        '<div class="main-title">📋 Challan Details</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Generated violation and notification details'
        '</div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # CHECK IF CHALLAN EXISTS
    # -----------------------------------------------------

    if "notice" not in st.session_state:

        st.warning(
            "⚠️ No challan has been generated yet."
        )

        st.info(
            "Go to **📷 Detect Violation** and analyze an image first."
        )

    else:

        info = st.session_state["info"]
        notice = st.session_state["notice"]

        col1, col2 = st.columns([1, 1])

        # =================================================
        # CHALLAN
        # =================================================

        with col1:

            st.subheader("📄 Generated Challan")

            st.text_area(
                "Challan",
                value=notice,
                height=260,
                label_visibility="collapsed"
            )

            st.download_button(
                "⬇️ Download Challan",
                data=notice,
                file_name="traffic_challan.txt",
                mime="text/plain",
                use_container_width=True
            )

        # =================================================
        # NOTIFICATION
        # =================================================

        with col2:

            st.subheader("📱 WhatsApp Notification")

            st.markdown(
                "### 🚨 Traffic Violation Notice"
            )

            st.caption(
                "Official notification generated by TrafficGuard"
            )

            st.info(
                f"📱 **Recipient:** +91 {info[3]}"
            )

            st.text_area(
                "WhatsApp Message",
                value=notice,
                height=180,
                label_visibility="collapsed"
            )

            st.success(
                "🟢 Notification Ready"
            )

            st.button(
                "📤 Send WhatsApp Notification",
                use_container_width=True
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        🚦 TrafficGuard • Traffic Challan Automation System
        <br>
        Computer Vision • OCR • SQLite • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)


