import os
from enum import Enum
import folium

class StyleConfig(Enum):
    # CSS so that we have a better looking app
    # Voila has troubles importing this from a file
    MATERIAL_CSS = f"""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Karla:wght@400&display=swap');

                    /* Set the default font for the entire document */
                    body, button, input, select, textarea, label {{
                    font-family: 'Karla', sans-serif;
                    }}

                    /* Increase the font size for h1 elements */
                    h1 {{
                    font-size: 48px;
                    }}

                    /* Material Design button styles */
                    button.material-button {{
                    display: inline-block;
                    padding: 10px 20px;
                    font-size: 16px;
                    text-align: center;
                    text-decoration: none;
                    outline: none;
                    color: #fff;
                    background-color: #2196F3;
                    border: none;
                    border-radius: 5px;
                    box-shadow: 0 5px 15px rgba(33, 150, 243, 0.3);
                    cursor: pointer;
                    }}

                    button.material-button:hover {{
                    background-color: #1565C0;
                    }}

                    button.material-button:active {{
                    background-color: #0D47A1;
                    }}

                    /* Material Design text input styles */
                    input.material-input {{
                    padding: 10px;
                    font-size: 16px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    }}

                    input.material-input:focus {{
                    border-color: #2196F3;
                    box-shadow: 0 0 5px rgba(33, 150, 243, 0.5);
                    }}

                    /* Material Design Combobox styles */
                    div.material-combobox {{
                    display: inline-block;
                    position: relative;
                    }}

                    div.material-combobox select {{
                    width: 100%;
                    padding: 10px;
                    font-size: 16px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    cursor: pointer;
                    }}

                    div.material-combobox select:focus {{
                    border-color: #2196F3;
                    box-shadow: 0 0 5px rgba(33, 150, 243, 0.5);
                    }}

                    /* Material Design label styles */
                    label.material-label {{
                    font-size: 16px;
                    color: #2196F3;
                    margin-bottom: 5px;
                    }}
                    </style>
                    """
