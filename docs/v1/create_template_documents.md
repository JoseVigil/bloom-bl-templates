Perfecto.
Acá viene **EL DOCUMENTO DEFINITIVO**, listo para incorporar como estándar global del sistema Bloom.

Es **la descripción formal del contenido que debe tener cada archivo `.bl`**, diseñada específicamente para tu modelo de negocio de *iteración AI-driven* basado en:

* Intents DEV (Project UI): briefing → execution → refinement
* Intents DOC (Flat UI): un solo turn
* Codebase expandible
* Estado persistido por intent
* Núcleo estático que garantiza coherencia entre turnos

La documentación está escrita **como un manual de normas duras**, con las mejores prácticas de prompting para máxima efectividad de IA en ciclos iterativos complejos.

---

# 📘 BLOOM SYSTEM SPEC — DEFINICIÓN FORMAL DE CADA `.BL`

A continuación se describe **el contenido ideal de cada archivo**, redactado como *plantilla conceptual*, no como contenido literal.
Esto te permite que **la IA pueda autogenerar** estos archivos con calidad profesional y máxima coherencia.

---

# 1. `.core/` — Núcleo Global Inmutable

Estos archivos **no cambian nunca**.
La IA los usa para saber “cómo pensar”, “cómo escribir”, “cómo iterar”.

---

## 1.1 `.core/.doc.instructions.bl`

**Propósito:**
Define **cómo debe operar la IA durante cualquier Intent DOC**.

**Contenido esperado:**

* **Reglas maestras para procesar documentación:**

  * Cómo identificar el tipo de documentación (arquitectura, workflow, implementación, mixed).
  * Cómo detectar conflictos y resolverlos.
  * Cómo elegir entre actualizar, reemplazar o fusionar contenido.
* **Cómo interpretar un `.intent.bl`**:

  * Identificación de objetivos.
  * Extracción de alcance.
  * Identificación de documentos objetivo.
* **Formato estricto para respuestas:**

  * Bloques de archivo completo.
  * Sin diffs, siempre archivo completo.
  * Separación limpia entre secciones.
* **Cómo ensamblar correctamente un `.doc.prompt.bl`.**
* **Reglas para leer el árbol (`.tree.bl`).**
* **Estándares obligatorios de calidad:**

  * Terminología consistente.
  * Nombres exactos de archivos.
  * No inventar módulos que no existen sin justificación.

---

## 1.2 `.core/.dev.instructions.bl`

**Propósito:**
Define **cómo funciona el ecosistema DEV entero**.

**Contenido esperado:**

* **Cómo leer el codebase:**

  * Prioridad de fuentes (archivos entregados por usuario > generados por IA > inferidos).
  * Reglas estrictas para leer archivos segmentados o incompletos.
* **How-to del flujo DEV:**

  * Función de BRIEFING.
  * Función de EXECUTION.
  * Función de REFINEMENT.
* **Obligaciones del modelo:**

  * Nunca romper consistencia.
  * Nunca reescribir código sin antes entender dependencias.
  * Mantener integridad del codebase entre turnos.
* **Cómo escribir código:**

  * Archivos completos siempre.
  * Nada de pseudo-código salvo que el usuario lo pida.
  * Código seguro, optimizado y consistente con estándares del proyecto.
* **Cómo debe funcionar el `.intent.json` en cada fase.**

---

## 1.3 `.core/.dev.rules.bl`

**Propósito:**
Define **qué está permitido, prohibido y obligatorio** a nivel técnico dentro del modo DEV.

**Contenido esperado:**

* **Principios obligatorios del sistema:**

  * Minimizar side effects.
  * Mantener separación de capas.
  * Preservar compatibilidad con el codebase existente.
* **Patrones permitidos/prohibidos:**

  * Uso aceptado de frameworks, librerías, naming conventions.
  * Prohibiciones: duplicados, reconstrucción completa de módulos sin necesidad, etc.
* **Templates obligatorios para respuestas AI:**

  * Estructura JSON.
  * Estructura de archivos completos.
* **Integridad entre turnos:**

  * Estado persistido debe ser interpretado siempre.
  * codebase.bl debe leerse “como verdad".

