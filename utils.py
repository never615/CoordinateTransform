import math
import os



# 获取指定目录下所有文件的路径
def all_path(dirname):
	postfix = {'geojson'}  # 设置要保存的文件格式

	filePaths = []
	for maindir, subdir, file_name_list in os.walk(dirname):
		for filename in file_name_list:
			apath = os.path.join(maindir, filename)
			# print(apath)
			if True:  # 保存全部文件名。若要保留指定文件格式的文件名则注释该句
				if apath.split('.')[-1] in postfix:  # 匹配后缀，只保存所选的文件格式。若要保存全部文件，则注释该句
					filePaths.append(apath)
	return filePaths


# 经纬度转墨卡托坐标
def ls(lat, lng):
	# list=ll_wl.split(',')
	lat = float(lat)
	lng = float(lng)
	x = lng * 20037508.34 / 180
	y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
	y = y * 20037508.34 / 180
	return str(x), str(y)


# 墨卡托坐标转经纬度坐标
def ll(x, y):
	x = float(x)
	y = float(y)
	x = x / 20037508.34 * 180
	y = y / 20037508.34 * 180
	y = 180 / math.pi * (2 * math.atan(math.exp(y * math.pi / 180)) - math.pi / 2)
	return x, y


if __name__ == '__main__':
	print(ls('30.697218', '104.073694'))
	print(ll('12985924.36', '4789962.05'))
