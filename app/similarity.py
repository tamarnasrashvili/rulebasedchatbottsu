import math
import re
from collections import Counter

WORD = re.compile(r"\w+")


def get_cosine(vec1, vec2):#როგორ შემიძლია ავიღო სესხი? -> {'რ':2,'ო':3,'გ':1, 'შ':1, 'ე':2, 'მ':1,'ი':4, 'ძ':1, 'ლ':1,'ა':2,'ვ':1, 'ღ':1, 'ს':2, ხ:1}
    # შეიძლება? -> {'შ':1,'ე':2, 'ი':1, 'ძ':1, 'ლ':1, 'ბ':1, 'ა':1}
    intersection = set(vec1.keys()) & set(vec2.keys()) # 'შ', 'ე', 'ი', 'ძ', 'ლ', 'ა'
    numerator = sum([vec1[x] * vec2[x] for x in intersection]) # 1*1 + 2*2 + 4*1 + 1*1 + 1*1 + 2*1 = 13

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())]) # 50  #როგორ -> {'რ':2,'ო':2,'გ':1}
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())]) # 1**2 + 2**2 + 1**2 + 1**2 + 1**2 + 1**2 + 1**2 = 10  #როგორს -> {'რ':2,'ო':2,'გ':1,'ს':1}
    denominator = math.sqrt(sum1) * math.sqrt(sum2) # 7.07 * 10 = 70.07

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator  #0.1855


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)  #როგორ -> {'რ':2,'ო':2,'გ':1}


def get_similarity(text_1, text_2): #როგორ შემიძლია ავიღო სესხი? - შეიძლება?
    vector1 = text_to_vector(text_1) #როგორ შემიძლია ავიღო სესხი? -> {'რ':2,'ო':3,'გ':1, 'შ':1, 'ე':2, 'მ':1,'ი':4, 'ძ':1, 'ლ':1,'ა':2,'ვ':1, 'ღ':1, 'ს':2, ხ:1}
    vector2 = text_to_vector(text_2) #შეიძლება? -> {'შ':1,'ე':2, 'ი':1, 'ძ':1, 'ლ':1, 'ბ':1, 'ა':1}

    value = round(get_cosine(vector1, vector2) * 100) # 18(%)

    if value < 95:
        return False, value
    else:
        return True, value

