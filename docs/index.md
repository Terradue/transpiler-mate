# Transpiler Mate

_Transpiler Mate_ is small and light yet powerful Python API + CLI to extract [Schema.org/SoftwareApplication](https://schema.org/SoftwareApplication) Metadata from an annotated [CWL](https://www.commonwl.org/) document and:

* transpile it to the [CodeMeta](https://codemeta.github.io/index.html) format;
* transpile it to the [DataCite Metadata](https://inveniordm.docs.cern.ch/reference/metadata/#metadata) properties;
* transpile it to [OGC API - Records](https://ogcapi.ogc.org/records/);
* transpile & publish a Record on [Invenio RDM](https://inveniosoftware.org/products/rdm/).

## Pre-requisites

To publish a Record on Invenio, users must obtain an authentication Token, see how to create a [new Token](https://inveniordm.docs.cern.ch/reference/rest_api_index/).

## Installation

```
pip install transpiler-mate
```

## CLI Usage

```
$ transpiler-mate --help
Usage: transpiler-mate [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  codemeta         Transpiles the input CWL to CodeMeta representation.
  datacite         Transpiles the input CWL to DataCite Metadata..
  invenio-publish  Publishes the input CWL to an Invenio instance.
  ogcrecord        Transpiles the input CWL to OGC API Record.
```
