import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyDONU1LmKi9fVNEG9tsopZvRB0EcdKcfs8")
# genai.configure(api_key=os.getenv("AIzaSyDONU1LmKi9fVNEG9tsopZvRB0EcdKcfs8"))
# genai.configure(api_key=os.environ["AIzaSyDONU1LmKi9fVNEG9tsopZvRB0EcdKcfs8"])
## streamlit app
st.title("AI- Learning Companion")
st.text("Improve your learning potential with AI-Learning Companion!")
avbl_model = []
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
  	avbl_model.append(m.name)

# selected_model_name = st.selectbox("Choose a Model:", [""] + avbl_model, index = 2)
# model = genai.GenerativeModel(selected_model_name)

model = genai.GenerativeModel('gemini-1.0-pro-001')                          # This 
                                                                               # OR
# model = genai.GenerativeModel("models/gemini-1.0-pro-latest")                  # This According to good results


# Allow user to select the subject
selected_subject = st.sidebar.selectbox("Select Subject:", ["Social Studies", "Economics", "English", "Science", "Mathematics"])

 temperature=st.sidebar.number_input("temperature", value=0.9, step=0.1, placeholder="Type a temperature...")
 top_p=st.sidebar.number_input("top_p", value=1.0, step=0.1, placeholder="Type a top_p...")
 top_k=st.sidebar.number_input("top_k", value=20, placeholder="Type a top_k...")
 max_output_tokens=st.sidebar.number_input("max_output_tokens", value=400000, placeholder="max_output_tokens...")
 generation_config = genai.GenerationConfig(
 	max_output_tokens=max_output_tokens,
 	temperature=temperature,
 	top_p=top_p,
 	top_k=top_k
 )
generation_config = genai.GenerationConfig(
	max_output_tokens=400000,
	temperature=0.9,
	top_p=1.0,
	top_k=None
)

# models = genai.list_models()

# model=genai.GenerativeModel('gemini-pro')
def get_gemini_repsonse(input):
	# model=genai.GenerativeModel('gemini-pro')
	response=model.generate_content(input, generation_config=generation_config)
	return response.text


# Define the MCQs for Science
# 1.SOCIAL STUDIES

