# Function to create SPICE subcircuit model for SMS7630 diode with extra L and C
def create_sms7630_subcircuit(file_name="sms7630_with_LC.lib"):
    """
    Generates a SPICE subcircuit model for the SMS7630 Schottky diode 
    with an additional series inductance (L) and parallel capacitance (C).
    """

    # Define subcircuit name
    subckt_name = "SMS7630_LC"

    # Define SPICE model parameters from the datasheet
    model_name = "SMS7630"  # Diode model name

    # External elements
    ls = 0.7E-9    # Series inductance (H)
    cp = 0.07E-12  # Parallel capacitance (F)

    # Electrical characteristics from Table 5 of the datasheet
    isat = 5E-6      # Saturation current (A)
    rs = 20          # Series resistance (Ω)
    n = 1.05         # Ideality factor
    tt = 1E-11       # Transit time (s)
    cjo = 0.14E-12   # Zero-bias junction capacitance (F)
    vj = 0.34        # Junction potential (V)
    m = 0.40         # Grading coefficient
    eg = 0.69        # Band gap energy (eV)
    xti = 2          # Saturation current temperature exponent
    fc = 0.5         # Forward-bias depletion capacitance coefficient
    bv = 2           # Reverse breakdown voltage (V)
    ibv = 1E-4       # Current at breakdown voltage (A)

    # Create the SPICE subcircuit and model definition
    spice_model = f""" 
* SPICE Subcircuit Model for {subckt_name} Schottky Diode
.SUBCKT {subckt_name} 1 2  ; Define ports: 1 = Input, 2 = Output
    Ls  1 N1 {ls}  ; Series inductance
    D1  N1 2 {model_name}  ; Diode model
    Cp  N1 2 {cp}  ; Parallel capacitance
.ENDS {subckt_name}

* Diode SPICE Model
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
    create_sms7630_subcircuit()
