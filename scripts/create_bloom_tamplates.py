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
    Crea un ejemplo de intent DEV
    """
    base_path = Path(base_path).resolve()
    intent_name = "example-dev"
    intent_path = base_path / ".bloom" / ".intents" / ".dev" / f".{intent_name}"
    
    print(f"\n💻 Creando intent DEV: {intent_name}")
    
    # Crear directorio del intent
    os.makedirs(intent_path, exist_ok=True)
    print(f"✓ Directorio creado: {intent_path.relative_to(base_path)}")
    
    # Estructura de archivos para intent DEV
    dev_structure = {
        ".session_state.json": json.dumps({
            "metadata": {
                "nombre": intent_name,
                "tipo": "DEV",
                "fecha_creacion": datetime.now().isoformat(),
                "estado": "iniciado"
            },
            "turn_controls": {
                "turno_actual": 0,
                "max_turnos": 10
            },
            "flags": {
                "completado": False
            }
        }, indent=2, ensure_ascii=False),
        
        ".briefing": {
            ".intent.bl": "# Intent DEV de ejemplo\n\n## Objetivo\nImplementar funcionalidad de ejemplo.",
            ".codebase.bl": "# Scope de código para análisis\n\n// Código relevante aquí",
            ".intent.json": json.dumps({
                "objetivos": ["Implementar funcionalidad"],
                "tipo": "DEV"
            }, indent=2, ensure_ascii=False),
            ".index.json": json.dumps({
                "resumen": "Intent DEV de ejemplo"
            }, indent=2, ensure_ascii=False)
        },
        
        ".execution": {
            ".index.json": json.dumps({
                "registro": ["Ejecución iniciada"]
            }, indent=2, ensure_ascii=False),
            ".intent.json": json.dumps({
                "prompt": "Prompt de ejecución"
            }, indent=2, ensure_ascii=False),
            ".response.json": json.dumps({
                "deliverable": "Código implementado"
            }, indent=2, ensure_ascii=False)
        },
        
        ".refinement": {
            ".turn_1": {
                ".index.json": json.dumps({
                    "resumen": "Primer turno de refinamiento"
                }, indent=2, ensure_ascii=False),
                ".intent.json": json.dumps({
                    "prompt": "Refinar implementación"
                }, indent=2, ensure_ascii=False),
                ".response.json": json.dumps({
                    "respuesta": "Refinamientos aplicados"
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
                "requerimiento": "Crear documentación",
                "tipo": "DOC",
                "prioridad": "media"
            }, indent=2, ensure_ascii=False),
            ".intent.bl": "# Intent DOC de ejemplo\n\nDocumentar funcionalidad específica.",
            ".doc.standards.bl": "# Estándares de documentación aplicables",
            ".doc.prompt.bl": "# Prompt final para la IA\n\nGenerar documentación técnica...",
            ".doc.app.context.bl": "# Contexto del proyecto\n\nInformación relevante...",
            ".tree.bl": "# Estructura de archivos relevante\n\n- /src\n- /docs",
            "index.json": json.dumps({
                "resumen": "Intent DOC de ejemplo"
            }, indent=2, ensure_ascii=False)
        },
        
        ".response": {
            ".response.json": json.dumps({
                "entrega": "Documentación generada",
                "contenido": "# Documentación técnica\n\nContenido aquí..."
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
    
    # Ordenar: directorios primero, luego archivos, y excluir algunos
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
        description='Crea la estructura de archivos .bloom con carpetas .dev y .doc',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  %(prog)s                            # Crea en directorio actual
  %(prog)s /ruta/destino              # Crea en ruta específica
  %(prog)s --path /mi/proyecto        # Usando flag --path
  
El script crea automáticamente:
  • Estructura base .bloom
  • Un intent DEV de ejemplo (.example-dev)
  • Un intent DOC de ejemplo (.example-doc)
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
    print("  ls -la .bloom/.intents/.dev")
    print("  ls -la .bloom/.intents/.doc")
    print("\n🌳 Estructura completa creada:")
    print(f"  .bloom/")
    print(f"  ├── .core/")
    print(f"  ├── .intents/")
    print(f"  │   ├── .dev/")
    print(f"  │   │   └── .example-dev/")
    print(f"  │   │       ├── .session_state.json")
    print(f"  │   │       ├── .briefing/")
    print(f"  │   │       ├── .execution/")
    print(f"  │   │       └── .refinement/")
    print(f"  │   └── .doc/")
    print(f"  │       └── .example-doc/")
    print(f"  │           ├── .intent/")
    print(f"  │           └── .response/")
    print(f"  └── .project/")
    print("\n✅ Listo! Puedes ahora crear tus propios intents dentro de .dev/ o .doc/")

if __name__ == "__main__":
    main()