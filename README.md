# LSS-MRI-AISSLab-Dataset

**LSS MRI AISSLab Dataset** is a large-scale, IRB-approved sagittal lumbar spine MRI dataset designed for **foraminal stenosis detection, severity grading, and anatomical segmentation**.  
The dataset supports **explainable AI research** by combining **pixel-level anatomical segmentation** with **multi-level foraminal stenosis detection and grading**.

🔗 **Dataset DOI (Mendeley Data)**  
https://data.mendeley.com/datasets/rgb77xm3jf/1  

---

## 🖼️ Dataset Overview and Annotation Schema

![Overview of the LSS MRI AISSLab Dataset](figures/Picture4.png)

**Figure 1.** Overview of the LSS MRI AISSLab Dataset.  
From left to right:  
**(a)** Sagittal lumbar spine DICOM volumes illustrating left, middle, and right sagittal slices used for analysis.  
**(b)** Expert-annotated foraminal stenosis detection represented as bounding boxes for lumbar levels **L1–L2 through L5–S1** on both left (LFS) and right (RFS) sides, with severity grades *(0: Normal, 1: Mild, 2: Moderate, 3: Severe)*.  
**(c)** Pixel-level multi-class anatomical segmentation on the middle sagittal slice, including anterior region, posterior elements (Posterior A and Posterior B), vertebral bodies, intervertebral discs (IVDs), and sacrum.

---

### 📊 Dataset Summary

- **Patients:** 500  
- **MRI Modality:** Sagittal T2-weighted lumbar spine MRI  
- **Total slices:** ~8,500 sagittal slices  
- **Annotations:**
  - **2,979** foraminal stenosis bounding boxes
  - Left / Right laterality labels
  - Severity grading: *Normal, Mild, Moderate, Severe*
  - Pixel-level anatomical segmentation masks

---

## 🔄 End-to-End CAD Pipeline for Foraminal Stenosis Analysis

![End-to-end CAD pipeline](figures/Picture1.png)

**Figure 2.** End-to-end computer-aided diagnosis (CAD) pipeline for lumbar foraminal stenosis analysis using sagittal MRI.  
The workflow consists of five stages:  
**(1)** Data acquisition from 3D sagittal lumbar spine DICOM volumes;  
**(2)** Automated slice selection using a 3D CNN to identify the most informative sagittal slice along with its adjacent slices *(N−1, N, N+1)*;  
**(3)** AI-based region-of-interest (ROI) detection to localize neural foramina across lumbar levels *(L1–L2 to L5–S1)*;  
**(4)** ROI-based stenosis severity classification using a weighted fusion of a DeiT transformer and a custom CNN;  
**(5)** Final level-wise output of stenosis grades and confidence scores for both left and right sides.

---

## 🧠 Clinical Motivation

Lumbar foraminal stenosis is a major cause of radiculopathy and chronic lower back pain.  
Although MRI is the gold standard for diagnosis, interpretation remains **time-consuming**, **costly**, and **highly dependent on expert radiologists or neurosurgeons**.

This dataset enables:
- Explainable AI-assisted diagnosis
- Morphology-aware stenosis grading
- Measurement-based assessment using anatomical segmentation
- Development of end-to-end CAD systems for lumbar spine analysis

---

## 🧩 Dataset Components

### 1. Sagittal Foraminal Detection & Classification

- Bounding-box annotations on sagittal MRI slices  
- Lumbar levels: **L1–L2 to L5–S1**  
- Laterality: **Left (LFS) / Right (RFS)**  
- Severity encoding:
  - `0` → Normal  
  - `1` → Mild  
  - `2` → Moderate  
  - `3` → Severe  
- Annotation format: **PASCAL VOC (XML)**

---

### 2. Anatomical Segmentation Masks

Pixel-level segmentation masks are provided for the following anatomical structures:
- Vertebral bodies  
- Intervertebral discs (IVD)  
- Sacrum  
- Posterior A  
- Posterior B  
- Background (anterior region)

Segmentation masks were generated using a **human-in-the-loop AI annotation workflow** and validated by expert neurosurgeons to ensure anatomical accuracy and clinical reliability.

---

## 🧠 Foraminal Anatomy and Severity Grading Standard

![Lumbar foraminal anatomy and grading](figures/Picture2.png)

**Figure 3.** Lumbar neural foramen anatomy and foraminal stenosis grading on sagittal T2-weighted MRI.  
**(a)** Anatomical landmarks used for annotation, including superior pedicle *(sp)*, inferior pedicle *(ip)*, superior vertebral body *(sc)*, inferior vertebral body *(ic)*, intervertebral disc *(d)*, facet joint *(j)*, and neural foramen *(f)*.  
**(b)** Representative examples of the four stenosis grades: **Normal**, **Mild**, **Moderate**, and **Severe**, defined based on the degree of perineural fat compression surrounding the exiting nerve root.

---

## 📄 Annotation Format Example (PASCAL VOC)

![XML annotation example](figures/Picture3.png)

**Figure 4.** Example of sagittal foraminal stenosis annotation.  
The left panel shows bounding-box annotations for multiple lumbar levels on a sagittal MRI slice, while the right panel presents the corresponding **PASCAL VOC XML file**.  
Each annotation includes the lumbar level, anatomical laterality *(LFS/RFS)*, stenosis severity grade, and bounding-box coordinates.

---

## 🗂️ Dataset Organization

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
│   └── Masks/
│       ├── *.png
│       └── *.xml
│
├── Foramina_Detection/
│   ├── Images/
│   │   └── *.png
│   └── Annotations/
│       └── *.xml
│
├── figures/
│   ├── Picture1.png
│   ├── Picture2.png
│   ├── Picture3.png
│   └── Picture4.png
│
├── models/
├── de_identification.py
└── README.md
