#Importing Requirements
import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to get tone-specific configuration``
def get_tone_config(tone):
    """Return model configuration based on selected tone"""
    tone_configs = {
        "Informative": {
            "temperature": 0.3,  # Lower temperature for more factual, consistent content
            "top_p": 0.8,
            "top_k": 40,
            "max_output_tokens": 8192
        },
        "Professional": {
            "temperature": 0.4,  # Balanced for formal but not rigid content
            "top_p": 0.85,
            "top_k": 50,
            "max_output_tokens": 8192
        },
        "Friendly": {
            "temperature": 0.7,  # Higher creativity for conversational tone
            "top_p": 0.9,
            "top_k": 60,
            "max_output_tokens": 8192
        },
        "Humorous": {
            "temperature": 0.9,  # Highest creativity for jokes and fun content
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192
        }
    }
    
    return genai.GenerationConfig(**tone_configs[tone])


# Joke-List
jokes = [
    "Why don't programmers like nature? It has too many bugs.",
    "Why do Java developers wear glasses? Because they don't C#.",
    "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
    "Why do Python programmers prefer snake_case? Because it's easier to read!",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "Why did the developer go broke? Because he used up all his cache.",
    "Why do programmers mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
    "Why did the computer get cold? It left its Windows open.",
    "Why was the developer unhappy at their job? They wanted arrays.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "There are only 10 kinds of people in the world: those who understand binary and those who don't.",
    "Why do programmers hate writing documentation? Because they'd rather commit than explain.",
    "Why was the function so clingy? Because it had closure issues.",
    "What did the bit say to the byte? 'I'm feeling a little off today.'",
    "What do you call a programmer from Finland? Nerdic.",
    "Why did the loop break up with the function? Too many arguments.",
    "Why was the C++ developer drowning? He couldn't handle exceptions.",
    "What's a programmer's favorite hangout place? The Foo Bar.",
    "Why was the code so bloated? Because it had too many dependencies.",
    "Why was the variable so moody? It kept changing values.",
    "How do you comfort a JavaScript bug? You console it.",
    "Why don't Python programmers need glasses? Because they have clear syntax.",
    "Why are Assembly programmers always soaking wet? Because they work below C-level.",
    "I told my computer I needed a break, and now it won't stop sending me coffee ads.",
    "Why can't computers take their hats off? Because they have CAPS LOCK on.",
    "Why did the Boolean get dumped? Because it couldn't commit.",
    "Why don't robots have brothers? Because they all share the same motherboard.",
    "Why did the software developer go broke? Because he lost his domain in a bet."
]

# Joke GET Function for displaying during blog generation
def get_joke():
    return random.choice(jokes)

# Enhanced blog generation function with tone-specific prompts and word count
def generate_blog(topic: str, keywords: str, tone: str, word_count: int):
    try:
        # Display spinner and joke
        st.write("✍ Generating your blog... Please wait!")
        joke = get_joke()
        st.info(f"💡 While you wait, here's a tech joke:\n\n*{joke}*")

        # Get tone-specific configuration
        tone_config = get_tone_config(tone)
        
        # Initialize model with tone-specific config
        model = genai.GenerativeModel(
            model_name="models/gemini-1.5-flash",
            generation_config=tone_config
        )

        # Create tone-specific prompts with word count
        tone_prompts = {
            "Informative": f"""Write a comprehensive, well-researched blog post about '{topic}' in approximately {word_count} words. 
                            Focus on providing accurate information, data, and insights. 
                            Include the following keywords naturally: {keywords}.
                            Structure the content with clear headings and maintain an educational tone throughout.
                            Ensure the final output is close to {word_count} words while maintaining quality and completeness.""",
            
            "Professional": f"""Create a professional blog post about '{topic}' in approximately {word_count} words, suitable for a business audience.
                            Use formal language while remaining accessible and engaging.
                            Incorporate these keywords strategically: {keywords}.
                            Include industry insights and maintain a polished, authoritative tone.
                            Target exactly {word_count} words while ensuring comprehensive coverage of the topic.""",
            
            "Friendly": f"""Write a warm, conversational blog post about '{topic}' in approximately {word_count} words, as if talking to a friend.
                            Use a casual, approachable tone with personal touches and relatable examples.
                            Naturally weave in these keywords: {keywords}.
                            Make it engaging and easy to read with a welcoming personality.
                            Aim for {word_count} words while keeping the friendly, conversational flow.""",
            
            "Humorous": f"""Create an entertaining and witty blog post about '{topic}' in approximately {word_count} words that makes readers smile.
                            Use humor, jokes, and playful language while still being informative.
                            Include these keywords in creative ways: {keywords}.
                            Balance fun content with useful information, and don't be afraid to be quirky!
                            Target {word_count} words while maintaining the humor and entertainment value."""
        }

        # Start chat and send tone-specific prompt
        chat_session = model.start_chat()
        response = chat_session.send_message(tone_prompts[tone])

        st.success("✅ Blog successfully generated!")
        return response.text.strip()

    except Exception as e:
        st.error(f"❌ Failed to generate blog: {e}")
        return None

# Main app UI
def main():
    st.set_page_config(page_title="BlogMaster ✍️", layout="wide")

    #Background Color
    st.markdown("""
        <style>
            body {
            background-color: #8a83a6;
            }
        </style>
    """, unsafe_allow_html=True)
        
    # Header Section
    st.markdown("""
        <h1 style='text-align: center; color: #4A66FF;'> BlogMaster: Powered by Gemini Flash</h1>
        <p style='text-align: center; font-size: 18px;'>Create engaging, structured blog posts — with a smile while you wait!</p>
        <hr style="border-top: 1px solid #bbb;">
    """, unsafe_allow_html=True)

    st.header("📝 Generate a Blog Post")

    # Show tone configuration info
    with st.expander("ℹ️ How Tones Affect Generation"):
        st.markdown("""
        **Informative**: Lower creativity, more factual and consistent content
        
        **Professional**: Balanced approach, formal but engaging
        
        **Friendly**: Higher creativity for conversational, warm content
        
        **Humorous**: Maximum creativity for entertaining, witty content
        
        """)


    # Input Form
    with st.form("blog_form"):
        col1, col2 = st.columns(2)
        with col1:
            topic = st.text_input("💡 Blog Topic", placeholder="e.g., Future of AI in Education")
        with col2:
            keywords = st.text_input("🔑 Keywords", placeholder="e.g., AI, edtech, learning")

        col3, col4 = st.columns(2)
        with col3:
            tone = st.selectbox("🎛️ Choose Tone", ["Informative", "Friendly", "Professional", "Humorous"])
        with col4:
            word_count = st.slider("📊 Word Count", min_value=300, max_value=2000, value=1000, step=50)
        
        submitted = st.form_submit_button("🚀 Generate Blog")

    if submitted:
        if topic and keywords:
            with st.spinner("💭 Thinking deeply... Generating content..."):
                blog = generate_blog(topic, keywords, tone, word_count)

            if blog:
                st.subheader(f"📃Your Blog Post ")
                st.markdown(f"<div style='background-color: #7587eb; padding: 15px; border-radius: 10px;'>{blog}</div>", unsafe_allow_html=True)
                
                # Display approximate word count
                actual_word_count = len(blog.split())
                st.info(f" Approximate word count: {actual_word_count} words")
            else:
                st.error("!!! Something went wrong while generating the blog.")
        else:
            st.error("🚫 Please enter both a topic and some keywords.")


    # Footer with fun vibe
    st.markdown("""
        <hr>
        <p style='text-align: center; font-size: 14px; color: gray;'>Made with ❤️ using Gemini Flash</p>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()