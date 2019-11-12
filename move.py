import os
import shutil
filedir = './input'
outdir_a = '../../FCNorigin/FCNchange.tensorflow/Data_zoo/MIT_SceneParsing/ADEChallengeData2016/annotations'
outdir_i = '../../FCNorigin/FCNchange.tensorflow/Data_zoo/MIT_SceneParsing/ADEChallengeData2016/images'
filelists = os.listdir(filedir)
filelists.sort()
for i,filename in enumerate(filelists):
	print(filename)
	filename = os.path.join(filedir, filename)

	shutil.copy(os.path.join(filename,'label.png'),os.path.join(outdir_a,'training'))
	name1 = 'train-' + str(i+1).zfill(3) + '.png'

	os.rename(os.path.join(outdir_a,'training/label.png'),os.path.join(outdir_a,'training',name1))


	shutil.copy(os.path.join(filename,'img.png'),os.path.join(outdir_i,'training'))
	name2 = 'train-' + str(i+1).zfill(3) + '.png'
	os.rename(os.path.join(outdir_i,'training/img.png'),os.path.join(outdir_i,'training',name2))
