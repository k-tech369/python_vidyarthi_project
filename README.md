MBTI Personality Profiler
A Python-based application that conducts the MBTI (Myers–Briggs Type Indicator) personality assessment, calculates the result, and presents the personality type with descriptions.

##Overview

The MBTI Personality Profiler is a command-line Python project designed to help users understand their personality preferences based on the MBTI model.
The system displays a series of questions, collects user responses, evaluates scores for each personality dimension (E/I, S/N, T/F, J/P), and returns the final MBTI type with explanations.

This project demonstrates:
Modular programming
File handling
Input validation
Data processing
User-friendly output formatting


#Features

1.40+ MBTI-based questions
2.Automated scoring for all 4 MBTI dimensions
3.Clean, modular code structure
4.Input validation
5.Personality type generation (e.g., ENFP, ISTJ)
6.Personality explanation output
7.Ready for CLI execution
8.Extendable question bank

#Technologies / Tools Used
Python 3.x
JSON / Text files (optional for storing questions)
Diagram tools (workflow/use case) – optional
Git & GitHub for version control
VS Code / PyCharm (recommended IDE)

#How to Install & Run the Project

1. Clone the Repository
git clone https://github.com/yourusername/MBTI-Profiler.git
cd MBTI-Profiler

2. Install Requirements (if any)
If you have a requirements.txt:
pip install -r requirements.txt
(Most projects won’t need it unless external libraries are used.)

3. Run the Project
python main.py



#Instructions for Testing

You can test the application through manual test cases:
Test Case 1 – Correct Input
Input: Valid numeric answers (1–5)
Output: MBTI type + explanation


Test Case 2 – Invalid Input
Input: Letter or number outside range
Output: System should show:
"Invalid Input. Please enter a number between 1–5."


Test Case 3 – Extreme Personality
Input: Mostly 1s or 5s
Output: Strongly leaning MBTI type


Test Case 4 – Mixed Responses
Output: Balanced or neutral MBTI type


