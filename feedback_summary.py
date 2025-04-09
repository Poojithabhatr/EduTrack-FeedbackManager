def summarize_feedback(feedback_list):
    if not feedback_list:
        return "No feedback yet."
    
    summary = f"Received {len(feedback_list)} feedback entries:\n"
    for i, entry in enumerate(feedback_list, start=1):
        summary += f"{i}. Score: {entry['score']} - \"{entry['feedback']}\"\n"
    return summary
