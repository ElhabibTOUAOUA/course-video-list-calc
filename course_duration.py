import os
import cv2
import datetime

base_path = "E:\Courses\Self Development Courses\10X SUPERHUMAN Focus Maximize Your Brain & Focus 2020-11"
course_name = base_path.split('\\')[-1]
dirTree = next(os.walk(base_path))[1]


for dir_name in dirTree:
    if (dir_name.split(' ')[0][0]).isnumeric():
        continue
    else:
        dirTree.remove(dir_name)

with open(f"{course_name}_duration.txt", "w") as text_file:
    duration = 0
    for sub_dir in dirTree:
        current_dir = f'{base_path}\\{sub_dir}'
        for file in os.listdir(current_dir):
            if any(x in file for x in ('.mp4', '.mkv',)):
                video_path = f'{current_dir}\\{file}'
                # print(video_path)
                data = cv2.VideoCapture(video_path)
                fps = data.get(cv2.CAP_PROP_FPS)
                frames = int(data.get(cv2.CAP_PROP_FRAME_COUNT))
                # print(frames)
                # print(fps)
                if frames != 0 and fps != 0:
                    duration += frames / fps
    hours = int(duration / 3600)
    minutes = int(duration / 60) % 60
    text_file.write(f"Course duration = {hours}h {minutes}m")

