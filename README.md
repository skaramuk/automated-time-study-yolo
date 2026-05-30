# automated-time-study-yolo
# Automated Time Study Using YOLO-Based Computer Vision

## Project Overview

This project investigates the feasibility of using deep learning-based computer vision techniques for automated work study and cycle time measurement in manual packaging operations.

The study combines object detection, video analysis, and statistical hypothesis testing to evaluate whether computer vision can support traditional time study practices and to examine the presence of the Hawthorne Effect under different observation conditions.

---

## Research Objectives

- Automate cycle time measurement using computer vision.
- Compare manual stopwatch measurements with automated measurements.
- Evaluate the reliability of YOLO-based cycle time estimation.
- Investigate the Hawthorne Effect by comparing observed and unobserved working conditions.
- Validate findings through statistical hypothesis testing.

---

## Methodology

### Phase 1 – Observed Condition

The operator was aware of being observed.

- Manual cycle times were collected using a stopwatch.
- The same process was recorded on video.
- YOLOv8 was used to detect completed packages.
- Cycle times extracted from video were compared with manual measurements.

### Phase 2 – Unobserved Condition

The operator was not informed about the exact observation period.

- Cycle times were obtained through video analysis.
- Results were compared with Phase 1 measurements.
- Behavioral differences were evaluated to investigate the Hawthorne Effect.

---

## System Workflow

<p align="center">
  <img src="workflow.png" width="800">
</p>

---

## Technologies Used

- Python
- YOLOv8
- OpenCV
- NumPy
- Pandas
- SciPy
- R
- Matplotlib

---

## Repository Structure

```text
.
├── README.md
├── requirements.txt
│
├── src
│   ├── roi_cycle_counter.py
│   ├── faz2_cycle_counter.py
│   └── time_study.py
│
└── results
    ├── boxplot.png
    ├── bland_altman.png
    ├── phase1_ttest.png
    ├── phase2_ttest.png
    └── cohens_d.png
```

---

## Statistical Analysis

The following statistical methods were used:

- Paired Sample t-Test
- Independent Samples t-Test
- Cohen's d Effect Size
- Bland–Altman Analysis

These analyses were performed to assess measurement agreement and evaluate behavioral changes between experimental conditions.

---

## Results

### Phase 1: Manual vs Computer Vision

The statistical analysis indicated no significant difference between manual measurements and computer vision-based measurements, supporting the feasibility of automated cycle time estimation.

### Phase 2: Observed vs Unobserved

The comparison revealed behavioral differences between observation conditions, providing evidence consistent with the Hawthorne Effect.

---

## Example Detection Output

<p align="center">
  <img src="results/prediction_frame.png" width="800">
</p>

---

## Future Work

- Multi-object tracking integration
- Real-time cycle monitoring systems
- Higher resolution video acquisition
- Deployment in industrial environments
- Extension to different work-study applications

---

## Author

**Semih Karamuk**

Industrial Engineering Student

Computer Vision • Deep Learning • Data Analysis
