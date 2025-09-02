import gradio as gr
from orchestrator import Orchestrator
from analysis.sentiment import analyze_sentiment
from analysis.emotion import detect_emotion

orchestrator = Orchestrator()

# ---------------------------
# Core Functions
# ---------------------------
def start_interview():
    q = orchestrator.run_interview()
    return [("AI Interviewer", q)], q  # chatbot history + first question

def next_step(user_answer, difficulty, history):
    q = orchestrator.next_round(user_answer, difficulty)
    sentiment = analyze_sentiment(user_answer)
    emotion = detect_emotion(user_answer)

    # Append user’s answer + AI response to chat history
    history = history or []
    history.append(("You", user_answer))
    history.append(("AI Interviewer", f"{q}\n(Sentiment: {sentiment}, Emotion: {emotion})"))

    return history, q, history

def end_interview(user_answer, history):
    summary = orchestrator.conclude(user_answer)

    history = history or []
    history.append(("You (Final)", user_answer))
    history.append(("AI Interviewer", f"✅ Final Feedback:\n{summary}"))

    return history, summary

# ---------------------------
# Gradio UI
# ---------------------------
with gr.Blocks() as demo:
    gr.Markdown("# 🎤 Agentic AI Interview Simulator")

    chatbot = gr.Chatbot(height=400)
    state = gr.State([])   # keeps conversation history
    q_state = gr.State("") # keeps current question

    start_btn = gr.Button("🚀 Start Interview")

    with gr.Row():
        user_inp = gr.Textbox(placeholder="Type your answer here...")
        diff = gr.Dropdown(["easy", "medium", "hard"], value="easy", label="Difficulty")
        next_btn = gr.Button("➡️ Next Question")

    final_inp = gr.Textbox(placeholder="Your final thoughts...")
    end_btn = gr.Button("🏁 End Interview")
    summary_box = gr.Textbox(label="Summary", interactive=False)

    # Button wiring
    start_btn.click(start_interview, outputs=[chatbot, q_state])
    next_btn.click(next_step, inputs=[user_inp, diff, state], outputs=[chatbot, q_state, state])
    end_btn.click(end_interview, inputs=[final_inp, state], outputs=[chatbot, summary_box])

# Launch app
if __name__ == "__main__":
    demo.launch(share=True)
