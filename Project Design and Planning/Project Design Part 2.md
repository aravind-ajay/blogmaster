# Project Design — Part 2

---

## 1. System Architecture

**Model**: Client–API (no database or persistent backend)

   User Input<br>
        ↓<br>
  Prompt Builder<br>
        ↓<br>
 Gemini Flash API<br>
        ↓<br>
Blog Response + Joke Display<br>

---

## 2. Module Breakdown

| Module                | Description                                              |
|------------------------|----------------------------------------------------------|
| Input Handler          | Captures and validates topic, keywords, tone, word count |
| Prompt Generator       | Builds tone-specific prompts with target word count      |
| API Communicator       | Handles communication with Gemini Flash API             |
| Joke Engine            | Fetches a random tech joke from a preset list            |
| Output Renderer        | Displays blog and word count in styled format            |

---

## 3. Tone Configuration Design

Each tone maps to a distinct configuration for creativity:

| Tone         | Temperature | top_p | top_k | Max Tokens |
|--------------|-------------|-------|-------|------------|
| Informative  | 0.3         | 0.8   | 40    | 8192       |
| Professional | 0.4         | 0.85  | 50    | 8192       |
| Friendly     | 0.7         | 0.9   | 60    | 8192       |
| Humorous     | 0.9         | 0.95  | 64    | 8192       |

---

## 5. UI/UX Considerations

- Responsive layout for desktop users
- Form validation with error messages
- Humor added via rotating joke pool

---

## 6. Error Handling Strategy

| Scenario                  | Handling Method                              |
|---------------------------|-----------------------------------------------|
| Empty topic or keyword    | Show validation error before submit           |
| API timeout               | Display failure message and retry option      |
| No internet / key issue   | Fail-safe with user instructions              |

---

## 7. Extensibility Plan

- Export to `.docx` or `.pdf`
- Blog translation (multi-language support)
- Alternative LLMs

---

## 8. Final Outcome of Part 2

- Concrete architecture and tone logic finalized
- Ready to move into full-scale development & integration
- Ensured error safety and future scalability

