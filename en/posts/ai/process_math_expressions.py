import re

def process_math_expressions_in_file(file_path):
    """
    读取Markdown文件，处理其中的数学公式，然后将更改保存回文件。
    """
    # 用于匹配单个$或$$包围的数学公式的正则表达式
    math_expr_pattern = r'(\${1,2})(.+?)\1'
    
    # 用于在数学表达式中查找和替换{单个字符}的正则表达式
    single_elem_pattern = r'\{(\w)\}'

    # 从文件读取内容
    with open(file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # 查找并处理所有数学公式
    def replacement(match):
        delimiter, expr = match.groups()  # 获取数学公式内容及其定界符
        # 将内容中的\mathb去除
        expr = expr.replace('\\mathb', '')
        expr = expr.replace('\\mathcal', '')
        # 去除多余的回车
        expr = expr.replace('\n', '')
        # expr = expr.replace('\\', '\\\\') # 将\替换为\\
        expr = expr.replace('_', '\\_')
        # 在数学表达式中替换{单个字符}
        return f'{delimiter}' + re.sub(single_elem_pattern, r'\1', expr) + f'{delimiter}'
    
    processed_content = re.sub(math_expr_pattern, replacement, md_content, flags=re.DOTALL)

    # 将处理后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(processed_content)

# 指定要处理的Markdown文件的路径
file_path = 'diffusion.md'  # 请替换为你的Markdown文件的实际路径

# 调用函数处理文件
process_math_expressions_in_file(file_path)
