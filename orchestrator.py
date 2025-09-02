from agents.hr_agent import HRAgent
from agents.tech_agent import TechAgent
from agents.feedback_agent import FeedbackAgent
from core.memory import Memory

class Orchestrator:
    def __init__(self):
        self.hr = HRAgent()
        self.tech = TechAgent()
        self.feedback = FeedbackAgent()
        self.memory = Memory()

    def run_interview(self):
        hr_q = self.hr.ask_question(self.memory)
        return f"HR Round:\n{hr_q}"

    def next_round(self, user_answer, difficulty="easy"):
        self.hr.process_answer(user_answer, self.memory)
        tech_q = self.tech.ask_question(self.memory, difficulty)
        return f"Technical Round ({difficulty}):\n{tech_q}"

    def conclude(self, user_answer):
        self.tech.process_answer(user_answer, self.memory)
        feedback_summary = self.feedback.summarize_session(self.memory)
        return f"Final Feedback:\n{feedback_summary}"
