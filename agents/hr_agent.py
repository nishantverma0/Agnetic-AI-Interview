from core.llm_utils import call_llm

class HRAgent:
    def __init__(self):
        self.role = "HR Agent"

    def ask_question(self, memory):
        # First HR round question
        hr_question = "Tell me about yourself."
        memory.store_interaction(self.role, hr_question)
        return hr_question

    def process_answer(self, answer, memory):
        feedback_prompt = f"As an HR interviewer, evaluate this response:\n{answer}"
        evaluation = call_llm(feedback_prompt)
        memory.store_interaction("User", answer)
        memory.store_interaction(self.role, evaluation)
        return evaluation
