# Transpiler Mate

A small and light yet powerful API + CLI to extract [Schema.org/SoftwareApplication](https://schema.org/SoftwareApplication) Metadata from an annotated [CWL](https://www.commonwl.org/) document and publish it as a Record on [Invenio RDM](https://inveniosoftware.org/products/rdm/).

## Pre-requisites

You must own an authentication Token to pusblish on Invenio, see how to create a [new Token](https://inveniordm.docs.cern.ch/reference/rest_api_index/).

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
  invenio-publish  Publishes the input CWL to an Invenio instance.
  ogcrecord        Transpiles the input CWL to OGC API Record.
```
