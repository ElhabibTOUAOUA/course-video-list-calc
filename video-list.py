import os
import cv2
import datetime
# import re

base_path = "E:\Courses\The Coding Interview Bootcamp Algorithms  Data Structures"
course_name = base_path.split('\\')[-1]
dirTree = next(os.walk(base_path))[1]
video_formats = ['.mp4', '.mkv']


def convert_millis(millis):
    seconds = round(millis / 1000) % 60
    minutes = round(millis / (1000 * 60)) % 60
    hours = round(millis / (1000 * 60 * 60)) % 24
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


'''
COURSE DURATION CALC FUNCTION 
    * This function takes a course folder on a specific provided path 
    * it browse all the folders in the course and calc only the video files with the format "mp4 or mkv". 
    * other video formats can be added to the array of formats. 
    * this function only works when a course direct folder is provided that container other folders with videos. 
    exp: Udemy - Advanced CSS and Sass Flexbox, Grid, Animations and More/04 Introduction to Sass and 
    NPM/001 Section Intro.mp4 
    * the output is a txt file with the name of the course and the duration
'''


def course_duration(dir_tree, course_n):
    with open(f"Output/{course_n}_duration.txt", "w") as text_file:
        seconds = 0
        for sub_dir in dirTree:
            current_dir = f'{base_path}\\{sub_dir}'
            for file in os.listdir(current_dir):
                if any(x in file for x in video_formats):
                    video_path = f'{current_dir}\\{file}'
                    # print(video_path)
                    data = cv2.VideoCapture(video_path)
                    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
                    # print(frames)
                    fps = data.get(cv2.CAP_PROP_FPS)
                    # print(fps)
                    if fps != 0:
                        seconds += round(frames / fps)
                    else:
                        print(f'{video_path} -- frames={frames} -- fps={fps}')
        hours = int(seconds / 3600)
        minutes = int(seconds / 60) % 60
        text_file.write(f"Course duration = {hours}h {minutes}m")
    print('Duration Calc finished with Success!!!')


'''
COURSE VIDEO LIST EXTRACTION FUNCTION 
    * This function takes a course folder on a specific provided path 
    * it browse all the folders in the course and extract only the video files with the format "mp4 or mkv". 
    * other video formats can be added to the array of formats. 
    * this function only works when a course direct folder is provided that container other folders with videos. 
    exp: Udemy - Advanced CSS and Sass Flexbox, Grid, Animations and More/04 Introduction to Sass and 
    NPM/001 Section Intro.mp4 
    * the output is a txt file with the name of the subfolder plus all the videos in it each with its duration 
'''


def course_video_list(course_tree, course_n):
    with open(f"Output/{course_n}.txt", "w") as text_file:
        for sub_dir in dirTree:
            # text_file.write("Purchase Amount: %s" % TotalAmount)
            text_file.write(f'------------------ {sub_dir} ------------------\n')
            current_dir = f'{base_path}\\{sub_dir}'
            for file in os.listdir(current_dir):
                # if '.mp4' in file:
                if any(x in file for x in video_formats):
                    video_path = f'{current_dir}\\{file}'
                    data = cv2.VideoCapture(video_path)
                    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
                    fps = data.get(cv2.CAP_PROP_FPS)
                    if fps != 0:
                        seconds = round(frames / fps)
                    else:
                        print(f'{video_path} -- frames={frames} -- fps={fps}')
                    video_time = datetime.timedelta(seconds=seconds)
                    text_file.write(f"{file.replace('.mp4', '')} | {str(video_time).replace('0:', '')}\n")
    print('Videos List Extraction finished with success')


course_folders_filter(dirTree)
course_duration(dirTree, course_name)
course_video_list(dirTree, course_name)
