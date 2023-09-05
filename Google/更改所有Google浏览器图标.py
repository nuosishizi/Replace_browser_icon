import os
import shutil

# 使用os模块获取当前脚本所在的目录作为源图标文件夹路径
source_icons_folder = os.path.dirname(os.path.abspath(__file__))# 替换为包含1.ico到100.ico的文件夹路径
# 使用双反斜杠
target_icons_folder = rf"C:\Users\{os.getenv('USERNAME')}\AppData\Local\Google\Chrome\User Data"  # 目标文件夹路径

# 获取当前用户的用户名
username = os.getenv('USERNAME')

# 遍历每个Profile文件夹路径
for profile_folder_name in os.listdir(target_icons_folder):
    profile_folder_path = os.path.join(target_icons_folder, profile_folder_name)
    
    # 检查是否为Profile文件夹
    if os.path.isdir(profile_folder_path):
        # 获取当前Profile文件夹的序号
        profile_number = profile_folder_name.split(" ")[-1]
        
        # 构建目标图标文件路径
        target_icon_name = f"Google Profile.ico"
        target_icon_path = os.path.join(profile_folder_path, target_icon_name)
        
        # 检查源图标文件是否存在
        source_icon_name = f"{profile_number}.ico"
        source_icon_path = os.path.join(source_icons_folder, source_icon_name)
        
        if os.path.exists(source_icon_path):
            # 复制并覆盖目标图标文件
            shutil.copy(source_icon_path, target_icon_path)
            print(f"复制并覆盖 {source_icon_name} 到 {target_icon_path}")

print("完成任务！")
