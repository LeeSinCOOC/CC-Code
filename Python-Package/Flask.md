## Flask 学习笔记
### 在IPv4中运行
```python
app.run(host='0.0.0.0', port=port, debug=True)
```
### 在IPv6中运行
```python
app.run(host='::', port=port, debug=True)
```

### 案例：获取视频并解帧
```python
from flask import Flask, request,jsonify
import imageio
import numpy as np
import skimage
import cv2

# from PIL import ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        video = request.files['mp4'].read()   # .save('cache.mp4')保存视频
        vid = imageio.get_reader(video, 'ffmpeg')
        for im in enumerate(vid):
            img = cv2.cvtColor(im[1], cv2.COLOR_RGB2BGR)
            cv2.imwrite('tmp.jpg',img)
        return str(0)
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8000, debug=True)
```