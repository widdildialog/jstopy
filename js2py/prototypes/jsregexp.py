
class RegExpPrototype:
    def toString():
        flags = u''
        if this.glob:
            flags += u'g'
        if this.ignore_case:
            flags += u'i'
        if this.multiline:
            flags += u'm'
        return u'/%s/'%self.value + flags

    def test(string):
        return Exec(this, string) is not this.null




def Exec(this, string):
    if this.Class!='RegExp':
        raise this.Js(TypeError)('RegExp.prototype.exec is not generic!')
    string = string.to_string()
    length = len(string)
    i = this.get('lastIndex').to_int() if this.glob else 0
    matched = False
    while not matched:
        if i < 0 or i > length:
            this.put('lastIndex', this.Js(0))
            return this.null
        matched = this.match(string, i)
        i += 1
    start, end = matched.span()
    if this.glob:
        this.put('lastIndex', this.Js(end))
    arr = this.Js([this.Js(e) for e in [matched.group()]+matched.groups()])
    arr.put('index', this.Js(start))
    arr.put('input', string)
    return arr
