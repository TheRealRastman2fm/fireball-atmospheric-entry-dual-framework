function F = drag_force(v,rho,A,Cd)
F = 0.5*Cd*rho*A*v^2;
end