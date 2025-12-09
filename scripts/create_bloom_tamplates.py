import os
import json
import sys
from pathlib import Path
from datetime import datetime

def create_file_structure(base_path="."):
    """
    Crea la estructura completa de archivos .bloom con las nuevas carpetas .dev y .doc
    """
    
    # Asegurar que la ruta base existe
    base_path = Path(base_path).resolve()
    print(f"📍 Creando estructura en: {base_path}")
    
    # Definir la estructura como un diccionario
    structure = {
        ".bloom": {
            ".core": {
                ".doc.instructions.bl": "",
                ".dev.instructions.bl": "",
                ".dev.rules.bl": "",
                ".doc.rules.bl": ""
            },
            
            ".intents": {
                ".dev": {
                    # Directorios de intents DEV se crearán dinámicamente
                },
                ".doc": {
                    # Directorios de intents DOC se crearán dinámicamente
                }
            },
            
            ".project": {
                ".dev.strategy.standards.bl": "",
                ".dev.strategy.context.bl": "",
                ".doc.app.architecture.bl": "",
                ".doc.app.workflow.bl": "",
                ".doc.app.implementation.bl": "",
                ".tree.bl": ""
            }
        }
    }

    def create_files_and_dirs(base, structure):
        """
        Función recursiva para crear directorios y archivos
        """
        for name, content in structure.items():
            path = base / name
            
            if isinstance(content, dict):
                # Es un directorio
                os.makedirs(path, exist_ok=True)
                print(f"✓ Directorio creado: {path.relative_to(base_path)}")
                create_files_and_dirs(path, content)
            else:
                # Es un archivo
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Archivo creado: {path.relative_to(base_path)}")

    # Crear la estructura
    print("🚀 Creando estructura .bloom...")
    print("=" * 50)
    
    try:
        create_files_and_dirs(base_path, structure)
        
        # Crear intents de ejemplo
        create_example_dev_intent(base_path)
        create_example_doc_intent(base_path)
        
        print("=" * 50)
        print(f"✅ Estructura creada exitosamente en: {base_path}")
        
        # Mostrar resumen de lo creado
        print("\n📁 Resumen de estructura creada:")
        print_tree(base_path / ".bloom")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def create_example_dev_intent(base_path):
    """
    Crea un ejemplo de intent DEV con la estructura actualizada
    """
    base_path = Path(base_path).resolve()
    intent_name = "example-dev"
    intent_path = base_path / ".bloom" / ".intents" / ".dev" / f".{intent_name}"
    
    print(f"\n💻 Creando intent DEV: {intent_name}")
    
    # Crear directorio del intent
    os.makedirs(intent_path, exist_ok=True)
    print(f"✓ Directorio creado: {intent_path.relative_to(base_path)}")
    
    # Estructura de archivos para intent DEV (actualizada)
    dev_structure = {
        ".session_state.json": json.dumps({
            "metadata": {
                "nombre": intent_name,
                "tipo": "DEV",
                "fecha_creacion": datetime.now().isoformat(),
                "estado": "iniciado",
                "version": "1.0.0"
            },
            "turn_controls": {
                "turno_actual": 0,
                "max_turnos": 10,
                "historial_turnos": []
            },
            "flags": {
                "completado": False,
                "necesita_revision": False,
                "bloqueado": False
            },
            "internal_references": {
                "archivos_modificados": [],
                "dependencias": []
            },
            "continuity": {
                "contexto_previo": "",
                "decisiones_pendientes": []
            }
        }, indent=2, ensure_ascii=False),
        
        ".briefing": {
            ".intent.bl": """# Intent DEV de ejemplo

## Objetivo
Implementar una nueva funcionalidad de ejemplo para el sistema.

## Contexto
Este es un intent de desarrollo para demostrar la estructura actualizada.

## Requerimientos
1. Crear nuevo módulo de ejemplo
2. Implementar pruebas unitarias
3. Documentar la implementación

## Restricciones
- Mantener compatibilidad con versiones anteriores
- Seguir estándares de código establecidos
- No modificar APIs existentes sin aprobación

## Entregables
1. Código fuente del módulo
2. Pruebas unitarias
3. Documentación técnica""",
            
            ".intent.json": json.dumps({
                "objetivos": [
                    "Implementar módulo de ejemplo",
                    "Crear pruebas unitarias",
                    "Documentar la implementación"
                ],
                "restricciones": [
                    "Mantener compatibilidad con versiones anteriores",
                    "Seguir estándares de código establecidos",
                    "No modificar APIs existentes sin aprobación"
                ],
                "parametros": {
                    "ambito": "backend",
                    "tecnologias": ["python", "fastapi", "pytest"],
                    "tiempo_estimado": "4 horas"
                },
                "metadata": {
                    "tipo": "DEV",
                    "prioridad": "media",
                    "complejidad": "media",
                    "autor": "sistema",
                    "fecha": datetime.now().isoformat()
                }
            }, indent=2, ensure_ascii=False),
            
            ".codebase.bl": """# Codebase para análisis - Intent DEV

## Archivos relevantes del proyecto

### Estructura del proyecto
/proyecto/
├── src/
│   ├── main.py
│   └── modules/
│       └── ejemplo.py
├── tests/
│   └── test_ejemplo.py
└── requirements.txt

### Código existente (referencia)
# src/main.py
from fastapi import FastAPI
from modules import ejemplo

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API funcionando"}

# src/modules/ejemplo.py
def funcion_existente():
    return "Función existente"

### Dependencias
fastapi>=0.100.0
pytest>=7.4.0""",
            
            ".index.json": json.dumps({
                "resumen": "Intent DEV para implementar nuevo módulo de ejemplo",
                "alcance": "Desarrollo de funcionalidad nueva con pruebas",
                "contexto": "Proyecto necesita expandir funcionalidades base",
                "elementos_clave": [
                    "módulo-nuevo",
                    "pruebas-unitarias", 
                    "documentación-técnica"
                ],
                "hipotesis": [
                    "El código base es estable",
                    "Los estándares están documentados",
                    "El equipo conoce las tecnologías"
                ],
                "definiciones_criticas": {
                    "módulo-nuevo": "Componente independiente con funcionalidad específica",
                    "pruebas-unitarias": "Tests que validan unidades individuales de código"
                }
            }, indent=2, ensure_ascii=False)
        },
        
        ".execution": {
            ".index.json": json.dumps({
                "registro": [
                    "Inicio de ejecución del intent DEV",
                    "Análisis de codebase proporcionado",
                    "Diseño de solución propuesta"
                ],
                "decisiones": [
                    "Usar arquitectura modular",
                    "Implementar patrón repository",
                    "Separar lógica de negocio de API"
                ],
                "insumos": [
                    "briefing/.intent.bl",
                    "briefing/.codebase.bl",
                    "briefing/.intent.json"
                ],
                "dependencias": [
                    ".dev.strategy.standards.bl",
                    ".dev.strategy.context.bl"
                ],
                "anotaciones": [
                    "Priorizar código limpio y mantenible",
                    "Considerar escalabilidad futura"
                ]
            }, indent=2, ensure_ascii=False),
            
            ".intent.json": json.dumps({
                "prompt": "Implementar nuevo módulo de ejemplo basado en el codebase proporcionado, incluyendo pruebas y documentación.",
                "ajustes_sistema": {
                    "formato_respuesta": "código-completo",
                    "incluir_pruebas": True,
                    "incluir_documentacion": True,
                    "nivel_detalle": "alto"
                }
            }, indent=2, ensure_ascii=False),
            
            ".codebase.bl": """# Codebase para ejecución - Estado actual

## Archivos a modificar/crear

### Nuevo archivo: src/modules/nuevo_modulo.py
# [ESPERANDO IMPLEMENTACIÓN]

### Archivo de pruebas: tests/test_nuevo_modulo.py  
# [ESPERANDO IMPLEMENTACIÓN]

### Actualización: src/main.py
# Necesita importar el nuevo módulo

### Contexto técnico actual
- Python 3.11+
- FastAPI 0.100.0+
- Pytest 7.4.0+
- Estructura modular establecida""",
            
            ".response.json": json.dumps({
                "deliverable": "Implementación completa del nuevo módulo",
                "analisis": "Solución propuesta cumple con requisitos y estándares",
                "artefactos": [
                    "src/modules/nuevo_modulo.py",
                    "tests/test_nuevo_modulo.py",
                    "actualización de src/main.py"
                ],
                "notas_tecnicas": [
                    "Usa type hints para mejor mantenibilidad",
                    "Incluye docstrings completos",
                    "Pruebas cubren casos edge"
                ]
            }, indent=2, ensure_ascii=False)
        },
        
        ".refinement": {
            ".turn_1": {
                ".index.json": json.dumps({
                    "resumen": "Primer turno de refinamiento - Revisión de implementación",
                    "cambios_solicitados": "Optimizar rendimiento y mejorar manejo de errores",
                    "problemas_detectados": [
                        "Algunas funciones pueden ser más eficientes",
                        "Falta validación de inputs en casos edge"
                    ],
                    "lineamientos": "Mantener funcionalidad existente, mejorar calidad del código"
                }, indent=2, ensure_ascii=False),
                
                ".intent.json": json.dumps({
                    "prompt": "Refinar la implementación del módulo nuevo, optimizando rendimiento y mejorando manejo de errores basado en el codebase actual.",
                    "contexto_turno": {
                        "turno_anterior": "implementacion-inicial",
                        "estado_actual": "codigo-funcional-necesita-optimizacion",
                        "feedback": "Buena implementación base, necesita mejoras de rendimiento y robustez"
                    }
                }, indent=2, ensure_ascii=False),
                
                ".codebase.bl": """# Codebase para refinamiento - Estado actual

## Código implementado (para revisión)

### src/modules/nuevo_modulo.py
def funcion_ejemplo(param):
    # Implementación actual
    resultado = procesar(param)
    return resultado

def procesar(data):
    # Lógica actual
    return data * 2

### tests/test_nuevo_modulo.py
def test_funcion_ejemplo():
    assert funcion_ejemplo(2) == 4

### Áreas para mejora identificadas:
1. Optimización de algoritmos
2. Mejor manejo de errores  
3. Validación más robusta de inputs
4. Logging y monitoreo

### Métricas actuales:
- Complejidad ciclomática: 5
- Cobertura de tests: 85%
- Tiempo ejecución: 15ms promedio""",
                
                ".response.json": json.dumps({
                    "respuesta": "Refinamientos aplicados al código",
                    "cambios_aplicados": [
                        "Algoritmo optimizado para mejor rendimiento",
                        "Manejo de errores mejorado con excepciones específicas",
                        "Validación de inputs más robusta",
                        "Logging agregado para diagnóstico"
                    ],
                    "resultados": [
                        "Reducción 30% en tiempo de ejecución",
                        "Cobertura de tests aumentada a 95%",
                        "Mejor manejo de casos edge"
                    ]
                }, indent=2, ensure_ascii=False)
            }
        }
    }
    
    # Crear estructura DEV recursivamente
    def create_dev_intent_structure(base, structure):
        for name, content in structure.items():
            path = base / name
            
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                print(f"✓ Directorio creado: {path.relative_to(base_path)}")
                create_dev_intent_structure(path, content)
            else:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Archivo creado: {path.relative_to(base_path)}")
    
    create_dev_intent_structure(intent_path, dev_structure)
    print(f"✅ Intent DEV '{intent_name}' creado exitosamente!")
    return True

