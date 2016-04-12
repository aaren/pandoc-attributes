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

attr_html = ('''id="identify" '''
             '''class="class1 class2 unnumbered" '''
             '''key1=blah key2="o'brien = 1"''')

attr_pandoc = ['identify',
               ['class1', 'class2', 'unnumbered'],
               [['key1', 'blah'],
                ['key2', '"o\'brien = 1"']]
               ]


def test_markdown():
    attr = PandocAttributes(attr_markdown, 'markdown')

    print(attr_dict)
    print(attr.to_dict())
    nt.assert_dict_equal(attr_dict, attr.to_dict())
    nt.assert_equal(attr_html, attr.to_html())
    nt.assert_equal(attr_markdown.replace('\n', ' '), attr.to_markdown())
    nt.assert_equal(attr_pandoc, attr.to_pandoc())


def test_html():
    attr = PandocAttributes(attr_html, 'html')

    print(attr_dict)
    print(attr.to_dict())
    nt.assert_dict_equal(attr_dict, attr.to_dict())
    nt.assert_equal(attr_html, attr.to_html())
    nt.assert_equal(attr_markdown.replace('\n', ' '), attr.to_markdown())
    nt.assert_equal(attr_pandoc, attr.to_pandoc())


def test_dict():
    attr = PandocAttributes(attr_dict, 'dict')

    print(attr_dict)
    print(attr.to_dict())
    nt.assert_dict_equal(attr_dict, attr.to_dict())
    nt.assert_equal(attr_html, attr.to_html())
    nt.assert_equal(attr_markdown.replace('\n', ' '), attr.to_markdown())
    nt.assert_equal(attr_pandoc, attr.to_pandoc())


def test_pandoc():
    attr = PandocAttributes(attr_pandoc, 'pandoc')

    print(attr_dict)
    print(attr.to_dict())
    nt.assert_dict_equal(attr_dict, attr.to_dict())
    nt.assert_equal(attr_html, attr.to_html())
    nt.assert_equal(attr_markdown.replace('\n', ' '), attr.to_markdown())
    nt.assert_equal(attr_pandoc, attr.to_pandoc())


def test_markdown_special():
    attr = PandocAttributes(attr_markdown, 'markdown')
    attr_special = PandocAttributes(attr_markdown_special, 'markdown')

    nt.assert_equal(attr.id, attr_special.id)
    nt.assert_equal(attr.classes, attr_special.classes)
    nt.assert_equal(attr.kvs, attr_special.kvs)


def test_markdown_single():
    attr = PandocAttributes('python', 'markdown')

    nt.assert_equal(attr.id, '')
    nt.assert_equal(attr.classes, ['python'])
    nt.assert_equal(attr.kvs, OrderedDict())


def test_empty():
    attr = PandocAttributes()
    nt.assert_true(attr.is_empty)


def test_getitem():
    attr = PandocAttributes()
    nt.assert_equal(attr['id'], '')
    nt.assert_equal(attr['classes'], [])

    with nt.assert_raises(KeyError):
        attr['whatever']

    attr.kvs['whatever'] = 'dude'
    nt.assert_equal(attr['whatever'], 'dude')


def test_markdown_format():
    attr = PandocAttributes()
    attr.id = 'a'
    attr.classes = ['b']
    attr.kvs['c'] = 'd'

    md = attr.to_markdown(format='{classes} {id} {kvs}')
    nt.assert_equal(md, '{.b #a c=d}')


def test_properties():
    attr = PandocAttributes(attr_markdown, 'markdown')
    nt.assert_equal(attr.html, attr.to_html())
    nt.assert_equal(attr.markdown, attr.to_markdown())
    nt.assert_equal(attr.dict, attr.to_dict())
    nt.assert_equal(attr.list, attr.to_pandoc())


def test_surround():
    attr = PandocAttributes(attr_markdown, 'markdown')
    print(attr.to_markdown(surround=False))
    print(attr_markdown.replace('\n', ' ').strip('{}'))
    nt.assert_equal(attr.to_markdown(surround=False),
                    attr_markdown.replace('\n', ' ').strip('{}'))
