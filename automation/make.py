import json
import re
import os

def dump(dict, filename):
	json.dump(dict, open("final/" + filename + ".json", "w"), sort_keys=True, indent="\t", separators=(",", ": "))

def translateMethod(method, prefix=""):
	newMethod = {}

	# Adding prefix
	newMethod["prefix"] = prefix + method["name"]

	# Adding description, removing any left over HTML tags
	if "description" in method:
		newMethod["description"] = re.sub(r"\<[^>]*\>", "", method["description"])
	else:
		newMethod["description"] = ""

	# Formatting body
	newMethod["body"] = [prefix + method["name"] + "("]

	if "arguments" in method:
		i = 1
		for arg in method["arguments"]:
			newMethod["body"][0] += "${" + str(i) + ":" + arg["name"] + ("=" + arg["default"] if "default" in arg else "") + "}, "
			i += 1

	newMethod["body"][0] = newMethod["body"][0].removesuffix(", ")
	newMethod["body"][0] += ")$0"

	return newMethod

def translateGlobals():
	f = open("output/global-functions.json")
	d = json.load(f)
	finalGlobals = {}

	for g in d:
		finalGlobals[g["name"]] = translateMethod(g)

	return finalGlobals

def translateClasses():
	f = open("output/classes.json")
	d = json.load(f)
	finalClasses = {}

	for c in d:
		for m in c["functions"]:
			finalClasses[c["name"] + ":" + m["name"]] = translateMethod(m)

	return finalClasses

def translateLibs():
	f = open("output/libraries.json")
	d = json.load(f)
	finalLibs = {}

	for l in d:
		for m in l["functions"]:
			finalLibs[l["name"] + "." + m["name"]] = translateMethod(m, l["name"] + ".")

	return finalLibs

if not os.path.exists("final"):
	os.makedirs("final")


dump(translateGlobals(), "globals")
dump(translateClasses(), "classes")
dump(translateLibs(), "libraries")