social_studies_mcqs = [
    {
        "question": "Who was the first President of the United States?",
        "options": ["Select an option", "George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
        "answer": "George Washington",
        "topic": "History"
    },
    {
        "question": "Which of the following countries was NOT a member of the Axis Powers during World War II?",
        "options": ["Select an option", "Germany", "Japan", "Italy", "Russia"],
        "answer": "Russia",
        "topic": "World War II"
    },
    {
        "question": "What is the capital city of Canada?",
        "options": ["Select an option", "Ottawa", "Toronto", "Montreal", "Vancouver"],
        "answer": "Ottawa",
        "topic": "Geography"
    },
    {
        "question": "Who wrote 'The Wealth of Nations', often considered the foundational work of modern economics?",
        "options": ["Select an option", "Adam Smith", "Karl Marx", "John Maynard Keynes", "Milton Friedman"],
        "answer": "Adam Smith",
        "topic": "Economics"
    },
    {
        "question": "What is the main purpose of the United Nations (UN)?",
        "options": ["Select an option", "Promotion of world peace and security", "Advancement of economic development", "Protection of human rights", "All of the above"],
        "answer": "All of the above",
        "topic": "International Organizations"
    }
]


# 2.ECONOMICS

economics_mcqs = [
    {
        "question": "What is the primary function of central banks in a country's economy?",
        "options": ["Select an option", "Regulation of interest rates", "Control of inflation", "Management of monetary policy", "All of the above"],
        "answer": "All of the above",
        "topic": "Monetary Policy"
    },
    {
        "question": "Which of the following is NOT a factor of production?",
        "options": ["Select an option", "Land", "Labor", "Money", "Capital"],
        "answer": "Money",
        "topic": "Factors of Production"
    },
    {
        "question": "What does GDP stand for in economics?",
        "options": ["Select an option", "Gross Domestic Profit", "Global Development Policy", "Gross Domestic Product", "General Demand Price"],
        "answer": "Gross Domestic Product",
        "topic": "Macroeconomics"
    },
    {
        "question": "What is the economic term for a situation where the demand for a good exceeds its supply, leading to a rise in prices?",
        "options": ["Select an option", "Inflation", "Deflation", "Recession", "Shortage"],
        "answer": "Shortage",
        "topic": "Microeconomics"
    },
    {
        "question": "Which of the following is an example of a regressive tax?",
        "options": ["Select an option", "Progressive income tax", "Sales tax", "Corporate income tax", "Property tax"],
        "answer": "Sales tax",
        "topic": "Taxation"
    }
]


# 3.ENGLISH

english_mcqs = [
    {
        "question": "Who is the author of the play 'Hamlet'?",
        "options": ["Select an option", "William Shakespeare", "Jane Austen", "Charles Dickens", "Emily Bronte"],
        "answer": "William Shakespeare",
        "topic": "Drama"
    },
    {
        "question": "What is an example of a literary device used in the poem 'The Road Not Taken'?",
        "options": ["Select an option", "Metaphor", "Personification", "Simile", "Alliteration"],
        "answer": "Metaphor",
        "topic": "Poetry"
    },
    {
        "question": "Which of the following is a characteristic of the Romantic literary movement?",
        "options": ["Select an option", "Emphasis on reason and logic", "Focus on ordinary life", "Celebration of nature and individualism", "Preference for simple language"],
        "answer": "Celebration of nature and individualism",
        "topic": "Literary Movements"
    },
    {
        "question": "Who is the protagonist in the novel 'Pride and Prejudice'?",
        "options": ["Select an option", "Elizabeth Bennet", "Mr. Darcy", "Jane Bennet", "Mr. Bingley"],
        "answer": "Elizabeth Bennet",
        "topic": "Prose Fiction"
    },
    {
        "question": "What is the theme of the short story 'The Necklace' by Guy de Maupassant?",
        "options": ["Select an option", "The pursuit of wealth", "The importance of honesty", "The power of love", "The value of friendship"],
        "answer": "The pursuit of wealth",
        "topic": "Short Stories"
    }
]


# 4.Science

science_mcqs = [
    {
        "question": "What is the chemical symbol for water?",
        "options": ["Select an option", "H2O", "CO2", "O2", "NaCl"],
        "answer": "H2O",
        "topic": "Chemical Symbols"
    },
    {
        "question": "Which organelle is known as the powerhouse of the cell?",
        "options": ["Select an option", "Nucleus", "Golgi Apparatus", "Mitochondria", "Endoplasmic Reticulum"],
        "answer": "Mitochondria",
        "topic": "Cell Biology"
    },
    {
        "question": "What is the process by which plants make their food called?",
        "options": ["Select an option", "Photosynthesis", "Respiration", "Fermentation", "Transpiration"],
        "answer": "Photosynthesis",
        "topic": "Photosynthesis"
    },
    {
        "question": "Who proposed the theory of relativity?",
        "options": ["Select an option", "Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
        "answer": "Albert Einstein",
        "topic": "Physics"
    },
    {
        "question": "What is the main function of the kidneys?",
        "options": ["Select an option", "Regulate Blood Sugar", "Produce Hormones", "Filter Waste from Blood", "Produce Red Blood Cells"],
        "answer": "Filter Waste from Blood",
        "topic": "Human Anatomy"
    }
]

# 5.MATHEMATICS

mathematics_mcqs = [
    {
        "question": "What is the solution to the equation 2x + 3 = 9?",
        "options": ["Select an option", "x = 3", "x = 6", "x = 8", "x = 5"],
        "answer": "x = 3",
        "topic": "Algebra"
    },
    {
        "question": "What is the value of sin(45°)?",
        "options": ["Select an option", "1", "0", "0.5", "√2/2"],
        "answer": "√2/2",
        "topic": "Trigonometry"
    },
    {
        "question": "What is the derivative of the function f(x) = x^3 - 2x^2 + 5x - 1?",
        "options": ["Select an option", "3x^2 - 4x + 5", "3x^2 - 4x", "2x^3 - 4x^2 + 5x", "3x^2 - 4"],
        "answer": "3x^2 - 4x + 5",
        "topic": "Calculus"
    },
    {
        "question": "What is the area of a rectangle with length 8 units and width 6 units?",
        "options": ["Select an option", "48 square units", "36 square units", "24 square units", "30 square units"],
        "answer": "48 square units",
        "topic": "Geometry"
    },
    {
        "question": "What is the probability of rolling a number greater than 4 on a fair six-sided die?",
        "options": ["Select an option", "1/6", "1/3", "1/2", "2/3"],
        "answer": "1/3",
        "topic": "Probability"
    }
]

# Create the Streamlit app
# st.title("MCQs Generator")



if selected_subject == "Social Studies":
	mcqs = social_studies_mcqs
elif selected_subject == "Economics":
	mcqs = economics_mcqs
elif selected_subject == "English":
	mcqs = english_mcqs
elif selected_subject == "Science":
	mcqs = science_mcqs
else:
  mcqs = mathematics_mcqs

# Initialize results
results = {mcq["topic"]: "Needs Preparation" for mcq in mcqs}
st.subheader(selected_subject)
# Display all MCQs at once
for i, mcq in enumerate(mcqs):
    st.subheader(f"Question {i+1}: {mcq['topic']}")
    st.write(mcq["question"])
    selected_option = st.radio(f"Options for Question {i+1}:", mcq["options"])
    if selected_option != "Select an option":
        if selected_option == mcq["answer"]:
            results[mcq["topic"]] = "Understood"


rs = []
for topic, result in results.items():
	# rs = f"- **{topic}**: {result}"
	rs.append(f"- **{topic}**: :orange[{result}]")
	# st.write(f"- **{topic}**: {result}")
print("rs->",rs)

submit = st.button("Analyze")

if submit:
	if rs is not None:
		with st.spinner(f'Analyzing your {selected_subject} knowledge...'):
			# text=input_pdf_text(rs)
			#Prompt Template

			input_prompt=f"""
			Your job is to guide studient according to below prompt:
			### Performance Report:

			**Subject: 12th-grade {selected_subject}**

			#### Topic-wise Performance:{rs}

			### Feedback and Guidance:

			Based on your performance, here are some recommendations:

			{"**feedback**"}

			### Teaching Assistance:

			For the topics where you did not perform well, here are some resources to help you improve:

			{"**teaching_assistance**"}

			---

			"""
			for topic, result in results.items():
				# rs = f"- **{topic}**: {result}"
				# rs.append(f"- **{topic}**: :orange[{result}]")
				st.write(f"- **{topic}**: :orange[{result}]")
			response=get_gemini_repsonse(input_prompt)
			st.subheader(response)

			st.write("_________________________")
			# Output results
			# st.markdown("# Results")
			# st.write(rs)
			# st.write(text)
