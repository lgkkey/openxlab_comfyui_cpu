from fastapi import FastAPI
import uvicorn

import gradio as gr
fastapi_app=FastAPI()

def output_txt(input):
    return "output: "+input
with gr.Blocks() as demo:
    gr.Markdown("Hello, **world!**")
    with gr.Row():
        input=gr.Textbox()
        output=gr.Textbox()
    
    run=gr.Button("Run")
    clear=gr.Button("Clear")
    event=run.click(output_txt,inputs=[input],outputs=[output])
    clear.click(lambda: ["",""],inputs=[],outputs=[input,output])
 
fastapi_app=gr.mount_gradio_app(fastapi_app,demo,path="/hello")
uvicorn.run(fastapi_app,host='0.0.0.0',port=7890)
