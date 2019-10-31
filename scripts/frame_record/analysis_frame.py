import sys,os
import argparse

def main(args):
	files=args
	for file in files:
		if not file.endswith(".csv"):
			continue
		file_path=os.path.expanduser(file)
		file_name=os.path.splitext(file)[0]
		file_parse_name=file_name+"_parse.csv"
		print(file_parse_name)
		with open(file_path) as f,open(file_parse_name,"w+") as r:
			for line in f.readlines():
				if line is not None:
					nums = [int(word) for word in line.split(',')] 
					for index,num in enumerate(nums):
						if index == 0:
							r.write(str(num))
						else:
							r.write(hex(num))
						if index != len(nums)-1:
							r.write(',')
					r.write('\n')
						

if __name__ == '__main__':
    main(sys.argv[1:])
