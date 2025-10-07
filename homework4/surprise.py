# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions --
# 1) Write a function that uses a loop to print the name of each star.
for i in targets:
	print(i)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
for name, spec in targets.items():
	spectral = spec.get("Spectral Type")
	print(name, spectral)

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
for star, dic in targets.items():
	if dic.get("Magnitude") >= 0.1:
		print(star)

# 4) Look up another target, add all the necessary information to the targets list.
targets["Wolf 359"] = {
	"RA": "10h 56m 29s",
	"Dec": "+7° 0′ 52″",
	"Magnitude": 16.614,
	"Spectral Type": "M6V"
}
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def closesttovalue(dic, numbs):
	closest = None
	sml_dif = float('inf')
	for starnm, starinf in dic.items():
		decstr = starinf.get("Dec", "")
		newstr = decstr.split("°")[0].replace("+", "").replace("\u2212", "-").strip()
		newstr = newstr.replace("′", "").replace("″", "")
		decdeg = float(newstr)
		dif = abs(numbs - decdeg)
		if dif < sml_dif:
			sml_dif = dif
			closest = starnm
	return closest
print(closesttovalue(targets, 20))
# 6) What is your favorite constellation?
print('Saggitarius, easiest to spot on a dark night + milky way steam')

