# Arquitectura Final BTIP — Documentación Oficial Actualizada (Diciembre 2025)

A continuación se presenta la estructura completa y actualizada del ecosistema BTIP (Bloom-TIP), con todas las carpetas, archivos y su propósito exacto.

## 1. Carpeta `.bloom/.core/`

Contiene las reglas maestras del ecosistema BTIP. Define el comportamiento obligatorio tanto para IA como para humanos.

| Archivo                  | Propósito principal                                                               | Contenido clave esperado                                                                                  |
|--------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `.doc.instructions.bl`   | Guía operativa para leer, interpretar y actualizar cualquier documentación       | • Navegación de archivos DOC<br>• Buenas prácticas de redacción<br>• Orden lógico arquitectura → workflow → implementación<br>• Convenciones de formato<br>• Reglas de actualización por IA |
| `.dev.instructions.bl`   | Instrucciones para interpretar el codebase y escribir/modificar código           | • Uso de .codebase.bl y .tree.bl<br>• Políticas archivos completos vs patches<br>• Estructura respuestas DEV |
| `.dev.rules.bl`          | Reglas técnicas obligatorias para todos los Intents DEV                           | • Restricciones técnicas<br>• Modelos de respuesta<br>• Políticas de seguridad y consistencia            |
| `.doc.rules.bl`          | Reglas generales de documentación técnica                                         | • Límites de modificación<br>• Estructura estándar<br>• Coherencia entre archivos                         |

## 2. Carpeta `.bloom/.intents/.dev/<intent>/`

Flujo complejo de 3 etapas: **briefing → execution → refinement**

### 2.1 Control de sesión
- `.session_state.json` → Estado persistente (turno, flags, progreso, checkpoints)

### 2.2 `.briefing/`

| Archivo         | Contenido                                                                 |
|-----------------|---------------------------------------------------------------------------|
| `.intent.bl`    | Requerimiento original del usuario (texto libre)                          |
| `.codebase.bl`  | Scope autorizado de código (solo archivos relevantes)                     |
| `.intent.json`  | Parsing estructurado: objetivo, constraints, parámetros, dependencias     |
| `.index.json`   | Resumen sintético del alcance y hipótesis                                 |

### 2.3 `.execution/`

| Archivo          | Contenido                                                                 |
|------------------|---------------------------------------------------------------------------|
| `.index.json`    | Log completo de decisiones y dependencias                                 |
| `.intent.json`   | Prompt exacto enviado a la IA                                             |
| `.response.json` | Primera respuesta del modelo (código + análisis)                          |

### 2.4 `.refinement/`
```
turn_1/
   ├─ .index.json
   ├─ .intent.json
   └─ .response.json
turn_2/
   └─ ...
```

## 3. Carpeta `.bloom/.intents/.doc/<intent>/`

**Intent DOC:** single-turn, directo y transaccional (sin refinement)

### 3.1 `.intent/` (todo lo necesario para un único output)

| Archivo                 | Propósito                                                             | Contenido clave                                                                 |
|-------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------------|
| `intent.json`           | Representación estructurada del requerimiento documental             | tipo, archivos a modificar, secciones nuevas, criterios de aceptación          |
| `.intent.bl`            | Requerimiento original en texto libre                                 | Descripción cruda + contexto                                                    |
| `.doc.standards.bl`     | Reglas normalizadas específicas de este Intent DOC                   | .doc.rules.bl + reglas propias                                                  |
| `.doc.prompt.bl`        | Prompt final enviado a la IA (generado automáticamente por BTIP)     | Instrucciones + contexto + archivos objetivo + formato esperado                |
| `.doc.app.context.bl`   | Contexto documental relevante                                        | Extractos de architecture/workflow/implementation                              |
| `.tree.bl`              | Árbol actual del filesystem                                           | Navegación abstracta                                                            |
| `index.json`            | Resumen interno para auditoría                                        | objetivo, archivos, tipo de cambio                                              |

### 3.2 `.response/`
- Único deliverable final
```json
{
  "files": {
    "doc.app.architecture.bl": "<contenido completo actualizado>",
    "doc.app.workflow.bl": "<contenido completo actualizado>"
  },
  "summary": "Se actualizaron 2 archivos con las nuevas descripciones…",
  "notes": "Razonamiento interno y decisiones tomadas"
}
```
→ **Transacción cerrada. No hay más turnos.**

## 4. Carpeta `.bloom/.project/`

Documentación oficial canónica del proyecto

