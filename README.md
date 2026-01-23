# MicroVM SDK

Multi-language SDK for the MicroVM secure code execution service.

## Repository Structure

```
microvm-sdk/
├── openapi-config.yaml    # SDK generation config
├── python/                # Python SDK
│   ├── microvm/          # Import package
│   ├── pyproject.toml
│   └── README.md
├── javascript/            # JavaScript SDK (future)
└── README.md
```

## Generating/Updating SDKs

### Prerequisites

```bash
pip install openapi-python-client
```

### Generate Python SDK

From the root of this repository:

```bash
openapi-python-client generate \
  --path ../microvm/api/openapi.yaml \
  --output-path ./python \
  --config openapi-config.yaml
```

This will:
- Read the OpenAPI spec from the microvm service
- Generate Python client code in `./python/`
- Use package name `microvm-sdk` (for pip install)
- Use import name `microvm` (for code imports)

### Update Existing SDK

When the OpenAPI spec changes, regenerate:

```bash
# Remove old generated code (keeps your customizations in git)
rm -rf python
openapi-python-client generate \
  --path ../microvm/api/openapi.yaml \
  --output-path ./python \
  --config openapi-config.yaml
```

## Installation

### From GitHub (Development)

Install directly from the GitHub repository:

```bash
# Latest from main branch
pip install git+https://github.com/Mechademy-Git/microvm-sdk.git#subdirectory=python

# Specific branch
pip install git+https://github.com/Mechademy-Git/microvm-sdk.git@develop#subdirectory=python

# Specific commit
pip install git+https://github.com/Mechademy-Git/microvm-sdk.git@abc1234#subdirectory=python

# Specific tag/version
pip install git+https://github.com/Mechademy-Git/microvm-sdk.git@v1.0.0#subdirectory=python
```

### In requirements.txt

```txt
# requirements.txt
microvm-sdk @ git+https://github.com/Mechademy-Git/microvm-sdk.git#subdirectory=python
```

### In pyproject.toml

```toml
[project]
dependencies = [
    "microvm-sdk @ git+https://github.com/Mechademy-Git/microvm-sdk.git#subdirectory=python"
]
```

### With uv

```bash
uv pip install "microvm-sdk @ git+https://github.com/Mechademy-Git/microvm-sdk.git#subdirectory=python"
```

### From Local Path (Development)

```bash
# Editable install
pip install -e ./python

# Regular install
pip install ./python
```

### From PyPI (Future)

Once published to PyPI:

```bash
pip install microvm-sdk
```

## Usage

```python
from microvm import Client

# Initialize client
client = Client(
    base_url="<micro_vm_base_url>",
    headers={"X-API-Key": "your-api-key"}
)

# Execute code
from microvm.models import ExecuteRequest

request = ExecuteRequest(
    code="def add(a, b):\n    return a + b",
    function_name="add",
    args=[5, 3]
)

response = client.execute.sync(json_body=request)

if response.success:
    print(f"Result: {response.output}")
else:
    print(f"Error: {response.error}")
```

## Configuration

Edit `openapi-config.yaml` to customize SDK generation:

```yaml
project_name_override: "microvm-sdk"  # PyPI package name
package_name_override: "microvm"      # Python import name
```

## Development Workflow

### 1. Update MicroVM API

Make changes to `../microvm/api/openapi.yaml`

### 2. Regenerate SDK

```bash
openapi-python-client generate \
  --path ../microvm/api/openapi.yaml \
  --output-path ./python \
  --config openapi-config.yaml
```

### 3. Test Changes

```bash
cd python
pytest
```

### 4. Commit and Tag

```bash
git add .
git commit -m "Update SDK for OpenAPI spec v1.2.0"
git tag v1.2.0
git push origin main --tags
```

### 5. Update Dependent Services

In services using the SDK:

```bash
# Update to latest
pip install --upgrade git+https://github.com/Mechademy-Git/microvm-sdk.git#subdirectory=python

# Or update to specific version
pip install git+https://github.com/Mechademy-Git/microvm-sdk.git@v1.2.0#subdirectory=python
```

## Adding Other Languages

### JavaScript/TypeScript

```bash
npm install @openapitools/openapi-generator-cli

openapi-generator-cli generate \
  -i ../microvm/api/openapi.yaml \
  -g typescript-fetch \
  -o ./javascript \
  --additional-properties=npmName=microvm-sdk
```

### Go

```bash
openapi-generator-cli generate \
  -i ../microvm/api/openapi.yaml \
  -g go \
  -o ./go \
  --additional-properties=packageName=microvm
```

## Troubleshooting

### "No module named 'microvm'"

Make sure you installed from the `python` subdirectory:

```bash
pip install git+https://github.com/Mechademy-Git/microvm-sdk.git#subdirectory=python
```

### Updates not reflected

Clear pip cache:

```bash
pip cache purge
pip install --force-reinstall git+https://github.com/Mechademy-Git/microvm-sdk.git#subdirectory=python
```

### Local development

Use editable install:

```bash
pip install -e ./python
```

## Related Projects

- **microvm** - Code execution service ([../microvm](../microvm))
- **turbomechanica-server** - Main application server
- **turboai** - LLM service that generates code

## License

MIT License - See [LICENSE](LICENSE) file for details.
