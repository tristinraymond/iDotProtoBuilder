#idot protobuilder V1.1 - has individual replicate capability
#idot protobuilder V1.2 - has scrollbar update
#source plate selection available
#randomization works perfectly fine 
#V1.5 has import function for csv (compound_name, volume, replicate)
#working on help update for instructions
import streamlit as st
import tkinter as tk
from tkinter import simpledialog, filedialog, ttk
from ttkthemes import ThemedTk
from tkinter.scrolledtext import ScrolledText
import csv
import random #random module for randomizing
#import theme library




# Define dictionaries for the three options ('240', '308', and '384')
source_well_values = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12']

plate_well_values_384 = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D24', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'E23', 'E24', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20', 'H21', 'H22', 'H23', 'H24', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15', 'I16', 'I17', 'I18', 'I19', 'I20', 'I21', 'I22', 'I23', 'I24', 'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15', 'J16', 'J17', 'J18', 'J19', 'J20', 'J21', 'J22', 'J23', 'J24', 'K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11', 'K12', 'K13', 'K14', 'K15', 'K16', 'K17', 'K18', 'K19', 'K20', 'K21', 'K22', 'K23', 'K24', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12', 'L13', 'L14', 'L15', 'L16', 'L17', 'L18', 'L19', 'L20', 'L21', 'L22', 'L23', 'L24', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10', 'O11', 'O12', 'O13', 'O14', 'O15', 'O16', 'O17', 'O18', 'O19', 'O20', 'O21', 'O22', 'O23', 'O24', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P22', 'P23', 'P24']

plate_well_values_308 = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'E23', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20', 'H21', 'H22', 'H23', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15', 'I16', 'I17', 'I18', 'I19', 'I20', 'I21', 'I22', 'I23', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15', 'J16', 'J17', 'J18', 'J19', 'J20', 'J21', 'J22', 'J23', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11', 'K12', 'K13', 'K14', 'K15', 'K16', 'K17', 'K18', 'K19', 'K20', 'K21', 'K22', 'K23', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12', 'L13', 'L14', 'L15', 'L16', 'L17', 'L18', 'L19', 'L20', 'L21', 'L22', 'L23', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10', 'O11', 'O12', 'O13', 'O14', 'O15', 'O16', 'O17', 'O18', 'O19', 'O20', 'O21', 'O22', 'O23']

