"""
Dirman - Directory Information Tool
Developed By Zoda

File Creation Date: 18:38 01/08/2024
Languages: Turkish,English
"""
from pathlib import Path
import sys
import json
import os
import time

SOURCEPATH = Path(__file__).parents[0]

def sp(path):
    return os.path.abspath(os.path.join(SOURCEPATH, path))


class Dir:
	def __init__(self,data,path):
		self.data:dict=data
		"Directory Information Data"
		self.path:str=path
		"Directory Path"

		self.calculate()

	def calculate(self):
		"Do calculation required things"
		
		full_path=sp(f"{self.path}/dirman.json")

		dirman_creation_ut=os.path.getctime(full_path)
		c_ti = time.ctime(dirman_creation_ut)
		m_ti = time.ctime(dirman_creation_ut)

		self.data["calc.creation"]=m_ti
		
		self.data["calc.all_files_count"]=0 # Well I Think dirman.json is a file so...
		for path in Path(self.path).rglob("*"):
			if path.is_file():
				self.data["calc.all_files_count"]+=1

			

	def get_key(self,key) -> str:
		"Try to get data in self.data"
		if key in self.data:
			return self.data[key]
		else:
			return "Not Found."

	def print_info(self):
		print(f"""Directory: {self.path}

Author: {self.get_key("author")}
Project: {self.get_key("project")}
License: {self.get_key("license")}
Dirman File Creation: {self.get_key("calc.creation")}

Description:
\t{self.get_key("description")}

Total Files: {self.get_key("calc.all_files_count")}
""")

if len(sys.argv)==1:
	print(f"No Arguments! Usage:\n{__file__} <Directory>")
	sys.exit(1)
else:
	path=sp(sys.argv[1])
	if not os.path.exists(path):
		print("Directory Path Is Not Valid.")
		sys.exit(1)
	if not os.path.isdir(path):
		print(f"{path} Is Not A Directory")
		sys.exit()
	if not "dirman.json" in os.listdir(path):
		print(f"No Dirman File In Directory.")
		sys.exit(1)
	else:
		info=Dir(
			json.load(
				open(
					sp(f"{path}/dirman.json"),"r",encoding="utf-8")
				),
			path
		)
		info.print_info()