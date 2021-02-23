#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jie Wang @ 2021-02-23
import base64
import librosa
import soundfile as sf
import os
from math import *


# wav_path = '/Users/wangjie/Downloads/corpus/nus-smc-corpus_48/ADIZ/sing/18.wav'
# rootDir = '/Users/wangjie/Downloads/corpus/nus-smc-corpus_48'
rootDir = '/workspace/project-nas-10801-sh/datasets/nus_16k'
# targetDir = '/Users/wangjie/Downloads/corpus/nus-smc-corpus_48/five_second'
targetDir = '/workspace/project-nas-10801-sh/datasets/five_seconds'
dirName, subdirList, _ = next(os.walk(rootDir))
for subdir in sorted(subdirList):    # 说话人list
    # print(subdir)
    if not os.path.exists(os.path.join(targetDir, subdir)):
        os.makedirs(os.path.join(targetDir, subdir))
    
    _, _, fileList = next(os.walk(os.path.join(dirName, subdir)))
    for fileName in sorted(fileList):
        # print(fileName)
        # x, fs = sf.read(os.path.join(dirName,subdir,fileName))
        wav_path = os.path.join(dirName,subdir,fileName)
        data, samplerate = librosa.load(wav_path, sr=16000)
        duration = len(data) / samplerate    # 单位是s
        print(duration)
        segments = floor(duration / 5)
        print(segments)
        for i in range(1, segments + 1):
            print(i)
            if i * 16000 >= duration:
                y = data[ (i - 1) * 16000 :]
            else: 
                y = data[(i - 1) * 16000: i * 16000]
            print(y)
            nn = fileName[:-4] + '_' + str(i)
            # librosa.output.write_wav('results/' + nn + '.wav', waveform_NOP, sr=16000)
            save_path = os.path.join(targetDir, subdir) 
            sf.write(os.path.join(save_path, f"{nn}.wav"), y, 16000, "PCM_16")
# print(duration)
# for i in range():
    # y = data[i : i + 80000]
# y = data[:80000]
# i = 19
# nn = '18' + '_' + str(i)
# sf.write(os.path.join('results/', f"{nn}.wav"), y, 16000, "PCM_16")


# print(data, samplerate, '{:.2f}s'.format(duration))
# with open(wav_path, 'rb') as f:
#     buff = f.read()
#     buff = buff[:78] + buff[64000:]
#     # buff = buff[:32078] #将音频切分为你想要的长度，这里是1s（需包含RIFF头）
# buff_str = base64.b64encode(buff).decode()
# print(type(buff_str))
# buff = base64.b64decode(buff_str)
# data, samplerate = librosa.load(io.BytesIO(buff), sr=16000)
# print(len(data)) # 这个例子里是 1s, 即为16000
# duration = len(data) / samplerate
# print(data, samplerate, '{:.2f}s'.format(duration))


