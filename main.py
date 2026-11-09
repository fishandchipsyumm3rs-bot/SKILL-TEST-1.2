# Yum Food
from pyscript import display, document

# Function that searches for the element
def show_element(e):

    # Clears the previous result
    document.getElementById('result').innerHTML = ''

    # Gets the user's input
    user_input = document.getElementById('user_input').value.capitalize().strip()

    # Dictionary containing non-metal elements
    # Format: Symbol: (Symbol, Name, Atomic Number, Atomic Mass)
    elements = {
        'H': ('H', 'Hydrogen', '1', '1.008'),
        'He': ('He', 'Helium', '2', '4.0026'),
        'C': ('C', 'Carbon', '6', '12.011'),
        'N': ('N', 'Nitrogen', '7', '14.007'),
        'O': ('O', 'Oxygen', '8', '15.999'),
        'F': ('F', 'Fluorine', '9', '18.998'),
        'Ne': ('Ne', 'Neon', '10', '20.180'),
        'P': ('P', 'Phosphorus', '15', '30.974'),
        'S': ('S', 'Sulfur', '16', '32.06'),
        'Cl': ('Cl', 'Chlorine', '17', '35.45'),
        'Ar': ('Ar', 'Argon', '18', '39.948'),
        'Se': ('Se', 'Selenium', '34', '78.971'),
        'Br': ('Br', 'Bromine', '35', '79.904'),
        'Kr': ('Kr', 'Krypton', '36', '83.798'),
        'I': ('I', 'Iodine', '53', '126.904'),
        'Xe': ('Xe', 'Xenon', '54', '131.293'),
        'Rn': ('Rn', 'Radon', '86', '222'),
        'Og': ('Og', 'Oganesson', '118', '294')
    }

    # Checks if the entered symbol exists
    element_checker = user_input in elements

    # Gets the element information
    element_data = elements.get(user_input, ['', '', '', ''])

    # Displays the information or an error message
    display_message = {
        False: f"<b>{user_input}</b> is not a Non-Metal Element.",
        
        True: f"""
        <b>Element Symbol:</b> {element_data[0]}<br>
        <b>Element Name:</b> {element_data[1]}<br>
        <b>Atomic Number:</b> {element_data[2]}<br>
        <b>Atomic Mass:</b> {element_data[3]}
        """
    }

    # Shows the result on the webpage
    document.getElementById('result').innerHTML = display_message[element_checker]