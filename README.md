This is a simple parser / emitter for pandoc block attributes,
intended for use with [pandocfilters].

[pandocfilters]: https://github.com/jgm/pandocfilters

It can read and write attributes in any of these formats:
    - markdown
    - html
    - dictionary
    - pandoc

Installation:

    pip install pandoc-attributes

Usage:

```python
from pandocattributes import PandocAttributes

attrs = '#id .class1 .class2 key=value'
attributes = PandocAttributes(attrs, format='markdown')

attributes.to_markdown()
>>> '{#id .class1 .class2 key=value}'

attributes.to_dict()
>>> {'id': 'id', 'classes': ['class1', 'class2'], 'key'='value'}

attributes.to_html()
>>> id="id" class="class1 class2" key='value'

attributes.to_pandoc()
>>> ['id', ['class1', 'class2'], [['key', 'value']]]

attributes.id
>>> 'id'

attributes.classes
>>> ['class1', 'class2']

attributes.kvs
>>> OrderedDict([('key', 'value')])
```
