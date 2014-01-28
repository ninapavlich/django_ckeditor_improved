import json
from django.conf import settings
from django.forms.util import flatatt
from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django import forms


class CKEditorInlineWidget(Textarea):
    default_config = {}
    def __init__(self, attrs=None, config={}):
        self.config = self.__class__.default_config.copy()
        self.config.update(config)
        super(CKEditorInlineWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        cssclass = 'ckeditorwidget'
        if 'class' in attrs:
            cssclass += ' ' + attrs['class']
        attrs['class'] = cssclass
        final_attrs = self.build_attrs(attrs, name=name)


        #NOTE -- for inline editors: Inline forms will be assigned an ID after render is called. SO what we do is assign a data attribute here so we can re-look it up.
        script = ('\n<script type="text/javascript">\n'
                    'var inited_editors = {{}};'
                    'grp.jQuery.extend( grp.jQuery.fn, {{\n'
                    '    hasParent: function( p ) {{\n'
                    '        return this.filter(function () {{\n'
                    '            return grp.jQuery(p).find(this).length;\n'
                    '        }}).length>0;\n'
                    '    }}\n'
                    '}});\n'
                    'function replaceCKEditor(editor_id, replace){{\n'
                        '//console.log("Replace editor: "+editor_id);'
                        'if(typeof replace == "undefined"){{replace = true;}}\n'
                        'var editor = CKEDITOR.instances[editor_id];\n'
                        'if(editor){{ try{{editor.destroy(true);}}catch(error){{console.log("Error destroying editor: "+error);}} }}\n'
                        'if(document.getElementById("cke_"+editor_id)){{ try{{var element = document.getElementById("cke_"+editor_id);element.parentNode.removeChild(element);}}catch(error){{console.log("Error removing container: "+error);}} }}\n'
                        'if(replace==true){{\n'
                            'CKEDITOR.replace(editor_id, {config});\n'
                        '}}\n'                                            
                    '}}\n'    
                    'function getCKEditorContent(editor_id){{\n'
                        'try{{\n'
                            'var iframe = grp.jQuery("#"+editor_id).parent().find("iframe");\n'
                            'var iframedoc = iframe[0].contentWindow.document;\n'
                            'var body = grp.jQuery(iframedoc).find("body");\n'
                            'return grp.jQuery(body).html()\n'                        
                        '}}catch(e){{return "";}}\n'
                    '}}\n' 
                    'function setTextAreaContent(editor_id, content){{\n'
                        'try{{\n'
                            'grp.jQuery("#"+editor_id).html(content);\n'                            
                        '}}catch(e){{return '';}}\n'
                    '}}\n'                    
                    'function initEditors(){{\n'
                        'var textareas = grp.jQuery.find("textarea.ckeditorwidget:not(.ckinited)");\n'
                        '//console.log("Found: "+textareas.length+" editrors not inited");\n'           
                        'for(var k=0; k<textareas.length; k++){{\n'
                        '    var textarea = textareas[k];\n'
                        '    var textarea_id = grp.jQuery(textarea).attr("id");\n'
                        '    var isInEmptyForm = grp.jQuery(textarea).hasParent(".grp-empty-form");\n'
                        '    //console.log(textarea_id+" isInEmptyForm? "+isInEmptyForm);\n'
                        '    if(isInEmptyForm==false){{\n'
                        '       grp.jQuery(textarea).addClass("ckinited");\n'                        
                        '       replaceCKEditor(textarea_id, true);\n'  
                        '       var parent_containers = grp.jQuery(textarea).parents(".grp-dynamic-form");\n'
                        '       var dragging_editor_content = "";\n'
                        '       grp.jQuery(parent_containers).find(".grp-drag-handler").bind("mousedown", {{id:textarea_id}}, function(event ){{\n'
                        '           dragging_editor_content = getCKEditorContent(event.data.id);\n'
                        '           replaceCKEditor(event.data.id, false);\n'
                        '           if(dragging_editor_content!=""){{setTextAreaContent(event.data.id, dragging_editor_content);}}\n'
                        '       }});\n'
                        '       grp.jQuery(parent_containers).find(".grp-drag-handler").bind("mouseup", {{id:textarea_id}}, function(event ){{\n'
                        '           setTimeout(function(){{replaceCKEditor(event.data.id, true);}},500);\n'     
                        '       }});\n'
                        '    }}\n'
                        '}}\n'             
                    '}}\n'                    
                    'setTimeout(function(){{initEditors();}},500);\n'                                  
                    '</script>\n').format( id=attrs['id'], config=json.dumps(self.config, indent=2))
        return mark_safe(u'<textarea{attrs}>{value}</textarea>{script}'.format(attrs=flatatt(final_attrs),
                                                                       value=conditional_escape(force_unicode(value)),
                                                                       script=script))


    def _media(self):
        js = [settings.STATIC_URL + 'ckeditorfiles/ckeditor.js']
        return forms.Media(js=js)
    media = property(_media)

class CKEditorWidget(Textarea):
    default_config = {}
    def __init__(self, attrs=None, config={}):
        self.config = self.__class__.default_config.copy()
        self.config.update(config)
        super(CKEditorWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        cssclass = 'ckeditorwidget'
        if 'class' in attrs:
            cssclass += ' ' + attrs['class']
        attrs['class'] = cssclass
        final_attrs = self.build_attrs(attrs, name=name)
        script = ('\n<script type="text/javascript">\n'
                  'CKEDITOR.replace("{id}", {config});\n'
                  '</script>\n').format(id=attrs['id'],
                                        config=json.dumps(self.config, indent=2))
        return mark_safe(u'<textarea{attrs}>{value}</textarea>{script}'.format(attrs=flatatt(final_attrs),
                                                                       value=conditional_escape(force_unicode(value)),
                                                                       script=script))

    def _media(self):
        js = [settings.STATIC_URL + 'ckeditorfiles/ckeditor.js']
        return forms.Media(js=js)
    media = property(_media)
