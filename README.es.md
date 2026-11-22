# Servicio de asistencia de Netheret, paso 09: mi agenda

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Un ejemplo para enseñar. En dieciséis pasos construimos una aplicación web de servicio de asistencia para Netheret, una empresa inventada que da soporte informático a pequeñas empresas. Este paso da a los técnicos de Tier 2 y Tier 3 su propia agenda y una ficha para cada trabajo, donde marcan su progreso.

## Qué añade este paso

En `helpdesk/jobs.py`:

- `/jobs/mine`: los trabajos de un técnico de hoy en adelante, agrupados por día, más
  cualquier trabajo anterior que siga marcado como "in progress".
- `/jobs/<id>`: la ficha del trabajo: cuándo, dónde, el teléfono del cliente, las
  instrucciones y, si el trabajo viene de una solicitud, el problema original del cliente.
- `/jobs/<id>/progress`: el técnico pasa el trabajo a "in progress" o
  "done" y escribe notas. Cuando un trabajo que viene de una solicitud termina, se añade una nota a
  la línea de tiempo de esa solicitud.

En `helpdesk/models.py`, `Job.can_be_seen_by()` y `Job.can_be_updated_by()`
guardan en un solo sitio las reglas sobre quién puede ver y cambiar un trabajo. La vista
semanal y la página de la ficha las usan las dos.

## Ejecútalo

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

Inicia sesión como `tier2@netheret.example` o `tier3@netheret.example` (contraseña de
demostración `password123`) y abre My schedule. Prueba a abrir el trabajo de otro
técnico desde la vista semanal: no hay enlace, y si escribes la dirección
recibes un 403.

## En qué fijarse

- `days.setdefault(day, []).append(job)`: una forma corta de agrupar una lista en un
  diccionario de listas.
- Un técnico no puede cancelar un trabajo. El formulario no ofrece esa opción y el
  servidor también la rechaza, porque quien usa un formulario puede modificarlo.
- `finished_now`: la nota de la línea de tiempo solo se escribe la primera vez que un trabajo
  pasa a terminado, no cada vez que se guardan las notas.

## Aprende este paso

Este es el paso 9 de 16 de **Task 2. Developing the solution**, una serie gratuita de lecciones de T Level Digital Software Development, en inglés, que construye el servicio de asistencia de Netheret en sprints ágiles con Python y Flask. Lee la lección de este paso:
[La agenda de un técnico y las fichas de trabajo](https://mitsurutech.co.uk/resources/t-level/dsd-t2-09-my-schedule).

- Paso anterior: [paso 08, programar trabajos in situ](https://github.com/mitsurutech/netheret-helpdesk-08-jobs)
- Paso siguiente: [paso 10, la base de conocimiento](https://github.com/mitsurutech/netheret-helpdesk-10-knowledge-base)
- [Todas las lecciones gratuitas de T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Enseña estas lecciones a tu clase en MitsuruTech](https://mitsurutech.co.uk/es/learning), [mira los precios](https://mitsurutech.co.uk/es/pricing) o
  [empieza un año gratis para tu centro](https://mitsurutech.co.uk/es/signup)

## Acerca de

Escrito por [Mitsuru Technologies](https://mitsurutech.co.uk/es) (MitsuruTech) como ejemplo para enseñar T Level Digital
Software Development. El encargo de Netheret IT Support Solutions procede del material de evaluación de muestra de Pearson; este código
y sus notas son nuestros, y no los publica, respalda ni aprueba Pearson ni el Department for Education.
"T Level" es una marca registrada del Department for Education.
