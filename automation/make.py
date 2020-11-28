import json
import re
import os

def dump(dict, filename):
	json.dump(dict, open("final/" + filename + ".json", "w"), sort_keys=True, indent="\t", separators=(",", ": "))

def translateGlobals():
	f = open("output/global-functions.json")
	d = json.load(f)
	finalGlobals = {}

	for g in d:
		curGlobal = finalGlobals[g["name"]] = {}

		# Adding prefix
		curGlobal["prefix"] = g["name"]

		# Adding description, removing any left over HTML tags
		curGlobal["description"] = re.sub(r"\<[^)]*\>", "", g["description"])

		# Formatting body
		curGlobal["body"] = [g["name"] + "("]

		if "arguments" in g:
			i = 1
			for arg in g["arguments"]:
				curGlobal["body"][0] += "${" + str(i) + ":" + arg["name"] + ("=" + arg["default"] if "default" in arg else "") + "}, "
				i += 1

		curGlobal["body"][0] = curGlobal["body"][0].removesuffix(", ")
		curGlobal["body"][0] += ")$0"

	return finalGlobals

if not os.path.exists("final"):
	os.makedirs("final")


dump(translateGlobals(), "globals")
