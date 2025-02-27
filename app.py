import streamlit as st

# Unit conversion functions
def convert_length(value, from_unit, to_unit):
    units = {'meters': 1, 'kilometers': 0.001, 'centimeters': 100, 'millimeters': 1000, 'miles': 0.000621371}
    return value * units[to_unit] / units[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return None  # Handle unsupported conversions

def convert_weight(value, from_unit, to_unit):
    units = {'grams': 1, 'kilograms': 0.001, 'milligrams': 1000, 'pounds': 0.00220462, 'ounces': 0.035274}
    return value * units[to_unit] / units[from_unit]

# Streamlit app
st.title('✨ Unit Converter ✨')

# Custom CSS for background and styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #a1c4fd, #c2e9fb);
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .stNumberInput, .stSelectbox, .stButton>button {
        background-color: rgba(255, 255, 255, 0.9);
        color: #333;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #ddd;
    }
    .stButton>button {
        background-color: #ff6f61;
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #ff3b2f;
    }
    .highlight-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        color: #333;
    }
    .stHeader {
        color: #333;
    }
    .sidebar .sidebar-content {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .sidebar .sidebar-content .stHeader {
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for conversion type

st.sidebar.header('🔧 Choose Conversion Type 🔧')
conversion_type = st.sidebar.selectbox('Type', ('📏 Length', '🌡 Temperature', '⚖ Weight'))
st.sidebar.subheader("🌱Learning Hub!")
st.sidebar.subheader("💗Created By Rabia Rizwan💗")
st.sidebar.subheader("Happy Coding💦")


# Main content
st.header('📥 Input Value 📥')
value = st.number_input('Value', min_value=0.0, format='%.2f')

if conversion_type == '📏 Length':
    from_unit = st.selectbox('From Unit', ('meters', 'kilometers', 'centimeters', 'millimeters', 'miles'))
    to_unit = st.selectbox('To Unit', ('meters', 'kilometers', 'centimeters', 'millimeters', 'miles'))
elif conversion_type == '🌡 Temperature':
    from_unit = st.selectbox('From Unit', ('celsius', 'fahrenheit', 'kelvin'))
    to_unit = st.selectbox('To Unit', ('celsius', 'fahrenheit', 'kelvin'))
elif conversion_type == '⚖ Weight':
    from_unit = st.selectbox('From Unit', ('grams', 'kilograms', 'milligrams', 'pounds', 'ounces'))
    to_unit = st.selectbox('To Unit', ('grams', 'kilograms', 'milligrams', 'pounds', 'ounces'))

# Convert button and result
if st.button('Convert'):
    if conversion_type == '📏 Length':
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == '🌡 Temperature':
        result = convert_temperature(value, from_unit, to_unit)
    elif conversion_type == '⚖ Weight':
        result = convert_weight(value, from_unit, to_unit)
    
    if result is not None:
        st.markdown(f'<div class="highlight-box"><b>Converted Value: {result:.2f} {to_unit}</b></div>', unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("Unsupported conversion! Please check your unit selections.")