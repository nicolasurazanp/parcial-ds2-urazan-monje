# parcial-ds2-urazan-monje

#Integrantes
#David Santiago Monje Cuellar
#Nicolas Urazan Padilla

Nombre de la MongoDB : MatriculApp

Colecciones : tickets , semanas , agentes

Coleccion tickets : ticket : string , llegadaMin : Int32 , atencionMin : Int32 , prioridad : 
string

Coleccion semanas :  semana : Int32 , defectosFind : Int32

Coleccion agentes :  usuario : string , rango : string , ticketshora : Int32

Relacion : Los tickets se relacionan con el agente mediante por el id unico del agente generado por mongo.

Seleccionamos la opcion B

Respuesta a la pregunta opcion B:

¿Cuántos defectos quedarían sin descubrir si se libera hoy?
R Unos 59 defectos (58.77). El modelo estima un total de 198 defectos y 
hasta la semana 8 se han encontrado 139. Es decir, hasta ahora se ha
descubierto solo el 70%.

¿En qué semana se llegaría al 95 %?
En la semana 19.7, más o menos la semana 20.

Parte 3. Interpretación (15 %)

Con los defectos que se encontraron durante las 8 semanas de pruebas
(139 en total), el modelo calcula que la versión 11.0 de MatriculApp tiene unos
198 defectos en total. Eso quiere decir que, si HuilaSoft la libera hoy, todavía
quedarían unos 59 defectos escondidos que tarde o temprano le saldran a los usuarios. Hasta ahora solo se ha encontrado el 70% de los problemas. En la gráfica podemos evidenciar que los puntos reales siguen muy bien la curva, pero que esta misma sigue subiendo y no se ha aplanado. Esto que quiere decir, que cada semana se siguen encontrando nuevos errores. Según el modelo el 95% de los defectos se encontrarían en la semana 20. Por eso no recomendamos lanzar la versión todavía
