class Encoder:
    
    
    
    
    def encode(self, text):
        text_obj = {}
        text_list = list(text)
        text_arr = []
        for i in range(len(text_list)):
            if text_list[i] in text_arr:
                new_list = text_obj[text_list[i]]
                new_list.append(i+1)
                text_obj[text_list[i]] = new_list
            else:
                text_arr.append(text_list[i])
                text_obj[text_list[i]] = [i+1]
        return text_obj
        
    
    def decode(self, text):
        text_list = []
        for i in text:
            text_list.extend(text[i])
        text_list.sort()
        for i in text:
            for x in text[i]:
                text_list[x-1] = i
        str_text = "".join(text_list)
        return str_text
