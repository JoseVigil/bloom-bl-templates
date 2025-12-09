
# Arquitectura Final BTIP — Documentación Oficial Actualizada (Diciembre 2025)

A continuación se presenta la estructura completa y actualizada del ecosistema BTIP (Bloom-TIP), con todas las carpetas, archivos y su propósito exacto.

---

## Estructura de archivos:

`
.bloom/
├── .core/
│   ├── .doc.instructions.bl
│   ├── .dev.instructions.bl
│   ├── .dev.rules.bl
│   └── .doc.rules.bl
├── .intents/
│   ├── .dev/
│   │   └── .<intent-name-uiid>/
│   │       ├── .session_state.json
│   │       ├── .briefing/
│   │       │   ├── .intent.bl
│   │       │   ├── .intent.json
│   │       │   ├── .codebase.bl
│   │       │   └── .index.json
│   │       ├── .execution/
│   │       │   ├── .index.json
│   │       │   ├── .intent.json
│   │       │   ├── .codebase.bl
│   │       │   └── .response.json
│   │       └── .refinement/
│   │           └── .turn_X/
│   │               ├── .index.json
│   │               ├── .intent.json
│   │               ├── .codebase.bl
│   │               └── .response.json
│   └── .doc/
│       └── .<intent-name-uiid>/
│           ├── .intent/
│           │   ├── intent.json
│           │   ├── .intent.bl
│           │   ├── .doc.standards.bl
│           │   ├── .doc.prompt.bl
│           │   ├── .doc.app.context.bl
│           │   ├── .tree.bl
│           │   └── index.json
│           └── .response/
│               └── .response.json
└── .project/
    ├── .dev.strategy.standards.bl
    ├── .dev.strategy.context.bl
    ├── .doc.app.architecture.bl
    ├── .doc.app.workflow.bl
    ├── .doc.app.implementation.bl
    └── .tree.bl 
`

---

## 1. Carpeta `.bloom/.core/`

Contiene las reglas maestras del ecosistema BTIP. Define el comportamiento obligatorio tanto para IA como para humanos.

### `.doc.instructions.bl`
Instrucciones detalladas de cómo leer, interpretar y actualizar la documentación del proyecto.  
Define el orden recomendado de lectura, los archivos intervinientes, las secuencias de lectura y escritura, y las buenas prácticas de redacción.  
Establece cómo la IA y los humanos deben aplicar cambios sobre los archivos DOC.

### `.dev.instructions.bl`
Instrucciones de cómo leer el codebase, la documentación técnica y escribir código.  
Define el formato esperado de escritura, la política de archivos completos vs modificaciones parciales, y las pautas para navegar el contexto técnico de los Intents orientados a desarrollo.

### `.dev.rules.bl`
Reglas fundamentales del ecosistema de desarrollo.  
Define principios, restricciones y comportamientos obligatorios para cualquier Intent orientado a código.  
Incluye templates y modelos de respuestas para la integración automática, así como criterios de calidad y consistencia del código generado.

### `.doc.rules.bl`
Reglas globales para la documentación técnica del proyecto.  
Define la ubicación lógica de los contenidos (arquitectura, workflow, implementación) y las estructuras recomendadas.  
Incluye modelos de respuestas para autogestionar actualizaciones de archivos documentales, asegurando coherencia entre secciones.

---

## 2. Carpeta `.bloom/.intents/`

Contiene todos los **Intents**, tanto de desarrollo (**DEV**) como de documentación (**DOC**).

---

# 2.1 Plantilla global de Intent
### `.intent.bl`
Plantilla base para crear nuevos Intents DEV o DOC.  
Define secciones estándar:  
- objetivo  
- contexto  
- restricciones  
- archivos objetivo  
- criterios de aceptación  

Es la fuente que luego se parsea a `intent.json`.

---

# 2.2 Intents DEV — `.bloom/.intents/.dev/<intent-name-uuid>/`

Un Intent DEV se ejecuta en **3 etapas**:  
**briefing → execution → refinement**

---

## A. `.session_state.json`
Estado persistente del Intent DEV:  
- turno actual  
- flags internos  
- fase del Intent  
- referencias a archivos  
- auditoría y tracking  

---

## B. Carpeta `.briefing/`

### `.intent.bl`
Requerimiento original del usuario (texto libre).  
Define contexto, aclaraciones, ejemplos, acciones y restricciones.

