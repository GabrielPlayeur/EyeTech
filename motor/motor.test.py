from parentsMotor import ParentsMotor
from debut import Debut
from attention import Attention
from fin import Fin

p = ParentsMotor()
p.setPin()

print("Debut")
Debut(p.MG, p.MD).start()
print("Attention")
Attention(p.MG, p.MD).start()
print("Fin")
Fin(p.MG, p.MD).start()