#!usr/bin/python3 
import os 
fileids = open("./etc/ara_train.fileids","w")
transcription = open("./etc/ara_train.transcription","w")
filesp = os.popen("ls wav").read()

for i in filesp.split("\n"): 
	if i != "" : 
		filwav = os.popen("ls wav/"+i+" -t").read()
		for j in filwav.split("\n"):
			if j != "" :
				name=j[:len(j)-5]
				transcription.write("<s> "+j[:len(j)-5]+" </s> ("+j[:len(j)-4]+")\n")
				fileids.write(i+"/"+j[:len(j)-4]+"\n")
				os.system("cd wav/"+i+"&& yes Y|ffmpeg -i "+j+" -acodec pcm_s16le -ar 16000 "+j)

fileids.close()
transcription.close()
