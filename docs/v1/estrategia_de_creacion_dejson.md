Te sigo perfecto ahora 👍
La clave es: **los `.bl` de base del proyecto se crean una sola vez** y viven en `.core/` y `.project/`.
Los turns DEV **solo referencian** esos `.bl`, no los “reenvían”.
En cada turn solo cambia la capa dinámica (intent, codebase, responses, etc.).

A continuación te detallo **solo los `.bl` involucrados**, separados por:

* Base fija del proyecto (para DEV y DOC)
* Turns DEV en Project UI (briefing / execution / refinement)
* Turn DOC en Flat UI
* Al final va el summary que pediste

---

## BASE FIJA DEL PROYECTO (SE CREA UNA VEZ POR INTENT DEV / PROJECT UI)

Estos `.bl` NO son por turn, son la base sobre la que operan todos los turns DEV:

* `.core/.dev.instructions.bl`
* `.core/.dev.rules.bl`
* `.project/.dev.strategy.standards.bl`
* `.project/.dev.strategy.context.bl`
* `.project/.doc.app.architecture.bl`
* `.project/.doc.app.workflow.bl`
* `.project/.doc.app.implementation.bl`
* `.project/.tree.bl`

Y para DOC (flat UI) la base fija es:

* `.core/.doc.instructions.bl`
* `.core/.doc.rules.bl`
* `.project/.doc.app.architecture.bl`
* `.project/.doc.app.workflow.bl`
* `.project/.doc.app.implementation.bl`
* `.project/.tree.bl`

---

## TURNS DEV – PROJECT UI

🟦 **Turn DEV – BRIEFING**

Objetivo:
Entender el pedido, anclarlo al proyecto, y disparar las 5 preguntas que la IA necesita para clarificar el trabajo.

**`.bl` específicos que participan en este turn (además de la base fija):**

* `.intents/.intent.bl`
  Plantilla genérica usada para redactar el requerimiento del Intent.

* `.intents/.dev/<intent-name>/.briefing/.intent.bl`
  Requerimiento concreto del usuario para este Intent DEV específico.
  Es la materia prima que la IA lee en este turn para:

  * interpretar el pedido
  * generar las 5 preguntas clave
  * definir el scope inicial del trabajo

*(Los demás artefactos del turn –.intent.json, .codebase.bl, .index.json– existen, pero no los listamos porque pediste solo `.bl`.)*

---

🟩 **Turn DEV – EXECUTION**

Objetivo:
Con las 5 preguntas ya respondidas (fuera del scope de archivos .bl), la IA:

* arma el plan técnico
* genera el primer deliverable de código
* deja la base consistente para futuros refinement

**`.bl` específicos que participan en este turn (además de la base fija):**

En este diseño, **no se agregan nuevos `.bl` propios del turn de execution**.
Execution reutiliza:

* `.intents/.dev/<intent-name>/.briefing/.intent.bl`
  como fuente original del requerimiento.

y toda la base fija del proyecto:

* `.core/.dev.instructions.bl`
* `.core/.dev.rules.bl`
* `.project/.dev.strategy.standards.bl`
* `.project/.dev.strategy.context.bl`
* `.project/.doc.app.architecture.bl`
* `.project/.doc.app.workflow.bl`
* `.project/.doc.app.implementation.bl`
* `.project/.tree.bl`

La materia prima “nueva” de execution no está en `.bl` sino en:

* las respuestas a las 5 preguntas
* el `codebase.bl` enriquecido
* los JSON de intent/index/response

Pero como me pediste **solo `.bl`**, en execution no aparece ningún `.bl` adicional.

---

🟨 **Turn DEV – REFINEMENT (turn_X)**

Objetivo:
Iterar sobre la base creada en execution, con máxima flexibilidad:

* ajustar
* extender
* corregir
* siempre apoyándose en el `codebase.bl` ya acumulado

**`.bl` específicos que participan en este turn (además de la base fija):**

Tampoco se crean nuevos `.bl` propios de cada `turn_X`.
Refinement reutiliza exactamente la misma base:

* `.core/.dev.instructions.bl`
* `.core/.dev.rules.bl`
* `.project/.dev.strategy.standards.bl`
* `.project/.dev.strategy.context.bl`
* `.project/.doc.app.architecture.bl`
* `.project/.doc.app.workflow.bl`
* `.project/.doc.app.implementation.bl`
* `.project/.tree.bl`
* `.intents/.dev/<intent-name>/.briefing/.intent.bl`

Cada `turn_X` se diferencia por:

* su `intent.json` propio
* su `codebase.bl` actualizado
* su `response.json`

pero **no introduce nuevos `.bl`**.

---

## TURN DOC – FLAT UI

En DOC no hay múltiples turns: es **un único turn**.
La base fija del proyecto se lee una vez, y el intent de documentación se resuelve en un solo ciclo.

**`.bl` que intervienen en el turn DOC:**

Base fija (proyecto):

* `.core/.doc.instructions.bl`
* `.core/.doc.rules.bl`
* `.project/.doc.app.architecture.bl`
* `.project/.doc.app.workflow.bl`
* `.project/.doc.app.implementation.bl`
* `.project/.tree.bl`

Materia prima específica del Intent DOC:

* `.intents/.doc/<intent-name>/.intent/.intent.bl`
  Pedido de documentación original del usuario.

* `.intents/.doc/<intent-name>/.intent/.doc.standards.bl`
  Estándares específicos aplicables a este Intent (puede derivar de `.doc.rules.bl` + ajustes).

* `.intents/.doc/<intent-name>/.intent/.doc.app.context.bl`
  Subconjunto de contexto de proyecto necesario para este Intent DOC (trozos de arquitectura, workflow, implementación).

* `.intents/.doc/<intent-name>/.intent/.doc.prompt.bl`
  Prompt final ensamblado que se le envía a la IA para resolver toda la documentación en un solo turn.

---

## SUMMARY

* **DEV / Project UI**:

  * Se crea una vez una base de proyecto con todos los `.bl` de contexto e instrucciones en `.core/` y `.project/`.
  * Esa base NO se reenvía en cada turn; simplemente está disponible para briefing, execution y refinement.
  * El único `.bl` realmente “dinámico de intent” es `.briefing/.intent.bl`.
  * Execution y Refinement no introducen `.bl` nuevos; trabajan con:

    * base de proyecto
    * intent original
    * `codebase.bl` y JSONs que van mutando.

* **DOC / Flat UI**:

  * También tiene una base fija de proyecto en `.core/` y `.project/`.
  * El turn DOC único se arma con:

    * `.intent.bl` del intent DOC
    * `.doc.standards.bl`
    * `.doc.app.context.bl`
    * `.doc.prompt.bl`
  * No hay iteraciones ni turns adicionales.

En otras palabras:

* Los `.bl` de **base** viven en el proyecto y se crean una única vez.
* Los turns DEV **no replican esos `.bl`**, solo los consumen.
* La única capa “mutable” de texto humano a nivel `.bl` por intent es:

  * `.briefing/.intent.bl` en DEV
  * `.intent/*.bl` en DOC.
