# {{software_application.name}} v{{software_application.softwareVersion}}

{{software_application.description}}

> This software is licensed under the terms of the [{{software_application.license.name}}]({{software_application.license.url}}) license - SPDX short identifier: [{{software_application.license.identifier}}](https://spdx.org/licenses/{{software_application.license.identifier}})
>
> {{software_application.dateCreated}} - {{timestamp}} Copyright [{{software_application.publisher.name}}](mailto:{{software_application.publisher.email}}) - {% if software_application.publisher.identifier %}> [{{software_application.publisher.identifier}}]({{software_application.publisher.identifier}}){% endif %}

# Project Team

## Authors

| Name | Email | Organization | Role | Identifier |
|------|-------|--------------|------|------------|
{% for role in software_application.author | normalize_author %}| {{role.author.familyName}}, {{role.author.givenName}} | [{{role.author.email}}](mailto:{{role.author.email}}) | [{{role.author.affiliation.name}}]({{role.author.affiliation.identifier}}) | [{{role.roleName}}]({{role.additionalType}}) | [{{role.author.identifier}}]({{role.author.identifier}}) |
{% endfor %}

## Contributors
{% if software_application.contributor %}
| Name | Email | Organization | Role | Identifier |
|------|-------|--------------|------|------------|
{% for role in software_application.contributor | normalize_contributor %}| {{role.contributor.familyName}}, {{role.contributor.givenName}} | [{{role.contributor.email}}](mailto:{{role.contributor.email}}) | [{{role.contributor.affiliation.name}}]({{role.contributor.affiliation.identifier}}) | [{{role.roleName}}]({{role.additionalType}}) | [{{role.contributor.identifier}}]({{role.contributor.identifier}}) |
{% endfor %}
{% else %}
The are no contributors for this project.
{% endif %}

{% if software_application.softwareHelp %}# {{software_application.softwareHelp.name}}

{{software_application.softwareHelp.name}} can be found on [{{software_application.softwareHelp.url}}]({{software_application.softwareHelp.url}}).
{% endif %}

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
