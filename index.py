# -*- coding: utf-8 -*-
"""شات كرة القدم الذكي - تصميم خارق مع Gemini API"""

!pip install -q gradio requests

import gradio as gr
import requests
import json

API_KEY = "AQ.Ab8RN6KCfkWTrOkbj93cTvdOiY6qCW2vo7W0UUn8qBWkBkzPsQ"
MODEL = "gemini-flash-latest"

# تعليمات النظام - متخصصة في كرة القدم
SYSTEM_PROMPT = """أنت خبير كرة قدم متحمس، اسمك "محلل الكرة". تخصصك فقط في كرة القدم: الدوريات (الدوري الإنجليزي، الإسباني، الإيطالي، الألماني، الفرنسي، السعودي، المصري، إلخ)، الأندية، اللاعبون، كأس العالم، دوري أبطال أوروبا، البطولات القارية، الإحصائيات، التاريخ، والتحليلات. 
أجب بحماس باللغة العربية الفصحى أو العامية المفهومة.
إذا سألك المستخدم عن أي شيء خارج كرة القدم، اعتذر بلطف وقل أن تخصصك هو كرة القدم فقط.
إذا سألك عن المطور، فقل: "المهندس عبدالله الشرجبي هو المطور العبقري لهذا الشات الخرافي."
كن سريعًا ومفيدًا، واستخدم تعابير كروية حماسية مثل: "يا هلال!", "هدف!", "رائعة!", "تسديدة رائعة".
"""

