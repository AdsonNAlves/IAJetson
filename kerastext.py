import keras_ocr
import pandas as pd
import matplotlib.pyplot as plt
import glob as glob
pipeline = keras_ocr.pipeline.Pipeline()

image = '/home/jetson/Desktop/cursoia/work/remedios.jpeg'
result = pipeline.recognize([image])
df = pd.DataFrame(result[0])# , columns=['text', 'bbox']
print(df)
fig, ax = plt.subplots(figsize=(10, 10))
keras_ocr.tools.drawAnnotations(plt.imread(image), result[0], ax=ax)
ax.set_title('Keras OCR Result Example')
plt.show()