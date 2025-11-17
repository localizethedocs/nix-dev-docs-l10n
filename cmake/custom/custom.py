# Distributed under the OSI-approved BSD 3-Clause License.
# See accompanying file LICENSE-BSD for details.

import json
import os

# Default configuration values.
DEFAULT_CONFIG_VALUES = {
    "html_baseurl"        : "",
    "current_language"    : "",
    "current_version"     : "",
}

def add_default_config_values(app):
    """
    Add default configuration values to the Sphinx app if not already defined.
    """
    for key, default in DEFAULT_CONFIG_VALUES.items():
        if key not in app.config.values:
            app.add_config_value(key, default, "env")

def configure_html_context(app):
    """
    Configure the html_context with necessary switchers, base URL,
    current version, and current language for Sphinx HTML output.
    """
    for key in DEFAULT_CONFIG_VALUES.keys():
        app.config.html_context[key] = getattr(app.config, key, "")

def setup(app):
    """
    Sphinx extension entry point.
    """
    add_default_config_values(app)

    # Connect to the builder-inited event to configure the HTML context.
    app.connect("builder-inited", configure_html_context)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
