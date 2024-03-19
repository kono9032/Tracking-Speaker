import os
def playSound(callnum, chang_gu_num):
    def one(callnum, chang_gu_num):
        soundplaylist = [str(str(callnum) + ".wav"),"Hangul0.wav",str(str(chang_gu_num) + ".wav"),"Hangul1.wav"]
        print(soundplaylist)
        os.system("mpg123 " + "TTS_sounds/bell.mp3")
        for i in range(len(soundplaylist)):
            print(soundplaylist[i])
            os.system("aplay " + "TTS_sounds/"+ soundplaylist[i])
        soundplaylist.clear()

    def ten(callnum, chang_gu_num):
        print(callnum)

        if callnum == 10:
            soundplaylist = ["10.wav", "Hangul0.wav",str(str(chang_gu_num) + ".wav"),"Hangul1.wav"]

        elif str(callnum)[0] == str(1):
            soundplaylist = ["10.wav",str(str(callnum)[1] + ".wav"),"Hangul0.wav",str(str(chang_gu_num) + ".wav"),"Hangul1.wav"]
        else:
            soundplaylist = [str(str(callnum)[0] + ".wav"),"10.wav",str(str(callnum)[1] + ".wav"),"Hangul0.wav",str(str(chang_gu_num) + ".wav"),"Hangul1.wav"]

        os.system("mpg123 " + "TTS_sounds/bell.mp3")
        for i in range(len(soundplaylist)):
            print(soundplaylist[i])
            os.system("aplay " + "TTS_sounds/"+ soundplaylist[i])
        soundplaylist.clear()

    def hundred(callnum, chang_gu_num):
        soundplaylist = []

        if str(callnum)[0] == str(1):
            soundplaylist.append("100.wav")
        elif str(callnum)[0] != str(1):
            soundplaylist.append(str(str(callnum)[0] + ".wav"))
            soundplaylist.append("100.wav")

        if str(callnum)[1] == str(0) and str(callnum)[2] == str(0):
            pass
        elif str(callnum)[1] == str(0) and str(callnum)[2] != str(0):
            soundplaylist.append(str(str(callnum)[2] + ".wav"))

        if str(callnum)[1] == str(1) and str(callnum)[2] == str(0):
            soundplaylist.append("10.wav")
        elif str(callnum)[1] == str(1) and str(callnum)[2] != str(0):
            soundplaylist.append("10.wav")
            soundplaylist.append(str(str(callnum)[2] + ".wav"))

        if int(str(callnum)[1]) >= 2 and str(callnum)[2] == str(0):
            soundplaylist.append(str(str(callnum)[1] + ".wav"))
            soundplaylist.append("10.wav")
        elif int(str(callnum)[1]) >= 2 and str(callnum)[2] != str(0):
            soundplaylist.append(str(str(callnum)[1] + ".wav"))
            soundplaylist.append("10.wav")
            soundplaylist.append(str(str(callnum)[2] + ".wav"))

        print(soundplaylist)
        soundplaylist.append("Hangul0.wav")
        soundplaylist.append(str(str(chang_gu_num) + ".wav"))
        soundplaylist.append("Hangul1.wav")

        os.system("mpg123 " + "TTS_sounds/bell.mp3")
        for i in range(len(soundplaylist)):
            os.system("aplay " + "TTS_sounds/"+ soundplaylist[i])
        soundplaylist.clear()

    soundplaylist = []
    if len(str(callnum)) == 1:
        one(callnum, chang_gu_num)
    elif len(str(callnum)) == 2:
        ten(callnum, chang_gu_num)
    else:
        hundred(callnum, chang_gu_num)
