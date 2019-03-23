# Exif-Editor
Edit photos time information in exif 

看到[小众软件的微博](https://weibo.com/1684197391/Hmg0aq7du?from=page_1006061684197391_profile&wvr=6&mod=weibotime&type=comment#_rnd1553342415013)有个朋友想要根据文件名修改照片的Exif，于是用python写了一个简单的小工具。

# 使用方法
代码里面使用了`piexif`库，所以要先安装依赖。
```python
pip install -r requirements.txt
```
然后在图片目录下运行py文件就好
```python
python exifeditor.py
```
文件名的格式是在代码里面确定的，如果格式有变化，修改py文件第5行`datetime.strptime('20' + filename, r'%Y-%m-%d_%H%M')`的两个参数即可。
