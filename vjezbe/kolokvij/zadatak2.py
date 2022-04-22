import projectile as pr 

a= pr.ProjectileDrop()
b = pr.ProjectileDrop()

a.set_initial_conditions(10, 10)
b.set_initial_conditions(4, 6)

ay = a.change_y(5)
av = a.change_v(5)
by = b.change_y(4)
bv = b.change_v(-2)

print("Nova visina i brzina prvog objekta je", ay, av)
print("Nova visina i brzina drugog objekta je", by, bv)