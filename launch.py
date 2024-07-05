import os
import subprocess
import time
import threading
os.system("pwd")
os.system("ls -la")
print("---------------launch.py-----------------------")
os.system("git clone https://github.com/comfyanonymous/ComfyUI")

os.chdir("ComfyUI")

os.system("pip install -r requirements.txt")
os.chdir("models/checkpoints")
os.system("wget -c https://hf-mirror.com/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors")
os.system("wget -c https://hf-mirror.com/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors")
os.chdir("../upscale_models")
os.system("wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-general-x4v3.pth")
os.chdir("../clip_vision")
os.system("wget -c https://hf-mirror.com/comfyanonymous/clip_vision_g/resolve/main/clip_vision_g.safetensors")
os.chdir("../..")
os.system("ls -la")
print("----------------start app_start.py----------------------")

import gradio as gr
def output_txt(input):
    return "output: "+input
with gr.Blocks() as demo:
    gr.Markdown("Hello, **world!**")
    with gr.Row():
        input=gr.Textbox()
        output=gr.Textbox(show_copy_button=True)
    
    run=gr.Button("Run")
    clear=gr.Button("Clear")
    event=run.click(output_txt,inputs=[input],outputs=[output])
    clear.click(lambda: ["",""],inputs=[],outputs=[input,output])
    


def start():
    try:
        command="nohup python main.py --cpu --listen  --port 7860 "
        process = subprocess.Popen(command, shell=True)
        print("start success----------------")
        time.sleep(60*30)
        print("end----------------")
    except Exception as e:
        print("start error: ",e)
        
start_thread = threading.Thread(target=start)
start_thread.start()
start_thread.join()

while True:
    print("loop...")
    demo.launch()
    # os.system(f"python main.py --cpu --listen ")
    time.sleep(10)