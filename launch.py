import os
os.system("pwd")
os.system("ls -la")
print("---------------launch.py-----------------------")
os.system("git clone https://github.com/comfyanonymous/ComfyUI")

os.chdir("ComfyUI")

os.system("pip install -r requirements.txt")
os.chdir("models/checkpoints")
os.system("wget https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors")
os.system("wget https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors")
os.chdir("../upscale_models")
os.system("wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-general-x4v3.pth")
os.chdir("../clip_vision")
os.system("wget https://huggingface.co/comfyanonymous/clip_vision_g/resolve/main/clip_vision_g.safetensors")
os.chdir("../..")
os.system("ls -la")
print("----------------start app_start.py----------------------")

os.system(f"python main.py --cpu --listen")