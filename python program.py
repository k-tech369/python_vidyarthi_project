import string

# MBTI Dichotomy definitions:
# E/I: Energy Focus
# S/N: Information Gathering
# T/F: Decision Making
# J/P: Lifestyle/Organization

DICHOTOMIES = [
    # (Dichotomy, Letter1, Letter2)
    ("Energy Focus (E/I)", "E", "I"),
    ("Information Gathering (S/N)", "S", "N"),
    ("Decision Making (T/F)", "T", "F"),
    ("Lifestyle/Organization (J/P)", "J", "P"),
]

# Questions are now declarative statements.
# Agreement (score 1) always pushes the result toward the first letter (E, S, T, J).
# Disagreement (score 5) always pushes the result toward the second letter (I, N, F, P).
# 8 Questions total: 2 per dichotomy
QUESTIONS = [
    # E/I (Energy)
    {"dichotomy": 0, "q_text": "I feel energized when I spend time in large groups or social gatherings."},
    {"dichotomy": 0, "q_text": "I prefer to take frequent breaks to talk or socialize while working."},
    
    # S/N (Information)
    {"dichotomy": 1, "q_text": "I am focused on practical facts, details, and what is happening now."},
    {"dichotomy": 1, "q_text": "When describing events, I focus on the specific facts and sequence."},

    # T/F (Decisions)
    {"dichotomy": 2, "q_text": "When making decisions, I am guided more by logical analysis and objective criteria."},
    {"dichotomy": 2, "q_text": "I find it easier to stay objective and logical in a conflict than to connect emotionally."},

    # J/P (Lifestyle)
    {"dichotomy": 3, "q_text": "I prefer to have things settled and planned in advance, rather than keeping options open."},
    {"dichotomy": 3, "q_text": "I feel motivated and organized when working toward a clear, set deadline."},
]

# --- CORE FUNCTIONS ---

def get_preference(question_data):
    """
    Prompts the user for a preference score (1-5) on an Agree/Disagree scale.
    1 = Strongly Agree (leans to Letter A); 5 = Strongly Disagree (leans to Letter B).
    """
    while True:
        try:
            print(f"\nQ: {question_data['q_text']}")
            print("Rate your agreement (1-5):")
            print("  [1] Strongly Agree | [3] Neutral | [5] Strongly Disagree")
            
            score = int(input("Enter your score (1-5): ").strip())
            
            if 1 <= score <= 5:
                return score
            else:
                print("❌ Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def calculate_type(responses):
    """
    Calculates the final 4-letter type based on user preference scores (1-5 scale).
    The score change is calculated as: 3 - response (range: +2 to -2).
    """
    # Initialize scores for the four dichotomies (index 0 to 3)
    # Max possible score is +4 (2 questions * +2 per question)
    # Min possible score is -4 (2 questions * -2 per question)
    scores = [0, 0, 0, 0] 
    
    # 1. Tally scores
    for i, user_score in enumerate(responses):
        q_data = QUESTIONS[i]
        dichotomy_index = q_data['dichotomy']
        
        # Calculate the directional score contribution: 
        # 1 (Agree) -> +2, 3 (Neutral) -> 0, 5 (Disagree) -> -2
        directional_score = 3 - user_score
        
        scores[dichotomy_index] += directional_score

    # 2. Determine the final 4-letter code and preference strength
    personality_type = ""
    result_breakdown = {}
    
    for i in range(4):
        dichotomy_name, letter1, letter2 = DICHOTOMIES[i]
        score = scores[i]
        
        # Determine the resulting letter based on the total preference score
        # Note: Score boundaries (>= 3 or <= -3) are used to define "Strong" preference
        if score > 0:
            final_letter = letter1
            leaning_strength = "Strong Preference" if score >= 3 else "Moderate Preference"
        elif score < 0:
            final_letter = letter2
            leaning_strength = "Strong Preference" if score <= -3 else "Moderate Preference"
        else:
            final_letter = letter1 # Default letter for tie, but categorized as balanced
            leaning_strength = "Balanced/Moderate"
            
        personality_type += final_letter
        
        result_breakdown[dichotomy_name] = {
            "score": score,
            "letter": final_letter,
            "leaning_strength": leaning_strength
        }

    return personality_type, result_breakdown

def get_type_description(mbti_type):
    """Provides a brief, hardcoded description for each MBTI type."""
    # A dictionary for common types. This can be expanded to all 16 types.
    descriptions = {
        "INTJ": "The Architect. Imaginative and strategic thinkers, with a plan for everything.",
        "INFP": "The Mediator. Poetic, kind, and altruistic people, always eager to help a good cause.",
        "ESTJ": "The Executive. Excellent administrators, unsurpassed at managing things or people.",
        "ENFJ": "The Protagonist. Charismatic and inspiring leaders, able to mesmerize their listeners.",
        "ISTP": "The Virtuoso. Bold and practical experimenters, masters of all kinds of tools.",
        "ESFP": "The Entertainer. Spontaneous, energetic, and enthusiastic people—life is never boring around them.",
        "INFJ": "The Advocate. Quiet and mystical, yet very inspiring and tireless idealists.",
        "ENTP": "The Debater. Smart and curious thinkers who cannot resist an intellectual challenge.",
        "DEFAULT": "A unique blend of Introversion/Extraversion, Sensing/Intuition, Thinking/Feeling, and Judging/ Perceiving."
    }
    
    return descriptions.get(mbti_type, descriptions["DEFAULT"])

def main():
    """The main function to run the MBTI Personality Profiler."""
    
    responses = []

    print("=====================================================")
    print(" 🔮 MBTI 16-Type Personality Profiler (Agree/Disagree Scale) ")
    print("=====================================================")
    print("Rate your agreement with each statement on a scale of 1 to 5.")
    print("1: Strongly Agree, 5: Strongly Disagree.")
    print("-----------------------------------------------------")
    
    # Trigger image to explain the model
    print("")
    
    # 1. Collect Responses
    for q in QUESTIONS:
        score = get_preference(q) # Using the new Agree/Disagree scale input
        responses.append(score)
        
    # 2. Score the Test
    personality_type, breakdown = calculate_type(responses)
    description = get_type_description(personality_type)
    
    # 3. Interpret and Display Results

    print("\n\n=====================================================")
    print("          ✨ Your 4-Letter Personality Code ✨        ")
    print("=====================================================")
    
    print(f"\n🎉 Your Personality Type is: {personality_type}")
    print(f"   ({description})")
    
    print("\n--- Preference Breakdown ---")
    for dichotomy, data in breakdown.items():
        clean_name = dichotomy.split('(')[0].strip()
        
        # Determine the letter and its polarity (A or B)
        _, letter1, letter2 = [d for d in DICHOTOMIES if dichotomy in d[0]][0]
        
        if data['score'] > 0:
            dominant_letter = letter1
        elif data['score'] < 0:
            dominant_letter = letter2
        else:
            dominant_letter = f"({letter1}/{letter2})"
            
        print(f"[{clean_name:25}]: {dominant_letter} | Strength: {data['leaning_strength']:20} | Score: {data['score']:+d}")
        
    print("\n=====================================================")
    print("The score (ranging from -4 to +4) indicates the strength of your preference.")
    print("\nDisclaimer: This is a simplified tool for learning Python. Professional personality assessment requires certified testing.")

if __name__ == "__main__":
    main()
    