---

## 1.4 `.core/.doc.rules.bl`

**Propósito:**
Define **los estándares globales de documentación técnica**.

**Contenido esperado:**

* Estructura oficial de documentación:

  * Arquitectura → Workflow → Implementación
* Convenciones terminológicas.
* Cómo actualizar secciones existentes.
* Cómo detectar documentación inconsistente.
* Cómo formatear texto técnico (títulos, bullets, tablas, ejemplos, disclaimers).
* Cómo ordenar secciones dentro de un archivo doc grande.

---

# 2. `.project/` — Documentación Base Estática del Proyecto

Se crean **una sola vez** cuando inicia el proyecto.
Sirven como *contexto permanente* para DEV y DOC.

---

## 2.1 `.project/.dev.strategy.standards.bl`

**Propósito:**
Define **cómo debe escribirse el código del proyecto a nivel estándar técnico**.

**Contenido esperado:**

* Estilo global del proyecto:

  * Indentación.
  * Nomenclatura.
  * Estándares de modularización.
* Lineamientos para refactorización.
* Reglas para escribir tests (si existen).
* Reglas para encapsulación y boundaries internos.

---

## 2.2 `.project/.dev.strategy.context.bl`

**Propósito:**
Describe el estado técnico actual del proyecto, usado por la IA durante cualquier Intent DEV.

**Contenido esperado:**

* Arquitectura global del proyecto.
* Módulos existentes.
* Dependencias.
* Tecnologías usadas.
* Patrones internos implementados.
* Limitaciones y restricciones de diseño.

---

## 2.3 `.project/.doc.app.architecture.bl`

**Propósito:** “Qué es el sistema”.

**Contenido esperado:**

* Componentes principales.
* Subsistemas.
* Relación entre módulos.
* Modelo conceptual y dominios.
* Diagrama descriptivo (en texto).

---

## 2.4 `.project/.doc.app.workflow.bl`

**Propósito:** “Cómo funciona”.

**Contenido esperado:**

* Flujos de usuario.
* Roles.
* Casos de uso.
* Reglas del negocio.
* Secuencia operativa.

---

## 2.5 `.project/.doc.app.implementation.bl`

**Propósito:** “Cómo está implementado”.

**Contenido esperado:**

* Estructura backend.
* Estructura frontend.
* Servicios.
* Endpoints.
* Integraciones externas.
* Infraestructura.
* Restricciones técnicas.

---

## 2.6 `.project/.tree.bl`

**Propósito:**
Árbol completo del filesystem del proyecto.

**Contenido esperado:**

* Listado de carpetas y archivos.
* Explicación de propósito por carpeta.
* Observaciones sobre archivos clave.
* Marcado de zonas “core” y zonas “extensibles”.

---

# 3. `.intents/.dev/<intent-name>/` — INTENTS DEV (BRIEFING → EXECUTION → REFINEMENT)

---

## 3.1 `.briefing/.intent.bl`

**Propósito:**
Requerimiento original del usuario, sin procesar.

**Contenido esperado:**

* Descripción textual cruda del objetivo del Intent.
* Restricciones mencionadas por el usuario.
* Alcance percibido.
* Cualquier archivo adjunto (referencia textual).

La IA lo usa para generar:

* `.intent.json`
* 5 preguntas
* el codebase inicial

---

## 3.2 `.briefing/.codebase.bl`

**Propósito:**
Base inicial del codebase para este Intent.

**Contenido esperado:**

* Fragmentos enviados por el usuario.
* Archivos relevantes detectados por IA.
* Archivos placeholders marcados como:

  ```
  ### MISSING - to be generated in EXECUTION
  ```
* Relaciones detectadas entre archivos.

---

## 3.3 `.execution/.codebase.bl`

**Propósito:**
Codebase COMPLETO actualizado después de execution.

**Contenido esperado:**

* Archivos generados en esta etapa.
* Refactorizaciones.
* Eliminación de artefactos erróneos.
* Expansión de contexto.
* Codebase consistente y listo para refinement.

---

