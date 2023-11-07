# Make a fully functional contact form using streimlit
# website:- https://formsubmit.co/
import streamlit as st
# header
st.header(":mailbox: Get in Touch with Me!!")
contact_form = """
<form action="https://formsubmit.co/ghartirem072@email.com" method="POST">
<input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Enter your Email" required>
     <input type="email" name="email" placeholder = "Enter your Name" required>
      <textarea name="message" placeholder="Your Message"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form,unsafe_allow_html=True)