plate_well_values_240 = ['C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20', 'H21', 'H22', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15', 'I16', 'I17', 'I18', 'I19', 'I20', 'I21', 'I22', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15', 'J16', 'J17', 'J18', 'J19', 'J20', 'J21', 'J22', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11', 'K12', 'K13', 'K14', 'K15', 'K16', 'K17', 'K18', 'K19', 'K20', 'K21', 'K22', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12', 'L13', 'L14', 'L15', 'L16', 'L17', 'L18', 'L19', 'L20', 'L21', 'L22', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22']

selected_source_well_values = plate_well_values_240  # Default selection




def create_input_boxes():
    global input_box_vars  # Declare the global variable to store the input box variables
    input_box_vars = []  # Create a new list to store input box variables

    global volume_box_vars
    volume_box_vars = []  # Create a list to store input box variables for volume

    global replicate_box_vars
    replicate_box_vars = []

    root.attributes("-fullscreen", True)

    # Get the selected number from the dropdown
    selected_number = int(selected_number_var.get())

    # Get the selected dictionary option
    selected_option = option_var.get()

    # Set the source well values based on the selected option
    if selected_option == '240':
        selected_source_well_values = plate_well_values_240
    elif selected_option == '308':
        selected_source_well_values = plate_well_values_308
    elif selected_option == '384':
        selected_source_well_values = plate_well_values_384

    # Destroy any existing input boxes
    for widget in input_frame.winfo_children():
        widget.destroy()

    # Create input boxes for Compound Name and Volume [uL] for each compound side by side
    for i in range(selected_number):
        frame = ttk.Frame(input_frame, padding=(20, 10))
        frame.grid(padx=5, pady=5, rowspan=6)
        
        label_text = f"Compound {i + 1} Name:"
        label = ttk.Label(frame, text=label_text)
        label.grid(row=0, column=0, padx=5, pady=5)

        name_entry = ttk.Entry(frame)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        input_box_vars.append(name_entry)

        label_text = f"Volume {i + 1} [uL]:"
        label = ttk.Label(frame, text=label_text)
        label.grid(row=0, column=2, padx=5, pady=5)

        volume_entry = ttk.Entry(frame)
        volume_entry.grid(row=0, column=3, padx=5, pady=5)
        volume_box_vars.append(volume_entry)

        label_text = f"Replicates {i + 1}:"
        label = ttk.Label(frame, text=label_text)
        label.grid(row=0, column=4, padx=5, pady=5)

        replicate_entry = ttk.Entry(frame)
        replicate_entry.grid(row=0, column=5, padx=5, pady=5)
        replicate_box_vars.append(replicate_entry)


    # Enable the "Next" button
    create_button.config(state=tk.NORMAL)
    next_button.config(state=tk.NORMAL)
    import_button.config(state=tk.NORMAL)

def randomize_source_well_values():
    global selected_source_well_values
    random.shuffle(selected_source_well_values)

def change_option(*args):
    global selected_option
    selected_option = option_var.get()

def get_help():
    help_window = tk.Toplevel(canvas)
    help_window.title("Help")

    instructions = """IF YOU ARE ONLY BUILDING FROM THE APPLICATION:

    Begin by selecting the number of compounds you are planning to dispense.
    Then select the source plate type you are planning to use (this can either be an S.100 or S.200 plate)
    Choose your well format options (240, 308, and 384 are currently the only options)
    Click the randomize checkbox if you would like the platemap to be randomized
    Click "Create Input Boxes"
    This will create boxes for you to enter your compounds, dispense volumes, and replicate amounts
    Once you have filled out all of the boxes, click save and save the file to your computer/flashdrive
    
IF YOU ARE BUILDING FROM AN IMPORTED CSV:

    Begin by selecting the number of compounds you are planning to dispense.
    Then select the source plate type you are planning to use (this can either be an S.100 or S.200 plate)
    Choose your well format options (240, 308, and 384 are currently the only options)
    Click the randomize checkbox if you would like the platemap to be randomized
    Click "Create Input Boxes"
    Click the "Import" button and select your csv file (MUST BE A CSV FILE)
    Your CSV should have three columns: Compounds, Volumes, and Replicates **IN THIS ORDER**
    Make sure that row 1 of the csv either has the headings mentioned above (the import reads beginning at row 2)
    Once you have opened the csv in the application, the input boxes should have auto-populated with your csv data (if done correctly)
    From here, you can save your new csv to be used on the iDot"""

    text = ScrolledText(help_window, wrap=tk.WORD)
    text.insert("1.0", instructions)
    text.grid()

def import_variable_csv():
    global input_box_vars
    import_path = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", ".csv")])

    if import_path:
        #clear existing input box data
        for entry in input_box_vars:
            entry.delete(0, tk.END)

        for volume_entry in volume_box_vars:
            volume_entry.delete(0, tk.END)

        for replicate_entry in replicate_box_vars:
            replicate_entry.delete(0, tk.END)

        #read csv data and populate input boxes
        with open(import_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader) #skip header row

            #assuming structure is "compounds Name, Volume [uL], Replicates"
            for row in reader:
                if len(row) >= 2:
                    compound_name = row[0]
                    volume = row[1]
                    replicate_number = row[2]

                #populate input boxes with data
                for i in range(len(input_box_vars)):
                    if not input_box_vars[i].get():
                        input_box_vars[i].insert(0, compound_name)
                        volume_box_vars[i].insert(0, volume)
                        replicate_box_vars[i].insert(0, replicate_number)
                        break


def get_replicates():
    global selected_option
    selected_option = option_var.get()
    selected_source_plate_type = selected_source_var.get() #setting the value to read form the sourceplate dropdown
    randomize = randomize_var.get()


    replicates_per_compound = [int(entry.get()) for entry in replicate_box_vars]  # Get the number of replicates for each compound
    data = [entry.get() for entry in input_box_vars]
    volumes = [entry.get() for entry in volume_box_vars]
    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])

    if save_path:
        write_csv_with_replicates(data, volumes, replicates_per_compound, save_path, selected_option)
            #define values for the iDot header
        title = ""
        time = "0:08"
        date = "Date"
        user_name = "<UserName>"
        dispense_plate_type = "MWP 384"
        target_plate_number = "Target Plate 1"
        waste_error = "WasteErrorHandlingLevel=Ask"
        save_liquids = "SaveLiquids=Ask"
        source_plate_type = selected_source_plate_type
        dispense_to_waste = "DispenseToWaste=False"
        dispense_to_waste_cycles = "DispenseToWasteCycles=3"
        dispense_to_waste_volume = "DispenseToWasteVolume=1e-7"
        use_deionization = "UseDeionisation=True"
        optimization_level = "OptimizationLevel=ReorderAndParallel"
        source_plate_number = "Source Plate 1"



        with open(save_path, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                #write the fixed header
                writer.writerow([title, "1.7.2021.1205", user_name, date, time])
                writer.writerow([source_plate_type, source_plate_number, "", "0.8", dispense_plate_type, target_plate_number, "", "P24"])
                writer.writerow([dispense_to_waste, dispense_to_waste_cycles, dispense_to_waste_volume, use_deionization, optimization_level, waste_error, save_liquids])
                writer.writerow(['Source Well', 'Target Well', 'Volume [uL]', 'Liquid Name'])
                
                source_well_index = 0
                current_source_well = 0

                
                if selected_option == '240':
                    selected_source_well_values = plate_well_values_240
                    target_well_values = plate_well_values_240.copy()
                elif selected_option == '308':
                    selected_source_well_values = plate_well_values_308
                    target_well_values = plate_well_values_308.copy()
                elif selected_option == '384':
                    selected_source_well_values = plate_well_values_384
                    target_well_values = plate_well_values_384.copy()

                if randomize:
                    random.shuffle(target_well_values)

                for i, (compound_name, volume, replicates) in enumerate(zip(data, volumes, replicates_per_compound)):
                    if compound_name:
                         #Get the source well
                        source_well = source_well_values[i]

                        

                        # Determine target wells based on the replicates
                        target_wells = [target_well_values[(source_well_index + j) % len(target_well_values)] for j in range(replicates)]

                        for target_well in target_wells:
                            writer.writerow([source_well, target_well, volume, compound_name])

                        current_source_well = (current_source_well + 1) % len(selected_source_well_values)
                        source_well_index = (source_well_index + replicates) % len(target_well_values)

                        

def write_csv_with_replicates(data, volumes, replicates_per_compound, save_path, selected_option):
    # Create a list of rows for the CSV, with compound names in column B, well positions in column A, volumes in column D, and dictionary option in column C
    csv_data = [['Source Well', 'Target Well', 'Volume [uL]', 'Liquid Name']]
    source_well_index = 0  # Initialize the source well index

    for i, (compound_name, volume, replicates) in enumerate(zip(data, volumes, replicates_per_compound)):
        if compound_name:
            # Get the source well
            source_well = source_well_values[i]

            selected_source_well_values = None
            if selected_option == '240':
                selected_source_well_values = plate_well_values_240
            elif selected_option == '308':
                selected_source_well_values = plate_well_values_308
            elif selected_option == '384':
                selected_source_well_values = plate_well_values_384

            for j in range(replicates):
                target_well = [selected_source_well_values[(source_well_index + j) % len(selected_source_well_values)]]
                csv_data.append([source_well, target_well, volume, compound_name])


            # Determine target wells based on the replicates
                
            source_well_index = (source_well_index + replicates) % len(selected_source_well_values)
                

    with open(save_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)

# Create the main window
root=ThemedTk(theme='adapta')
root.title("iDot ProtoBuilder")

root.geometry("800x500")

scrollbar = ttk.Scrollbar(root, orient='vertical')
scrollbar.pack(side="right", fill="y")
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)



