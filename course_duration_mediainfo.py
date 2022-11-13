import os
import cv2
import datetime
import re
from pymediainfo import MediaInfo


base_path = "E:\Courses\Web Development\[FreeCourseSite.com] Udemy - React - The Complete Guide (incl Hooks, React Router, Redux)"
course_name = base_path.split('\\')[-1]
dirTree = next(os.walk(base_path))[1]


def convert_millis(millis):
    seconds = round(millis/1000)%60
    minutes = round(millis/(1000*60))%60
    hours = round(millis/(1000*60*60))%24
    return f'{hours}:{minutes}:{seconds}'

'''
for sub_dir in dirTree:
    current_dir = f'{base_path}\\{sub_dir}'
    for file in os.listdir(current_dir):
        if any(x in file for x in ('.mp4', '.mkv')):
            video_path = f'{current_dir}\\{file}'
            duration = max([float(track.duration) for track in MediaInfo.parse(video_path).tracks])
            print(f"{file} | {duration}")
'''


def course_folders_filter(dir_tree):
    for dir_name in dir_tree:
        if (dir_name.split(' ')[0][0]).isnumeric():
            continue
        else:
            dirTree.remove(dir_name)


def course_duration(dir_tree, course_n):
    with open(f"{course_n}_duration.txt", "w") as text_file:
        duration = 0
        for sub_dir in dirTree:
            current_dir = f'{base_path}\\{sub_dir}'
            for file in os.listdir(current_dir):
                if any(x in file for x in ('.mp4', '.mkv')):
                    video_path = f'{current_dir}\\{file}'
                    duration += max([float(track.duration) for track in MediaInfo.parse(video_path).tracks])
        seconds = duration/1000
        minutes = int(seconds/60)
        re_sec = int(seconds%60)
        re_min = int(minutes%60)
        hours = int(minutes/60)
        text_file.write(f"Course duration = {hours}h {minutes}m {seconds}s")
    print('Duration Calc finished with Success!!!')


def course_video_list(course_tree, course_n):
    with open(f"{course_n}.txt", "w") as text_file:
        for sub_dir in dirTree:
            # text_file.write("Purchase Amount: %s" % TotalAmount)
            text_file.write(f'------------------ {sub_dir} ------------------\n')
            current_dir = f'{base_path}\\{sub_dir}'
            for file in os.listdir(current_dir):
                # if '.mp4' in file:
                if any(x in file for x in ('.mp4', '.mkv')):
                    video_path = f'{current_dir}\\{file}'
                    data = cv2.VideoCapture(video_path)
                    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
                    fps = data.get(cv2.CAP_PROP_FPS)
                    if fps != 0:
                        seconds = round(frames / fps)
                    else:
                        print(f'{video_path} -- frames={frames} -- fps={fps}')
                    video_time = datetime.timedelta(seconds=seconds)
                    text_file.write(f"{file.replace('.mp4','')} | {str(video_time).replace('0:','')}\n")
    print('Videos List Extraction finished with success')


course_folders_filter(dirTree)
course_duration(dirTree, course_name)
# course_video_list(dirTree, course_name)