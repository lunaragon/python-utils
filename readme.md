# 一些用于文本处理的小工具

> requirements: `python 3.6+`

## 1. 按行随机抽取文本

> shuffle.py

```bash
# 从指定文件中随机取出一定行数
python shuffle.py --input-file input_file --output-file output_file --number line_number
# 从指定文件中随机取出一定百分比的内容 (按行):  parameter: percent valued from 0 to 1
python shuffle.py --input-file input_file --output-file output_file --percent percent
# 未指定行数与百分比，则将原文本打乱
python shuffle.py --intput-file input_file --output-file output_file
```

## 2. 文本拆分 (按行)

> text_split.py

```bash
# 按固定行数拆分, 指定 --line_number 参数
python text_split.py --input-file input_file --output-dir output_dir --by-line-number line_number
# 按文件个数拆分, 指定 --file_number 参数
python text_split.py --input-file input_file --output-dir output_dir --by-file-number file_number
```

## 3. 文本合并

> text_merge.py

```bash
# 多个文件合并成一个文件
python text_merge.py by-file [filename1, filename2, filename3, ..., filenameN] merged_file
# 将指定目录下的所有文件（不递归）合并成一个文件
python text_merge.py by-dir dir_name merged_file
```

## 4. 指定文件下重命名

> rename.py

```bash
python rename.py --input_dir input_dir
```