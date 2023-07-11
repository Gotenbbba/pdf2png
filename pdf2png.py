import os
import fitz

def pdf_image(pdfPath, imgPath, zoom_x, zoom_y, rotation_angle):
    pdf = fitz.open(pdfPath) # 打开PDF文件
    os.makedirs(imgPath, exist_ok=True)  # 创建保存图像文件的文件夹
    for pg in range(pdf.page_count): # 遍历每一页
        page = pdf[pg] # 获取当前页对象
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle) # 设置缩放和旋转
        pm = page.get_pixmap(matrix=trans, alpha=False) # 生成图片对象
        imgFilePath = os.path.join(imgPath, f"{pg}.png") # 图像文件保存路径
        pm.save(imgFilePath) # 保存图片

pdf_image("/Users/chronicat/Desktop/Problemset11.pdf", "/Users/chronicat/Desktop/test", 16, 16, 0) #pdf路径，保存png文件夹路径，放大倍数
