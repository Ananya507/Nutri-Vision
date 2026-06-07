
import streamlit as st
import pandas as pd
import requests
from PIL import Image
from transformers import pipeline

# =====================================
# CONFIGURATION
# =====================================

USDA_API_KEY = "lQN4rcNNEZGVcSuRYDpmnjhVg8nAmN3IXYUH8PBt"

CSV_FILE = "Food Ingredients and Recipe Dataset with Image Name Mapping.csv"

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Recipe Generator & Nutrition Analyzer",
    page_icon="🍽️",
    layout="wide"
)

# =====================================
# LOAD DATASET
# =====================================

@st.cache_data
def load_dataset():
    return pd.read_csv(CSV_FILE)

# =====================================
# LOAD FOOD CLASSIFIER
# =====================================

@st.cache_resource
def load_classifier():
    classifier = pipeline(
        "image-classification",
        model="vishnudas08/food101-vit-model"
    )
    return classifier

# =====================================
# FOOD PREDICTION
# =====================================

def predict_food(image):

    classifier = load_classifier()

    predictions = classifier(image)

    food_name = predictions[0]["label"]

    return food_name, predictions[:5]

# =====================================
# RECIPE SEARCH
# =====================================

def find_recipe(food_name, df):

    food_name = food_name.replace("_", " ").lower()

    matches = df[
        df["Title"].astype(str)
        .str.lower()
        .str.contains(food_name, na=False)
    ]

    if len(matches) == 0:
        return None

    return matches.iloc[0]

# =====================================
# USDA NUTRITION LOOKUP
# =====================================

def get_nutrition(food_name):

    try:

        url = (
            f"https://api.nal.usda.gov/fdc/v1/foods/search"
            f"?query={food_name}"
            f"&api_key={USDA_API_KEY}"
        )

        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        foods = data.get("foods", [])

        if len(foods) == 0:
            return None

        food = foods[0]

        nutrition = {
            "Calories": "N/A",
            "Protein": "N/A",
            "Fat": "N/A",
            "Carbohydrates": "N/A"
        }

        for item in food.get("foodNutrients", []):

            nutrient = item.get("nutrientName", "")
            value = item.get("value", "")

            if nutrient == "Energy":
                nutrition["Calories"] = value

            elif nutrient == "Protein":
                nutrition["Protein"] = value

            elif nutrient == "Total lipid (fat)":
                nutrition["Fat"] = value

            elif nutrient == "Carbohydrate, by difference":
                nutrition["Carbohydrates"] = value

        return nutrition

    except Exception:
        return None

# =====================================
# HEALTHIER ALTERNATIVES
# =====================================

def healthier_alternative(food):

    food = food.lower()

    alternatives = {
        "pizza": "Whole Wheat Veggie Pizza",
        "burger": "Grilled Chicken Burger",
        "fried rice": "Brown Rice Vegetable Bowl",
        "french fries": "Baked Sweet Potato Fries",
        "ice cream": "Greek Yogurt Parfait",
        "cake": "Banana Oat Cake",
        "donut": "Whole Wheat Muffin",
        "hot dog": "Grilled Chicken Wrap"
    }

    for key in alternatives:
        if key in food:
            return alternatives[key]

    return "Fresh Salad Bowl"

# =====================================
# MAIN APP
# =====================================

def main():

    st.title("🍽️ AI Recipe Generator & Nutrition Analyzer")

    st.write(
        "Upload a food image to identify the dish, "
        "retrieve a recipe, analyze nutrition, "
        "and receive healthier alternatives."
    )

    try:
        df = load_dataset()
    except Exception as e:
        st.error(f"Dataset loading failed: {e}")
        return

    uploaded_file = st.file_uploader(
        "Upload a food image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image")

        if st.button("Analyze Food"):

            with st.spinner("Identifying food..."):

                try:
                    food_name, predictions = predict_food(image)

                except Exception as e:
                    st.error(f"Prediction error: {e}")
                    return

            st.success("Food identified successfully!")

            st.subheader("Predicted Food")

            st.write(
                food_name.replace("_", " ").title()
            )

            st.subheader("Top Predictions")

            pred_df = pd.DataFrame(predictions)

            st.dataframe(pred_df)

            recipe = find_recipe(food_name, df)

            if recipe is not None:

                st.subheader("Recipe Name")

                st.write(recipe["Title"])

                st.subheader("Ingredients")

                st.write(recipe["Cleaned_Ingredients"])

                st.subheader("Instructions")

                st.write(recipe["Instructions"])

            else:

                st.warning(
                    "No matching recipe found in dataset."
                )

            st.subheader("Nutrition Analysis")

            nutrition = get_nutrition(food_name)

            if nutrition:

                c1, c2, c3, c4 = st.columns(4)

                c1.metric(
                    "Calories",
                    nutrition["Calories"]
                )

                c2.metric(
                    "Protein",
                    nutrition["Protein"]
                )

                c3.metric(
                    "Fat",
                    nutrition["Fat"]
                )

                c4.metric(
                    "Carbohydrates",
                    nutrition["Carbohydrates"]
                )

            else:

                st.warning(
                    "Nutrition information unavailable."
                )

            st.subheader("Healthier Alternative")

            st.success(
                healthier_alternative(food_name)
            )

# =====================================
# RUN APP
# =====================================

if __name__ == "__main__":
    main()

