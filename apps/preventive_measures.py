# import streamlit as st

# def app():

#     session_state = st.session_state
#     if 'shared_variable' not in session_state:
#         session_state.shared_variable = 0
#     predicted_intensity = session_state.shared_variable
#     print(predicted_intensity)

#     # Set background color
#     st.markdown(
#         """
#         <style>
#         body {
#             background-color: white;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     # Overview of Cyclones
#     st.markdown(
#         """
#         <div class="card">
#             <div class="header">Overview of Cyclones</div>
#             <div class="content">Cyclones are large-scale weather systems that rotate counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere. They typically form in tropical or subtropical regions and are fueled by warm ocean waters. Cyclones can vary in size and intensity, ranging from tropical depressions with sustained winds of less than 39 mph (63 km/h) to Category 5 hurricanes with winds exceeding 157 mph (252 km/h).</div>
#             <img src="https://th.bing.com/th/id/OIG1.D2uqRy3mswVvjSmyAbZC?pid=ImgGn" alt="Cyclone Image" width="100%" />
#         </div>
#         """, unsafe_allow_html=True
#     )

#     # Preventive Measures
#     st.markdown(
#         """
#         <div class="card">
#             <div class="header">Preventive Measures</div>
#         """, unsafe_allow_html=True
#     )
    
#     if predicted_intensity < 40:
#         preventive_measures = [
#             ("Stay Informed", 
#             "Keep track of weather forecasts and advisories issued by local authorities. Stay tuned to radio, television, or official social media channels for updates.",
#             "https://th.bing.com/th/id/OIG3.VHnKiGSRxSqvg0WvUMf_?pid=ImgGn"),
#             ("Prepare an Emergency Kit", 
#             "Assemble an emergency kit containing essential items such as non-perishable food, water, medications, flashlights, batteries, and important documents. Ensure that your emergency kit is easily accessible and kept in a designated location.",
#             "https://th.bing.com/th/id/OIG2.9vbP7H0cT4bj3iqXrKEg?pid=ImgGn"),
#         ]
#     elif predicted_intensity < 45:
#         preventive_measures = [
#             ("Secure Property", 
#             "Secure your property by reinforcing windows and doors, trimming trees and bushes, and securing outdoor furniture to prevent damage from strong winds. Consider installing storm shutters or impact-resistant windows for added protection.",
#             "https://th.bing.com/th/id/OIG4.TYikXXa25DNfpZ9fqMFT?pid=ImgGn"),
#             ("Evacuate if Necessary", 
#             "Follow evacuation orders issued by authorities. Have a designated evacuation route and plan in place, and evacuate to a safe location well in advance of the storm. Take your emergency kit with you and ensure that your pets are also safely evacuated.",
#             "https://th.bing.com/th/id/OIG3.hjuHr1SwZiqhf.cgk1W0?w=1024&h=1024&rs=1&pid=ImgDetMain"),
#         ]
#     else :
#         preventive_measures = [
#             ("Stay Indoors During the Storm", 
#             "Seek shelter indoors and stay away from windows, doors, and exterior walls. Avoid using candles and open flames, and use battery-powered devices for lighting and communication. Listen to local news updates and follow instructions from emergency officials.",
#             "https://th.bing.com/th/id/OIG1.coT8FbAQHlJ0UqGroMRc?w=1024&h=1024&rs=1&pid=ImgDetMain"),
#             ("After the Storm", 
#             "Wait for authorities to declare it safe before returning home. Be cautious of downed power lines, flooding, and debris, and avoid walking or driving through floodwaters. Check your property for any damage and contact your insurance company if necessary.",
#             "https://th.bing.com/th/id/OIG2.ZW3gy7bweKOerkraQS7e?pid=ImgGn")
#         ]
    
#     for measure, description, image_url in preventive_measures:
#         st.markdown(
#             f"""
#             <div class="card">
#                 <div class="content">
#                     <div class="text">
#                         <h3>{measure}</h3>
#                         <p>{description}</p>
#                     </div>
#                     <div class="image">
#                         <img src="{image_url}" alt="{measure}" width="80%" />
#                     </div>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True
#         )

#     st.markdown("</div>", unsafe_allow_html=True)

#     # CSS styling for header
#     st.markdown(
#         """
#         <style>
#         .card {
#             background-color: #ffffff;
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             margin-bottom: 20px;
#         }
#         .header {
#             color: #007bff;
#             font-size: 24px;
#             font-weight: bold;
#             margin-bottom: 10px;
#         }
#         .content {
#             display: flex;
#             align-items: center;
#         }
#         .text {
#             flex: 1;
#             padding-right: 20px;
#         }
#         .text h3 {
#             margin-bottom: 10px;
#         }
#         .text p {
#             font-size: 16px;
#             margin-bottom: 10px;
#         }
#         .image {
#             flex: 1;
#             text-align: right;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# if __name__ == "__main__":
#     app()


import streamlit as st

