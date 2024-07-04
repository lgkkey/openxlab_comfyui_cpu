import os
os.system("pwd")
os.system("ls -la")
print("--------------------------------------")

# 更新文件
root_path="/home/xlab-app-center"
launch="https://raw.githubusercontent.com/lgkkey/openxlab_comfyui_cpu"

if (os.path.exists(f"{root_path}/openxlab_comfyui_cpu")):
    print("openxlab_comfyui_cpu exists")
    os.system(f"rm -rf {root_path}/openxlab_comfyui_cpu")

print(f"git clone {launch}")
os.system(f"git clone {launch}")

if (os.path.exists(f"{root_path}/launch.py")):
    print("launch.py exists")
    os.system(f"rm -rf {root_path}/launch.py")
    os.system(f"cp {root_path}/openxlab_comfyui_cpu/launch.py {root_path}/launch.py")
    os.system(f"cat {root_path}/launch.py")
    print("launch.py update success")
    print("--------------------------------------")
    
os.system("ls -la")
print("----------------start launch.py----------------------")
os.chdir(root_path)

os.system("python launch.py")