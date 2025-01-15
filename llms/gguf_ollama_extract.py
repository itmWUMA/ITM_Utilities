import os
import pathlib

# 获取脚本所在目录
current_dir = pathlib.Path(__file__).parent

# 遍历目录下所有.gguf文件
for gguf_file in current_dir.glob("*.gguf"):
    # 构建对应的.mf文件路径
    mf_file = gguf_file.with_suffix(".mf")
    
    # 如果.mf文件不存在，则创建
    if not mf_file.exists():
        # 写入FROM语句
        with open(mf_file, "w") as f:
            f.write(f"FROM {gguf_file.name}")
        print(f"Created manifest file for {gguf_file.name}")

print("Process completed.") 