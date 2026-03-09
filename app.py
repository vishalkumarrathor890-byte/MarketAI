import streamlit as st

st.set_page_config(page_title="MarketAI", page_icon="🚀")

st.title("🚀 MarketAI")
st.write("AI Tool for Business Ideas and Market Trends")

menu = st.sidebar.selectbox(
    "Choose Feature",
    ["Home", "Idea Generator", "Trend Analyzer", "AI Assistant"]
)

# HOME
if menu == "Home":

    st.header("Welcome to MarketAI")

    st.write("This tool helps you generate startup ideas and analyze market demand.")

    st.info("Use the sidebar to explore features.")

# IDEA GENERATOR
elif menu == "Idea Generator":

    st.header("💡 Business Idea Generator")

    niche = st.text_input("Enter niche (AI, fitness, food)")

    if st.button("Generate Idea"):

        if niche.lower() == "ai":
            st.success("AI Resume Builder for students")
            st.write("Target: College students")
            st.write("Revenue Model: Subscription")

        elif niche.lower() == "fitness":
            st.success("Online Fitness Coaching App")
            st.write("Target: Busy professionals")
            st.write("Revenue Model: Monthly membership")

        elif niche.lower() == "food":
            st.success("Healthy Meal Delivery Startup")
            st.write("Target: Gym lovers")
            st.write("Revenue Model: Weekly plan")

        else:
            st.warning("Try niches like AI, fitness or food")

# TREND ANALYZER
elif menu == "Trend Analyzer":

    st.header("📈 Market Trend Analyzer")

    keyword = st.text_input("Enter keyword")

    if st.button("Analyze Trend"):

        if "ai" in keyword.lower():

            st.success("🔥 High Demand Trend")

            score = 9

        elif "fitness" in keyword.lower():

            st.info("📊 Medium Demand")

            score = 6

        elif "food" in keyword.lower():

            st.info("Stable Demand")

            score = 5

        else:

            st.warning("Trend unclear")

            score = 3

        st.write("Trend Score:")

        st.progress(score * 10)

        if score >= 8:
            st.write("💡 Suggested Business: AI automation tools")

        elif score >= 5:
            st.write("💡 Suggested Business: Online coaching platform")

        else:
            st.write("💡 Do more research before starting")

# AI ASSISTANT
elif menu == "AI Assistant":

    st.header("🤖 Business Assistant")

    question = st.text_input("Ask a startup question")

    if st.button("Ask"):

        st.success("Advice: Start small, validate the idea, then scale.")