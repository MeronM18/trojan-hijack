"""Layer 2: content separation.

Will wrap untrusted content in tags with a random id per load, e.g.
<untrusted_data source="..." id="k3f9a2"> ... </untrusted_data id="k3f9a2">,
escape any look-alike tags inside the content, and provide
SYSTEM_PROMPT_ADDENDUM telling Claude that wrapped content is data, never commands.
"""
