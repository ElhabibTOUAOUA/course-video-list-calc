import os
import cv2
import datetime
import re
import tqdm

def remove_non_video_files(files):
	VIDEO_FILE_PATTERN = r'.*\.(mp4|mkv|avi|flv|mov|wmv|vob|mpg|3gp|m4v)$'
	return [file for file in files if re.match(VIDEO_FILE_PATTERN, file)]

def sort_list(unsorted_list):
	# Split the list elements into a list of lists, where each inner list
	# contains the element number, split character, and element name
	lst = []
	for item in unsorted_list:
	# Find the split character using a regular expression
		split_char = re.search(r'[^\d][\d]*(?=\D)', item).group()

		# Split the element into the element number, split character, and element name
		item_num, item_name = item.split(split_char, 1)
		lst.append([int(item_num), item_num,split_char, item_name])
		
	# Sort the list by element number
	lst.sort(key=lambda x: x[0])
	# Build the sorted list by combining the element number, split character, and element name
	sorted_list = [f"{item[1]}{item[2]}{item[3]}" for item in lst]
	return sorted_list

def remove_non_numeric_elements(lst):
	return [item for item in lst if item[0].isdigit()]

def course_duration(course_path, course_name):
	with open(f"Output/Courses Duration/{course_name}_duration.txt", "w") as text_file:
			seconds = 0
			dirs = os.listdir(course_path)
			dirs = remove_non_numeric_elements(dirs)
			dirs = sort_list(dirs)
			for dir in dirs:
					current_dir = os.path.join(course_path, dir)
					files = os.listdir(current_dir)
					files = remove_non_numeric_elements(files)
					files = remove_non_video_files(files)
					files = sort_list(files)
					# print(f"Sorted Files: {files}")
					for file in tqdm.tqdm(files, desc='Calculating duration'):
						video_path = os.path.join(current_dir, file)
						try:
								data = cv2.VideoCapture(video_path)
								frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
								fps = data.get(cv2.CAP_PROP_FPS)
								if fps != 0:
										seconds += round(frames / fps)
								else:
										print(f'\n{video_path} -- frames={frames} -- fps={fps}')
						except Exception as e:
								print(f'Error while processing {video_path}: {e}')
			hours = int(seconds / 3600)
			minutes = int(seconds / 60) % 60
			text_file.write(f"Course duration = {hours}h {minutes}m")
	print('Duration Calc finished with Success!!!')

def course_video_list(course_path, course_name):
	with open(f"Output/Courses Video lists/{course_name}.txt", "w") as text_file:
			dirs = os.listdir(course_path)
			dirs = remove_non_numeric_elements(dirs)
			dirs = sort_list(dirs)
			for dir in dirs:
					# Write the current directory name to the file
					text_file.write(f'------------------ {dir} ------------------\n')
					current_dir = os.path.join(course_path, dir)
					files = os.listdir(current_dir)
					files = remove_non_numeric_elements(files)
					files = remove_non_video_files(files)
					files = sort_list(files)
					for file in tqdm.tqdm(files, desc='Extracting video list'):
							seconds = 0
							video_path = os.path.join(current_dir, file)
							data = cv2.VideoCapture(video_path)
							frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
							fps = data.get(cv2.CAP_PROP_FPS)
							if fps != 0:
									seconds = round(frames / fps)
							else:
									print(f'\n{video_path} -- frames={frames} -- fps={fps}')
							video_time = datetime.timedelta(seconds=seconds)
							formatted_time = '{:02d}:{:02d}'.format(video_time.seconds // 60, video_time.seconds % 60)
							# Write the file name and duration to the file
							text_file.write(f"{file.replace('.mp4', '')} | {formatted_time}\n")
	print('Videos List Extraction finished with success')


def course_duration_list(course_name):
	base_path = os.path.join("E:\\","Courses", "Web Development",course_name)
	course_name = base_path.split('\\')[-1]
	course_duration(base_path, course_name)
	course_video_list(base_path, course_name)

if __name__ == '__main__':
	courses_dir = os.path.join("E:\\","Courses", "Web Development")
  
  # uncomment the next line if you want to process just one course
  # course_duration_list("Node.js - The Complete Guide (incl. MVC, REST APIs, GraphQL)")

	courses = [course for course in os.listdir(courses_dir) if os.path.isdir(os.path.join(courses_dir, course))]
	for course in courses:
			print("\n=============================================")
			print(f"Processing {course}")
			course_duration_list(course)
