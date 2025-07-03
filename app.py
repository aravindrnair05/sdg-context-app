import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
import json

# Sample SDG data (expand to all 17 SDGs + targets + indicators)
sdg_data = [
    {
        "sdg_no": 2,
        "title": "Zero Hunger",
        "content": "End hunger, achieve food security, improve nutrition and promote sustainable agriculture.",
        "targets": [
            {"target_no": "2.1", "description": "By 2030, end hunger and ensure access to safe, nutritious and sufficient food all year round."},
            {"target_no": "2.2", "description": "By 2030, end all forms of malnutrition."}
        ],
        "indicators": [
            {"indicator_no": "2.1.1", "description": "Prevalence of undernourishment"},
            {"indicator_no": "2.2.1", "description": "Prevalence of stunting among children under 5"}
        ]
    },
    {
        "sdg_no": 3,
        "title": "Good Health and Well-being",
        "content": "Ensure healthy lives and promote well-being for all at all ages.",
        "targets": [
            {"target_no": "3.1", "description": "Reduce global maternal mortality."}
        ],
        "indicators": [
            {"indicator_no": "3.1.1", "description": "Maternal mortality ratio"}
        ]
    },
    # Add more SDGs here...
]

# Prepare texts and metadata
def prepare_sdg_texts(sdg_data):
    texts = []
    meta = []
    for sdg in sdg_data:
        texts.append(f"SDG {sdg['sdg_no']} {sdg['title']} {sdg['content']}")
        meta.append({"level": "goal", "sdg_no": sdg["sdg_no"], "title": sdg["title"]})

        for target in sdg.get("targets", []):
            texts.append(f"SDG {sdg['sdg_no']} Target {target['target_no']} {target['description']}")
            meta.append({"level": "target", "sdg_no": sdg["sdg_no"], "target_no": target["target_no"]})

        for indicator in sdg.get("indicators", []):
            texts.append(f"SDG {sdg['sdg_no']} Indicator {indicator['indicator_no']} {indicator['description']}")
            meta.append({"level": "indicator", "sdg_no": sdg["sdg_no"], "indicator_no": indicator["indicator_no"]})

    return texts, meta

# Load model
@st.cache_resource
def load_model():
    return SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

# Embed SDG data
@st.cache_resource
def compute_sdg_embeddings(texts, model):
    return model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)

# Main app
st.title("🌱 SDG Context Analysis Tool")
st.write("Analyze your text against SDG goals, targets, and indicators.")

query = st.text_area("Enter your text:", height=150)
top_n = st.slider("Number of top matches", 1, 10, 3)
threshold = st.slider("Minimum similarity threshold", 0.0, 1.0, 0.5, 0.01)

if query and st.button("Analyze"):
    with st.spinner("Processing..."):
        model = load_model()
        texts, meta = prepare_sdg_texts(sdg_data)
        sdg_embeddings = compute_sdg_embeddings(texts, model)
        query_emb = model.encode(query, convert_to_numpy=True, normalize_embeddings=True)

        similarities = np.dot(sdg_embeddings, query_emb)
        sorted_idx = np.argsort(similarities)[::-1]
        
        results = []
        for idx in sorted_idx[:top_n]:
            if similarities[idx] < threshold:
                continue
            entry = meta[idx].copy()
            entry["text"] = texts[idx]
            entry["similarity"] = round(float(similarities[idx]), 3)
            results.append(entry)

    if results:
        st.success("Analysis complete!")
        for r in results:
            st.markdown(f"**{r['level'].capitalize()}**: SDG {r['sdg_no']}" +
                        (f" Target {r.get('target_no')}" if r['level'] == "target" else "") +
                        (f" Indicator {r.get('indicator_no')}" if r['level'] == "indicator" else "") +
                        f" — *{r.get('title', '')}*")
            st.markdown(f"Similarity: `{r['similarity']}`")
            st.markdown(f"Text: {r['text']}")
            st.markdown("---")
        
        # Export options
        df = pd.DataFrame(results)
        st.download_button("Download CSV", df.to_csv(index=False).encode('utf-8'), file_name="sdg_results.csv")
        st.download_button("Download JSON", json.dumps(results, indent=2).encode('utf-8'), file_name="sdg_results.json")
    else:
        st.warning("No matches above the threshold found.")

