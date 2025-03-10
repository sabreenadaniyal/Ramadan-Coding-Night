import streamlit as st # streamlit is a library for building web applications

# function to convert units based on predefined conversions factorrs or formulas
def convert_units(value, unit_from, unit_to):

    conversions = {
        "meter_kilometer": 0.001, # 1 meter =0.00, kilometer
        "kilometer_meter": 1000,  # 1 kilometer = 1000 meter
        "gram_kilogram": 0.001,   # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000,    # 1 kilogram = 1000 gram
    }

    key = f"{unit_from}_{unit_to}" # Gnerate a key based on the input and output units

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"
    
st.title("Unit Converter")

value = st.number_input("Enter the value to convert:")

unit_from = st.selectbox("Selectthe unit to convert from:",["meter", "kilometer", "gram", "kilogram"])

unit_to = st.selectbox("Select the unit to convert to:",["meter", "kilometer"," gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to) # call the conversion function
    st.write(f"The converted value is {result}") # display the result