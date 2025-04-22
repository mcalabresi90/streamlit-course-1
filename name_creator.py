import streamlit as st
import pandas as pd

# text input for favorite color
favorite_color = st.text_input("Enter your favorite color")

# text input for favorite animal
favorite_animal = st.text_input("Enter your favorite animal")

# superhero name generator
st.header("Superhero Name Generator")

# Check if we have the necessary inputs
if favorite_color and favorite_animal:
    # Generate a superhero name based on inputs
    superhero_name = f"{favorite_color} {favorite_animal}"
    st.write(f"Your superhero name is: {superhero_name}")
else:
    st.info("Please enter your favorite color and favorite animal to generate your superhero identity!")

    



