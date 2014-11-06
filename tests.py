import nose.tools as nt

from pandocattributes import PandocAttributes


def test_attributes():
    attr_markdown = r"""{#identify .class1 .class2
    key1=blah key2="o'brien = 1" -}"""
    attr_dict = {'id': 'identify',
                'classes': ['class1', 'class2', 'unnumbered'],
                'key1': 'blah',
                'key2': '"o\'brien = 1"'
                }
    attr_html = '''id="identify" class="class1 class2 unnumbered" key1=blah key2="o'brien = 1"'''

    attr = PandocAttributes(attr_markdown, 'markdown')

    print attr_dict
    print attr.to_dict()
    nt.assert_dict_equal(attr_dict, attr.to_dict())
    nt.assert_equal(attr_html, attr.to_html())
