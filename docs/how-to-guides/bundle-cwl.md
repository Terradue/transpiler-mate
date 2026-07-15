# Bundle a CWL document

The `bundle` command loads a CWL document, resolves its external references, and serializes the resulting processes into a self-contained CWL file. The command supports references loaded from local files, HTTP(S), S3, and OCI registries.

This command was migrated from the [CWL Loader CLI](https://terradue.github.io/cwl-loader/).

## Help usage

```text
$ transpiler-mate bundle --help
Usage: transpiler-mate bundle [OPTIONS] SOURCE

  Creates a self-contained CWL document with all references resolved.

Options:
  --output PATH         The output file path  [default: bundle.cwl]
  --oci-hostname TEXT   [env var: OCI_HOSTNAME]
  --oci-username TEXT   [env var: OCI_USERNAME]
  --oci-password TEXT   [env var: OCI_PASSWORD]
  --oauth2-bearer TEXT  [env var: OAUTH2_BEARER]
  --help                Show this message and exit.
```

## Bundle a local workflow

Provide the root CWL document and the destination file:

```bash
transpiler-mate bundle ./workflow.cwl --output ./dist/bundle.cwl
```

The parent directory of the output file is created automatically. If `--output` is omitted, the command writes `bundle.cwl` in the current directory.

## Resolve authenticated HTTP references

Set `OAUTH2_BEARER` when the workflow contains HTTP or HTTPS references protected by a bearer token:

```bash
export OAUTH2_BEARER="<token>"
transpiler-mate bundle ./workflow.cwl --output ./dist/bundle.cwl
```

## Resolve OCI references

OCI connection settings can be supplied through environment variables:

```bash
export OCI_HOSTNAME="registry.example.org"
export OCI_USERNAME="<username>"
export OCI_PASSWORD="<password>"
transpiler-mate bundle ./workflow.cwl --output ./dist/bundle.cwl
```

The corresponding `--oci-hostname`, `--oci-username`, and `--oci-password` options can be used instead. S3 references use the credentials and region configuration available to the underlying AWS client.
