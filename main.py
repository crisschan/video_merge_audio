from merge_audio import MergeAudio
from get_dirAndfiles import DirAndFiles
from video_merge_audio import VideoMergeAudio
from pic2video import Pic2Video
from moviepy import *
from moviepy.audio.io.AudioFileClip import AudioFileClip
from remover import Remover
# 设置输入输出目录
input_path = '/Users/crisschan/workspace/PySpace/video_merge_audio/input'
out_path ='/Users/crisschan/workspace/PySpace/video_merge_audio/output'
tmp_path = '/Users/crisschan/workspace/PySpace/video_merge_audio/tmp'
# 获取输入的音频和视频文件
df = DirAndFiles()
audios = df.filesWithFilter(input_path,'.flac')
# pics = df.filesWithFilter(input_path,'.png')




# 合并音频
merge_audio = MergeAudio(audios,output_audio = tmp_path+'/output_audio.mp3')
merge_audio.merge_audio()
# 生成视频
audioclip = AudioFileClip(tmp_path+'/output_audio.mp3')

Pic2Video(input_path,out_file_path=tmp_path+'/video_tmp.mp4',fps=24,size=(1280,720),duration=audioclip.duration).pic2video()



# 给视频加背景音
# video = df.filesWithFilter(tmp_path,'.mp4')
vma = VideoMergeAudio(tmp_path+'/video_tmp.mp4',tmp_path+'/output_audio.mp3',out_file_path =out_path+'/out.mp4',duration_flag=1)
vma.merge()

# # 清理文件
# Remover.dir_under(input_path+'/')
# Remover.dir_under(out_path+'/')
# Remover.dir_under(tmp_path+'/')