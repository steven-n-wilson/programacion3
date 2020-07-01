import sys
import yaml
import pprint

filename = sys.argv["info.yml"]

y = yaml.safe_load(open("info.yml", 'r'))

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(y)

