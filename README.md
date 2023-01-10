# VideoCourseListAndDuration

A Python script that helps in calculating the duration of a course, which is provided in the form of videos and it lists the videos in a course as well.

## Requirements

-   openCV
-   os
-   datetime
-   re
-   tqdm

## Functionality

### `remove_non_video_files(files)`

This function filters out the non-video files from the given list of files. It uses a regular expression to match the file names with the pattern of common video file extensions such as mp4, mkv, avi, flv, mov, wmv, vob, mpg, 3gp, and m4v.

### `sort_list(unsorted_list)`

This function sorts the given list of items in the format of 'element number' + 'split character' + 'element name'

### `remove_non_numeric_elements(lst)`

This function removes the non-numeric elements from the given list.

### `course_duration(course_path, course_name)`

This function calculates the duration of the course by traversing through the directories and files in the given course path and extracting the duration of each video using openCV's `VideoCapture` class. The duration is calculated by counting the total number of frames in the video and dividing it by the frame rate of the video. The calculated duration is written to a text file with the name format 'course_name_duration.txt' in the Output/Courses Duration folder.

### `course_video_list(course_path, course_name)`

This function lists the videos in a course by traversing through the directories in the given course path. It writes the list of videos to a text file with the name format 'course_name.txt' in the Output/Courses Video lists folder.

## Usage

```python
course_path = 'path/to/course'
course_name = 'example_course'
course_duration(course_path, course_name)
course_video_list(course_path, course_name)
```

## Output

The script will generate two text files, one for duration and the other for videos list, in the Output folder.

## Note

-   The script assumes that the course is provided in the format of directories containing videos and the videos are named in the format of 'element number' + 'split character' + 'element name'
-   The script assumes that the output folders ('Output/Courses Duration/' and 'Output/Courses Video lists/') already exist.
-   It's recommended to run the script on a high-performance machine because of the heavy computation required for processing video frames.
-   It may be necessary to adjust the regular expression in the remove_non_video_files function to match your specific naming conventions.
-   It's a good practice to verify the output files to check the correctness of the calculated duration and video list.
-   The script doesn't currently handle errors that may occur while reading the video files, such as file not found errors, and it may be necessary to add error handling to the script to handle such scenarios.
-   It could be wise to check if the folder where the files are being written to are present, if not, you could make those folders on runtime for the code to work seamlessly.
