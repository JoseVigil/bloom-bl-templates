# Arquitectura Final BTIP — Documentación Oficial Actualizada (Diciembre 2025)

    A continuación se presenta la estructura completa y actualizada del ecosistema BTIP (Bloom-TIP), con todas las carpetas, archivos y su propósito exacto.

    ## 1. Carpeta .bloom/.core/
    Contiene las reglas maestras del ecosistema BTIP. Define el comportamiento obligatorio tanto para IA como para humanos.

    | Archivo                  | Propósito principal                                                               | Contenido clave esperado                                                                                  |
    |--------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
    | .doc.instructions.bl     | Guía operativa para leer, interpretar y actualizar cualquier documentación       | • Navegación de archivos DOC<br>• Buenas prácticas de redacción<br>• Orden lógico arquitectura → workflow → implementación<br>• Convenciones de formato<br>• Reglas de actualización por IA |
    | .dev.instructions.bl     | Instrucciones para interpretar el codebase y escribir/modificar código           | • Uso de .codebase.bl y .tree.bl<br>• Políticas archivos completos vs patches<br>• Estructura respuestas DEV |
    | .dev.rules.bl            | Reglas técnicas obligatorias para todos los Intents DEV                           | • Restricciones técnicas<br>• Modelos de respuesta<br>• Políticas de seguridad y consistencia            |
    | .doc.rules.bl            | Reglas generales de documentación técnica                                         | • Límites de modificación<br>• Estructura estándar<br>• Coherencia entre archivos                         |

    ## 2. Carpeta .bloom/.intents/.dev/<intent>/
    Flujo complejo de 3 etapas: briefing → execution → refinement

        2.1 Control de sesión
            • .session_state.json → Estado persistente (turno, flags, progreso, checkpoints)

        2.2 .briefing/
            | Archivo         | Contenido                                                                 |
            |-----------------|---------------------------------------------------------------------------|
            | .intent.bl      | Requerimiento original del usuario (texto libre)                          |
            | .codebase.bl    | Scope autorizado de código (solo archivos relevantes)                     |
            | .intent.json    | Parsing estructurado: objetivo, constraints, parámetros, dependencias     |
            | .index.json     | Resumen sintético del alcance y hipótesis                                 |

        2.3 .execution/
            | Archivo         | Contenido                                                                 |
            |-----------------|---------------------------------------------------------------------------|
            | .index.json     | Log completo de decisiones y dependencias                                 |
            | .intent.json    | Prompt exacto enviado a la IA                                             |
            | .response.json  | Primera respuesta del modelo (código + análisis)                          |

        2.4 .refinement/
            turn_1/
               ├─ .index.json
               ├─ .intent.json
               └─ .response.json
            turn_2/
               └─ ...

    ## 3. Carpeta .bloom/.intents/.doc/<intent>/
    Intent DOC: single-turn, directo y transaccional (sin refinement)

        3.1 .intent/ (todo lo necesario para un único output)
            | Archivo                 | Propósito                                                             | Contenido clave                                                                 |
            |-------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------------|
            | intent.json             | Representación estructurada del requerimiento documental             | tipo, archivos a modificar, secciones nuevas, criterios de aceptación          |
            | .intent.bl              | Requerimiento original en texto libre                                 | Descripción cruda + contexto                                                    |
            | .doc.standards.bl       | Reglas normalizadas específicas de este Intent DOC                   | .doc.rules.bl + reglas propias                                                  |
            | .doc.prompt.bl          | Prompt final enviado a la IA (generado automáticamente por BTIP)     | Instrucciones + contexto + archivos objetivo + formato esperado                |
            | .doc.app.context.bl     | Contexto documental relevante                                        | Extractos de architecture/workflow/implementation                              |
            | .tree.bl                | Árbol actual del filesystem                                           | Navegación abstracta                                                            |
            | index.json              | Resumen interno para auditoría                                        | objetivo, archivos, tipo de cambio                                              |

        3.2 .response/
            • Único deliverable final
            {
              "files": {
                "doc.app.architecture.bl": "<contenido completo actualizado>",
                "doc.app.workflow.bl": "<contenido completo actualizado>"
              },
              "summary": "Se actualizaron 2 archivos con las nuevas descripciones…",
              "notes": "Razonamiento interno y decisiones tomadas"
            }
            → Transacción cerrada. No hay más turnos.

    ## 4. Carpeta .bloom/.project/
    Documentación oficial canónica del proyecto

    | Archivo                        | Contenido principal                                                                      |
    |--------------------------------|------------------------------------------------------------------------------------------|
    | .dev.strategy.standards.bl     | Reglas técnicas universales: patrones, convenciones, arquitectura obligatoria           |
    | .dev.strategy.context.bl       | Contexto técnico: módulos, dependencias, configuraciones                                 |
    | .doc.app.architecture.bl       | Qué es el sistema: componentes, dominio, modelos, relaciones                            |
    | .doc.app.workflow.bl           | Cómo se usa: casos de uso, roles, flujos operativos                                      |
    | .doc.app.implementation.bl     | Cómo está implementado: servicios, APIs, integraciones, detalles técnicos               |
    | .tree.bl                       | Árbol completo del proyecto (usado por Intents DEV y DOC)                                |

    ## Resumen de la evolución
        • Intents DEV → mantienen 3 etapas (complejo e iterativo)
        • Intents DOC → ahora single-turn y transaccionales → máxima velocidad y consistencia
        • Prompt final de documentación → generado automáticamente en .doc.prompt.bl
        • Respuesta DOC → siempre archivos completos (nunca patches)

    Este diseño es la versión final y vigente de BTIP a diciembre 2025.