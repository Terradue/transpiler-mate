{% macro serialize_clt(clt) -%}## {{clt.id}}

### CWL Class

```
{{clt.class_}}
```

### Inputs

| Id | Option | Type |
|----|------|-------|
{% for input in clt.inputs %}| `{{input.id}}` | `{% if input.inputBinding.prefix %}{{input.inputBinding.prefix}}{% else %}--{{input.id}}{% endif %}` | `{{ input.type_ | type_to_string }}` |
{% endfor %}
### Execution usage example:

```
{{clt | get_exection_command}} \
{% for input in clt.inputs %}{% if input.type_ is nullable %}({% endif %}{% if input.inputBinding.prefix %}{{input.inputBinding.prefix}}{% else %}--{{input.id}}{% endif %} <{{input.id.upper()}}>{% if input.type_ is nullable %}){% endif %}{% if not loop.last %} \{% endif %}
{% endfor %}```
{%- endmacro %}

{% macro serialize_workflow(workflow) -%}## {{workflow.id}}

### CWL Class

`{{workflow.class_}}`

### Inputs

| Id | Type | Label | Doc |
|----|------|-------|-----|
{% for input in workflow.inputs %}| `{{input.id}}` | `{{ input.type_ | type_to_string }}` | {{input.label}} | {{input.doc}} |
{% endfor %}

### Steps

| Id | Runs | Label | Doc |
|----|------|-------|-----|
{% for step in workflow.steps %}| [{{step.id}}](#{{step.run[1:]}}) | `{{step.run}}` | {{step.label}} | {{step.doc}} |
{% endfor %}

### Outputs

| Id | Type | Label | Doc |
|----|------|-------|-----|
{% for output in workflow.outputs %}| `{{output.id}}` | `{{ output.type_ | type_to_string }}` | {{output.label}} | {{output.doc}} |
{% endfor %}

### UML Diagrams
{% set diagrams=['activity', 'component', 'class', 'sequence', 'state'] %}
{% for diagram in diagrams %}
#### UML `{{diagram}}` diagram

![{{workflow.id}} flow diagram](./{{workflow.id}}/{{diagram}}.svg "{{workflow.id}} {{diagram}} diagram")
{% endfor %}

{% for step in workflow.steps %}

{% set resolved_step = index.get(step.run[1:]) %}
{% if "Workflow" == resolved_step.class_ %}
{{serialize_workflow(resolved_step)}}
{% else %}
{{serialize_clt(resolved_step)}}
{% endif %}

### Run in step

`{{step.id}}`
{% endfor %}

{%- endmacro %}
