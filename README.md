# Vaquitas

Vamos a simular que hay vacas yendo por un camino, todas para el mismo lado, y se topan con un puente.
Las vacas caminan a diferentes velocidades, y el puente no soporta el paso de más de una vaca a la vez.

Mirá la implementación que esta ahora, correla algunas veces, y familiarizate con el código.

Ahora agregale semáforos para asegurar que haya solamente una vaca cruzando el puente a la vez. La ejecución debería verse así:

![vaquitas cruzando el puente](assets/vaquitas.gif)

## Bonus: variantes 

Ahora podés probar algunas variantes. En principio implementalas todas por separado y siempre tomando como punto de partida la versión que hiciste en el punto anterior.

* Como máximo haya 2 vacas cruzando el puente a la vez. 
* Lo mismo que antes, pero para una cantidad _N_ de vacas que se configura antes de ejecutar el programa.
* Que haya dos puentes.
* Lo mismo que antes, pero para una lista de puentes que se configura antes de ejecutar el programa. (Acá sería buena idea tener una clase `Puente` que indique dónde empieza y qué tan largo es).
* Que haya vacas caminando en ambos sentidos.
* Que además de vacas, hayan liebres (muy muy rápidas) y *una* tortuga (muy muy lenta).
