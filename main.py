from paddlenlp import Taskflow
text_correction = Taskflow("text_correction",home_path='./')
res = text_correction('把我的收集拿来')
print(res)