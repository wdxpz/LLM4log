import matplotlib.pyplot as plt
import numpy as np

# IP precision
# x: chunk size
labels = ["192k","128k"]

count = [0.899,0.797]
correct_count = [0.984-0.899, 0.987-0.797]
extraction = [0.872,0.755]
correct_extraction = [0.991-0.872,0.994-0.755]

x = np.arange(len(labels)) # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots()


rects1 = ax.bar(x - width/2, count, width, label='Count')
rects2 = ax.bar(x + width/2, extraction, width, label='Extraction')
rects3 = ax.bar(x - width/2, correct_count,width,bottom=count, label='Correction')
rects4 = ax.bar(x + width/2, correct_extraction,width,bottom=extraction, label='Correction')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('IP Precision')
ax.set_xlabel('Chunk Size')
ax.set_title('IP Precision by Chunk Size')
ax.set_xticks(x,labels)
ax.legend(loc = "lower right")



ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)
ax.bar_label(rects4, padding=3)

fig.tight_layout()
plt.ylim(ymin=0.5)
plt.show()