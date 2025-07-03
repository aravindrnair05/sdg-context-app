# SDG Context Analysis App

The **SDG Context Analysis App** is a **Streamlit-based web tool** that analyzes user-provided text for its relevance to the **United Nations Sustainable Development Goals (SDGs)**, including associated targets and indicators. It uses **SentenceTransformer’s `all-mpnet-base-v2` model** to compute semantic similarity, providing ranked matches to help align projects, policies, or research with SDG priorities.

---

## ✨ Features

- **Text Analysis:** Match input text to SDGs, targets, and indicators using semantic similarity.
- **Interactive UI:** User-friendly Streamlit interface for seamless interaction.
- **Custom Parameters:** Adjust `Top N Results` (1–20) and `Similarity Threshold` (0.0–1.0) via sliders.
- **Visualization:** Bar chart displaying similarity scores for top matches.
- **Export:** Download results as CSV or JSON files.
- **Robust Error Handling:** Input validation and reliable processing of data.

---

## 🚀 Usage

1️⃣ **Enter Text:** Provide your text (e.g., a project description or policy statement) in the text area.

2️⃣ **Set Parameters:**  
   - Use the **Top N Results** slider to select the number of matches to display (1–20).  
   - Set the **Similarity Threshold** slider to filter matches by similarity score (0.0–1.0).

3️⃣ **Analyze:** Click the **Analyze** button to compute matches.

4️⃣ **View Results:** Review top matching SDGs, targets, and indicators with their similarity scores and details.

5️⃣ **Visualize:** Explore a bar chart showing similarity scores for top matches.

6️⃣ **Export:** Download results as CSV or JSON using the provided buttons.

---

## 📝 Example

**Input:**  
> We aim to provide clean drinking water to rural communities to improve health outcomes.

**Sample Output:**  
- SDG 6 Indicator 6.1.32: Safe drinking water access (Similarity: 0.85)  
- SDG 6 Indicator 6.1.47: Improving water access (Similarity: 0.78)  
- SDG 3 Indicator 3.1.25: Ensuring healthy lives (Similarity: 0.75)

---

## 📂 File Structure

- `app.py`: The main application script containing the Streamlit app and SDG dataset.
- `requirements.txt`: Lists the required Python packages for deployment.
- `README.md`: This documentation file.

---

## 🛠 Dependencies

The app depends on the following Python packages:
- `streamlit`: Powers the interactive web interface.
- `sentence-transformers`: Computes text embeddings using the `all-mpnet-base-v2` model.
- `numpy`: Handles numerical computations.
- `pandas`: Manages data manipulation and export.

---

## 🌐 Deployment

To deploy the app on Streamlit Cloud or similar platforms:
1. Push the repository to GitHub.
2. Create a `requirements.txt` file with the following content:
   ```text
   streamlit
   sentence-transformers
   numpy
   pandas

Deploy via Streamlit Cloud:

Log in to Streamlit Cloud.

Connect your GitHub repository.

Specify app.py as the main script and ensure Python version compatibility (e.g., 3.8+).

Monitor deployment logs to troubleshoot any issues.



⚠️ Limitations

Data Accuracy: The sdg_data dataset includes some non-standard indicators that may not align with the official UN SDG framework. Consider updating with official UN SDG metadata for production use.

Performance: Embedding large datasets may be slow, though batch processing helps mitigate this.

Model Dependency: Requires internet access to download the all-mpnet-base-v2 model on first run.

🔮 Future Improvements

Align sdg_data with official UN SDG indicators and targets.

Support uploading custom SDG datasets (e.g., CSV or JSON files).

Enhance visualizations with interactive charts, such as grouping by SDG.

Implement additional caching for faster query processing.

Add multilingual support using multilingual SentenceTransformer models.

🤝 Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a feature branch (git checkout -b feature/your-feature).

Commit your changes (git commit -m "Add your feature").

Push to the branch (git push origin feature/your-feature).

Open a pull request.

Please ensure code adheres to PEP 8 style guidelines and includes relevant tests.

📜 License

This project is licensed under the MIT License. See the LICENSE file for details.