### `.codebase.bl`
Scope de código que la IA puede tocar o usar como referencia:  
- archivos completos  
- fragmentos críticos  
- snippets reducidos  
- archivos JSON / YAML / configs  

Actúa como sandbox técnica.

### `.intent.json`
Parsing estructurado del requerimiento:  
- objetivos  
- constraints  
- parámetros  
- metadata técnica  
- archivos objetivo  

### `.index.json`
Resumen procesado del briefing:  
- alcance  
- contexto crítico  
- hipótesis  
- definiciones clave  

Facilita revisión rápida sin inspeccionar archivos completos.

---

## C. Carpeta `.execution/`

### `.index.json`
Log completo del proceso de ejecución:  
- decisiones  
- dependencias consultadas  
- anotaciones  
- reasoning útil para auditoría  

### `.intent.json`
Prompt exacto enviado a la IA durante la ejecución inicial (puede diferir del briefing).

### `.response.json`
Deliverable inicial:  
- código generado o modificado  
- análisis  
- notas para refinamiento  

---

## D. Carpeta `.refinement/`

Contiene cada turno posterior al deliverable inicial.

```
.turn_1/
    .index.json
    .intent.json
    .response.json

.turn_2/
    ...
```

### `.index.json`
Resumen por turno: qué se pidió, qué cambió, problemas encontrados.

### `.intent.json`
Prompt específico del turno.

### `.response.json`
Respuesta ajustada para ese turno.

---

# 2.3 Intents DOC — `.bloom/.intents/.doc/<intent-name-uuid>/`

Un Intent DOC es **single-turn**. No tiene refinamiento.

---

## A. Carpeta `.intent/`

### `intent.json`
Requerimiento estructurado del Intent documental.

Incluye:  
- tipo: documentation  
- archivos a modificar/crear  
- secciones objetivo  
- criterios de aceptación  
- metadata  

### `.intent.bl`
Requerimiento original del usuario (texto libre).  
Ejemplos, motivaciones y estilo deseado.

### `.doc.standards.bl`
Reglas documentales del Intent:  
- estilo  
- estructura  
- lenguaje  
- convenciones terminológicas  

Combina reglas globales + reglas específicas.

### `.doc.prompt.bl`
Prompt final consolidado que se envía a la IA.  
Integra:  
- instrucciones de `.doc.instructions.bl`  
- reglas de `.doc.rules.bl` y `.doc.standards.bl`  
- el requerimiento de `intent.json`  
- contexto documental: `.doc.app.context.bl`  
- referencias del árbol de archivos: `.tree.bl`

### `.doc.app.context.bl`
Contexto documental relevante:  
- arquitectura  
- workflow  
- implementación  

Solo lo necesario para este Intent.

### `.tree.bl`
Mapa estructural del proyecto.

### `index.json`
Resumen de alto nivel:  
- objetivo  
- archivos involucrados  
- contexto aplicado  
- decisiones previas  

---

## B. Carpeta `.response/`

### `.response.json`
Único deliverable final de un Intent DOC.

Incluye:  
- mapa de archivos → contenido completo nuevo  
- resumen de cambios  
- notas adicionales  

---

# 3. Carpeta `.bloom/.project/`

Documentación canónica del proyecto (fuente oficial).

### `.dev.strategy.standards.bl`
Reglas técnicas centrales del proyecto.

### `.dev.strategy.context.bl`
Contexto técnico global:  
- arquitectura  
- módulos  
- dependencias  
- convenciones  

### `.doc.app.architecture.bl`
Qué es el sistema:  
- arquitectura conceptual  
- dominio  
- componentes  
- relaciones  

### `.doc.app.workflow.bl`
Cómo se usa el sistema:  
- roles  
- casos de uso  
- procesos operativos  
- validaciones  

### `.doc.app.implementation.bl`
Cómo está implementado:  
- servicios  
- modelos de datos  
- APIs  
- integraciones  
- infraestructura  

### `.tree.bl`
Árbol completo del proyecto.  
Usado por Intents DEV y DOC.

---

# Resumen final

- **Intents DEV:** complejos, iterativos, multietapa.  
- **Intents DOC:** single-turn, transaccionales, consistentes y rápidos.  
- **Todo contenido técnico del proyecto vive en `.bloom/.project/`.**  
- **Toda actividad operativa corre dentro de `.bloom/.intents/`.**  
- **Reglas maestras del ecosistema están en `.bloom/.core/`.**

Este diseño es **la versión final y vigente del ecosistema BTIP a diciembre 2025**.