#create frame to hold the widgets
scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0,0), window=scrollable_frame, anchor="nw")



scrollbar.config(command=canvas.yview)
canvas.yview_moveto(0)




def _on_mousewheel(event):
    canvas.yview_scroll(int(-1**(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Function to update the Canvas scroll region when the frame inside it changes
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", lambda event, canvas=canvas: on_frame_configure(canvas))


#make app responsive
for index in [0, 1, 2]:
    canvas.columnconfigure(index=index, weight=1)
    canvas.rowconfigure(index=index, weight=1)

#create frame for compound selection
compounds_frame = ttk.LabelFrame(scrollable_frame, text='Compounds', padding=(10,10))
compounds_frame.grid(row=1,column=0,padx=(10, 10), pady=(10,10), sticky="nsew")

# Dropdown menu to select a number
selected_number_var = tk.StringVar()
selected_number_label = ttk.Label(compounds_frame, text="Select a number of Compounds:")
selected_number_label.grid(padx=5, pady=10, sticky="nsew")
selected_number_dropdown = ttk.OptionMenu(compounds_frame, selected_number_var, *range(1, 97))
selected_number_dropdown.grid(padx=10, pady=10, sticky="nsew")


#create frame for source plate type
source_type_frame = ttk.LabelFrame(scrollable_frame, text='Source Plate Type', padding=(10,10))
source_type_frame.grid(row=1, column=1, padx=(10,10), pady=(10, 10), sticky="nsew")

#dropdown menu for selecting source plate type
selected_source_var = tk.StringVar()
selected_source_plate_type_label = ttk.Label(source_type_frame, text="Source Plate Type: ")
selected_source_plate_type_label.grid(padx=10, pady=10)


selected_source_plate_type_dropdown = ttk.OptionMenu(source_type_frame, selected_source_var, '', 'S.100 Plate', 'S.200 Plate')
selected_source_plate_type_dropdown.grid(padx=10, pady=10)

#create frame for the well format options+randomization checkbox
well_format_frame = ttk.LabelFrame(scrollable_frame, text='Well Format', padding=(10,10))
well_format_frame.grid(row=1, column=2, padx=(10,10), pady=(10,10), sticky="ew")

# Frame to hold input boxes
input_frame = ttk.Frame(scrollable_frame, padding=(10,10))
input_frame.grid(row=2, column=(0), padx=(10,10), pady=(10,10), rowspan=6)


# Dropdown menu to select the dictionary option
option_var = tk.StringVar()
option_var.set('240')  # Set the default option to '240'
option_label = ttk.Label(well_format_frame, text="Select a Well Format Option:")
option_label.grid(padx=5, pady=10)


option_dropdown = ttk.OptionMenu(well_format_frame, option_var, '', '240', '308', '384', command=change_option)
option_dropdown.grid(padx=6, pady=10)

#create checkbox for randomizing
randomize_var = tk.IntVar()
randomize_label = ttk.Label(well_format_frame, text='Randomize')
randomize_label.grid()

randomize_checkbutton = ttk.Checkbutton(well_format_frame, variable=randomize_var)
randomize_checkbutton.grid(padx=6, pady=0)

# Button to create input boxes
create_button = ttk.Button(scrollable_frame, text="Create Input Boxes", command=create_input_boxes, state=tk.NORMAL)
create_button.grid(row=5, column=1, padx=10, pady=10, sticky='nsew')

#create button for compound + volume import
import_button = ttk.Button(scrollable_frame, text="Import", command=import_variable_csv, state=tk.DISABLED)
import_button.grid(row=5, column=2, padx=10, pady=10, sticky='nsew')

# "Next" button to go to replicates input window (disabled by default)
next_button = ttk.Button(scrollable_frame, text="Save", command=get_replicates, state=tk.DISABLED)
next_button.grid(row=6, column=7, padx=10, pady=10, sticky='nsew')

#sizegrip window adjuster
sizegrip = ttk.Sizegrip(scrollable_frame)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

#create "?" button for how to use and csv  formatting help
help_button = ttk.Button(scrollable_frame, text="?", command=get_help, state=tk.NORMAL)
help_button.grid(row=0, column=8, pady=(5,5), padx=(5,5), sticky='nw')


#size window and place middle
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_coordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
y_coordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
root.geometry("+{}+{}".format(x_coordinate, y_coordinate-20))

# Start the GUI main loop
root.mainloop()
