is_tired = True
has_finishedProj = False

if is_tired and has_finishedProj:
    print("Have some rests")
elif not is_tired and not has_finishedProj:
    print("Keep Learning to Code")
elif not is_tired or has_finishedProj:
    print("Go and Learn more")
else:
    print("Take a Nap")