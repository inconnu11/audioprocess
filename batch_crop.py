import base64
import librosa
import soundfile as sf
import os


wav_path = '/Users/wangjie/Downloads/corpus/nus-smc-corpus_48/ADIZ/sing/18.wav'
data, samplerate = librosa.load(wav_path, sr=16000)
duration = len(data) / samplerate    # 单位是s
# print(duration)
# for i in range():
    # y = data[i : i + 80000]
y = data[:80000]
i = 19
nn = '18' + '_' + str(i)
sf.write(os.path.join('results/', f"{nn}.wav"), y, 16000, "PCM_16")






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

