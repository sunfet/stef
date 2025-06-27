import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 检查并读取或生成 CSV 文件
csv_path = 'TEK00000.csv'
try:
    data = pd.read_csv(csv_path)
except FileNotFoundError:
    # 如果文件不存在，则生成一个示例数据并保存为 CSV
    data = pd.DataFrame({'CH1': [i * 0.1 for i in range(10000)]})
    data.to_csv(csv_path, index=False)

# 启用交互模式
plt.ion()

# 创建一个图形窗口
fig, ax = plt.subplots(figsize=(12, 6))
plt.subplots_adjust(bottom=0.25)  # 留出空间给滚动条

# 绘制波形图
line, = ax.plot(data['CH1'], label='CH1 Values')

# 设置标题和坐标轴标签
ax.set_title('Interactive Waveform Plot with Scrollbar')
ax.set_xlabel('Index')
ax.set_ylabel('CH1 Values')
ax.grid(True)

# 显示图例
ax.legend()

# 添加滚动条
ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(
    ax=ax_slider,
    label='View Position',
    valmin=0,
    valmax=len(data) - (ax.get_xlim()[1] - ax.get_xlim()[0]),
    valinit=0
)

# 定义滚动条回调函数
def update(val):
    pos = slider.val
    current_width = ax.get_xlim()[1] - ax.get_xlim()[0]
    ax.set_xlim([pos, pos + current_width])
    fig.canvas.draw_idle()

slider.on_changed(update)

# 添加缩放功能
zoom_factor = 1.5  # 缩放步长

def on_scroll(event):
    """处理鼠标滚轮事件以实现缩放"""
    cur_xlim = ax.get_xlim()
    cur_ylim = ax.get_ylim()
    
    # 如果鼠标不在图表区域内，则不进行缩放操作
    if event.xdata is None or event.ydata is None:
        return
    
    xdata = event.xdata  # 获取当前鼠标位置的x坐标
    ydata = event.ydata  # 获取当前鼠标位置的y坐标

    if event.button == 'up':
        # 放大
        scale_factor = 1 / zoom_factor
    elif event.button == 'down':
        # 缩小
        scale_factor = zoom_factor
    else:
        scale_factor = 1

    # 计算新的坐标范围
    new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
    new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

    relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
    rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])

    ax.set_xlim([xdata - new_width * (1 - relx), xdata + new_width * relx])
    ax.set_ylim([ydata - new_height * (1 - rely), ydata + new_height * rely])

    # 更新滚动条范围
    slider.valmax = len(data) - new_width
    slider.set_val(xdata - new_width * (1 - relx))

    fig.canvas.draw_idle()

# 连接滚动事件
fig.canvas.mpl_connect('scroll_event', on_scroll)

# 显示图形
plt.show(block=True)

# 将数据保存为 Excel 文件（使用 .xlsx 格式）
data.to_excel('TEK00000.xlsx', index=False)