def app():

    session_state = st.session_state
    if 'shared_variable' not in session_state:
        session_state.shared_variable = 0
    predicted_intensity = session_state.shared_variable
    print(predicted_intensity)

    # Set background color
    st.markdown(
        """
        <style>
        body {
            background-color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Overview of Cyclones
    st.markdown(
        """
        <div class="card">
            <div class="header">Overview of Cyclones</div>
            <div class="content">Cyclones are large-scale weather systems that rotate counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere. They typically form in tropical or subtropical regions and are fueled by warm ocean waters. Cyclones can vary in size and intensity, ranging from tropical depressions with sustained winds of less than 39 mph (63 km/h) to Category 5 hurricanes with winds exceeding 157 mph (252 km/h).</div>
            <img src="https://th.bing.com/th/id/OIG1.D2uqRy3mswVvjSmyAbZC?pid=ImgGn" alt="Cyclone Image" width="100%" />
        </div>
        """, unsafe_allow_html=True
    )

    # Preventive Measures
    st.markdown(
        """
        <div class="card">
            <div class="header">Preventive Measures</div>
        """, unsafe_allow_html=True
    )
    
    if predicted_intensity < 40:
        preventive_measures = [
            (
                "Cyclone Type: Tropical Depression to Tropical Storm",
                "Typically, the area radius affected by a cyclone of this intensity range is around 100-200 kilometers from the center of the storm. However, cyclones can be unpredictable, and their size and impact zone may vary. It's essential to stay updated on weather advisories and warnings issued by meteorological agencies.",
                "Depending on the speed and trajectory of the cyclone, people should leave the area at least 12-24 hours before the cyclone is expected to make landfall. Evacuating early ensures safety and reduces the risk of being caught in dangerous conditions.",
                "Secure Loose Objects: Bring inside or secure any loose objects in your yard or on your property, such as patio furniture, garden tools, and toys, to prevent them from becoming projectiles in high winds. Reinforce Doors and Windows: Install storm shutters or board up windows to protect against flying debris. Strengthen garage doors to prevent them from buckling under wind pressure. Stock Up on Essentials: Ensure you have a sufficient supply of food, water, medications, and other essential supplies to last for several days in case of power outages or restricted access to stores. Stay Informed: Monitor local weather advisories and forecasts for updates on the cyclone's intensity and trajectory. Have a battery-powered radio or NOAA weather radio for emergency alerts."
            ),
        ]
    elif predicted_intensity < 45:
        preventive_measures = [
            (
                "Cyclone Type: Severe Tropical Storm",
                "The affected area can extend up to 300 kilometers or more from the center of the cyclone, encompassing coastal regions and inland areas. The intensity of winds and rainfall may vary within this radius, posing significant risks to life and property. Residents in low-lying areas or near water bodies should be especially vigilant.",
                "Residents should evacuate vulnerable areas at least 24-48 hours before the cyclone's anticipated landfall. Early evacuation allows time for safe travel and minimizes the risk of being caught in dangerous weather conditions. Plan your evacuation route in advance and inform family members and neighbors of your plans. Follow instructions from local authorities regarding evacuation routes and shelter locations.",
                "Secure Outdoor Furniture: Anchor or bring inside any outdoor furniture, grills, or decorations that could become airborne during high winds. Trim Trees and Bushes: Prune trees and bushes to remove weak or dead branches that could break off and cause damage during the storm. Reinforce Roofs and Structures: Inspect and repair roofs, windows, doors, and garage doors to ensure they can withstand high winds and flying debris. Plan Evacuation Routes: Identify multiple evacuation routes and establish a communication plan with family members and neighbors. Share your plans and evacuation routes with trusted contacts outside the affected area."
            ),
        ]
    else:
        preventive_measures = [
            (
                "Cyclone Type: Hurricane",
                "The impact zone can extend beyond 500 kilometers from the center of the cyclone, covering extensive coastal areas and inland regions. The destructive potential of hurricanes is immense, with strong winds, heavy rainfall, and storm surges posing severe threats to communities within the impact zone. Residents in evacuation zones must heed evacuation orders without delay.",
                "Residents should evacuate high-risk areas at least 48-72 hours before the expected landfall of the cyclone. Early evacuation is crucial to avoid being stranded or exposed to life-threatening conditions as the storm approaches. Follow evacuation orders issued by local authorities and seek shelter in designated evacuation centers or sturdy buildings. Plan your evacuation route in advance and inform family members and neighbors of your plans.",
                "Prepare an Emergency Kit: Assemble an emergency kit with essential supplies, including first aid items, flashlights, batteries, non-perishable food, water, medications, and important documents (such as identification, insurance policies, and medical records). Follow Evacuation Orders: Follow evacuation orders issued by local authorities without delay. Leaving high-risk areas ahead of the storm can prevent unnecessary risks to life and property. Seek Shelter in Sturdy Buildings: Identify designated evacuation centers or sturdy buildings where you can seek shelter during the storm. Avoid staying in mobile homes or structures that may not withstand hurricane-force winds. Stay Informed: Keep communication devices charged and stay informed through radio, TV, or official weather updates. Follow instructions from local authorities and emergency management agencies for the latest information and safety recommendations."
            ),
        ]

    for measure, area, evacuation, additional in preventive_measures:
        additional_list = "<ul>"
        additional_list += "".join([f"<li>{item}</li>" for item in additional.split(". ")])
        additional_list += "</ul>"

        st.markdown(
            f"""
            <div class="card">
                <div class="content">
                    <div class="text">
                        <h3>{measure}</h3>
                        <h5>Area Radius Affected:</h5>
                        <p>{area}</p>
                        <h5>Evacuation Time:</h5>
                        <p>{evacuation}</p>
                        <h5>Additional Considerations:</h5>
                        {additional_list}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # CSS styling for header
    st.markdown(
        """
        <style>
        .card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .header {
            color: #007bff;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .content {
            display: flex;
            align-items: center;
        }
        .text {
            flex: 1;
            padding-right: 20px;
        }
        .text h3 {
            margin-bottom: 10px;
        }
        .text p {
            font-size: 16px;
            margin-bottom: 10px;
        }
        .image {
            flex: 1;
            text-align: right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()
