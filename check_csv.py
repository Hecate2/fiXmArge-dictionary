#!/usr/bin/env python3
"""检查 魔女語辞典fiXmArge.csv 的重复词和列数一致性"""
import csv
import sys
from collections import Counter

CSV_FILE = '魔女語辞典fiXmArge.csv'
EXPECTED_COLUMNS = 7

def main():
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    # 1. 检查列数
    print(f"=== 列数检查 ===")
    print(f"表头列数: {len(header)} (期望: {EXPECTED_COLUMNS})")
    if len(header) != EXPECTED_COLUMNS:
        print(f"  [错误] 表头列数不正确")

    wrong_col_rows = []
    for i, row in enumerate(rows, 1):
        if len(row) != EXPECTED_COLUMNS:
            wrong_col_rows.append((i, row[0] if row else '(空行)', len(row)))

    if wrong_col_rows:
        print(f"[错误] 有 {len(wrong_col_rows)} 行列数不正确:")
        for i, name, n in wrong_col_rows:
            print(f"  第 {i} 行: {name!r} - {n} 列")
    else:
        print(f"[通过] 所有 {len(rows)} 行的列数都是 {EXPECTED_COLUMNS}")

    # 2. 检查重复词
    print(f"\n=== 重复词检查 (基于 fiXmArge 列) ===")
    names = [row[0] for row in rows if row]
    counter = Counter(names)
    duplicates = {name: count for name, count in counter.items() if count > 1}

    if duplicates:
        print(f"[信息] 共有 {len(duplicates)} 个重复的词条:")
        for name, count in sorted(duplicates.items()):
            positions = [i for i, row in enumerate(rows, 1) if row and row[0] == name]
            print(f"  {name!r} 出现 {count} 次,位于: {positions}")
    else:
        print(f"[通过] 没有重复的词条")

    # 3. 汇总
    print(f"\n=== 汇总 ===")
    print(f"数据行总数: {len(rows)}")
    print(f"唯一词条数: {len(counter)}")
    if wrong_col_rows or duplicates:
        sys.exit(1)
    else:
        print("[完成] 所有检查通过")

if __name__ == '__main__':
    main()
