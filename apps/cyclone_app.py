import pickle
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

with open("Trained_model.sav", "rb") as a:
    loaded_model = pickle.load(a)

with open("Trained_direction_model.sav", "rb") as b:
    loaded_direction_model = pickle.load(b)

def app():

    session_state = st.session_state
    
    def load_and_prep_image(filename, img_shape=256):
        img = tf.io.read_file(filename)
        img = tf.image.decode_image(img, channels=3)
        img = tf.image.resize(img, size=[img_shape, img_shape])
        img = img / 255.
        return img
    
    def pred_and_plot_direction(model, filename):
        img = load_and_prep_image(filename)
        pred = model.predict(tf.expand_dims(img, axis=0))
        direction_index = tf.argmax(pred, axis=1).numpy()[0]
        directions = ["East", "West", "North", "South"]
        predicted_direction = directions[direction_index]
        return predicted_direction
    
    def pred_and_plot(model, filename):
        pred = model.predict(filename)
        return pred
    
    # Apply CSS styling for white background
    st.markdown(
        """
        <style>
        body {
            background-color: #ffffff;
        }
        .card {
                background-color: #f9f9f9;
                padding: 20px;
                margin: 20px 0; /* Add margin */
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Main content
    st.markdown('<div style="background-image: linear-gradient(to right, #4facfe 0%, #00f2fe 100%); padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><h1 style="font-family: sans-serif; color: white; font-size: 48px; text-shadow: 2px 2px 4px #000000;">Cyclone Intensity at Your Fingertips</h1></div>', unsafe_allow_html=True)

    # Introduction
    st.markdown('<div class="card"><p style="font-family:sans-serif; color:black; font-size: 20px;">Welcome to the Cyclone Intensity Calculator! Upload an image of a cyclone and let us determine its intensity and direction.</p></div>', unsafe_allow_html=True)
    
    # Sample image
    
    
    # Upload image
    file = st.file_uploader('Upload an image', type=["png", "jpg", "jpeg"])
    if file is not None:
        col1, col2 = st.columns(2)
        
        # Display uploaded image and compute intensity
        with col1:
            st.markdown('<p style="font-family:sans-serif; color:black; font-size: 20px;">Uploaded image 👇</p>', unsafe_allow_html=True)
            image = Image.open(file)
            st.image(
                image,
                caption="Your amazing image has shape",
                use_column_width=True,
            )
            img_array = np.array(image)
            img = tf.image.resize(img_array, size=(256, 256))
            img = tf.expand_dims(img, axis=0)
            img = img / 255.
            if st.button('Compute Intensity'):
                with col2:
                    intensity = pred_and_plot(loaded_model, img)
                    direction = pred_and_plot(loaded_direction_model, img)
                    direction_index = tf.argmax(direction, axis=1).numpy()[0]
                    directions = ["East", "West", "North", "South"]
                    predicted_direction = directions[direction_index]

                    Preventive_Measures = [
                    # Cyclones with intensity < 40 knots
                        [
                            {"Type": "Tropical Depression to Tropical Storm", 
                            "Area Radius Affected": "100-200 kilometers", 
                            "Evacuation Time": "12-24 hours before landfall"
                            }
                        ],
                        # Cyclones with intensity between 40 and 45 knots
                        [
                            {"Type": "Severe Tropical Storm", 
                            "Area Radius Affected": "Up to 300 kilometers", 
                            "Evacuation Time": "24-48 hours before landfall"
                            }
                        ],
                        # Cyclones with intensity > 45 knots
                        [
                            {"Type": "Hurricane", 
                            "Area Radius Affected": "Beyond 500 kilometers", 
                            "Evacuation Time": "48-72 hours before landfall"
                            }
                        ]
                    ]
                    session_state.shared_variable = intensity[0][0]
                    print(session_state.shared_variable)
                    if intensity[0][0] < 40:
                        index = 0
                    elif intensity[0][0] >= 40 and intensity[0][0] <= 45:
                        index = 1
                    else:
                        index = 2

                    st.markdown(f'<div class="card" style="margin-top:50px;"><p style="font-family:sans-serif; color:black;">The intensity of Cyclone is {str(intensity[0][0])} KNOTS, heading towards {directions[direction_index]} </p></div>', unsafe_allow_html=True)

                    st.markdown(f'<div class="card" style="margin-top:5px;"><p style="font-family:sans-serif; color:black;"><b>More Details About the Cyclone:</b></p> <p>Type of Cyclone: {Preventive_Measures[index][0]["Type"]}</p> <p>Area Radius Affected: {Preventive_Measures[index][0]["Area Radius Affected"]}</p> <p>Evacuation Time: {Preventive_Measures[index][0]["Evacuation Time"]}</p></div>', unsafe_allow_html=True)

                    # st.markdown(f'<div class="card" style="margin-top:5px;"><p style="font-family:sans-serif; color:black;">Preventive Measures</p> <p>Type of Cyclone: { Preventive_Measures[index]["Type"]}</p>  <p>Area Radius Affected: { Preventive_Measures[index]["Area Radius Affected"]}</p> <p>Evacuation Time: { Preventive_Measures[index]["Evacuation Time"]}</p>', unsafe_allow_html=True)
                    # for measure in Preventive_Measures[index]:
                    #     st.markdown(f'<p>Type of Cyclone: {measure["Type"]}</p>', unsafe_allow_html=True)
                    #     st.markdown(f'<p>Area Radius Affected: {measure["Area Radius Affected"]}</p>', unsafe_allow_html=True)
                    #     st.markdown(f'<p>Evacuation Time: {measure["Evacuation Time"]}</p>', unsafe_allow_html=True)
                    # st.markdown('</div>', unsafe_allow_html=True)





    st.markdown(
        """
        <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); margin-bottom: 25px">
            <h2 style="color: #007bff; text-decoration: underline; text-decoration-color: transparent; transition: text-decoration-color 0.3s ease;">How Our Tool Works:</h2>
            <p>Our tool uses a specialized type of artificial intelligence called a Convolutional Neural Network (CNN) to analyze images of cyclones. These images are captured by satellites and contain important information about the size, structure, and movement of cyclones.</p>
            <img src="https://th.bing.com/th/id/OIG1.HcclpL0mikxwm3XieyRr?pid=ImgGn" alt="Cyclone Image" style="width: 100%; max-width: 650px;">
            <h3 style="color: #333333;">Image Analysis:</h3>
            <p>The CNN model examines the images to identify patterns and features associated with cyclone intensity. It looks for characteristics such as cloud formations, wind patterns, and atmospheric pressure changes.</p>
            <h3 style="color: #333333;">Prediction:</h3>
            <p>Based on its analysis, the model generates a prediction of the cyclone's intensity. This prediction is presented as a numerical value, indicating the strength of the cyclone on a scale of low to high intensity.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Why It Matters section

    st.markdown(
        """
        <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <h2 style="color: #007bff; text-decoration: underline; text-decoration-color: transparent; transition: text-decoration-color 0.3s ease;">Why It Matters:</h2>
            <p>Understanding the intensity of cyclones is essential for communities and emergency responders to prepare for and respond to these events effectively. By accurately predicting cyclone intensity, our tool helps to:</p>
            <img src="https://th.bing.com/th/id/OIG3.rNIR7KsC8zFMIIe0xp.7?w=1024&h=1024&rs=1&pid=ImgDetMain" alt="Cyclone Image" style="width: 100%; max-width: 650px;">
            <ul>
                <li>Minimize Risks: Early detection of high-intensity cyclones allows for timely evacuation and other protective measures, reducing the risk of harm to people and property.</li>
                <li>Optimize Resources: By providing precise information about cyclone intensity, our tool helps to allocate resources more efficiently, ensuring that aid and support reach areas most in need.</li>
                <li>Enhance Resilience: Armed with knowledge about cyclone intensity, communities can develop strategies to build resilience and mitigate the impact of future storms.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

 
# Run the app
if __name__ == "__main__":
    app()
