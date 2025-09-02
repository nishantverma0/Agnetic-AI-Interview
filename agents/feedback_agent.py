from core.llm_utils import call_llm

class FeedbackAgent:
    def __init__(self):
        self.role = "Feedback Agent"

    def summarize_session(self, memory):
        conversation = memory.get_full_context()
        feedback_prompt = (
            "Summarize this interview session and give structured feedback "
            "(strengths, weaknesses, improvement tips):\n\n"
            f"{conversation}"
        )
        summary = call_llm(feedback_prompt)
        memory.store_interaction(self.role, summary)
        return summary
