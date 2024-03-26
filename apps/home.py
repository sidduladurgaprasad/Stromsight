import streamlit as st

def app():
    # Title card
    # st.markdown(
    #     """
    #     <div class="title-card">
    #         <div class="header">Welcome to Stromsight: Revolutionizing Cyclone Intensity Estimation</div>
    #     </div>
    #     """, unsafe_allow_html=True
    # )

    # CSS styling for the sections
    st.markdown(
        """
        <style>
            .title-card {
                background-color: rgba(255, 255, 255, 0.8);
                padding: 20px;
                margin: 20px 0; /* Add margin */
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .card {
                background-color: #f9f9f9;
                padding: 20px;
                margin: 20px 0; /* Add margin */
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            }
            .header {
                color: #007bff;
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .content {
                color: #333;
                font-size: 16px;
            }
            .content img {
                width: 100%;
                border-radius: 10px;
                margin-top: 10px;
                transition: all 0.3s ease;
            }
            .content img:hover {
                transform: scale(1.1);
            }
        </style>
        """, unsafe_allow_html=True
    )

    # Overview
    st.markdown(
        """
        <div class="card">
            <div class="header">Discover Stromsight</div>
            <div class="content">Welcome to Stromsight, where we are revolutionizing cyclone intensity estimation using INSAT 3D IR imagery. Our advanced feature includes estimating the direction of the cyclone, providing comprehensive insights for better disaster preparedness and response.</div>
            <img src="https://th.bing.com/th/id/OIG4.0dCyEGRjc26dbOXboIMR?w=1024&h=1024&rs=1&pid=ImgDetMain" alt="Stromsight Image" width="100%" />
        </div>
        """, unsafe_allow_html=True
    )

    # Importance
    st.markdown(
        """
        <div class="card">
            <div class="header">Why Stromsight Matters</div>
            <div class="content">Stromsight is crucial for accurate cyclone intensity estimation, enabling authorities and communities to prepare and respond effectively to cyclonic events. By leveraging INSAT 3D IR imagery and advanced algorithms, Stromsight provides real-time insights into cyclone intensity and direction.</div>
            <img src="https://th.bing.com/th/id/OIG1.rx7Ve5nArfMaZzVnTQBL?w=1024&h=1024&rs=1&pid=ImgDetMain" alt="Stromsight Image"  width="100%" />
        </div>
        """, unsafe_allow_html=True
    )

    # Methodology
    st.markdown(
        """
        <div class="card">
            <div class="header">How Stromsight Works</div>
            <div class="content">Stromsight utilizes state-of-the-art deep learning techniques to analyze INSAT 3D IR imagery and extract key features for cyclone intensity estimation. Additionally, our advanced feature involves predicting the direction of the cyclone based on image analysis and historical data.</div>
            <img src="https://th.bing.com/th/id/OIG3.4iRh8DolrNLcMnuOWXBq?w=1024&h=1024&rs=1&pid=ImgDetMain" alt="Stromsight Image"  width="100%" />
        </div>
        """, unsafe_allow_html=True
    )

    # Data
    st.markdown(
        """
        <div class="card">
            <div class="header">Powered by INSAT 3D IR Images</div>
            <div class="content">Stromsight harnesses the power of INSAT 3D IR images, which provide high-resolution data essential for accurate cyclone intensity estimation. By processing this imagery with advanced algorithms, Stromsight delivers real-time insights into cyclone intensity and direction.</div>
            <img src="https://th.bing.com/th/id/OIG1.EVMAghxkDsVNefRt0AHZ?w=1024&h=1024&rs=1&pid=ImgDetMain" alt="Stromsight Image"  width="100%" />
        </div>
        """, unsafe_allow_html=True
    )

    # Results
    st.markdown(
        """
        <div class="card">
            <div class="header">The Stromsight Advantage</div>
            <div class="content">With Stromsight, users gain access to accurate cyclone intensity estimates and directional predictions, empowering them to make informed decisions and take proactive measures to mitigate the impact of cyclones. Join us in revolutionizing cyclone intensity estimation with Stromsight!</div>
            <img src="https://th.bing.com/th/id/OIG2.fZg9YiAPT.ORz4EUeuWk?pid=ImgGn" alt="Stromsight Image"  width="100%" />
        </div>
        """, unsafe_allow_html=True
    )

    # Conclusion
    st.markdown(
        """
        <div class="card">
            <div class="header">Join the Stromsight Movement</div>
            <div class="content">Together, we can make a difference in cyclone intensity estimation and disaster preparedness. Join the Stromsight movement today and be part of a global effort to build a safer, more resilient world.</div>
            <img src="https://th.bing.com/th/id/OIG1.AGIiLgk5h7yFvUQ.irsx?pid=ImgGn" alt="Stromsight Image"  width="100%" />
        </div>
        """, unsafe_allow_html=True
    )


if __name__ == "__main__":
    app()
