import Projectile as pr 

p1 = pr.Projectile()
#p1.set_initial_conditions(10, 0, 0, 10, 1.2, 5, 2, 0.4, 0.01)
p1.angle_to_hit_target(2, 2, 1, 120, 0, 0, 1.2, 5, 2, 0.4, 0.01)

p2 = pr.Projectile()
p2.angle_to_hit_target(3, 3, 1, 12, 0, 0, 1.2, 6, 2, 0.4, 0.01)
