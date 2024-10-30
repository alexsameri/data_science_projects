# importing the libaries

import numpy as np
import pickle # to load the model
import streamlit as st
import pandas as pd


# loaded_model = pickle.load(open(r"C:/Users/Alex Sameri/Desktop/data_science_projects/Final Project Files/trained_model1.sav", "rb"))
with open(r"C:/Users/Alex Sameri/Desktop/data_science_projects/Final Project Files/trained_model1.sav", "rb") as file:
    loaded_model = pickle.load(file)