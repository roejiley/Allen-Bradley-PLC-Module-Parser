import csv
import os
import xml.etree.ElementTree as ET
from tkinter import filedialog
import tkinter as tk

# Joseph Riley
# AE Specialty Region Systems Engineer
# Created on 20210719
# rev 1.0

# Hide TKinter UI
root = tk.Tk()
root.withdraw()

# Start file picker at location of script
root_dir = os.path.dirname(__file__)

# Find all L5X files in local dir plus all subdirs
file_paths = []
for root, dirs, files in os.walk(root_dir):
    for filename in files:
        if filename.endswith('.L5X'):
            file_paths.append(os.path.join(root, filename))
with filedialog.asksaveasfile(defaultextension='.csv', initialdir=root_dir, title='Save As',
                              initialfile="PLC_Modules.csv",
                              filetypes=(("CSV file", "*.csv"), ("All Files", "*.*"))) as f:
    save_as_path = f.name

# Set variables
fields = ['Name', 'CatalogNumber', 'Vendor', 'ProductType', 'ProductCode', 'Major', 'Minor', 'SafetyEnabled']
output_data = []

# Read XML files
for fp in file_paths:
    with open(fp, 'r', encoding='utf-8') as f:
        file_data = f.read()
    root = ET.fromstring(file_data)
    # Find modules in L5X
    for module in root.iter('Module'):
        row = []
        for field in fields:
            try:
                row.append(module.get(field))
            except:
                row.append(None)
        for tn in root.iter('RSLogix5000Content'):
            name = tn.get('TargetName')
            try:
                row.append(name)
                row.append(os.path.basename(fp))
            except:
                row.append(None)
        output_data.append(row)

# Write data to new CSV file
with open(save_as_path, 'w', newline='') as f:
    writer = csv.writer(f)
    header = fields + ['Connection', 'Source File']
    writer.writerow(header)
    writer.writerows(output_data)
