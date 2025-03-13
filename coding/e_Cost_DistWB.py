-*- coding: utf-8 -*-
import arcpy
import os
import os
def get_subfolder_names(parent_folder):
    if not os.path.isdir(parent_folder):
        raise FileNotFoundError("The directory {} does not exist".format(parent_folder))

    # 获取所有子文件夹的名字
    subfolders = [f for f in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, f))]

    return subfolders

parent_folder = r'D:\file\a_clip_data\city_SHP\b_output_final_tem'
places = get_subfolder_names(parent_folder)
places2=[]
for place in places:
    place1= os.path.splitext(place)[0]
    place2 = place1.split('_')[-1]
    places2.append(place2)
print(places)
print(places2)

for place2 in places2:
    # 输入数据
    cost_surface = r"D:\file\d_zonalst\{}\water\water_cropped_Extract_{}.shp".format(place2, place2)
    destination_data = r"D:\file\d_zonalst\{}\water\{}_process.tif".format(place2, place2)  # 成本栅格文件路径

    # 输出路径，设置为文件系统中的一个目录
    output_cost_distance = r"D:\file\d_zonalst\{}\water\{}_cost_DistWB.tif".format(place2, place2)   # 输出路径

    # 检查输出文件是否已存在，如果存在则删除
    if os.path.exists(output_cost_distance):
        print("输出文件已存在，将覆盖: {}".format(output_cost_distance))
        os.remove(output_cost_distance)  # 删除现有文件
    else:
        print("输出文件不存在，将创建: {}".format(output_cost_distance))

    # 执行 CostDistance
    try:
        print("正在处理第 {} 个文件...".format(place2))
        arcpy.gp.CostDistance_sa(cost_surface, destination_data, output_cost_distance, "", "", "", "", "", "", "")
        print("第 {} 个文件处理完成: {}".format(place2, output_cost_distance))
    except Exception as e:
        print("处理第 {} 个文件时出错: {}".format(place2, e))

print("所有文件处理完成。")
