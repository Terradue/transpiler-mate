{% include "metadata.md" %}

---

# Workflow

{% import "workflow.md" as wf with context %}
{{wf.serialize_workflow(workflow)}}
