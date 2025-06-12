import os
import subprocess
import time

root_path="/home/xlab-app-center"

os.chdir(root_path)
os.system("git clone https://github.com/comfyanonymous/ComfyUI")

os.chdir("ComfyUI")

os.system("pip install -r requirements.txt")
os.chdir("models/checkpoints")
os.system("wget -c https://hf-mirror.com/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors")
os.system("wget -c https://hf-mirror.com/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors")
os.chdir("../upscale_models")
os.system("wget -c https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-general-x4v3.pth")
os.chdir("../clip_vision")
os.system("wget -c https://hf-mirror.com/comfyanonymous/clip_vision_g/resolve/main/clip_vision_g.safetensors")
os.chdir("../..")
os.system("ls -la")
print("----------------start app_start.py----------------------")


command="nohup python main.py --cpu --listen  --port 7861 "
process = subprocess.Popen(command, shell=True)

while True:
    # 查看端口7861是否被占用
    result = subprocess.run(["ps","-ef"], capture_output=True, text=True)
    #搜索是否存在 " python main.py --cpu --listen  --port 7861"
    if "python main.py --cpu --listen  --port 7861" in result.stdout:
        print("端口已占用")
        time.sleep(60*30)
    else:
        # 端口未被占用，跳出循环
        time.sleep(60*10)
        process = subprocess.Popen(command, shell=True)