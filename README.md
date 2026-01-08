# LSS-MRI-AISSLab Dataset

**LSS-MRI-AISSLab Dataset** is a large-scale, IRB-approved sagittal lumbar spine MRI dataset designed for lumbar foraminal stenosis detection, severity grading, and anatomical segmentation.

The dataset is specifically developed to support explainable and clinically meaningful AI research by combining pixel-level anatomical segmentation with multi-level, bilateral foraminal stenosis detection and grading across the lumbar spine.

**Dataset DOI (Mendeley Data):**  
https://data.mendeley.com/datasets/rgb77xm3jf/3

---

## Foraminal Anatomy and Severity Grading Standard

![Lumbar foraminal anatomy and grading](figures/Picture2.png)

**Figure 1.** Lumbar neural foramen anatomy and foraminal stenosis grading on sagittal T2-weighted MRI.  
(a) Anatomical landmarks used for expert annotation: superior pedicle (sp), inferior pedicle (ip), superior vertebral body (sc), inferior vertebral body (ic), intervertebral disc (d), facet joint (j), and neural foramen (f).  
(b) Representative examples of foraminal stenosis severity grades: **Normal**, **Mild**, **Moderate**, and **Severe**, defined according to the degree of perineural fat compression surrounding the exiting nerve root.

---

## Dataset Overview

![Overview of the LSS MRI AISSLab Dataset](figures/Picture4.png)

**Figure 2.** Overview of the LSS-MRI-AISSLab Dataset. Sagittal lumbar spine DICOM volumes illustrating left, middle, and right sagittal slices used for analysis.  
(a) Expert-annotated foraminal stenosis detection using bounding boxes for lumbar levels **L1–L2 through L5–S1**, on both **left (LFS)** and **right (RFS)** sides, with severity grades (0: Normal, 1: Mild, 2: Moderate, 3: Severe).  
(b) Pixel-level multi-class anatomical segmentation on the middle sagittal slice, including vertebral bodies, intervertebral discs (IVDs), sacrum, posterior elements (Posterior A and Posterior B), and background regions.

---

## Dataset Summary

- **Number of patients:** 500  
- **Imaging modality:** Sagittal T2-weighted lumbar spine MRI  
- **Total slices:** ~8,500 sagittal MRI slices  
- **Annotations include:**
  - 2,979 foraminal stenosis bounding boxes  
  - Left / Right laterality labels  
  - Four-level severity grading (Normal, Mild, Moderate, Severe)  
  - Pixel-level anatomical segmentation masks  

---

## Dataset Components

### 1. Sagittal Foraminal Detection and Severity Classification

- Bounding-box annotations on sagittal MRI slices  
- Lumbar levels: **L1–L2 to L5–S1**  
- Laterality: **Left (LFS)** and **Right (RFS)**  
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
- Intervertebral discs (IVDs)  
- Sacrum  
- Posterior A  
- Posterior B  
- Background / anterior region  

Segmentation masks were generated using a **human-in-the-loop AI annotation workflow** and validated by expert neurosurgeons to ensure anatomical accuracy and clinical reliability.

---

## Citation

If you use this dataset or the associated code, please cite:

```bibtex
@inproceedings{Salem2025AutoSpineAI,
  title     = {AutoSpineAI: Lightweight Multimodal CAD Framework for Lumbar Spine MRI Assessments},
  author    = {Salem, Saied and Habib, Afnan and Raza, Mukhlis and Al-Huda, Zaid and
               Al-maqtari, Omar and Ertu{\u{g}}rul, Bilal and Y{\i}ld{\i}r{\i}m, {\"O}zal and
               Gu, Yeong Hyeon and Al-Antari, Mugahed A.},
  booktitle = {Proceedings of the IEEE-EMBS International Conference on Biomedical and Health Informatics (BHI)},
  year      = {2025},
  organization = {IEEE}
}

@article{AlAntari2025AISystematicReview,
  title   = {Evaluating AI-powered predictive solutions for MRI in lumbar spinal stenosis: a systematic review},
  author  = {Al-Antari, Mugahed A. and Salem, Saied and Raza, Mukhlis and Elbadawy, Ahmed S. and
             B{\"u}t{\"u}n, Ertan and Aydin, Ahmet Arif and Aydo{\u{g}}an, Murat and
             Ertu{\u{g}}rul, Bilal and Talo, Muhammed and Gu, Yeong Hyeon},
  journal = {Artificial Intelligence Review},
  volume  = {58},
  number  = {8},
  pages   = {221},
  year    = {2025},
  publisher = {Springer}
}