| Archivo                        | Contenido principal                                                                      |
|--------------------------------|------------------------------------------------------------------------------------------|
| `.dev.strategy.standards.bl`   | Reglas técnicas universales: patrones, convenciones, arquitectura obligatoria           |
| `.dev.strategy.context.bl`     | Contexto técnico: módulos, dependencias, configuraciones                                 |
| `.doc.app.architecture.bl`     | Qué es el sistema: componentes, dominio, modelos, relaciones                            |
| `.doc.app.workflow.bl`         | Cómo se usa: casos de uso, roles, flujos operativos                                      |
| `.doc.app.implementation.bl`   | Cómo está implementado: servicios, APIs, integraciones, detalles técnicos               |
| `.tree.bl`                     | Árbol completo del proyecto (usado por Intents DEV y DOC)                                |

## Resumen de la evolución
- **Intents DEV** → mantienen 3 etapas (complejo e iterativo)
- **Intents DOC** → ahora single-turn y transaccionales → máxima velocidad y consistencia
- **Prompt final de documentación** → generado automáticamente en `.doc.prompt.bl`
- **Respuesta DOC** → siempre archivos completos (nunca patches)

---

# Estructura de archivos

```
.bloom/
    ├── .core/
    │   ├── .doc.instructions.bl
    │   │     Instrucciones detalladas de cómo leer, interpretar y actualizar la documentación del proyecto.
    │   │     Define el orden recomendado de lectura, los archivos intervinientes,
    │   │     las secuencias de lectura y escritura, y las buenas prácticas de redacción.
    │   │     Establece cómo la IA y los humanos deben aplicar cambios sobre los archivos DOC.
    │   │
    │   ├── .dev.instructions.bl
    │   │     Instrucciones de cómo leer el codebase, la documentación técnica y escribir código.
    │   │     Define el formato esperado de escritura, la política de archivos completos
    │   │     vs modificaciones parciales, y las pautas para navegar el contexto técnico
    │   │     de los Intents orientados a desarrollo.
    │   │
    │   ├── .dev.rules.bl
    │   │     Reglas fundamentales del ecosistema de desarrollo.
    │   │     Define principios, restricciones y comportamientos obligatorios
    │   │     para cualquier Intent orientado a código.
    │   │     Incluye templates y modelos de respuestas para la integración automática,
    │   │     así como criterios de calidad y consistencia del código generado.
    │   │
    │   └── .doc.rules.bl
    │         Reglas globales para la documentación técnica del proyecto.
    │         Define la ubicación lógica de los contenidos (arquitectura, workflow,
    │         implementación, etc.) y las estructuras recomendadas.
    │         Incluye modelos de respuestas para autogestionar actualizaciones de archivos
    │         de arquitectura, workflow e implementación a través de respuestas de la IA,
    │         asegurando coherencia entre secciones y documentos relacionados.
    │
    ├── .intents/
    │   ├── .intent.bl
    │   │     Plantilla general base para crear nuevos Intents, tanto DEV como DOC.
    │   │     Sirve como guía estructural para detallar requerimientos,
    │   │     recopilar el pedido del usuario y generar el briefing inicial.
    │   │     Define secciones estándar (objetivo, contexto, restricciones, archivos objetivo,
    │   │     criterios de aceptación) que luego serán parseadas a intent.json.
    │   │
    │   ├── .dev/
    │   │   └── .{intent-name}/
    │   │       │     Carpeta de un Intent específico de desarrollo (DEV).
    │   │       │     Su nombre identifica la acción técnica principal
    │   │       │     (por ejemplo: ui-refactory, add-auth-endpoint, optimize-query, etc.).
    │   │       │
    │   │       ├── .session_state.json
    │   │       │       Estado persistido del Intent DEV: metadata, controles de turno,
    │   │       │       flags internos, referencias a archivos y continuidad entre etapas.
    │   │       │       Registra en qué fase se encuentra el Intent (briefing, execution,
    │   │       │       refinement), así como información de auditoría y tracking.
    │   │       │
    │   │       ├── .briefing/
    │   │       │   ├── .intent.bl
    │   │       │   │       Archivo maestro del requerimiento expresado por el usuario
    │   │       │   │       para este Intent DEV específico.
    │   │       │   │       Contiene la descripción en lenguaje natural, ejemplos
    │   │       │   │       y cualquier aclaración relevante.
    │   │       │   │       Su contenido se transforma en intent.json mediante parsing estructurado.
    │   │       │   │
    │   │       │   ├── .codebase.bl
    │   │       │   │       Contenedor completo del scope de código relevante para el Intent DEV.
    │   │       │   │       Incluye únicamente los archivos que deben ser analizados,
    │   │       │   │       modificados, refactorizados o usados como referencia durante
    │   │       │   │       la ejecución del Intent.
    │   │       │   │
    │   │       │   │       Puede contener:
    │   │       │   │         • Archivos fuente completos
    │   │       │   │         • Fragmentos críticos extraídos de múltiples archivos
    │   │       │   │         • Snippets reducidos para reducir ruido contextual
    │   │       │   │         • Archivos complementarios como JSON, YAML, configs o assets técnicos
    │   │       │   │
    │   │       │   │       Este archivo define explícitamente la code surface autorizada
    │   │       │   │       para intervención por parte de la IA, actuando como una sandbox
    │   │       │   │       que limita, recorta y ordena el contexto técnico del Intent.
    │   │       │   │
    │   │       │   │       Solo está presente en Intents DEV.
    │   │       │   │       Intents DOC no utilizan .codebase.bl.
    │   │       │   │
    │   │       │   ├── .intent.json
    │   │       │   │       Requerimiento estructurado (parseado) extraído de .intent.bl.
    │   │       │   │       Define objetivos, restricciones, parámetros, archivos objetivo
    │   │       │   │       y metadata necesarios para iniciar el Intent DEV.
    │   │       │   │       Sirve como punto de verdad para la construcción de prompts
    │   │       │   │       y la orquestación posterior.
    │   │       │   │
    │   │       │   └── .index.json
    │   │       │           Resumen procesado del briefing del Intent DEV:
    │   │       │           alcance, contexto crítico, elementos clave,
    │   │       │           hipótesis relevantes y definiciones técnicas importantes.
    │   │       │           Facilita la revisión rápida del Intent sin leer
    │   │       │           todo el contenido de .intent.bl o .codebase.bl.
    │   │       │
    │   │       ├── .execution/
    │   │       │   ├── .index.json
    │   │       │   │       Registro completo del proceso de ejecución:
    │   │       │   │       decisiones tomadas por la IA, insumos utilizados,
    │   │       │   │       dependencias consultadas y anotaciones relevantes.
    │   │       │   │       Funciona como bitácora de la primera ejecución del Intent DEV.
    │   │       │   │
    │   │       │   ├── .intent.json
    │   │       │   │       Prompt exacto utilizado para la ejecución inicial del Intent DEV.
    │   │       │   │       Puede diferir de la versión de briefing debido a ajustes
    │   │       │   │       automáticos del sistema (ejemplo: reordenamiento, normalización,
    │   │       │   │       inclusión de instrucciones adicionales o restricciones específicas).
    │   │       │   │
    │   │       │   └── .response.json
    │   │       │           Resultado de la primera ejecución:
    │   │       │           deliverable inicial generado por la IA (código, análisis, refactores),
    │   │       │           junto con metadata adicional necesaria para futuras iteraciones.
    │   │       │
    │   │       └── .refinement/
    │   │           │     Contiene todas las iteraciones posteriores al deliverable inicial.
    │   │           │     Cada turno registra su propio set de prompts, contexto incremental
    │   │           │     y la respuesta resultante de la IA.
    │   │           │     Permite ajustar, corregir y profundizar sobre la solución DEV.
    │   │           │
    │   │           └── .turn_X/
    │   │               ├── .index.json
    │   │               │       Resumen explicativo del turno X:
    │   │               │       qué se pidió en esta iteración, qué cambió respecto
    │   │               │       a la versión anterior, problemas detectados y lineamientos
    │   │               │       específicos para la IA.
    │   │               │
    │   │               ├── .intent.json
    │   │               │       Prompt generado específicamente para el turno X de refinement.
    │   │               │       Puede componerse a partir de la respuesta anterior, correcciones
    │   │               │       del usuario y nuevas restricciones o aclaraciones.
    │   │               │
    │   │               └── .response.json
    │   │                       Respuesta obtenida en esta iteración concreta.
    │   │                       Registra el deliverable ajustado y cualquier información
    │   │                       adicional que influya en turnos posteriores.
    │   │
    │   └── .doc/
    │       └── .{intent-name}/
    │           │     Carpeta de un Intent específico de documentación (DOC).
    │           │     Su nombre identifica la acción documental principal
    │           │     (por ejemplo: update-architecture-docs, sync-workflow-spec, fix-impl-doc).
    │           │     A diferencia de los Intents DEV, este Intent se ejecuta en un único turno.
    │           │
    │           ├── .intent/
    │           │   ├── intent.json
    │           │   │       Requerimiento estructurado de documentación.
    │           │   │       Representa, en forma de JSON, lo que el usuario necesita
    │           │   │       cambiar o crear en la documentación.
    │           │   │
    │           │   │       Puede incluir:
    │           │   │         • tipo: "documentation"
    │           │   │         • archivos a modificar o crear
    │           │   │         • secciones objetivo (arquitectura, workflow, implementación)
    │           │   │         • criterios de aceptación de la actualización
    │           │   │         • metadata del Intent (origen, prioridad, tracking).
    │           │   │
    │           │   ├── .intent.bl
    │           │   │       Requerimiento original en texto libre, tal como lo expresa el usuario.
    │           │   │       Puede contener explicación contextual, ejemplos de antes/después,
    │           │   │       motivaciones del cambio y directivas de estilo.
    │           │   │       Es la fuente humana que luego se normaliza en intent.json.
    │           │   │
    │           │   ├── .doc.standards.bl
    │           │   │       Archivo de estándares de documentación aplicables al Intent DOC.
    │           │   │       Puede componerse de reglas globales (de .doc.rules.bl)
    │           │   │       más reglas específicas para este Intent.
    │           │   │       Define el estilo de redacción, estructura de secciones,
    │           │   │       lenguaje recomendado, nivel de detalle y convenciones terminológicas.
    │           │   │
    │           │   ├── .doc.prompt.bl
    │           │   │       Prompt final consolidado que será enviado a la IA para este Intent DOC.
    │           │   │       Integra:
    │           │   │         • instrucciones de .doc.instructions.bl
    │           │   │         • reglas de .doc.rules.bl y .doc.standards.bl
    │           │   │         • el requerimiento estructurado de intent.json
    │           │   │         • el contexto relevante de .doc.app.context.bl
    │           │   │         • referencias al árbol de archivos de .tree.bl
    │           │   │       Es el punto de entrada único para la ejecución de documentación,
    │           │   │       diseñado para un solo turno sin etapas de refinement.
    │           │   │
    │           │   ├── .doc.app.context.bl
    │           │   │       Contexto documental consolidado del proyecto relevante para este Intent DOC.
    │           │   │       Puede contener extractos de:
    │           │   │         • .doc.app.architecture.bl
    │           │   │         • .doc.app.workflow.bl
    │           │   │         • .doc.app.implementation.bl
    │           │   │       Incluye únicamente las partes necesarias para entender y actualizar
    │           │   │       correctamente la documentación objetivo del Intent.
    │           │   │
    │           │   ├── .tree.bl
    │           │   │       Mapa estructural (parcial o completo) del proyecto, enfocado en los
    │           │   │       archivos relevantes para la documentación a modificar.
    │           │   │       Permite a la IA entender cómo se organizan los archivos,
    │           │   │       sin necesidad de acceder a su contenido completo.
    │           │   │
    │           │   └── index.json
    │           │           Resumen de alto nivel del Intent DOC:
    │           │           objetivo, archivos/documentos involucrados, contexto aplicado,
    │           │           supuestos relevantes y cualquier decisión previa del sistema.
    │           │           Facilita la lectura rápida del Intent sin inspeccionar cada archivo.
    │           │
    │           └── .response/
    │               └── .response.json
    │                       Único deliverable final del Intent DOC.
    │                       Contiene la salida de la IA lista para aplicar sobre los archivos
    │                       de documentación del proyecto.
    │
    │                       Usualmente incluye:
    │                         • un mapa de archivos y su nuevo contenido completo
    │                         • un resumen de cambios realizados
    │                         • notas adicionales o aclaraciones que faciliten la implementación.
    │
    └── .project/
        ├── .dev.strategy.standards.bl
        │       Estándares técnicos, patrones arquitectónicos, convenciones
        │       de estilo y lineamientos que rigen la generación, refactorización
        │       y manipulación de código fuente a nivel de proyecto.
        │       Aplica como base para todos los Intents DEV.
        │
        ├── .dev.strategy.context.bl
        │       Contexto técnico del proyecto: estructura del código,
        │       arquitectura global, dependencias, convenciones internas, módulos
        │       principales y cualquier información necesaria para ejecutar Intents DEV.
        │       Proporciona una vista de alto nivel para que la IA entienda
        │       el entorno donde operan los cambios de código.
        │
        ├── .doc.app.architecture.bl
        │       Arquitectura conceptual del sistema: visión general del producto,
        │       componentes principales, relaciones entre subsistemas,
        │       modelo de dominio, reglas de negocio de alto nivel
        │       y estructura fundamental de la solución.
        │       Define “qué es” el sistema y cómo está organizado en términos estructurales.
        │
        ├── .doc.app.workflow.bl
        │       Flujos de uso del sistema: roles participantes, casos de uso,
        │       procesos operativos paso a paso, validaciones funcionales
        │       y escenarios típicos de interacción.
        │       Explica “cómo se utiliza” el sistema desde la perspectiva del negocio
        │       y de los usuarios finales.
        │
        ├── .doc.app.implementation.bl
        │       Detalle técnico de implementación: servicios, modelos de datos,
        │       integraciones externas, APIs, dependencias y restricciones técnicas.
        │       Explica “cómo se ejecuta y materializa” el sistema en términos
        │       de código, infraestructura y componentes tecnológicos.
        │
        └── .tree.bl
                Mapa estructural completo del proyecto (filesystem en formato árbol).
                Permite navegación abstracta, referencia cruzada y análisis
                sin necesidad de abrir archivos individuales.
                Es utilizado como base tanto para Intents DEV como DOC
                para comprender la topología del repositorio.
```

**Este diseño es la versión final y vigente de BTIP a diciembre 2025.**