## 3.4 `.refinement/turn_X/.codebase.bl`

**Propósito:**
Superficie autorizada para manipular en cada iteración.

**Contenido esperado:**

* Codebase completo post-turn_X.
* Incrementos o modificaciones.
* Archivos nuevos agregados en ese turno.

---

# 4. `.intents/.doc/<intent-name>/` — INTENTS DOC (FLAT UI, UN SOLO TURN)

---

## 4.1 `.intent/.intent.bl`

**Propósito:**
Pedido textual del usuario.

**Contenido esperado:**

* Qué documentación quiere.
* Dónde debe escribirse.
* Qué parte del proyecto implica.
* Notas y restricciones.

---

## 4.2 `.intent/.doc.standards.bl`

**Propósito:**
Estándares fusionados del sistema para este Intent DOC.

**Contenido esperado:**

* Reglas de `.core/.doc.rules.bl`.
* Ajustes aplicados al proyecto específico.
* Reglas de formato final.

---

## 4.3 `.intent/.doc.app.context.bl`

**Propósito:**
Contexto estático seleccionado del proyecto.

**Contenido esperado:**

* Partes relevantes de arquitectura.
* Partes relevantes de workflow.
* Partes relevantes de implementación.
* Dependencias.
* Secciones estrictamente necesarias para el Intent DOC.

---

## 4.4 `.intent/.doc.prompt.bl`

**Propósito:**
Prompt final ensamblado para ejecutar el Intent DOC.

**Contenido esperado:**

* Sección 1: Instrucciones de alto nivel.
* Sección 2: Reglas del proyecto.
* Sección 3: Contexto.
* Sección 4: Pedido del usuario.
* Sección 5: Checklist obligatorio de salida.
* Sección 6: Archivos destino.

---

# 📌 RESUMEN FINAL — DEFINICIÓN CONCISA DE TODOS LOS `.BL`

| Archivo                                             | Contenido esencial                                                 |
| --------------------------------------------------- | ------------------------------------------------------------------ |
| `.core/.doc.instructions.bl`                        | Manual maestro DOC: cómo documentar correctamente.                 |
| `.core/.dev.instructions.bl`                        | Manual maestro DEV: cómo operar briefing → execution → refinement. |
| `.core/.dev.rules.bl`                               | Reglas técnicas obligatorias del modo DEV.                         |
| `.core/.doc.rules.bl`                               | Reglas técnicas obligatorias del modo DOC.                         |
| `.project/.dev.strategy.standards.bl`               | Estándares técnicos del proyecto.                                  |
| `.project/.dev.strategy.context.bl`                 | Contexto técnico narrativo del proyecto.                           |
| `.project/.doc.app.architecture.bl`                 | Arquitectura del sistema.                                          |
| `.project/.doc.app.workflow.bl`                     | Workflow del sistema.                                              |
| `.project/.doc.app.implementation.bl`               | Implementación técnica del sistema.                                |
| `.project/.tree.bl`                                 | Árbol completo del proyecto.                                       |
| `.intents/.dev/.../.briefing/.intent.bl`            | Pedido original del usuario.                                       |
| `.intents/.dev/.../.briefing/.codebase.bl`          | Codebase inicial inferido.                                         |
| `.intents/.dev/.../.execution/.codebase.bl`         | Codebase actualizado tras execution.                               |
| `.intents/.dev/.../.refinement/turn_X/.codebase.bl` | Codebase actualizado por turno.                                    |
| `.intents/.doc/.../.intent/.intent.bl`              | Pedido de documentación del usuario.                               |
| `.intents/.doc/.../.intent/.doc.standards.bl`       | Estándares DOC fusionados.                                         |
| `.intents/.doc/.../.intent/.doc.app.context.bl`     | Contexto estático para DOC.                                        |
| `.intents/.doc/.../.intent/.doc.prompt.bl`          | Prompt final del Intent DOC.                                       |

---

Si querés, puedo generar **el contenido literal** de cada `.bl` como plantillas listas para copiar/pegar.
¿Querés que cree **todos los archivos completos**? ¿O empezamos por la carpeta `.core/`?
