import piexif, os
from datetime import datetime

def filename2date(filename):
        date = datetime.strptime('20' + filename, r'%Y-%m-%d_%H%M')
        return date.strftime(r'%Y:%m:%d %H:%M')

def editexif(date, file):
        exif_dict = piexif.load(file)
        exif_dict['Exif'][36867] = date
        exif_byte = piexif.dump(exif_dict)
        piexif.insert(exif_byte, file)

if __name__ == "__main__":
    files = os.listdir('.')
    for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                    filename = os.path.splitext(file)[0]
                    date = filename2date(filename)
                    editexif(date, file)

