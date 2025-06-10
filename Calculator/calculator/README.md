### **AI Calculator**

# **Overview**

AI Calculator is a Python-based agentic AI application that performs mathematical calculations using custom tools integrated with the Gemini 2.0 Flash model via the agents library.
The calculator supports basic arithmetic (addition, subtraction, multiplication, division) and advanced operations like square roots, exponentiation, logarithms, and trigonometric functions (sine, cosine, tangent).
The assistant provides accurate numerical results for user queries, leveraging an AI-driven interface to interpret mathematical expressions.

# **Features**

**Arithmetic Operations:** Addition, subtraction, multiplication, and division.
**Advanced Math:** Square root, exponentiation, natural logarithm, and trigonometric functions (sine, cosine, tangent).
**AI-Powered:** Uses the Gemini 2.0 Flash model to parse and respond to natural language queries.
**Custom Tools:** Built with the agents library, allowing extensible tool definitions for mathematical operations.
**Async Support:** Utilizes asynchronous functions for efficient tool execution.

# **Requirements**

Python 3.13 or higher
Virtual environment (recommended)
Gemini API key (set in a .env file as GEMINI_API_KEY)
Required Python packages (listed in requirements.txt):
agents
python-dotenv



# **Setup Instructions**

**Clone the Repository:** git clone <repository-url>
cd ai_calculator


**Set Up a Virtual Environment:** python -m venv .venv
source .venv/Scripts/activate  # On Windows
# or
source .venv/bin/activate  # On macOS/Linux


**Install Dependencies:** pip install -r requirements.txt


**Configure the API Key:**
Create a .env file in the project root.
Add your Gemini API key:GEMINI_API_KEY=your_api_key_here




**Run the Calculator:** python main.py


**Example query:** “What is 2 + 2?” will output 4.



# **Usage**

Run the main.py script to start the calculator.

The script initializes an AI agent with mathematical tools and processes a sample query (“What is 2 + 2?”).

Modify the query in main.py or extend the script for dynamic user input.

Example:
result = Runner.run_sync(agent, "What is the square root of 16?", run_config=config)
print(result.final_output)  # Output: 4.0



# **Project Structure**

main.py: Core script defining the AI agent, tools, and query execution.
.env: Configuration file for storing the Gemini API key.
requirements.txt: List of required Python packages.

# **Future Enhancements**

Add interactive user input for real-time queries.
Expand toolset with additional mathematical functions (e.g., factorial, matrix operations).
Improve error handling for edge cases (e.g., invalid inputs).
Integrate unit tests for tool reliability.

# **License**

This project is licensed under the MIT License. See the LICENSE file for details.

