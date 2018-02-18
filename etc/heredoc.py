# -*- coding: utf-8 -*-
# Pythonのヒアドキュメント
# 　https://qiita.com/ykhirao/items/c7cba73a3a563be5eac6
#

import textwrap


string = textwrap.dedent('''
  This is a {what}.
  I'm from {where}.
''').format(what="apple", where="Chiba").strip()
print(string)
