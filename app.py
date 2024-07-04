import os
os.system("pwd")
os.system("ls -la")
print("--------------------------------------")

# 更新文件
root_path="/home/xlab-app-center"
launch="https://github.com/lgkkey/openxlab_comfyui_cpu/blob/main/launch.py"

if (os.path.exists(f"{root_path}/launch.py")):
    print("launch.py exists")
    os.system(f"rm -rf {root_path}/launch.py")

print(f"wget -c -o launch.py  --no-check-certificate {launch}")
os.system(f"wget -c -o launch.py  --no-check-certificate {launch}")

if (os.path.exists(f"{root_path}/launch.py")):
    print("launch.py update success")
    os.system(f"cat {root_path}/launch.py")
    print("--------------------------------------")
    
os.system("ls -la")
print("----------------start launch.py----------------------")
os.chdir(root_path)

os.system("python launch.py")