def create_example_doc_intent(base_path):
    """
    Crea un ejemplo de intent DOC
    """
    base_path = Path(base_path).resolve()
    intent_name = "example-doc"
    intent_path = base_path / ".bloom" / ".intents" / ".doc" / f".{intent_name}"
    
    print(f"\n📄 Creando intent DOC: {intent_name}")
    
    # Crear directorio del intent
    os.makedirs(intent_path, exist_ok=True)
    print(f"✓ Directorio creado: {intent_path.relative_to(base_path)}")
    
    # Estructura de archivos para intent DOC
    doc_structure = {
        ".intent": {
            "intent.json": json.dumps({
                "requerimiento": "Documentar nueva funcionalidad del módulo de ejemplo",
                "tipo": "DOC",
                "prioridad": "media",
                "ambito": "documentacion-tecnica",
                "tecnologias": ["markdown", "diagramas", "ejemplos-codigo"],
                "tiempo_estimado": "2 horas",
                "metadata": {
                    "autor": "sistema",
                    "fecha": datetime.now().isoformat(),
                    "version": "1.0.0"
                }
            }, indent=2, ensure_ascii=False),
            
            ".intent.bl": """# Intent DOC: Documentar módulo de ejemplo

## Objetivo
Crear documentación técnica completa para el nuevo módulo implementado.

## Alcance
- Documentación de arquitectura
- Guías de uso
- Referencias de API
- Ejemplos de código

## Público objetivo
- Desarrolladores del equipo
- Nuevos integrantes
- Mantenimiento y soporte

## Formato requerido
- Markdown con extensiones técnicas
- Diagramas en formato Mermaid
- Ejemplos de código ejecutables
- Referencias cruzadas""",
            
            ".doc.standards.bl": """# Estándares de documentación aplicables

## Formato
- Usar Markdown con extensiones GitHub
- Encabezados: # Título, ## Sección, ### Subsección
- Código: ```python con resaltado de sintaxis
- Diagramas: ```mermaid para gráficos

## Estructura obligatoria
1. Introducción y propósito
2. Instalación y configuración
3. Uso básico y ejemplos
4. Referencia de API
5. Solución de problemas

## Calidad requerida
- Claridad y precisión técnica
- Ejemplos prácticos y realistas
- Mantenibilidad y facilidad de actualización
- Consistencia con documentación existente""",
            
            ".doc.prompt.bl": """# Prompt final para generación de documentación

Genera documentación técnica completa para el nuevo módulo de ejemplo, incluyendo:

## Secciones requeridas:
1. **Introducción**: Propósito y alcance del módulo
2. **Instalación**: Cómo integrar el módulo en un proyecto existente
3. **Uso básico**: Ejemplo mínimo funcional
4. **API Reference**: Documentación detallada de todas las funciones públicas
5. **Ejemplos avanzados**: Casos de uso complejos
6. **Solución de problemas**: Errores comunes y cómo resolverlos

## Requisitos específicos:
- Incluir diagramas Mermaid para arquitectura
- Proporcionar ejemplos de código ejecutables
- Usar tablas para parámetros y retornos
- Incluir notas de versión y compatibilidad
- Referenciar documentación relacionada

## Formato de salida:
Documento Markdown completo listo para usar en el proyecto.""",
            
            ".doc.app.context.bl": """# Contexto del proyecto para documentación

## Proyecto actual: bloom-videos
Sistema de gestión y procesamiento de videos con funcionalidades avanzadas.

## Arquitectura existente:
- Backend: FastAPI + Python
- Base de datos: PostgreSQL
- Almacenamiento: S3 compatible
- Colas de procesamiento: Redis + Celery

## Módulos relacionados:
- `video_processor`: Procesamiento de videos
- `storage_manager`: Gestión de almacenamiento
- `api_gateway`: Punto de entrada API

## Estándares técnicos:
- Python 3.11+
- Type hints obligatorios
- Pruebas unitarias > 90% cobertura
- Documentación en Markdown

## Estructura de archivos relevante:
/proyecto/
├── docs/
│   ├── api/          # Documentación de API
│   ├── guides/       # Guías de usuario
│   └── technical/    # Documentación técnica
└── src/
    └── modules/      # Módulos del sistema""",
            
            ".tree.bl": """# Estructura de archivos relevante para documentación

## Raíz del proyecto
/proyecto/
│
├── docs/                          # Documentación principal
│   ├── api/                       # Referencias de API
│   │   ├── video_processor.md     # Módulo procesador
│   │   ├── storage_manager.md     # Módulo almacenamiento
│   │   └── index.md               # Índice API
│   │
│   ├── guides/                    # Guías de usuario
│   │   ├── getting_started.md     # Inicio rápido
│   │   ├── deployment.md          # Despliegue
│   │   └── troubleshooting.md     # Solución problemas
│   │
│   └── technical/                 # Documentación técnica
│       ├── architecture.md        # Arquitectura
│       ├── modules.md             # Módulos
│       └── standards.md           # Estándares
│
└── src/                           # Código fuente
    └── modules/                   # Módulos implementados
        ├── video_processor/       # Procesador de videos
        ├── storage_manager/       # Gestor almacenamiento
        └── nuevo_modulo/          # [NUEVO] Módulo a documentar""",
            
            "index.json": json.dumps({
                "resumen": "Intent para documentar nuevo módulo de ejemplo",
                "alcance": "Documentación técnica completa",
                "contexto": "Proyecto requiere documentación para nuevo módulo",
                "elementos_clave": [
                    "documentacion-tecnica",
                    "referencia-api",
                    "ejemplos-codigo",
                    "diagramas-arquitectura"
                ],
                "hipotesis": [
                    "El módulo está implementado y funciona",
                    "Los desarrolladores usarán la documentación",
                    "La documentación será mantenida"
                ],
                "definiciones_criticas": {
                    "documentacion-tecnica": "Documentación para desarrolladores sobre uso y mantenimiento",
                    "referencia-api": "Documentación detallada de interfaces públicas"
                }
            }, indent=2, ensure_ascii=False)
        },
        
        ".response": {
            ".response.json": json.dumps({
                "entrega": "Documentación técnica completa del nuevo módulo",
                "contenido": "# Documentación del Módulo de Ejemplo\n\n## 1. Introducción\n\nEste módulo proporciona funcionalidades de ejemplo para el sistema...\n\n## 2. Instalación\n\n```bash\npip install proyecto-ejemplo\n```\n\n## 3. Uso básico\n\n```python\nfrom modulo_ejemplo import funcion_principal\n\nresultado = funcion_principal(parametro)\n```\n\n## 4. Referencia de API\n\n### `funcion_principal(parametro: str) -> str`\nProcesa el parámetro y retorna resultado...\n\n## 5. Ejemplos avanzados\n\n```python\n# Ejemplo de uso avanzado\n```\n\n## 6. Solución de problemas\n\n### Error común 1: ...\nSolución: ...\n\n---\n\n*Documentación generada el " + datetime.now().strftime("%Y-%m-%d") + "*",
                "metadatos": {
                    "formato": "markdown",
                    "longitud": "aproximadamente 1500 palabras",
                    "diagramas_incluidos": 2,
                    "ejemplos_codigo": 5,
                    "referencias_cruzadas": 8
                },
                "validaciones": [
                    "Cumple con estándares de formato",
                    "Incluye todos los elementos requeridos",
                    "Ejemplos de código verificados",
                    "Referencias cruzadas correctas"
                ]
            }, indent=2, ensure_ascii=False)
        }
    }
    
    # Crear estructura DOC recursivamente
    def create_doc_intent_structure(base, structure):
        for name, content in structure.items():
            path = base / name
            
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                print(f"✓ Directorio creado: {path.relative_to(base_path)}")
                create_doc_intent_structure(path, content)
            else:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Archivo creado: {path.relative_to(base_path)}")
    
    create_doc_intent_structure(intent_path, doc_structure)
    print(f"✅ Intent DOC '{intent_name}' creado exitosamente!")
    return True

