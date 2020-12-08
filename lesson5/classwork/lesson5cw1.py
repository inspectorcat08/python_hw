# .lower
# .upper
def low_reg (a):
	return a.lower()

def up_reg (a):
	return a.upper()

a = ['SdffDDSS', 'SDffdfdgfgD', 'Dsaddfdfd']

vverh = list(map(low_reg, a))
vniz = list(map(up_reg, a))

print(vverh)
print(vniz)