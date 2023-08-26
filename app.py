import streamlit as st
from PIL import Image



def main():
    
    # Centering everything
    st.markdown('<div style="text-align: center;">'
                '<h1>John Glenn Njoroge Wanjiru</h1>'
                '</div>', unsafe_allow_html=True)

    # Open and resize the image
    image = Image.open('Images\PSFix_20220622_161401 (12) (1).jpg')
    image_resized = image.resize((300, int(300 * image.height / image.width)))

    # Center the image with rounded corners
    st.markdown('<div style="text-align: center;">'
                f'<img src="data:image/png;base64,{image_to_base64(image_resized)}" alt="Glenn Njoroge" '
                'style="border-radius: 50px;"'
                'style="box-shadow: 0,0,12,20;"'
                'style="border-color: aqua;"'
                'style="border-width: 20px;">'
                
                '<p></p>'
                '</div>', unsafe_allow_html=True)

    st.markdown('<div style="text-align: center;">'
                '<h2>Summary</h2>'
                '<p>I am Glenn Njoroge, a versatile professional with expertise in machine learning '
                'and a background in 3D modeling and animation. I excel in data preprocessing, '
                'feature engineering, and model selection. Using Blender, I create visually stunning '
                '3D models. Currently pursuing a Bachelors degree in Computer Science at Kabarak '
                'University, I am dedicated to continuous learning and driving innovation.</p>'
                '</div>', unsafe_allow_html=True)

    st.markdown('<div style="text-align: center;">'
                '<h2>Experience</h2>'
                '</div>', unsafe_allow_html=True)

    # Template for Experience
    st.markdown('<div style="background-color: #B3001B; padding: 20px; border-radius: 10px;">'
                '<h3>3D Animator</h3>'
                '<p><strong>Peter</strong>, Nairobi</p>'
                '<p><em>Jan 2023- Jan-2023</em></p>'
                '<p>    I created a 3d animation for an investigation<br/> Followed Storyboard and concept art to create 3d versions of desired components</p>'
                '<p>                                                    </p>'
# job 2
                 '<h3>MPESA Agent</h3>'
                '<p><strong>Elizabeth Shop</strong>, Ruiru</p>'
                '<p><em>Sep 2021- Dec-2022</em></p>'
                '<p>    Completed day-to-day transactions such as withdrawal and deposit of money to serve clients<br/></p>'

                '<h3>Food Packer</h3>'
                '<p><strong>Posho Company</strong>, Kiambu</p>'
                '<p><em>Aug 2021- Sep-2021</em></p>'
                '<p>    Sorted and packed floor on the assembly line to prepare for shipping <br/> weighed and labeled completed items for shipment and storage <br/>promoted safe and clean workspace to increase productivity and job satisfaction  </p>'
               
                '<p>                                                    </p>'

                '<h3>Shop Keeper</h3>'
                '<p><strong>Fair price Shop</strong>, Laipikipia,Nyahururu</p>'
                '<p><em>Feb 2021- Aug-2021</em></p>'
                
                '<p>      Sold Products to customers                                              </p>'
                '</div>', unsafe_allow_html=True)
    
    st.text('')


    st.markdown('<div style="text-align: center;">'
                '<h2>Education</h2>'
                '<p>                                                    </p>'
                '</div>', unsafe_allow_html=True)

    # Template for Education
    st.markdown('<div style="background-color: #262626; padding: 20px; border-radius: 10px;">'
                '<h3>B.Sc Computer Science</h3>'
                '<p><strong>Kabarak University</strong>, Nakuru</p>'
                '<p><em>2020-2025</em></p>'
                '<p>Attended a Machine Learning bootcamp<br/> Member of the Google DSC group </p>'
                '<p>                                                    </p>'
                '<p>                                                    </p>'
                '<h3>High school Diploma</h3>'
                '<p><strong>Saint Joseph High School</strong>, Kiambu</p>'
                '<p><em>2016-2019</em></p>'
                '<p>Was Computer Lab Captain<br/> Was the head of IT club </p>'
                '<p>                                                    </p>'
                '<p>                                                    </p>'  
                '<h3>High school Diploma</h3>'
                '<p><strong>Saint Joseph High School</strong>, Kiambu</p>'
                '<p><em>2007-2015</em></p>'
                '<p>Was the school president <br/>Sub-county Environment President <br/>Member of the Redcross Club </p>'
                '<p>                                                    </p>'
                '<p>                                                    </p>'  
                                              
                              
                '</div>', unsafe_allow_html=True)
    st.text("")
    st.text("")


    # Two columns layout for Hobbies, Skills, and Projects
    col1, col2 = st.columns(2)

   

    # Template for Hobbies in column 1
    with col1:
        st.markdown('<div style="background-color: #255C99; padding: 20px; border-radius: 10px;">'
                    '<h2>Hobbies</h2>'
                    '<ul>'
                    '<li>3D Modelling</li>'
                    '<li>Game Development</li>'
                    '<li>Reading Scifi Comics</li>'
                    '<li>Making Animations</li>'
                    '<li>WoodWork</li>'
                    '</ul>'
                    '<p>                                                    </p>'
                    '<p>                                                    </p>'
                    '<p>                                                    </p>'
                    '</div>', unsafe_allow_html=True)
        st.text("")

    # Template for Skills in column 2
    with col2:
        st.markdown('<div style="background-color: #7EA3CC; padding: 20px; border-radius: 10px;">'
                    '<h2>Skills</h2>'
                    '<ul>'
                    '<li>.NET MAUI with C# : 🟣🟣🟣🟣⚫</li>'
                    '<li>Python :       🐍🐍🐍🐍🐍</li>'
                    '<li>Svelte: 🔴🔴🔴⚫⚫</li>'
                    '<li>Machine Learning : 🟤🟤🟤⚫⚫</li>'
                    '<li>Streamlit: 🔵🔵🔵🔵🔵</li>'
                    '<li>HTML and CSS: 🟡🟡🟡🟡⚫</li>'
                    '<li>JavaScript:⚪⚪⚪⚫⚫</li>'
                    '<li>BLender: 🟠🟠🟠🟠🟠</li>'
                    '<li>Unity: 🟣🟣🟣🟣⚫</li>'
                    '</ul>'
                    '<p>                                                    </p>'
                    '<p>                                                    </p>'
                    '<p>                                                    </p>'
                    
                    '</div>', unsafe_allow_html=True)
        st.text("")
        st.text("")

    # Template for Projects spanning both columns
    st.markdown('<div style="background-color: #CCAD8F; padding: 20px; border-radius: 10px;">'
                '<h2>Projects</h2>'
                '<h3>Gamma and Haron Predictor ML Model 🤖</h3>'
                '<p><a href="https://project-link/" target="_blank" rel="noopener noreferrer">'
                'Link to Project</a></p>'
                '<p>This is a machine learninng model am working on for predicting Gammas and Hadrons...<br/> I have use diffrerent approaches to make sure i get the best accuracy</p>'
                '<p>   </p>'
                '<h3>Cubotron 🎮</h3>'
                
                '<p>This is a game Am working on am supposed to release is by end this year 2023 <br/>Its a private project but i will make sure i put the link here when i finish</p>'


                '<h3>Lectacle 🤖</h3>'
                
                '<p>This is an app am developing with DOTNET MAUI<br/> Its a App for teaching you courses using the GPT model<br/>it is still in early development</p>'
                '<p>   </p>'

                '<h3>Blender Samples 📺</h3>'
                
                '<p>This are some of my work finish</p>'
                #youtube link      

                    



                '</div>', unsafe_allow_html=True)
       

    # YouTube video URL
    youtube_url = "https://www.youtube.com/shorts/4gLP-JneVtI?feature=share"
    st.video(youtube_url)

   
   
    st.text("")

    st.markdown('<div style="text-align: center;">'
                '<h2>Social Media and Contacts</h2>'
                '</div>', unsafe_allow_html=True)

    # Template for Social Media Handles
    st.markdown('<div style="text-align: center; margin-bottom: 20px;">'
            '<a href="https://www.linkedin.com/in/glenn-wanjiru-10213b24a/" target="_blank" rel="noopener noreferrer">'
            '<img src="Images/linkedin.png" alt="LinkedIn" width="30" height="30"></a>'
            '&nbsp;&nbsp;'
            '<a href="https://twitter.com/Glennnjoroge" target="_blank" rel="noopener noreferrer">'
            '<img src="Images/twitter-x-black-hexagon-logo-20917.png" alt="Twitter" width="30" height="30"></a>'
            '&nbsp;&nbsp;'
            '<a href="https://github.com/glennwanjiru" target="_blank" rel="noopener noreferrer">'
            '<img src="Images/github.png" alt="GitHub" width="30" height="30"></a>'

            '<a href="https://youtube.com/@stainedcoffeecup?si=OHmxfOEJhZTsop2F" target="_blank" rel="noopener noreferrer">'
            '<img src="Images/youtube.png" alt="Youtube" width="30" height="30"></a>'
            '</div>', unsafe_allow_html=True)


def image_to_base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

if __name__ == "__main__":
    main()
