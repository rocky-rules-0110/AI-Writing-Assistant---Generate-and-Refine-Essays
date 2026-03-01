from groq import generate_response 

def refine_essay_activity():
    print("\n=== ESSAY REFINEMENT ACTIVITY ===")
    topic = input("Enter a topic for your initial essay: ").strip()
    
    initial_prompt = f"Write a short 3-paragraph essay about {topic}."
    print("\nGenerating initial essay...")
    essay = generate_response(initial_prompt)
    print(f"\n--- INITIAL ESSAY ---\n{essay}\n")

    print("--- REFINEMENT PHASE ---")
    feedback = input("How should we improve the Introduction? (e.g., 'Make it more mysterious'): ")
    refine_prompt = f"Take this essay:\n\n{essay}\n\nRewrite the introduction based on this feedback: {feedback}. Keep the rest the same."
    essay = generate_response(refine_prompt)
    
    print("\n--- STYLE ADAPTATION ---")
    style = input("Choose a style (Formal or Conversational): ").strip().lower()
    style_prompt = f"Rewrite the following essay in a {style} tone:\n\n{essay}"
    final_essay = generate_response(style_prompt)
    
    print(f"\n--- FINAL REFINED ESSAY ({style.upper()}) ---\n{final_essay}")
    
    with open("activity_results/refined_essay.txt", "w") as f:
        f.write(final_essay)
    print("\nEssay saved to activity_results/refined_essay.txt")

if __name__ == "__main__":
    refine_essay_activity()