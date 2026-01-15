# {{software_application.name}} v{{software_application.softwareVersion}}

{{software_application.description}}

> This software is licensed under the terms of the [{{software_application.license.name}}]({{software_application.license.url}}) license - SPDX short identifier: [{{software_application.license.identifier}}](https://spdx.org/licenses/{{software_application.license.identifier}})
>
> {{software_application.dateCreated}} - {{timestamp}} Copyright [{{software_application.publisher.name}}](mailto:{{software_application.publisher.email}}) - {% if software_application.publisher.identifier %}> [{{software_application.publisher.identifier}}]({{software_application.publisher.identifier}}){% endif %}

# Project Team

| Name | Email | Organization | Role | Identifier |
|------|-------|--------------|------|------------|
{% for role in software_application.author %}| {{role.author.familyName}}, {{role.author.givenName}} | [{{role.author.email}}](mailto:{{role.author.email}}) | [{{role.author.affiliation.name}}]({{role.author.affiliation.identifier}}) | [{{role.roleName}}]({{role.additionalType}}) | [{{role.author.identifier}}]({{role.author.identifier}}) |
{% endfor %}
# Runtime environment

## Supported Operating Systems

{% for operatingSystem in software_application.operatingSystem %}- {{operatingSystem}}
{% endfor %}
## Requirements

{% for softwareRequirement in software_application.softwareRequirements %}- [{{softwareRequirement}}]({{softwareRequirement}})
{% endfor %}

{% if software_source_code %}# Software Source code

- Browsable version of the [source repository]({{software_source_code.codeRepository}});
- [Continuous integration]({{software_source_code.continuousIntegration}}) system used by the project;
- Issues, bugs, and feature requests should be submitted to the following [issue management]({{software_source_code.issueTracker}}) system for this project
{% endif %}

---

# Worflow `{{workflow.id}}`

## Inputs

| Id | Type | Label | Doc |
|----|------|-------|-----|
{% for input in workflow.inputs %}| `{{input.id}}` | `{{ input.type_ | type_to_string }}` | {{input.label}} | {{input.doc}} |
{% endfor %}

## Steps

| Id | Runs | Label | Doc |
|----|------|-------|-----|
{% for step in workflow.steps %}| `{{step.id}}` | `{{step.run}}` | {{step.label}} | {{step.doc}} |
{% endfor %}

## Outputs

| Id | Type | Label | Doc |
|----|------|-------|-----|
{% for output in workflow.outputs %}| `{{output.id}}` | `{{ output.type_ | type_to_string }}` | {{output.label}} | {{output.doc}} |
{% endfor %}

## UML Diagrams

{% set diagrams=['activity', 'component', 'class', 'sequence', 'state'] %}
{% for diagram in diagrams %}
### UML `{{diagram}}` diagram

![{{workflow.id}} flow diagram](./{{workflow.id}}/{{diagram}}.svg "{{workflow.id}} {{diagram}} diagram")
{% endfor %}
