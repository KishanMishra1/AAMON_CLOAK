import streamlit as st
import os
import time
import subprocess


def main():
    choices=['About Aamon','Try Aamon Passive']
    c=st.sidebar.selectbox("Select Activity",choices)
    st.sidebar.markdown("""
    FUN PROJECT\n
    NAME : KISHAN MISHRA
    """)

    if c=="About Aamon":
        st.title("AAMON - MOBILE LEGENDS BANG BANG !")
        st.caption("StoryVideo")
        video_file = open('The Night Chase _ New Hero Aamon Cinematic _ Mobile Legends_ Bang Bang.mp4', 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)

        st.caption("Storyline")
        html_temp_about1= """
                             		<div style="background-color:#98AFC7;padding:15px">
                             		<h4 style="color:white;text-align:center;">An infant's cry shattered the silent dawn of Castle Aberleen. House Paxley, the most powerful and influential duchy in the Moniyan Empire, finally had an heir.</h4>
                                    <h4 style="color:white;text-align:center;">The child's father of Duke Paxley named him Aamon, and soon his younger brothers were born on after another. But as the eldest son and the family heir, Aamon had been subject to more strict discipline since his childhood. He was never allowed to be as free-spirited as his brother Gusion, and since as early as his boyhood, he'd been occupied with studies and official duties all day.</h4>
                                    <h4 style="color:white;text-align:center;">Aamon did not only learn the things required for a normal nobleman. His father Duke Paxley also secretly [teaches] him the spell that was only passed down to the family's direct descendants. It was a devious, ruthless spell that killed people neither honestly nor honorably. Aamon once felt skeptical because the secret family spell didn't match the honorable history of House Paxley that believed in the Lord of Light, and for this, he went out of his way to read on the family history.</h4>
                                    <h4 style="color:white;text-align:center;">However, fate didn't allow him to find any answer. The year when Aamon just turned 18, his father who had high hopes for him went missing along with his mother in a sandstorm while visiting Altair. After his father's presumed death, Aamon had to bear the heavy responsibilities of the family as the young heir and become the head of House Paxley.</h4>
                                    <h4 style="color:white;text-align:center;">Aamon showed a degree of maturity that a young man like him barely had, whether it was due to his father's teachings or the heavy burdens of the family. He was passionate in social circles but cold and aloof when facing his political enemies. He displayed a perfect noble gentleman's kindness in politics, but on the battlefields, he seemed like a ghoul casting merciless spells. To most people who'd worked with him, Aamon was a shadow that could never be caught.</h4>
                                    <h4 style="color:white;text-align:center;">After the late Duke Paxley was presumed dead, Aamon was not only left with the responsibilities of the entire family, but also his younger brothers and sisters. In fact, he was not as mysterious and inscrutable as others saw. His intention was surprisingly simple: the duty of protecting House Paxley had been engraved in his mind since he was the heir, so his family and the blood ties were everything to Aamon. No matter what evil deeds or good things he'd done, they’d all been for one purpose – the future of House Paxley.</h4>
                                    <h4 style="color:white;text-align:center;">Aamon once thought that protecting he house and protecting his families were completely the same, until one day, the curse from the ancient prophecy befell his younger brother, Gusion…<h4>
                                    <h4 style="color:white;text-align:center;">Aamon never showed it to anyone, but among all his brothers and sisters, Gusion had been the one he'd paid the most attention to. Because Aamon saw the qualities that he didn't possess on Gusion – he was a free-spirited rebel who'd wreak havoc without a second thought. But Aamon didn't dislike his brother for it, and he thought maybe they were supposed to resemble each other as brothers, except that he had no choice but to turn into the person he was now. Whenever he looked at Gusion, he seemed to see the person he could have been.</h4>
                                    <h4 style="color:white;text-align:center;">Therefore, even though the entire Moniyan Empire knew that Aamon had a trickster good-for-nothing brother, he'd never discipline Gusion about his delinquent behaviors. Even one time when little Gusion accidentally cut Aamon's face with a knife, leaving a permanent scar on his cheek, Aamon only patted him and didn’t say anything more. Of course, Gusion didn't dare to bring any sharp objects near his respectable brother even again.</h4>
                                    <h4 style="color:white;text-align:center;">As the heir of the family, Aamon had heard about their ancestors' prophecy from his father since still young. He knew that whoever in House Paxley had a dark mark appearing on their body would be attached by the deity. So, when he found the mark on Gusion, he immediately made the decision to imprison him and cut out all the connection between him and the outside world, temporarily preventing the other family members from finding out about the changes on Gusion.</h4>
                                    <h4 style="color:white;text-align:center;">Aamon was engrossed by immense pain afterwards. Gusion's existence was without a doubt a sword of Damocles hanging above House Paxley, but Aamon didn't want to kill his brother. However, what he did to protect Gusion didn't buy them much time. A few days later, the elders of the family found out about Gusion's secret and soon arrived at the place where Gusion was held. And they were obviously not here to spare Gusion's life.</h4>
                                    <h4 style="color:white;text-align:center;">The situation didn't allow Aamon to hesitate any longer, so he made the decision to ask the servant who'd been watching over Gusion to free his brother in secret. But rather than just letting Gusion roam free, Aamon had been keeping an eye on his brother, and as expected, his wayward brother didn't follow his order and stayed in hiding in Castle Aberleen instead.</h4>
                                    <h4 style="color:white;text-align:center;">The young Duke Paxley let out a sigh and decided to do it himself―to find the root of the dark-mark curse and save his brother, while putting an end to the fetters of tragedies that had confined their family for centuries.</h4>
                                    </div>
                                     """
        st.markdown(html_temp_about1, unsafe_allow_html=True)
        st.write(' ');st.write(" ");st.write(" ")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(' ')

        with col2:
            st.image("image.webp")

        with col3:
            st.write(' ')
        st.markdown(f'<h1 style="color:#FFFFFF;font-size:24px; text-align:center;">{"It is better to be feared than loved, if you cannot both."}</h1>', unsafe_allow_html=True)
    elif c=="Try Aamon Passive":
        st.markdown(f'<h1 style="color:#FFFFFF;font-size:24px; text-align:left;">{"Select Your Cloak"}</h1>', unsafe_allow_html=True)
        st.markdown(
                """<style>span[data-baseweb="tag"] {background-color: blue !important;}</style>""",unsafe_allow_html=True,)
        agree = st.checkbox('Red')
        if agree:
            st.markdown(f'<h1 style="color:#FFFFFF;font-size:23px; text-align:left;">{"Get Ready with your Red Cloak !"}</h1>', unsafe_allow_html=True)
            time.sleep(3)
            st.write('');st.write('')
            col1, col2 = st.columns(2)
            with col1:
                st.write('')
            with col2:
                if st.button('Start'):
                    os.system('code.py')
                
                    

            
    
main()
'''st.write("")
                st.markdown(f'<h1 style="color:#FFFFFF;font-size:19px;">{"Opening Webcam . . ."}</h1>', unsafe_allow_html=True)
                time.sleep(2)
                st.markdown(f'<h1 style="color:#FFFFFF;font-size:19px;">{"Show your background !"}</h1>', unsafe_allow_html=True)
                time.sleep(2)
                st.markdown(f'<h1 style="color:#FFFFFF;font-size:19px;">{"Use cloak for camoulfage !"}</h1>', unsafe_allow_html=True)'''