def print_tree(path, indent=""):
    """
    Imprime la estructura de directorios en formato árbol
    """
    if not path.exists():
        return
    
    # Ordenar: directorios primero, luego archivos
    items = []
    for item in path.iterdir():
        if item.name not in ['.<intent-name>', '.<intent-name>']:
            items.append(item)
    
    items.sort(key=lambda x: (x.is_file(), x.name))
    
    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        prefix = "└── " if is_last else "├── "
        
        print(f"{indent}{prefix}{item.name}")
        
        if item.is_dir():
            extension = "    " if is_last else "│   "
            print_tree(item, indent + extension)

def main():
    """
    Función principal del script
    """
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Crea la estructura actualizada de archivos .bloom',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  %(prog)s                            # Crea en directorio actual
  %(prog)s /ruta/destino              # Crea en ruta específica
  %(prog)s --path /mi/proyecto        # Usando flag --path
  
Estructura creada incluye:
  • Archivos .codebase.bl en execution y refinement
  • Intent DEV completo con contenido de ejemplo
  • Intent DOC completo con contenido de ejemplo
        """
    )
    
    parser.add_argument(
        'path', 
        nargs='?', 
        default='.', 
        help='Ruta donde crear la estructura (por defecto: directorio actual)'
    )
    
    parser.add_argument(
        '--no-examples',
        action='store_true',
        help='No crear intents de ejemplo'
    )
    
    parser.add_argument(
        '--dev-intent',
        default='example-dev',
        help='Nombre del intent DEV de ejemplo (por defecto: example-dev)'
    )
    
    parser.add_argument(
        '--doc-intent', 
        default='example-doc',
        help='Nombre del intent DOC de ejemplo (por defecto: example-doc)'
    )
    
    # Si no se pasan argumentos, mostrar ayuda
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    args = parser.parse_args()
    
    # Crear estructura principal
    success = create_file_structure(args.path)
    
    if not success:
        print("\n❌ No se pudo crear la estructura. Verifica los permisos y la ruta.")
        return
    
    print("\n📋 Comandos útiles:")
    print(f"  cd {args.path}")
    print("  ls -la .bloom/.intents/.dev/.example-dev/.execution/.codebase.bl")
    print("  ls -la .bloom/.intents/.doc/.example-doc/.intent/.doc.prompt.bl")
    print("\n✅ Estructura actualizada creada exitosamente!")
    print("   • Archivos .codebase.bl añadidos en execution/ y refinement/turn_X/")
    print("   • Contenido de ejemplo en todos los archivos")

if __name__ == "__main__":
    main()