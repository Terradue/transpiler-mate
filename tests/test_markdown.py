from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from typing import Union

from transpiler_mate import markdown as md


class _ArrayType:
    items = "string"


class _Template:
    def render(self, **kwargs):
        return (
            f"v={kwargs['version']};"
            f"wf={kwargs['workflow'].id};"
            f"name={kwargs['software_application']['name']}"
        )


def test_normalize_author_wraps_person_dict() -> None:
    roles = md.normalize_author(
        {
            "@type": "https://schema.org/Person",
            "given_name": "Ada",
            "family_name": "Lovelace",
        }
    )

    assert len(roles) == 1
    assert roles[0]["@type"] == "https://schema.org/Role"
    assert roles[0]["role_name"] == "N/A"
    assert roles[0]["author"]["@type"] == "https://schema.org/Person"


def test_normalize_contributor_flattens_nested_lists() -> None:
    roles = md.normalize_contributor(
        [
            {
                "@type": "https://schema.org/Person",
                "given_name": "Grace",
                "family_name": "Hopper",
            },
            [
                {
                    "contributor": {
                        "@type": "https://schema.org/Person",
                        "given_name": "Katherine",
                        "family_name": "Johnson",
                    }
                }
            ],
        ]
    )

    assert len(roles) == 2
    assert roles[0]["contributor"]["family_name"] == "Hopper"
    assert roles[1]["contributor"]["family_name"] == "Johnson"


def test_normalize_author_rejects_invalid_shapes() -> None:
    try:
        md.normalize_author({"unexpected": "shape"})
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert "Unrecognized author dict shape" in str(exc)

    try:
        md.normalize_author(123)
        assert False, "Expected TypeError"
    except TypeError as exc:
        assert "author must be dict/list/None" in str(exc)


def test_type_to_string_and_nullable_helpers() -> None:
    assert (
        md.type_to_string(Union[str, int])
        == "One of:<ul><li>[str](https://www.commonwl.org/v1.2/Workflow.html#CWLType)</li><li>[int](https://www.commonwl.org/v1.2/Workflow.html#CWLType)</li></ul>"
    )
    assert (
        md.type_to_string(_ArrayType())
        == "[string](https://www.commonwl.org/v1.2/Workflow.html#CWLType)`[]`"
    )
    assert md.nullable(["null", "string"]) is True


def test_get_execution_command_formats_dynamic_arguments() -> None:
    command = md.get_exection_command(
        SimpleNamespace(
            baseCommand=["python", "-m", "module"],
            arguments=["--flag", 42],
        )
    )

    assert command == "python -m module --flag <ARGUMENT_DYNAMICALLY_SET>"


def test_markdown_transpile_renders_template(monkeypatch, tmp_path: Path) -> None:
    source = tmp_path / "workflow.cwl"
    source.write_text("cwlVersion: v1.2\n", encoding="utf-8")

    manager = SimpleNamespace(raw_document={"id": "#main"}, metadata=SimpleNamespace())

    monkeypatch.setattr(md, "MetadataManager", lambda _source: manager)
    monkeypatch.setattr(
        md,
        "CodeMetaTranspiler",
        lambda _repo: SimpleNamespace(
            transpile=lambda _metadata: {
                "@type": "SoftwareApplication",
                "name": "Example Tool",
            }
        ),
    )
    monkeypatch.setattr(md, "load_cwl_from_yaml", lambda _raw: "doc")
    monkeypatch.setattr(
        md, "search_process", lambda _id, _doc: SimpleNamespace(id="#main")
    )
    monkeypatch.setattr(md, "to_index", lambda _doc: {"main": "indexed"})
    monkeypatch.setattr(md, "_get_version", lambda: "9.9.9")
    monkeypatch.setattr(md.time, "time", lambda: 0)
    monkeypatch.setattr(
        md._jinja_environment, "get_template", lambda _name: _Template()
    )

    output = tmp_path / "out.md"
    with output.open("w", encoding="utf-8") as stream:
        md.markdown_transpile(source, "main", stream, None)

    rendered = output.read_text(encoding="utf-8")
    assert "v=9.9.9" in rendered
    assert "wf=#main" in rendered
    assert "name=Example Tool" in rendered


def test_markdown_transpile_raises_on_missing_workflow(
    monkeypatch, tmp_path: Path
) -> None:
    source = tmp_path / "workflow.cwl"
    source.write_text("cwlVersion: v1.2\n", encoding="utf-8")

    manager = SimpleNamespace(raw_document={"id": "#main"}, metadata=SimpleNamespace())

    monkeypatch.setattr(md, "MetadataManager", lambda _source: manager)
    monkeypatch.setattr(
        md,
        "CodeMetaTranspiler",
        lambda _repo: SimpleNamespace(
            transpile=lambda _metadata: {
                "@type": "SoftwareApplication",
                "name": "Example Tool",
            }
        ),
    )
    monkeypatch.setattr(md, "load_cwl_from_yaml", lambda _raw: "doc")
    monkeypatch.setattr(md, "search_process", lambda _id, _doc: None)

    try:
        with (tmp_path / "out.md").open("w", encoding="utf-8") as stream:
            md.markdown_transpile(source, "main", stream, None)
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert "Workflow main does not exist" in str(exc)