def ask_gemini(conversation_history):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }
    payload = {
        "contents": conversation_history,
        "generationConfig": {
            "temperature": 0.8,
            "maxOutputTokens": 600,
            "topP": 0.95
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"عذراً، حدث خطأ كروي: {response.status_code}"

def chat_function(message, history):
    conversation = [
        {"role": "user", "parts": [{"text": SYSTEM_PROMPT}]},
        {"role": "model", "parts": [{"text": "تم فهم التعليمات. أنا جاهز لتحليل كرة القدم بحماس!"}]}
    ]
    for human, assistant in history:
        conversation.append({"role": "user", "parts": [{"text": human}]})
        conversation.append({"role": "model", "parts": [{"text": assistant}]})
    conversation.append({"role": "user", "parts": [{"text": message}]})
    
    reply = ask_gemini(conversation)
    return reply

# CSS خيالي لكرة القدم
football_css = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
* {
    font-family: 'Poppins', 'Segoe UI', sans-serif;
}
body, .gradio-container {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364) !important;
    margin: 0;
    padding: 0;
}
.main-panel {
    max-width: 900px;
    margin: 20px auto;
    background: rgba(0,0,0,0.6);
    border-radius: 40px;
    backdrop-filter: blur(8px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    padding: 20px;
}
.header {
    text-align: center;
    padding: 10px;
    background: linear-gradient(90deg, #ffb347, #ffcc33);
    border-radius: 60px;
    margin-bottom: 25px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}
.header h1 {
    font-size: 32px;
    font-weight: 800;
    color: #1e2a3a;
    text-shadow: 2px 2px 0 #ffd700;
    margin: 0;
}
.header p {
    font-size: 16px;
    color: #2c3e2f;
    font-weight: bold;
}
.chatbot {
    background: transparent !important;
    border-radius: 30px;
}
.bot-message, .user-message {
    padding: 12px 20px;
    border-radius: 28px;
    max-width: 75%;
    font-size: 15px;
    font-weight: 500;
    line-height: 1.4;
    margin: 15px 0;
    animation: bounceIn 0.4s ease;
}
.user-message {
    background: linear-gradient(135deg, #00b4db, #0083b0);
    color: white;
    margin-left: auto;
    border-bottom-right-radius: 6px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
.bot-message {
    background: linear-gradient(135deg, #2b5876, #4e4376);
    color: #f0f0f0;
    margin-right: auto;
    border-bottom-left-radius: 6px;
    border-left: 5px solid #ffcc33;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
.input-row {
    background: rgba(255,255,255,0.1);
    border-radius: 50px;
    padding: 8px 15px;
    margin-top: 20px;
    backdrop-filter: blur(5px);
}
.input-textbox textarea {
    background: #ffffffdd !important;
    border: none !important;
    border-radius: 40px !important;
    padding: 12px 20px !important;
    font-size: 15px !important;
    color: #1e2a3a !important;
    font-weight: 500;
}
.send-btn {
    background: radial-gradient(circle at 30% 10%, #ffcc33, #ff9900) !important;
    border: none !important;
    border-radius: 40px !important;
    font-weight: bold !important;
    font-size: 16px !important;
    color: #1e2a3a !important;
    padding: 8px 24px !important;
    transition: 0.2s;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}
.send-btn:hover {
    transform: scale(1.02);
    background: radial-gradient(circle at 30% 10%, #ffdd55, #ffaa00) !important;
}
.clear-btn {
    background: #ff6b6b !important;
    border: none !important;
    border-radius: 40px !important;
    font-weight: bold;
    color: white;
    padding: 6px 18px;
}
@keyframes bounceIn {
    0% { opacity: 0; transform: translateY(20px); }
    80% { transform: translateY(-5px); }
    100% { opacity: 1; transform: translateY(0); }
}
.footer {
    text-align: center;
    margin-top: 25px;
    font-size: 12px;
    color: #ffdd99;
}
.footer a {
    color: #ffcc33;
    text-decoration: none;
}
/* كرة القدم متحركة خلفية اختيارية */
body::before {
    content: "⚽";
    font-size: 200px;
    position: fixed;
    bottom: -50px;
    left: -50px;
    opacity: 0.1;
    pointer-events: none;
    animation: rotateBall 20s linear infinite;
}
@keyframes rotateBall {
    0% { transform: rotate(0deg) translateX(0); }
    100% { transform: rotate(360deg) translateX(30px); }
}
"""

with gr.Blocks(css=football_css, title="⚽ شات كرة القدم الخرافي") as demo:
    with gr.Column(elem_classes="main-panel"):
        with gr.Row(elem_classes="header"):
            gr.HTML("""
                <div>
                    <h1>⚽ شات كرة القدم الخرافي ⚽</h1>
                    <p>تحليلات، أخبار، تاريخ، وإحصائيات 🔥 اسأل عن أي نادي أو لاعب أو بطولة</p>
                </div>
            """)
        
        chatbot = gr.Chatbot(
            height=520,
            bubble_full_width=False,
            avatar_images=(None, "https://cdn-icons-png.flaticon.com/512/2502/2502987.png"),  # كرة قدم
            show_copy_button=True,
            elem_classes="chatbot"
        )
        
        with gr.Row(elem_classes="input-row"):
            msg = gr.Textbox(
                placeholder="اكتب سؤالك الكروي... مثال: من فاز بكأس العالم 2022؟ أخبرني عن النادي الأهلي المصري...",
                lines=1,
                scale=9,
                elem_classes="input-textbox",
                show_label=False
            )
            send_btn = gr.Button("🚀 إرسال", variant="primary", scale=1, elem_classes="send-btn")
        
        with gr.Row():
            clear_btn = gr.Button("🗑️ مسح المحادثة", variant="secondary", elem_classes="clear-btn")
        
        gr.HTML("""
            <div class="footer">
                ⚡ تم التطوير بواسطة <strong>المهندس عبدالله الشرجبي</strong> | جميع الحقوق محفوظة © 2025 | ⚡
            </div>
        """)
    
    def respond(message, chat_history):
        if not message or not message.strip():
            return "", chat_history
        bot_message = chat_function(message, chat_history)
        chat_history.append((message, bot_message))
        return "", chat_history
    
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    send_btn.click(respond, [msg, chatbot], [msg, chatbot])
    clear_btn.click(lambda: None, None, chatbot, queue=False)

demo.launch(share=True, debug=False)
