list = ["DEXTER <dexter@hotmail.com>", "VIRUS <virus!@variable.:p>", "GEnericguy <genericmail@gen.mail>"]
import re

pattern = r'[A-Za-z]+\s?<[a-z]+[@][a-z]+[.][a-z]+>'
for thing in list:
    print("YES") if re.search(pattern, thing) else print("NO")
