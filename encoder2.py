
class Encoder:
 


    def encode(self, text):
        listConf = []
        position = 0
        wordMap = {}
        for character in text:
            position+=1
            if not character in listConf:
                listConf.append(character)
                wordMap[character] = [position]
            else:
                value = wordMap[character]
                value.append(position)
                wordMap[character] = value
        return wordMap

    def decode(self, obj):
        positionList = []
        for key in obj:
            for position in obj[key]:
                positionList.append(position)
        positionList.sort()
        for key in obj:
            for position in obj[key]:
                positionList[position-1] = key
        positionList = ''.join(positionList)
        return positionList