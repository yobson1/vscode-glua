import json
import re
import os

def dump(dict, filename):
	json.dump(dict, open("final/" + filename + ".json", "w"), sort_keys=True, indent="\t", separators=(",", ": "))

def formatDesc(desc):
	return re.sub(r"\<[^>]*\>", "", desc)

def translateMethod(method, prefix=""):
	newMethod = {}

	# Adding prefix
	newMethod["prefix"] = prefix + method["name"]

	# Adding description, removing any left over HTML tags
	if "description" in method:
		newMethod["description"] = formatDesc(method["description"])
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

hookPrefixs = {
	"ENTITY": "ENT",
	"WEAPON": "SWEP"
}

def translateHookPrefix(prefix):
	return (hookPrefixs[prefix] if prefix in hookPrefixs else prefix) + ":"

def translateHook(hook, prefix):
	newHook = {}

	# Adding prefix
	newHook["prefix"] = prefix + hook["name"]

	# Adding description
	if "description" in hook:
		newHook["description"] = formatDesc(hook["description"])
	else:
		newHook["description"] = ""

	# Formatting body
	newHook["body"] = ["function " + prefix + hook["name"] + "("]

	if "arguments" in hook:
		for arg in hook["arguments"]:
			newHook["body"][0] += arg["name"] + ", "

	newHook["body"][0] = newHook["body"][0].removesuffix(", ")
	newHook["body"][0] += ")\n\t$0\nend"

	return newHook

def translateValue(value):
	newValue = {}

	newValue["body"] = value["name"]
	newValue["description"] = formatDesc("Decimal value: " + str(value["value"]) + ("\n\n" + formatDesc(value["description"]) if "description" in value else ""))
	newValue["prefix"] = value["name"]

	return newValue

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

def translateEnums():
	f = open("output/enums.json")
	d = json.load(f)
	finalEnums = {}

	for eList in d:
		for e in eList["fields"]:
			finalEnums[e["name"]] = translateValue(e)

	return finalEnums

def translateHooks():
	f = open("output/hooks.json")
	d = json.load(f)
	finalHooks = {}

	for obj in d:
		for method in obj["functions"]:
			prefix = translateHookPrefix(method["parent"])
			finalHooks[prefix + method["name"]] = translateHook(method, prefix)

	return finalHooks

if not os.path.exists("final"):
	os.makedirs("final")


dump(translateGlobals(), "globals")
dump(translateClasses(), "classes")
dump(translateLibs(), "libraries")
dump(translateEnums(), "enums")
dump(translateHooks(), "hooks")
