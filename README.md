# 🍽️ AI Recipe Generator & Nutrition Analyzer

An AI-powered food recognition and nutrition analysis application that identifies food items from uploaded images, retrieves matching recipes, provides nutritional information, and suggests healthier food alternatives.

## 📌 Overview

The AI Recipe Generator & Nutrition Analyzer combines computer vision, machine learning, and external API integration to make food exploration easier.

Users can upload an image of a food item, and the application uses a pretrained image classification model to identify the dish. Based on the prediction, it searches a recipe dataset, retrieves nutritional information from the USDA FoodData Central API, and recommends a healthier alternative.

## ✨ Features

- **Food Image Recognition:** Identifies food items from uploaded images using a pretrained Vision Transformer (ViT)-based image classification model.
- **Top-5 Predictions:** Displays the five most probable food classifications with their prediction scores.
- **Recipe Retrieval:** Searches a recipe dataset to retrieve matching recipes, ingredients, and cooking instructions.
- **Nutrition Analysis:** Retrieves calorie, protein, fat, and carbohydrate information through the USDA FoodData Central API.
- **Healthier Alternatives:** Suggests alternative food options using a rule-based recommendation system.
- **Interactive Interface:** Provides an easy-to-use interface built with Streamlit.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Hugging Face Transformers | Pretrained image classification pipeline |
| Vision Transformer (ViT) | Food image classification |
| Pandas | Dataset loading and processing |
| Pillow (PIL) | Image processing |
| Requests | REST API integration |
| USDA FoodData Central API | Nutritional information |
| CSV Dataset | Recipe storage and retrieval |

## ⚙️ How It Works

1. The user uploads a food image.
2. The image is processed and passed to the pretrained food classification model.
3. The model predicts the food category and returns the top five predictions.
4. The application searches the recipe dataset for a matching dish.
5. The USDA API is queried to retrieve nutritional information.
6. A rule-based recommendation function suggests a healthier alternative.
7. Results are displayed through the Streamlit interface.

## 📂 Project Structure

```text
AI-Recipe-Analyzer/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
└── Food Ingredients and Recipe Dataset with Image Name Mapping.csv
```

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AI-Recipe-Analyzer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows:
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the USDA API key

Create a `.env` file or configure an environment variable:

```text
USDA_API_KEY=your_api_key_here
```

Read the key securely in Python using an environment variable.

### 5. Run the application

```bash
streamlit run app.py
```

## 🔮 Future Improvements

- Improve recipe matching using semantic search.
- Add serving-size-based nutritional calculations.
- Introduce personalized dietary preferences.
- Generate customized recipes based on available ingredients.
- Add user accounts and recipe bookmarking.
- Deploy the application for public access.

## 👩‍💻 Author

Developed as a machine learning and Python application integrating computer vision, dataset processing, and external nutritional data retrieval. & Machine Learning Enthusiast
