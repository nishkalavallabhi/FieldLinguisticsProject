"""
Purpose is to get the closest sound to the given sound from the IPA sounds inventory
Uses opensmile for getting sound file audio features, and returns the nearest IPA sounds using KDTree

I am running this file from OpenSmile Installation folder. 
"""

import sys,subprocess,os,math
from scipy import spatial

#Extracts opensmile features for all IPA sounds, and stores them in disk
#This has to be run once, and the results are stored in the ipa-features file. 
def store_features_IPA(dir_path):
   files = os.listdir(dir_path)
   fw = open("ipa-features","w") #a file to store audio features for all IPA sounds in the folder.
   for f in files:
       fpath = os.path.join(dir_path,f)
       #script features-python.sh takes 1 argument. a wav file. 
       #subprocess execution returns bytes, so decode to utf8
       out = subprocess.check_output(['sh', 'features-python.sh',fpath]).decode("utf-8")
       temp = out.split(",")
       #we need all columns in opensmile output except first and the last ones.
       to_write = f.split(".mp3")[0]+","+ ",".join(temp[1:len(temp)-2])
       fw.write(to_write)
       fw.write("\n")
       print("Wrote features for: ", f)
   fw.close()

#get opensmile features for the input audio file.
def get_features(file_path): #Full file path. 
    out = subprocess.check_output(['sh', 'features-python.sh',file_path]).decode("utf-8")
    temp = out.split(",")
    return [float(i) for i in temp[1:len(temp)-2]]

#load ipa features file into program, and save it as two lists - one containing sound names, one with sound features
def load_features_IPA(ipa_features_path):
    fh = open(ipa_features_path)
    sounds = []
    features = []
    for line in fh:
       what_we_need = line.split(",")
       sounds.append(what_we_need[0])
       features.append([float(i) for i in what_we_need[1:]])
    return sounds,features

#use KDTree to quickly calculate similarity and get the closest ipa sound to the input file.
def get_similar_sounds(sound_feat,ipafeats,sounds):
    tree = spatial.KDTree(ipafeats) #use k=i to get i nearest neighbors instead of the closest one.
    return sounds[tree.query(sound_feat)[1]]
   
#dir_path = str(sys.argv[1])
#store_features_IPA(dir_path)

wav_path = "/home/bangaru/Dropbox/myresearchstuff/IPAMp3s/IPA-WAV/apical_VL_alveolar_plosive.mp3.wav" #sys.argv[1]
ipasounds,ipafeats = load_features_IPA("ipa-features")
print(get_similar_sounds(get_features(wav_path),ipafeats,ipasounds))

