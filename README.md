
# LSS-MRI-AISSLab-Dataset

**LSS MRI AISSLab Dataset** is a large-scale, IRB-approved sagittal lumbar spine MRI dataset designed for **foraminal stenosis detection, severity grading, and anatomical segmentation**.  
The dataset supports explainable AI research by combining **pixel-level anatomical segmentation** with **multi-level foraminal stenosis detection and grading**.



🔗 **Dataset DOI (Mendeley Data)**  
https://data.mendeley.com/datasets/rgb77xm3jf/1  



---

## 📌 Dataset Overview

- **Patients:** 500
- **MRI Type:** Sagittal T2-weighted lumbar spine MRI
- **Slices:** ~8,500 sagittal slices
- **Annotations:**
  - 2,979  foraminal stenosis bounding boxes
  - Left / Right labeling
  - Severity grading: Normal, Mild, Moderate, Severe
  - Pixel-level anatomical segmentation masks

---

## 🧠 Clinical Motivation

Lumbar Foraminal Stenosis is a major cause of radiculopathy and lower back pain.  
While MRI is the gold standard for diagnosis, interpretation is **time-consuming** and **expert-dependent**.

This dataset enables:
- Explainable AI diagnosis
- Morphology-aware stenosis grading
- Measurement-based assessment using segmentation

---

## 🧩 Dataset Components

### 1. Sagittal Foraminal Detection & Classification
- Bounding-box annotations on sagittal slices
- Levels: **L1–L2 to L5–S1**
- Laterality: **Left (LFS) / Right (RFS)**
- Severity:
  - 0 → Normal
  - 1 → Mild
  - 2 → Moderate
  - 3 → Severe
- Format: **PASCAL VOC XML**

### 2. Anatomical Segmentation Masks
Pixel-level masks for:
- Vertebral bodies
- Intervertebral discs (IVD)
- Sacrum
- Posterior A
- Posterior B
- Background

Generated via **human-in-the-loop AI annotation**, validated by expert neurosurgeons.

---

## 🗂️ Directory Structure

```text
LSS-MRI-AISSLab-Dataset/
│
├── DICOM/
│   └── Patient_ID/
│       └── *.dcm
│
├── Segmentation/
│   ├── Middle_Slice/
│   │   └── *.png
│   ├── Masks/
│   │   ├── *.png
│   │   └── *.xml
│
├── Foramina_Detection/
│   ├── Images/
│   │   └── *.png
│   └── Annotations/
│       └── *.xml
│
├── models/
├── de_identification.py
└── README.md
