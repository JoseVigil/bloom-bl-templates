# 🌸 Bloom .bl Templates

Templates de documentación en formato `.bl` (Bloom) para el sistema Bloom Video.

---

## 📋 ¿Qué es esto?

Este repositorio contiene **templates de documentación en formato `.bl`** que se usan para inicializar la estructura Bloom en proyectos.

Los archivos `.bl` (Bloom) son fuentes de documentación que se convierten automáticamente en:
- 📄 `README.md` (para GitHub)
- 🌐 HTML (para GitHub Pages)

---

## 📂 Estructura

```
bloom-bl-templates/
├── README.md                      # Este archivo
├── templates.json                 # Metadata de templates
│
├── core/                          # Templates obligatorios
│   ├── .readme.main.bl.md        # README principal
│   ├── .prompting-guide.bl.md    # Guía para IAs
│   └── .system-prompt.bl         # System Prompt
│
└── optional/                      # Templates opcionales
    ├── .architecture-guide.bl.md  # Arquitectura técnica
    ├── .api-reference.bl.txt      # Referencia de API
    ├── .build-deploy.bl.md        # Build y deploy
    └── .testing-guide.bl.md       # Testing
```

---

## 🎯 Uso

### Con bloom-init-all.zsh

```bash
# El script lee automáticamente desde bloom-bl-templates/
cd bloom-videos
./bloom-init-all.zsh
```

### Con Plugin VSCode (bloom-development-extension)

```typescript
// El plugin carga templates desde:
const templatesPath = path.join(workspaceRoot, '..', 'bloom-bl-templates');
```

### Manual

```bash
# Copiar template a tu proyecto
cp bloom-bl-templates/core/.readme.main.bl.md ./
```

---

## ✏️ Editar Templates

**Ventaja principal:** Editas los templates SIN tocar código del plugin o scripts.

```bash
# 1. Editar template
cd bloom-bl-templates
vim core/.readme.main.bl.md

# 2. Commit y push
git add .
git commit -m "feat: agregar sección de testing"
git push

# 3. Los cambios se usan automáticamente
cd ../bloom-videos
./bloom-init-all.zsh  # ¡Usa la nueva versión!
```

---

## 📝 Sintaxis de Templates

### Frontmatter YAML

```yaml
---
type: readme
project: [Completar: nombre-proyecto]
version: 1.0.0
last_updated: [Completar: YYYY-MM-DD]
ai_context: true
priority: high
---
```

### Placeholders

Los templates usan placeholders que se reemplazan automáticamente:

```markdown
# [Completar: nombre-proyecto]

[Completar: Descripción breve]
```

**Variables disponibles:**
- `[Completar: nombre-proyecto]` → Nombre del repo
- `[Completar: YYYY-MM-DD]` → Fecha actual
- `[Completar: ...]` → Texto que debe completar el usuario

---

## 🔧 templates.json

Archivo de metadata que describe cada template:

```json
{
  "version": "1.0.0",
  "templates": {
    "readme.main": {
      "file": "core/.readme.main.bl.md",
      "priority": "high",
      "required": true,
      "description": "README principal del proyecto"
    }
  }
}
```

**Campos:**
- `file`: Ruta relativa al template
- `priority`: `high` | `medium` | `low`
- `required`: Si es obligatorio o no
- `type`: Tipo de template
- `ai_context`: Si la IA debe considerarlo al analizar proyecto

---

## 🎨 Crear Nuevos Templates

### 1. Crear archivo

```bash
cd bloom-bl-templates/optional
vim .new-template.bl.md
```

### 2. Agregar frontmatter

```yaml
---
type: new-template
project: [Completar: nombre-proyecto]
version: 1.0.0
last_updated: [Completar: YYYY-MM-DD]
ai_context: true
priority: medium
---
```

### 3. Registrar en templates.json

```json
{
  "new-template": {
    "file": "optional/.new-template.bl.md",
    "priority": "medium",
    "required": false,
    "description": "Descripción del nuevo template"
  }
}
```

### 4. Commit

```bash
git add .
git commit -m "feat: add new-template"
git push
```

---

## 🔄 Versionado

Los templates se versionan independientemente del plugin:

```
bloom-bl-templates v2.0.0
bloom-development-extension v1.0.0
```

### Tags de Versión

```bash
# Crear versión nueva
git tag v2.0.0
git push --tags

# Usar versión específica
cd bloom-videos
git clone --branch v2.0.0 https://github.com/JoseVigil/bloom-bl-templates.git
```

---

## 🤝 Contribuir

### Para mejorar templates existentes

1. Fork del repo
2. Edita el template
3. Pull request con descripción clara

### Para agregar nuevos templates

1. Fork del repo
2. Crea archivo en `optional/`
3. Registra en `templates.json`
4. Pull request

---

## 📊 Templates Disponibles

| Template | Archivo | Obligatorio | Descripción |
|----------|---------|-------------|-------------|
| **readme.main** | `core/.readme.main.bl.md` | ✅ Sí | README principal |
| **prompting-guide** | `core/.prompting-guide.bl.md` | ✅ Sí | Guía para IAs |
| **system-prompt** | `core/..system-prompt.bl` | ✅ Sí | System Prompt |
| **architecture-guide** | `optional/.architecture-guide.bl.md` | ❌ No | Arquitectura técnica |
| **api-reference** | `optional/.api-reference.bl.txt` | ❌ No | Referencia de API |
| **build-deploy** | `optional/.build-deploy.bl.md` | ❌ No | Build y deploy |

---

## 🌸 Filosofía

> "Los templates deben ser editables sin tocar código"

Ventajas de este enfoque:
- ✅ Mejora continua sin recompilar plugin
- ✅ Contribuciones más fáciles
- ✅ Versionado independiente
- ✅ Reutilización entre proyectos

---

## 📄 Licencia

MIT

---

**Repo:** https://github.com/JoseVigil/bloom-bl-templates  
**Sistema Bloom:** v1.0.0