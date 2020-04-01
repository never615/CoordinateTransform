import json
import os
from utils import all_path, ll, ls
import shutil
import chardet
from chardetUtils import *

print('----------- start -------------')

# 删除result下的文件
shutil.rmtree('./result')
os.mkdir('./result')

# 读取data下以geojson结尾的文件
dataFilePaths = all_path('./data')
for dataFilePath in dataFilePaths:
	resultPath = dataFilePath.replace("/data/", "/result/")
	print(dataFilePath)
	print(detectCode(dataFilePath))
	with open(dataFilePath, 'r', encoding="{0}".format(detectCode(dataFilePath))) as f:
		data = f.read()
		data = data.encode("utf-8")  # 将文件内容转化为utf-8格式
		# print(data)
		data = json.loads(data)
		# print(data['type'])
		features = data['features']
		for index, feature in enumerate(features):
			# print(feature)
			geometry = feature['geometry']
			geometry_type = geometry['type']
			geometry_coordinates = geometry['coordinates']
			if geometry_type == 'point':
				x = geometry_coordinates[0]
				y = geometry_coordinates[1]
				# print(x, y, sep=',')
				longitude, latitude = ll(x, y)
				# print(longitude, latitude, sep=',')
				geometry['coordinates'] = [longitude, latitude]
				feature['geometry'] = geometry
			# print(feature)
			elif geometry_type == 'Polygon':
				geometry_coordinates0 = geometry_coordinates[0]
				# print(geometry_coordinates0)
				new_geometry_coordinates0 = []
				for geometry_coordinate0 in geometry_coordinates0:
					x = geometry_coordinate0[0]
					y = geometry_coordinate0[1]
					# print(x, y, sep=',')
					longitude, latitude = ll(x, y)
					new_geometry_coordinates0.append([longitude, latitude])
				geometry['coordinates'] = [new_geometry_coordinates0]
				feature['geometry'] = geometry
			features[index] = feature

		data['features'] = features
		# print(features)

		path, file = os.path.split(resultPath)
		# print(path)
		if not os.path.exists(path):
			os.makedirs(path)
		with open(resultPath, 'w') as f:
			json.dump(data, f, indent=4)  # 和上面的效果一样

print('----------- finish -------------')
