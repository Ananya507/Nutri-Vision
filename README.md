# Nutri-Vision
# 🍽️ Nutri-Vision: AI-Powered Recipe Generator & Nutrition Analyzer

## Overview

NutriGenAI is an AI-powered food recognition and nutrition analysis system that identifies food items from uploaded images, retrieves recipes, analyzes nutritional content using the USDA FoodData Central API, and recommends healthier alternatives.

The project combines Computer Vision, Deep Learning, API Integration, and Data Analytics to provide users with intelligent food insights and meal recommendations.

---

## Features

* 📸 Food Image Recognition using Vision Transformer (ViT) trained on Food-101
* 🍳 Automatic Recipe Retrieval
* 🥗 Nutrition Analysis using USDA FoodData Central API
* 💡 Healthier Food Alternative Recommendations
* 📊 Interactive Web Interface built with Streamlit
* 🔍 Top Prediction Confidence Scores

---

## Tech Stack

### Frontend

* Streamlit

### Machine Learning

* Hugging Face Transformers
* Vision Transformer (ViT)
* Food-101 Dataset

### Backend

* Python

### Data Processing

* Pandas
* Pillow

### API Integration

* USDA FoodData Central API

---

## Project Architecture

```text
User Uploads Food Image
            │
            ▼
Food Classification Model
            │
            ▼
Predicted Food Item
            │
            ├────────► Recipe Retrieval
            │
            ├────────► Nutrition Analysis
            │
            ▼
Healthier Alternative Recommendation
            │
            ▼
Results Displayed in Streamlit
```

---

## Dataset

The project utilizes a recipe dataset containing:

* Food Title
* Ingredients
* Cooking Instructions
* Image Mapping Information

Dataset Columns:

```text
Title
Cleaned_Ingredients
Instructions
Image_Name
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Nutri-Vision.git
cd Nutri-Vision
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure USDA API Key

Open `app.py` and replace:

```python
USDA_API_KEY = "YOUR_USDA_API_KEY"
```

with your actual API key.

---

## Run Application

```bash
streamlit run app.py
```

---

## Usage

1. Launch the Streamlit application.
2. Upload a food image.
3. Wait for food classification.
4. View:

   * Predicted food item
   * Recipe details
   * Ingredients
   * Cooking instructions
   * Nutritional information
   * Healthier alternatives

---

## Results

The system provides:

* Food Identification
* Recipe Recommendation
* Calorie Estimation
* Protein Analysis
* Fat Analysis
* Carbohydrate Analysis
* Healthy Food Suggestions

---

## Future Enhancements

* Personalized Diet Planning
* BMI-Based Recommendations
* Multi-Food Detection
* Calorie Tracking Dashboard
* Meal Planning System
* Voice-Based Food Search
* LLM-Based Recipe Generation
* Nutritional Deficiency Detection

---

## Skills Demonstrated

* Machine Learning
* Deep Learning
* Computer Vision
* Transfer Learning
* API Integration
* Data Analysis
* Streamlit Deployment
* Python Development

---

## Author

Ananya Majumdar

Final Year B.Tech Student | Artificial Intelligence & Machine Learning Enthusiast
