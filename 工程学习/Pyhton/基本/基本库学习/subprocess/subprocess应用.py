import subprocess

# 使用 'dir' 命令列出文件
result = subprocess.run(["dir"], capture_output=True, text=True, shell=True)

# 打印输出
print(f"STDOUT: {result.stdout}")
print(f"STDERR: {result.stderr}")

# 检查返回码
print(f"Return code: {result.returncode}")
