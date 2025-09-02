from core.llm_utils import call_llm
import random
import json

class TechAgent:
    def __init__(self, faq_file="data/tech_faqs.json"):
        self.role = "Tech Agent"
        with open(faq_file, "r") as f:
            self.questions = json.load(f)

    def ask_question(self, memory, difficulty="easy"):
        q = random.choice(self.questions[difficulty])
        memory.store_interaction(self.role, q)
        return q

    def process_answer(self, answer, memory):
        feedback_prompt = f"Evaluate this technical answer:\n{answer}"
        evaluation = call_llm(feedback_prompt)
        memory.store_interaction("User", answer)
        memory.store_interaction(self.role, evaluation)
        return evaluation
