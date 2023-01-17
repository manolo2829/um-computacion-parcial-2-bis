from encoder2 import Encoder


if __name__ == '__main__':
    encoder = Encoder()
    result_dict = encoder.encode('hola hola manuh')
    print(result_dict)
    result_dict2 = encoder.decode({'h': [1, 6, 15], 'o': [2, 7], 'l': [3, 8], 'a': [4, 9, 12], ' ': [5, 10], 'm': [11], 'n': [13], 'u': [14]})
    print(result_dict2)