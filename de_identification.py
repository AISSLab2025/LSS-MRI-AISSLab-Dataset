import os
import pydicom

# Root folder containing patient folders
root_folder = r"D:\Dataset\DatasetV3.17 Dicom deidentify patient information(OSAMAH20251204)\DICOM"

# Tags to clear
tags_to_clear = [
    (0x0008, 0x0090),  # Referring Physician Name
    (0x0008, 0x0080),  # Institution Name
    (0x0008, 0x0081),  # Institution Address
    (0x0018, 0x1030),  # Protocol Name
    (0x0010, 0x21B0),  # Additional Patient History
    (0x0008, 0x1050),  # Performing Physician Name
    (0x0008, 0x1070),  # Operators Name
    (0x0010, 0x4000),  # Patient Comments
    (0x0040, 0x1400),  # Requested Procedure Comments
    (0x0040, 0x2400),  # Imaging Service Request Comments
    (0x0010, 0x2160),  # Ethnic Group
    (0x0040, 0x0006),  # Scheduled Performing Physician Name
    (0x0070, 0x0084),  # Content Creator Name
    (0x0008, 0x1010),  # Station Name
]

# Function to clean a single DICOM file
def clean_dicom(dicom_path):
    try:
        ds = pydicom.dcmread(dicom_path)
    except Exception as e:
        print(f"Error reading: {dicom_path} → {e}")
        return

    modified = False
    for group, element in tags_to_clear:
        tag = (group, element)
        if tag in ds:
            ds[tag].value = ""  # Clear value
            modified = True

    if modified:
        try:
            ds.save_as(dicom_path)
            print(f"Cleaned → {dicom_path}")
        except Exception as e:
            print(f"Error saving: {dicom_path} → {e}")

# ----------------------------------------------
# Process each patient folder (Axial & Sagittal)
# ----------------------------------------------
for patient_id in os.listdir(root_folder):
    patient_path = os.path.join(root_folder, patient_id)

    if not os.path.isdir(patient_path):
        continue

    # Look for Axial and Sagittal inside patient folder
    for sub_folder in ["Sagittal"]:
        sub_path = os.path.join(patient_path, sub_folder)

        if not os.path.isdir(sub_path):
            continue

        # Process all .dcm files inside this subfolder
        for file in os.listdir(sub_path):
            if file.lower().endswith(".dcm"):
                dicom_path = os.path.join(sub_path, file)
                clean_dicom(dicom_path)

print("Done! All DICOMs in Axial and Sagittal folders have been cleaned.")
