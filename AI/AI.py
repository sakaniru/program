import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 模型路徑（可以是 Hugging Face 的 repo id）
model_name_or_path = "tiiuae/falcon-7b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(model_name_or_path)

model.eval()

if torch.cuda.is_available():
    model.to("cuda")

# 修改過的聊天函式：使用 [[user, ai], [user, ai], ...] 格式的 chat_history
def chat_with_model(user_input, chat_history):
    # 把歷史訊息組成文字輸入給模型
    input_text = ""
    for user, bot in chat_history:
        input_text += f"User: {user}\nAI: {bot}\n"
    input_text += f"User: {user_input}\nAI:"

    # Tokenize 並送入模型
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        pad_token_id=tokenizer.eos_token_id
    )
    full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # 擷取模型產生的新回答
    response = full_response[len(input_text):].strip()

    # 加入新的對話進 chat history
    chat_history.append([user_input, response])
    return "", chat_history

# Gradio 介面
with gr.Blocks() as demo:
    chat_history = gr.State([])  # 使用 [[user, ai], ...] 格式
    chatbot = gr.Chatbot(label="ChatGPT-like 聊天機器人")
    msg = gr.Textbox(placeholder="請輸入你的問題...", show_label=False)
    submit = gr.Button("送出")

    submit.click(fn=chat_with_model, inputs=[msg, chat_history], outputs=[msg, chatbot])

demo.launch()
