class Text:
    __init__ = lambda self, text='', font='': vars(self).update(locals())
    write    = lambda self, value: vars(self).update({'text': self.text+value})
    set_font = lambda self, font: vars(self).update({'font': font})
    show     = lambda self: "[{0}]{1}[{0}]".format(self.font, self.text) if self.font else self.text
    restore  = lambda self, item: vars(self).update({'text': item.text, 'font': item.font})

class SavedText:
    __init__    = lambda self: vars(self).update({'history': []})
    save_text   = lambda self, item: vars(self).update({'history': self.history+[Text(item.text, item.font)]})
    get_version = lambda self, version: self.history[version]