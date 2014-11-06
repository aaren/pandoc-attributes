import nose.tools as nt

from collections import OrderedDict

from pandocattributes import PandocAttributes


attr_markdown = r"""{#identify .class1 .class2 .unnumbered
key1=blah key2="o'brien = 1"}"""

attr_markdown_special = r"""{#identify .class1 .class2
key1=blah key2="o'brien = 1" -}"""

attr_dict = OrderedDict()
attr_dict['id'] = 'identify'
attr_dict['classes'] = ['class1', 'class2', 'unnumbered']
attr_dict['key1'] = 'blah'
attr_dict['key2'] = '"o\'brien = 1"'

attr_html = '''id="identify" class="class1 class2 unnumbered" key1=blah key2="o'brien = 1"'''

attr_pandoc = ['identify',
               ['class1', 'class2', 'unnumbered'],
               [['key1', 'blah'],
                ['key2', '"o\'brien = 1"']]
               ]


def test_markdown():
    attr = PandocAttributes(attr_markdown, 'markdown')

    print attr_dict
    print attr.to_dict()
    nt.assert_dict_equal(attr_dict, attr.to_dict())
    nt.assert_equal(attr_html, attr.to_html())
    nt.assert_equal(attr_markdown.replace('\n', ' '), attr.to_markdown())
    assert(attr_pandoc == attr.to_pandoc())


def test_html():
    attr = PandocAttributes(attr_html, 'html')

    print attr_dict
    print attr.to_dict()
    nt.assert_dict_equal(attr_dict, attr.to_dict())
    nt.assert_equal(attr_html, attr.to_html())
    nt.assert_equal(attr_markdown.replace('\n', ' '), attr.to_markdown())
    assert(attr_pandoc == attr.to_pandoc())


def test_dict():
    attr = PandocAttributes(attr_dict, 'dict')

    print attr_dict
    print attr.to_dict()
    nt.assert_dict_equal(attr_dict, attr.to_dict())
    nt.assert_equal(attr_html, attr.to_html())
    nt.assert_equal(attr_markdown.replace('\n', ' '), attr.to_markdown())
    assert(attr_pandoc == attr.to_pandoc())


def test_pandoc():
    attr = PandocAttributes(attr_pandoc, 'pandoc')

    print attr_dict
    print attr.to_dict()
    nt.assert_dict_equal(attr_dict, attr.to_dict())
    nt.assert_equal(attr_html, attr.to_html())
    nt.assert_equal(attr_markdown.replace('\n', ' '), attr.to_markdown())
    assert(attr_pandoc == attr.to_pandoc())


def test_markdown_special():
    attr = PandocAttributes(attr_markdown, 'markdown')
    attr_special = PandocAttributes(attr_markdown_special, 'markdown')

    assert(attr.id == attr_special.id)
    assert(attr.classes == attr_special.classes)
    assert(attr.kvs == attr_special.kvs)

