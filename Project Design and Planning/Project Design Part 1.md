# Project Design — Part 1

---

## 1. Functional Requirements

- Accepts blog topic input from user
- Allows user to enter relevant keywords
- Provides dropdown for tone selection (Informative, Friendly, Professional, Humorous)
- Includes slider to select desired word count
- Generates blog post using Google Gemini API based on user input
- Displays a random tech joke while generating the blog
- Handles empty or invalid input with error messages

---

## 2. Non-Functional Requirements

- Fast, responsive generation (<10 seconds)
- Intuitive, user-friendly UI
- Output should align with selected tone
- Secure handling of API keys via environment variables
- Lightweight and easily deployable (Streamlit-compatible)

---

## 3. Initial UI Sketch / Layout Plan

- Two-column layout for blog topic & keyword input
- Dropdown for tone + slider for word count
- Submit button triggers generation
- Loading spinner with tech joke during processing
- Output displayed below with styled container
- Footer with credits


---

## 5. Tools & Technologies

| Tool                | Role                                   |
|---------------------|----------------------------------------|
| Python              | Core logic and Streamlit backend       |
| Streamlit           | Web application interface              |
| google-generativeai | Blog generation via Gemini API         |
| dotenv              | Manage sensitive API credentials       |
| GitHub              | Version control and collaboration      |


