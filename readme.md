# 一些用于文本处理的小工具

> requirements: `python 3.6+`

## 1. 按行随机抽取文本

```bash
# 从指定文件中随机取出一定行数
python shuffle.py --input_file input_file --output_file output_file --number line_number
# 从指定文件中随机取出一定百分比的内容 (按行):  parameter: percent valued from 0 to 1
python shuffle.py --input_file input_file --output_file output_file --percent percent
```

## 2. 文本拆分 (按行)

```bash
# 按固定行数拆分, 指定 --line_number 参数
python text_split.py --input_file input_file --output_dir output_dir --line_number line_number
# 按文件个数拆分, 指定 --file_number 参数
python text_split.py --input_file input_file --output_dir output_dir --file_number file_number
```

## 3. 指定文件下重命名

```bash
python rename.py --input_dir input_dir
```