
from remover import Remover
import os


input_path = '/Users/crisschan/workspace/PySpace/video_merge_audio/input'
out_path ='/Users/crisschan/workspace/PySpace/video_merge_audio/output'
tmp_path = '/Users/crisschan/workspace/PySpace/video_merge_audio/tmp'
Remover.dir_under(input_path)
Remover.dir_under(out_path)
Remover.dir_under(tmp_path)
os.mkdir(input_path)
os.mkdir(out_path)
os.mkdir(tmp_path)


