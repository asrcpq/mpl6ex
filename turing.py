def rulesel(states):
	for state in states:
		for sym in [0,1]:
			print(f"{state}{sym}(1,2) < q{state}(1,2) v{sym}(2)")

print(end = """
qa(l1,r1)
trunk(l1,l0)
trunk(r1,r0)
v0(l0)
v0(r0)
palloc > trunk
s(1,2) < trunk(1,2)
v0(2) < trunk(2,1)
calloc1(2) < trunk(2,1) v0(1)
calloc0(2) < trunk(2,1) v1(1)
calloc0 > !s assign0
v0(1) < assign0(1,2)
calloc1 > !s assign1
v1(1) < assign1(1,2)
findc0(1,2) < s(1,2) v0(2)
findc1(1,2) < s(1,2) v1(2)
""")

def left(s,s2,v):
	print(end = f"""
palloc(2) < {s}(1,2) trunk(2,3)
rp_{s}(1,3) < {s}(1,2) s(3,2)
calloc{v}(2) < rp_{s}(1,2) !trunk(2,3)
rv_{s}(1,3) < rp_{s}(1,2) findc{v}(2,3)
rc0_{s}(1,2) < rv_{s}(1,2) v0(1)
rc1_{s}(1,2) < rv_{s}(1,2) v1(1)
calloc0(2) < rc0_{s}(1,2) !trunk(2,3)
calloc1(2) < rc1_{s}(1,2) !trunk(2,3)
rc_{s}(1,3) < rc0_{s}(1,2) findc0(2,3)
rc_{s}(1,3) < rc1_{s}(1,2) findc1(2,3)
# left
palloc(1) < rc_{s}(1,2) trunk(1,3)
q{s2}(3,2) < rc_{s}(1,2) s(3,1)
""")

def right(s,s2,v):
	print(end = f"""
palloc(2) < {s}(1,2) trunk(2,3)
rp_{s}(1,3) < {s}(1,2) s(3,2)
# left
calloc{v}(1) < rp_{s}(1,2) !trunk(1,3)
q{s2}(3,2) < rp_{s}(1,2) findc{v}(1,3)
""")

def bb4():
	rulesel("abcd")
	right("a0", "b", 1)
	left("a1", "b", 1)
	left("b0", "a", 1)
	left("b1", "c", 0)
	right("c0", "h", 1)
	left("c1", "d", 1)
	right("d0", "d", 1)
	right("d1", "a", 0)

def bb3():
	rulesel("abc")
	right("a0", "b", 1)
	right("a1", "h", 1)
	right("b0", "c", 0)
	right("b1", "b", 1)
	left("c0", "c", 1)
	left("c1", "a", 1)

bb3()
