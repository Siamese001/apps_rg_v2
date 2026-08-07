"""Repository-root shim for the standalone ``src/apps_eval`` package."""

from _standalone_src_bootstrap import bootstrap_src_package

bootstrap_src_package(__name__, globals())
