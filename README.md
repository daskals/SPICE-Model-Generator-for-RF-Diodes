# SPICE-Model-Generator-for-RF-Diodes

This repository contains Python scripts to generate SPICE models for RF and Schottky diodes based on manufacturer datasheets. It currently supports the **SMS7630** diode, and can be easily extended for other diodes.


## 📚 Bibliography

The `bibliography/` folder contains reference materials, datasheets, and modeling notes used in the creation of the SPICE models. This includes:

- Manufacturer datasheets (e.g., Skyworks SMS7630)
- Technical modeling notes or publications
- Helpful links and resources related to SPICE modeling

Please consult these documents if you want to understand the source of parameter 

## 📦 Folder Structure

Each diode model is organized in its own folder. Currently included:

- `sms7630/` — SPICE models and scripts for the Skyworks SMS7630 Schottky diode.

## 📁 sms7630 Folder Contents

- `SMS7630_spice_model_creator.py`: Generates a `.lib` file for the basic SPICE diode model.
- `SMS7630_spice_model_creator_LC.py`: Generates a `.lib` file for a subcircuit model with parasitic inductance and capacitance.
- `sms7630.lib`: Output from the basic model generator.
- `sms7630_with_LC.lib`: Output from the subcircuit model generator.

## ⚙️ Requirements

Python 3.x is required. No additional Python libraries are needed.

## 🚀 Usage

To generate models for SMS7630:

```bash
cd sms7630
python SMS7630_spice_model_creator.py          # Generates sms7630.lib
python SMS7630_spice_model_creator_LC.py       # Generates sms7630_with_LC.lib
