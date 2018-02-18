# -*- coding: utf-8 -*-
# Pythonのヒアドキュメント
# 　https://qiita.com/ykhirao/items/c7cba73a3a563be5eac6
#

import argparse


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description = "description goes here")
	parser.add_argument("-i", type=str, help = "help text goes here. This option is required", required=True)
	parser.add_argument("-o", type=str, help = "help text goes here. This option is optional", required=False)

	#command_arguments is dictinary
	command_arguments = parser.parse_args()

	ivariable = command_arguments.i
	print(ivariable)
