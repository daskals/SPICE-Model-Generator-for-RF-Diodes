

# https://www.acsu.buffalo.edu/~wie/applet/spice_pndiode/spice_diode_table.html


# Function to create SPICE model file for SMS7630 diode
def create_sms7630_spice_model(file_name="sms7630.lib"):
    """
    Generates the SPICE model for the SMS7630 Schottky diode and saves it as a .lib file.
    """

    # Define SPICE model parameters
    model_name = "SMS7630"  # Model name

    # Electrical characteristics
    isat = 5E-6      # Saturation current (A)
    rs = 20          # Series resistance (Ω)
    n = 1.05         # Ideality factor
    tt = 1E-11       # Transit time (s)
    cjo = 0.14E-12   # Zero-bias junction capacitance (F)
    vj = 0.34        # Junction potential (V)
    m = 0.4          # Grading coefficient
    eg = 0.69        # Band gap energy (eV)
    xti = 2          # Saturation current temperature exponent
    fc = 0.5         # Forward-bias depletion capacitance coefficient
    bv = 2           # Reverse breakdown voltage (V)
    ibv = 1E-4       # Current at breakdown voltage (A)

    # Create the SPICE model string
    spice_model = f""" 
* SPICE Model for {model_name} Schottky Diode
.MODEL {model_name} D (
    IS={isat}    ; Saturation current
    RS={rs}      ; Series resistance
    N={n}        ; Ideality factor
    TT={tt}      ; Transit time
    CJO={cjo}    ; Zero-bias junction capacitance
    VJ={vj}      ; Junction potential
    M={m}        ; Grading coefficient
    EG={eg}      ; Band gap energy
    XTI={xti}    ; Saturation current temperature exponent
    FC={fc}      ; Forward-bias depletion capacitance coefficient
    BV={bv}      ; Reverse breakdown voltage
    IBV={ibv}    ; Current at breakdown voltage
)
"""

    # Save the model to a file
    with open(file_name, "w") as file:
        file.write(spice_model)

    print(f"SPICE model saved to {file_name}")

# Execute the function to generate the model
if __name__ == "__main__":
    create_sms7630_spice_model()